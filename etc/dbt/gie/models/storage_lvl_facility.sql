with


gas_region as (
    select
        *
    from
        {{ source('gie_stage', 'storage') }} r
),

erik as (
    SELECT [1, 2, 3]
),

gas_storage as (
    select
        null _sdc_batched_at,
        gas_day_start::DATE gas_day_start,
        split_part(url, '/', 2) as country,
        split_part(url, '/', 3) as company_eic,
        null key_hash,
        code as facility_eic,
        name as facility_name,
        status,
        TRY_CAST(t.full AS DOUBLE) as facility_fill_ratio,
        TRY_CAST(gas_in_storage AS DOUBLE) as gas_in_storage,
        TRY_CAST(working_gas_volume AS DOUBLE) as working_gas_volume,
        TRY_CAST(injection as DOUBLE) as injection,
        TRY_CAST(withdrawal AS DOUBLE) as withdrawal,
        url,
        split_part(url, '/', 1) as EIC_likely,
        split_part(url, '/', 2) as country_likely,
        split_part(url, '/', 3) as company_likely,
        _dlt_root_id
    from
        {{ source('gie_stage', 'storage__children__children__children') }} t
),

gas_loads as (
    select
        *
    from
        {{ source('gie_stage', '_load_info') }}
),

gas_loading as (
    select
        a.started_at,
        b.value as _dlt_load_id_root
    from
            {{ source('gie_stage', '_load_info') }} as a
        right join
            {{ source('gie_stage', '_load_info__loads_ids') }} as b
        on
            a._dlt_id = b._dlt_parent_id
)

select
    gas_loading.started_at as _sdc_extracted_at,
    gas_storage.*,
    gas_region._dlt_load_id
from
    gas_region join gas_storage on gas_region._dlt_id = gas_storage._dlt_root_id
    left join
        gas_loads on gas_region._dlt_load_id = gas_loads._dlt_load_id
    left join
        gas_loading on gas_region._dlt_load_id = gas_loading._dlt_load_id_root
