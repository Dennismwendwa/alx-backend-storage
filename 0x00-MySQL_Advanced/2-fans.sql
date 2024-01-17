-- Script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans
CREATE TEMPORARY TABLE IF NOT EXISTS tmp_fans as (
    SELECT origin, COUNT(*) AS nb_fans
    FROM metal_bands
    GROUP BY origin
);

-- Ranking the countries based on number of funs
SELECT origin, nb_fans
FROM tmp_fans
ORDER BY nb_fans DESC;
