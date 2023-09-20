select * from
    stage_gas._load_info as a right join stage_gas._load_info__loads_ids as b
    on a._dlt_id = b._dlt_parent_id

