with storage as (
    select * from stage_gas_staging.storage__children__children__children
)

select * from storage
