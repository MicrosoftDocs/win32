---
description: MsiViewGetColumnInfo and the ColumnInfo Property of the View object use the following format to describe database column definitions.
ms.assetid: 77379664-26f2-4c1d-8c44-d9be2376efa9
title: Column Definition Format
ms.topic: article
ms.date: 05/31/2018
---

# Column Definition Format

[**MsiViewGetColumnInfo**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewgetcolumninfo) and the [**ColumnInfo Property**](view-columninfo.md) of the [**View**](view-object.md) object use the following format to describe database column definitions. Each column is described by a string in the corresponding record field returned by the function or property. The definition string consists of a single letter representing the data type followed by the width of the column (in characters when applicable, bytes otherwise). A width of zero designates an unbounded width (for example, long text fields and streams). An uppercase letter indicates that null values are allowed in the column.



| Column descriptor | Definition string                 |
|-------------------|-----------------------------------|
| s?                | String, variable length (?=1-255) |
| s0                | String, variable length           |
| i2                | Short integer                     |
| i4                | Long integer                      |
| v0                | Binary Stream                     |
| g?                | Temporary string (?=0-255)        |
| j?                | Temporary integer (?=0,1,2,4)     |
| O0                | Temporary object                  |



 

The strings used to describe columns have the following relationship to the SQL query strings used by CREATE and ALTER. For more information, see [SQL Syntax](sql-syntax.md).



| Returned value | SQL syntax                |
|----------------|---------------------------|
| s0             | LONGCHAR                  |
| l0             | LONGCHAR LOCALIZABLE      |
| s \#           | CHAR(\#)                  |
| s \#           | CHARACTER(\#)             |
| l \#           | CHAR(\#) LOCALIZABLE      |
| l \#           | CHARACTER(\#) LOCALIZABLE |
| i2             | SHORT                     |
| i2             | INT                       |
| i2             | INTEGER                   |
| i4             | LONG                      |
| v0             | OBJECT                    |



 

If the letter is not capitalized, the SQL statement should be appended with NOT NULL.



| Returned value | SQL syntax        |
|----------------|-------------------|
| s0             | LONGCHAR NOT NULL |



 

The installer does not internally limit the length of columns to the value specified by the column definition format. If the data entered into a field exceeds the specified column length, the package fails to pass [package validation](package-validation.md). To pass validation in this case, either the data or the database schema must be changed. The only means to change the column length of a standard table is by exporting the table using [**MsiDatabaseExport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseexporta), editing the exported .idt file, and then importing the table using [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta). Authors cannot change the column data types, nullability, or localization attributes of any columns in standard tables. Authors can create custom tables with columns having any column attributes.

When using [**MsiDatabaseMerge**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasemergea) to merge a reference database into a target database, the column names, number of primary keys, and column data types must match. **MsiDatabaseMerge** ignores the localization and column length attributes. If a column in the reference database has a length that is 0 or greater than the that column's length in the target database, **MsiDatabaseMerge** increases the column length in the target database to the length in the reference database.

When using Mergmod.dll version 2.0, the application of a merge module to a .msi file never changes the length of columns or the column types of an existing database table. The application of a merge module can however change the schema of an existing database table if the module adds new columns to a table for which it is valid to add columns. When using a Mergemod.dll version less than version 2.0, the application of a merge module never changes the length of columns and never changes the schema of the target database.

 

 



