-- script that creates a function SafeDiv
-- that divides (and returns) the
-- first by the second number or returns 0

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT DETERMINISTIC
BEGIN   
    DECLARE result FLOAT;

    IF b != 0 THEN
        SET result = a / b;
    ELSE
        SET result = 0;
    END IF;

    RETURN result;
END;

//

DELIMITER ;
