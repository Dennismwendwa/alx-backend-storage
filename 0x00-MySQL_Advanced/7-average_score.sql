-- script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(p_user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;

    SELECT 0 INTO total_score;
    SELECT 0 INTO total_projects;

    SELECT
        SUM(score) INTO total_score
        FROM corrections
        WHERE corrections.user_id = p_user_id;
        
    SELECT
        COUNT(*) INTO total_projects
        FROM corrections
        WHERE corrections.user_id = p_user_id;

    UPDATE users
    SET users.average_score = IF(total_projects > 0, total_score / total_projects, 0)
    WHERE users.id = p_user_id;
END;

//

DELIMITER ;
