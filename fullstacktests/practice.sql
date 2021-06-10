CREATE TABLE users(
    firstname  VARCHAR(100) NOT NULL,
    lastname   VARCHAR(100) NOT NULL,
    address     VARCHAR(100) NOT NULL,
    cityid     INT FOREIGN KEY REFERENCES city(id)
    )

CREATE TABLE cities(
    id      INT PRIMARY KEY,
    name    VARCHAR(100) NOT NULL
)

SELECT c.id, c.name, COUNT(u)
FROM city as c, users as u
WHERE u.cityid = c.id
GROUP BY c.id
ORDER BY COUNT(u) DESC;
-- dsf