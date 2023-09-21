select
    a.started_at,
    b.value as _dlt_load_id_root
from
        {{ source('gie_stage', '_load_info') }} as a
    right join
        {{ source('gie_stage', '_load_info__loads_ids') }} as b
    on
        a._dlt_id = b._dlt_parent_id

