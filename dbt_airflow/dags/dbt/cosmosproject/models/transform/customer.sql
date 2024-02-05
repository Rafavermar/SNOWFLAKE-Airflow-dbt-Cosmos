SELECT UUID_STRING() AS id_uuid
    , ID
    , FIRST_NAME
    , LAST_NAME
    , birthdate
FROM {{ ref('customers') }}