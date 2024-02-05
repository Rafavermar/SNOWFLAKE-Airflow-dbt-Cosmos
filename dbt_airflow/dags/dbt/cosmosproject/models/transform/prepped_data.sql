SELECT
    UUID_STRING() AS id_uuid,
    A.ID,
    FIRST_NAME,
    LAST_NAME,
    birthdate,
    BOOKING_REFERENCE,
    HOTEL,
    BOOKING_DATE,
    COST
FROM {{ ref('customer') }} A
JOIN {{ ref('combined_bookings') }} B
ON A.ID = B.ID
