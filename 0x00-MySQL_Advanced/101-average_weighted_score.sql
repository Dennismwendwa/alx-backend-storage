-- script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers that computes and
-- store the average weighted score for all students

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS US,
        (SELECT US.id, SUM(score * weight) / SUM(weight) AS avg_weight
        FROM users AS US
        JOIN corrections as CORRE ON US.id = CORRE.user_id
        JOIN projects AS PROJ ON CORRE.project_id = PROJ.id
        GROUP BY US.id)
    AS WIN
    SET US.average_score = WIN.avg_weight
    WHERE US.id = WIN.id;
END;

//

DELIMITER ;
