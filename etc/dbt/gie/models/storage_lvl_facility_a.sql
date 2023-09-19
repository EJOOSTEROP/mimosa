with storage as (
    select
        null _sdc_batched_at,
        null _sdc_extracted_at,
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
        split_part(url, '/', 3) as company_likely
    from
        {{ source('gie_stage', 'storage__children__children__children') }} t
)
select * from storage