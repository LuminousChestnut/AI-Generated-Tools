-- 分区
ALTER TABLE table_name PARTITION BY RANGE (column_name) (
    PARTITION p0 VALUES LESS THAN (1991),
    PARTITION p1 VALUES LESS THAN (1992),
    ...
);

-- 创建视图
CREATE VIEW view_name AS
SELECT column1, column2 FROM table1 INNER JOIN table2 ON table1.id = table2.id;

-- 创建索引
CREATE INDEX idx_column_name ON table_name (column_name);

-- 查询分析
EXPLAIN SELECT * FROM users WHERE user_id = '12345';
