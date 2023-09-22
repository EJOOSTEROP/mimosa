with


gas_region as (
    select
        *
    from
        {{ source('gie_stage', 'storage') }} r
),

gas_storage as (
    select
        t.gas_day_start::DATE gas_day_start,
        split_part(t.url, '/', 2) as country,
        c.code as company_eic,
        c.name as company_name,
        null key_hash,
        t.code as facility_eic,
        t.name as facility_name,
        t.status,
        TRY_CAST(t.full AS DOUBLE) as facility_fill_ratio,
        TRY_CAST(t.gas_in_storage AS DOUBLE) as gas_in_storage,
        TRY_CAST(t.working_gas_volume AS DOUBLE) as working_gas_volume,
        TRY_CAST(t.injection as DOUBLE) as injection,
        TRY_CAST(t.withdrawal AS DOUBLE) as withdrawal,
        t.url,
        t._dlt_id as _fac_dlt_id,
        t_country._dlt_id as _country_dlt_id,
        t._dlt_root_id
    from
        {{ source('gie_stage', 'storage__children__children__children') }} as t
        left join
        {{ source('gie_stage', 'storage__children__children') }} as c
        on t._dlt_parent_id = c._dlt_id
        left join
        {{ source('gie_stage', 'storage__children__children') }} as t_country
        on c._dlt_parent_id = t_country._dlt_id
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
    transaction_timestamp() as _sdc_batched_at,
    gas_region.name as region,
    gas_storage.*,
    year(gas_storage.gas_day_start)::INTEGER as reporting_year,
    make_date(2000, month(gas_storage.gas_day_start), day(gas_storage.gas_day_start)) as reporting_day,
    gas_region._dlt_load_id as _root_dlt_load_id
from
    gas_region join gas_storage on gas_region._dlt_id = gas_storage._dlt_root_id
    left join
        gas_loading on gas_region._dlt_load_id = gas_loading._dlt_load_id_root
