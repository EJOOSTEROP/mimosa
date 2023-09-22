with


gas_region as (
    select
        *
    from
        {{ source('gie_stage', 'storage') }} r
),

gas_country as (
    select
        t.gas_day_start::DATE gas_day_start,
        t.code,
        t.name,
        TRY_CAST(t.consumption as DOUBLE) as consumption,
        TRY_CAST(t.consumption_full as DOUBLE) as consumption_full,
        t._dlt_id as _country_dlt_id,
        t._dlt_root_id
    from
        {{ source('gie_stage', 'storage__children') }} t
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
    gas_country.*,
    year(gas_country.gas_day_start)::INTEGER as reporting_year,
    make_date(2000, month(gas_country.gas_day_start), day(gas_country.gas_day_start)) as reporting_day,
    gas_region._dlt_load_id as _root_dlt_load_id
from
    gas_region join gas_country on gas_region._dlt_id = gas_country._dlt_root_id
    left join
        gas_loading on gas_region._dlt_load_id = gas_loading._dlt_load_id_root