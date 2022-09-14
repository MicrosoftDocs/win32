---
description: The SQL query strings for Windows Installer are restricted to the following formats.
ms.assetid: badee528-fa69-43ab-965e-d9e6f2529b99
title: SQL Syntax
ms.topic: article
ms.date: 05/31/2018
---

# SQL Syntax

The SQL query strings for Windows Installer are restricted to the following formats.



| Action                             | Query                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select a group of records          | SELECT \[DISTINCT\]{column-list} FROM {table-list} \[WHERE {operation-list}\] \[ORDER BY {column-list}\]                                                                                                                                                                                                                                                                                                                                                                                                       |
| Delete records from a table        | DELETE FROM {table} \[WHERE {operation-list}\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Modify existing records in a table | UPDATE {table-list} SET {column}= {constant} \[, {column}= {constant}\]\[, ...\] \[WHERE {operation-list}\]UPDATE queries only work on nonprimary key columns.<br/>                                                                                                                                                                                                                                                                                                                                      |
| Add records to a table             | INSERT INTO {table} ({column-list}) VALUES ({constant-list}) \[TEMPORARY\]Binary data cannot be inserted into a table directly using the INSERT INTO or UPDATE SQL queries. For more information, see [Adding Binary Data to a Table Using SQL](adding-binary-data-to-a-table-using-sql.md).<br/>                                                                                                                                                                                                       |
| Add a table                        | CREATE TABLE {table} ( {column} {column type}) \[HOLD\]Column types must be specified for each column when adding a table. At least one primary key column must be specified for the creation of a new table. The possible substitutions for {column type} in the above are: CHAR \[( {size} )\] \| CHARACTER \[( {size} )\] \| LONGCHAR \| SHORT \| INT \| INTEGER \| LONG \| OBJECT \[NOT NULL\] \[TEMPORARY\] \[LOCALIZABLE\] \[, column...\]\[, ...\] PRIMARY KEY column \[, column\]\[, ...\].<br/> |
| Remove a table                     | DROP TABLE {table}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Add a column                       | ALTER TABLE {table} ADD {column} {column type}The column type must be specified when adding a column. The possible substitutions for {column type} in the above are: CHAR \[( {size} )\] \| CHARACTER \[( {size} )\] \| LONGCHAR \| SHORT \| INT \| INTEGER \| LONG \| OBJECT \[NOT NULL\] \[TEMPORARY\] \[LOCALIZABLE\] \[HOLD\].<br/>                                                                                                                                                                  |
| Hold and free temporary tables     | ALTER TABLE {table name} HOLDALTER TABLE {table name} FREE<br/> The user can use the commands HOLD and FREE to control the life span of a temporary table or a temporary column. The hold count on a table is incremented for every SQL HOLD operation on that table and decremented for every SQL FREE operation on the table. When the last hold count is released on a table, all temporary columns become inaccessible. If all columns are temporary, the table becomes inaccessible.<br/>     |



 

For more information, see [Examples of Database Queries Using SQL and Script](examples-of-database-queries-using-sql-and-script.md).

### SQL Grammar

The optional parameters are shown enclosed in brackets \[ \]. When several choices are listed, the optional parameters are separated by a vertical bar.

A {constant} is either a string or an integer. A string must be enclosed in single quote marks 'example'. A {constant-list} is a comma-delimited list of one or more constants.

The LOCALIZABLE option sets a column attribute that indicates the column needs to be localized.

A {column} is a columnar reference to a value in a field of a table.

A {marker} is a parameter reference to a value supplied by a record submitted with the query. It is represented in the SQL statement by a question mark ?. For information regarding the use of parameters, see either the [**MsiViewExecute**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewexecute) function or the [**Execute**](view-execute.md) method.

The Windows Installer SQL syntax does not support the escaping of single-quotes (ASCII value 39) in a string literal. However, you can fetch or create the record, set the field with the [**StringData**](record-stringdata.md) or [**IntegerData**](record-integerdata.md) property, and then call the [**Modify**](view-modify.md) method. Alternatively, you can create a record and use the parameter markers (?) described in [**Execute**](view-execute.md) method. You can also do this using the database functions [**MsiViewExecute**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewexecute), [**MsiRecordSetInteger**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetinteger), and [**MsiRecordSetString**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetstringa).

A WHERE {operation-list} clause is optional and is a grouping of operations to be used to filter the selection. The operations must be of the following types:

-   {column} = {column}
-   {column} = \| <> \| > \| < \| >= \| <= {constant}
-   {column} = \| <> \| > \| < \| >= \| <= {marker}
-   {column} is null
-   {column} is not null

For string values, only the = or <> operations are possible. Object value comparisons are limited to IS NULL and IS NOT NULL.

Individual operations can be grouped by AND or OR operators. Ordering can be imposed by use of parentheses ( ).

The ORDER BY clause is optional and causes an initial delay during sorting. Ordering by strings will group identical strings together, but it will not alphabetize the strings.

The DISTINCT clause is optional and does not repeat identical records in the returned result set.

A {table-list} is a comma-delimited list of one or more table names referred to as {table} in the join.

A {column-list} is a comma-delimited list of one or more table columns referred to as {column} selected. Ambiguous columns may be further qualified as {tablename.column}. An asterisk may be used as a column-list in a SELECT query to represent all columns in the referenced tables. When referencing fields by column position, select the columns by name instead of using the asterisk. An asterisk cannot be used as a column-list in an INSERT INTO query.

To escape table names and column names that clash with SQL keywords, enclose the name between two grave accent marks \`\` (ASCII value 96). If a column name must be escaped and is qualified as {tablename.column}, then the table and the column must be escaped individually as {\`tablename\`.\`column\`}. It is recommended that all table names and column names be escaped in this fashion to avoid clashes with reserved words and gain significant performance.

Table names are limited to 31 characters. For more information, see [Table Names](table-names.md). Table and column names are case-sensitive. SQL keywords are not case-sensitive.

The maximum number of expressions in a WHERE clause of a SQL query is limited to 32.

Only inner joins are supported and are specified by a comparison of columns from different tables. Circular joins are not supported. A circular join is a SQL query that links three or more tables together into a circuit. For example, the following is a circular join:

``` syntax
WHERE Table1.Field1=Table2.Field1 AND Table2.Field2=Table3.Field1 AND Table3.Field2=Table1.Field2.
```

Columns that are part of the primary key(s) for a table must be defined first in priority order, followed by any nonprimary key columns. Persistent columns must be defined before temporary columns. The sort sequence of a text column is undefined; however, identical text values always group together.

Note that when adding or creating a column, you must specify the column type.

Tables may not contain more than one column of type 'object'.

The maximum size that can be explicitly specified for a string column in a SQL query is 255. A string column of infinite length is represented as having size 0. For more information, see [Column Definition Format](column-definition-format.md).

To execute any SQL statement, a view must be created. However, a view that does not create a result set, such as CREATE TABLE, or INSERT INTO, cannot be used with [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify) or the [**Modify**](view-modify.md) method to update tables though the view.

Note that you cannot fetch a record containing binary data from one database and then use that record to insert the data into a completely different database. To move binary data from one database to another, you should export the data to a file and then import it into the new database through a query and the [**MsiRecordSetStream**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetstreama) function. This ensures that each database has its own copy of the binary data.

 

 




