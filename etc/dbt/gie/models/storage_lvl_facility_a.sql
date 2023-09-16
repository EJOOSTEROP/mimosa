with storage as (
    select * from
    {{ source('gie_stage', 'storage__children__children__children') }} t
)
select * from storage