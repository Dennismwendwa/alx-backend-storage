-- script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes and store the
-- average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;

    --SELECT 0 INTO total_score;
    --SELECT 0 INTO total_weight;

    SELECT IFNULL(SUM(corrections.score * projects.weight), 0) INTO total_score
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = p_user_id;

    SELECT IFNULL(SUM(projects.weight), 0) INTO total_weight
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = p_user_id;

    UPDATE users
    SET average_score = IF(total_weight > 0, total_score / total_weight, 0)
    WHERE id = p_user_id;
END;

//

DELIMITER ;
