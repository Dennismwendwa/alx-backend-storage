-- script that lists all bands with Glam rock as their main style
-- ranked by their longevity
CREATE TEMPORARY TABLE IF NOT EXISTS tmp_glam_rock_lifespan AS (
    SELECT
        band_name,
        IFNULL((YEAR('2022-01-17') - FORMED), 0) AS lifespan
    FROM
        metal_bands
    WHERE
        style = 'Glam rock'
);

-- list Gram rock bands ranked by lifespan
SELECT
    band_name,
    lifespan
FROM
    tmp_glam_rock_lifespan
ORDER BY
    lifespan DESC;
