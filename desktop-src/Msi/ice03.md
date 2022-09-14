---
description: ICE03 validates the data types and foreign keys based on the \_Validation table and the database tables in the .msi file.
ms.assetid: e9be1c09-8468-4956-9aa0-12383ade4718
title: ICE03
ms.topic: article
ms.date: 05/31/2018
---

# ICE03

ICE03 validates the data types and foreign keys based on the [\_Validation table](-validation-table.md) and the database tables in the .msi file.

## Result

ICE03 posts the following messages for the validation errors.



| ICE03 error message                                                       | Description                                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Duplicate Primary Key                                                     | The primary keys of a new row duplicates the primary keys of an existing row. The Nullable column of the [\_Validation table](-validation-table.md) shows the primary keys in the database.                                                                                              |
| Not A Nullable Column                                                     | A table column that is not specified as nullable in the Nullable column of the [\_Validation table](-validation-table.md) contains an entry that is Null.                                                                                                                                |
| Not A Valid Foreign Key                                                   | A column that is a foreign key into a second table contains an entry that does not exist in the primary key of the second table.                                                                                                                                                          |
| Value exceeds MaxValue                                                    | The numeric value of an entry in a database table exceeds the maximum limit specified for this field in the MaxValue column of the [\_Validation table](-validation-table.md).                                                                                                           |
| Value below MinValue                                                      | The numeric value of an entry in a database table is less than the minimum limit specified for this field in the MinValue column of the [\_Validation table](-validation-table.md).                                                                                                      |
| Value not a member of the set                                             | The value of an entry in a database table is not a member of the acceptable set of values specified for this field in the Set column of the [\_Validation table](-validation-table.md).                                                                                                  |
| Invalid version string                                                    | See the [Version](version.md) data type.                                                                                                                                                                                                                                                 |
| All UPPER case required                                                   | See the [UpperCase](uppercase.md) data type.                                                                                                                                                                                                                                             |
| Invalid GUID string                                                       | See the [GUID](guid.md) data type.                                                                                                                                                                                                                                                       |
| Invalid file name/usage of wildcards                                      | The database contains an invalid file name or an incorrect wildcard. See the [WildCardFilename](wildcardfilename.md) data type.                                                                                                                                                          |
| Invalid identifier                                                        | See the [Identifier](identifier.md) data type.                                                                                                                                                                                                                                           |
| Invalid Language Id                                                       | The database contains an invalid numeric Language Identifier (LANGID). See the [Language](language.md) data type. See [Language Identifier Constants and Strings](../intl/language-identifier-constants-and-strings.md). For example, 1033 for the U.S. and 0 for language neutral.<br/> |
| Invalid Filename                                                          | See the [Filename](filename.md) data type.                                                                                                                                                                                                                                               |
| Invalid full path                                                         | See the [Path](path.md), [AnyPath](anypath.md), and [Paths](paths.md) data types.                                                                                                                                                                                                      |
| Bad conditional string                                                    | The database contains an invalid conditional string. This is a text string that must evaluate to TRUE or FALSE according to the [Conditional Statement Syntax](conditional-statement-syntax.md). See the [Condition](condition.md) data type.                                           |
| Invalid format string                                                     | See the [Formatted](formatted.md) data type.                                                                                                                                                                                                                                             |
| Invalid template string                                                   | See the [Template](template.md) data type.                                                                                                                                                                                                                                               |
| Invalid DefaultDir string                                                 | See the [DefaultDir](defaultdir.md) data type.                                                                                                                                                                                                                                           |
| Invalid registry path                                                     | See the [RegPath](regpath.md) data type.                                                                                                                                                                                                                                                 |
| Bad CustomSource data                                                     | See the [CustomSource](customsource.md) data type.                                                                                                                                                                                                                                       |
| Invalid property string                                                   | See the [Property](property.md) data type.                                                                                                                                                                                                                                               |
| Missing data in \_Validation table or old Database                        | There are columns in the database that are not listed in the Column column of the [\_Validation table](-validation-table.md). The database and \_Validation table do not match                                                                                                           |
| Bad cabinet syntax/name                                                   | See the [Cabinet](cabinet.md) data type.                                                                                                                                                                                                                                                 |
| \_Validation table: Invalid category string                               | This is an error in authoring the \_Validation table. Validation does not recognize the category string used for this particular column in the \_Validation table. See [Column Data Types](column-data-types.md) and specify a valid category.                                           |
| \_Validation table: Data in KeyTable column is incorrect                  | The KeyTable column in the \_Validation table references a table that does not exist in the database.                                                                                                                                                                                     |
| \_Validation table: Value in MaxValue column < that in MinValue column | This is an error in authoring the [\_Validation table](-validation-table.md). Min must always be less than or equal to Max.                                                                                                                                                              |
| Bad shortcut target                                                       | See the [Shortcut](shortcut.md) data type.                                                                                                                                                                                                                                               |
| String overflow (greater than length permitted in column)                 | The string's length is greater than the column width specified by the column definition. Note that the installer does not internally limit the column width to the specified value. See [Column Definition Format](column-definition-format.md).                                         |
| Undefined error                                                           | Unknown error.                                                                                                                                                                                                                                                                            |
| Column cannot be localized                                                | Primary key columns cannot be localized.                                                                                                                                                                                                                                                  |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 
