---
description: When authoring an installation package, you can use the MsiViewModify function or the View.Modify method to ensure that the data you enter is syntactically correct.
ms.assetid: c960e9df-dcd6-44d2-8662-40a1dea81f45
title: Internal Validation
ms.topic: article
ms.date: 05/31/2018
---

# Internal Validation

When authoring an installation package, you can use the [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify) function or the View.Modify method to ensure that the data you enter is syntactically correct. For more information, see [**Modify method**](view-modify.md). At the lowest level, a database table's column can store integers (short or long), strings, or binary data. However, an installation package requires specific integers or strings in certain tables. These specifications are maintained in the [\_Validation table](-validation-table.md). For example, the FileName column of the [File table](file-table.md) is a string column, but it specifically stores a file name. Therefore, not only should your entry be a string, but it should also follow the requirements for naming files.

The various validation enum values used with the [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify) function allow for immediate validation at different levels. The MSIMODIFY\_VALIDATE\_FIELD enum can be used to validate individual fields of a record. It does not validate foreign keys. The MSIMODIFY\_VALIDATE enum validates an entire row and includes foreign key validation. If you are inserting a new row into a table, use the MSIMODIFY\_VALIDATE\_NEW enum to verify that you are adding valid data as well as using unique primary keys. An insert fails if the primary keys are not unique. If a call to **MsiViewModify** with one of the validation enums returns an error, you can make repeated calls to [**MsiViewGetError**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewgeterrora) for diagnosing the problem. **MsiViewGetError** indicates the column where the error occurred as well as the enum value to help fix the problem. For more information, see [**GetError method**](view-geterror.md).

You can also use internal validation to ensure that other authors enter data correctly into your custom table. Add each of the columns of your custom table to the \_Validation table using the custom table name and column name as the primary key. Provide a description or purpose of each column in the Description column of the \_Validation table. Enter the applicable requirements for each column using the Nullable, MinValue, MaxValue, KeyTable, KeyColumn, Category, and Set columns:

-   If the column is Nullable, enter a 'Y'. If not, enter a 'N'.
-   If the column is an integer column and can contain a range of integers, enter that range using the MinValue and MaxValue columns.
-   Foreign key columns are identified using the KeyTable and KeyColumn columns.
-   For string columns, specify a Category such as Filename, GUID, or Identifier. For more information, see [column data types](column-data-types.md).
-   If the data can only pertain to a specific number of values (string or integer), use the Set column to list the acceptable values.

The following is a list of the columns (in addition to Table, Column, and Description) in the \_Validation table that can be filled in if your column is of the specified type. (Note that you do not have to fill in all the columns.)



| Type    | Columns                                                          |
|---------|------------------------------------------------------------------|
| Integer | Nullable, MinValue, MaxValue, KeyTable, KeyColumn, Set           |
| String  | Nullable, KeyTable, KeyColumn, Category, Set, MinValue, MaxValue |
| Binary  | Nullable, Category (Category must be "Binary")                   |



 

Authoring environments may make use of MSIMODIFY\_VALIDATE\_DELETE. This enum assumes that you want to delete the row. No field or foreign key validation is performed. This enum actually performs a reverse foreign key validation. It checks the \_Validation table for references in the KeyTable and KeyColumn columns for the table to which the "deleted" row belongs. If there are columns that list the table containing the "deleted" row as a potential foreign key, it cycles through that column to see if any of the values reference values in the "deleted" row. An error return means that you break the relational integrity of the database by deleting the row.

 

 



