---
description: The ModuleSubstitution table specifies the configurable fields of a module database and provides a template for the configuration of each field.
ms.assetid: 8e94c31f-b3a7-4f3a-aec4-32b0e1dd5400
title: ModuleSubstitution Table
ms.topic: article
ms.date: 05/31/2018
---

# ModuleSubstitution Table

The ModuleSubstitution table specifies the configurable fields of a module database and provides a template for the configuration of each field. The user or merge tool may query this table to determine what configuration operations are to take place. This table is not merged into the target database.

The following tables cannot contain configurable fields and must not be listed in this table:

ModuleSubstitution table

[ModuleConfiguration table](moduleconfiguration-table.md)

[ModuleExclusion table](moduleexclusion-table.md)

[ModuleSignature table](modulesignature-table.md)

The ModuleSubstitution table has the following columns.



| Column | Type                         | Key | Nullable |
|--------|------------------------------|-----|----------|
| Table  | [Identifier](identifier.md) | Y   | N        |
| Row    | [Text](text.md)             | Y   | N        |
| Column | [Identifier](identifier.md) | Y   | N        |
| Value  | [Text](text.md)             | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Table"></span><span id="table"></span><span id="TABLE"></span>Table
</dt> <dd>

This column specifies the name of the table being modified in the module database.

</dd> <dt>

<span id="Row"></span><span id="row"></span><span id="ROW"></span>Row
</dt> <dd>

This field specifies the primary keys of the target row in the table named in the Table column. Multiple primary keys are separated by semicolons. Target rows are selected for modification before any changes are made to the target table. If one record in the ModuleSubstitution table changes the primary key field of a target row, other records in the ModuleSubstitution table are applied based on the original primary key data, not the resulting of primary key substitutions. The order of row substitution is undefined.

Values in this column are always in [CMSM special format](cmsm-special-format.md). A literal semicolon (';') or equal sign ('=') can be added by prefixing the character with a backslash. '\\'. A null value for a key is signified by a null, a leading semicolon, two consecutive semicolons, or a trailing semicolon, depending on whether the null value is a sole, first, middle, or final key column value.

</dd> <dt>

<span id="Column"></span><span id="column"></span><span id="COLUMN"></span>Column
</dt> <dd>

This field specifies the target column in the row named in the Row column. If multiple rows in the ModuleSubstitution table change different columns of the same target row, all the column substitutions are performed before the modified row is inserted into the database. The order of column substitution is undefined.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

This column contains a string that provides a formatting template for the data being substituted into the target field specified by Table, Row, and Column. When a substitution string of the form \[=ItemA\] is encountered, the string, including the bracket characters, is replaced by the value for the configurable "ItemA." The configurable item "ItemA" is specified in the Name column of the [ModuleConfiguration table](moduleconfiguration-table.md) and its value is provided by the merge tool. If the merge tool declines to provide a value for any item in a replacement string, the default value specified in the DefaultValue column of the ModuleConfiguration Table is substituted. If a string references an item not in the ModuleConfiguration table, the merge fails.

-   This column uses [CMSM special format](cmsm-special-format.md). A literal semicolon (';') or equals sign ('=') can be added to the table by prefixing the character with a backslash. '\\'.
-   The Value field may contain multiple substitution strings. For example, the configuration of items "Food1" and "Food2" in the string: "\[=Food1\] is good, but \[=Food2\] is better because \[=Food2\] is more nutritious."
-   Replacement strings must not be nested. The template "\[=AB\[=CDE\]\]" is invalid.
-   If the Value field evaluates to null, and the target field is not nullable, the merge fails and an error object of type msmErrorBadNullSubstitution is created and added to the error list. For details, see the error types described in [**get\_Type Function**](/windows/win32/api/mergemod/nf-mergemod-imsmerror-get_type).
-   If the Value field evaluates to the null GUID: {00000000-0000-0000-0000-000000000000}, the null GUID is replaced by the name of the feature before the row is merged into the module. For details, see [Referencing Features in Merge Modules](referencing-features-in-merge-modules.md).
-   The template in the Value field is evaluated before being inserted into the target field. Substitution into a row is done before replacing any features.
-   If the Value column evaluates to a string of only integer characters (with an optional + or -), the string is converted into an integer before being substituted into an target field of the [Integer Format Type](integer-format-types.md). If the template evaluates to a string that does not consist only of integer characters (and an optional + or -) the result cannot be substituted into an integer target field. Attempting to insert a non-integer into an integer field causes the merge to fail and adds a msmErrorBadSubstitutionType error object to the error list.
-   If the target column specified in the Table and Column fields is a [Text Format Type](text-format-types.md), and evaluation of the Value field results in an [Integer Format Type](integer-format-types.md), a decimal representation of the number is inserted into the target text field.
-   If the target field is an [Integer Format Type](integer-format-types.md), and the Value field consists of a non-delimited list of items in [Bitfield Format](bitfield-format-types.md), the value in the target field is combined using the bitwise **AND** operator with the inverse of the bitwise **OR** of all of the mask values from the items, then combined using the bitwise **OR** operator with each of the integer or bitfield items when masked by their corresponding mask values. Essentially, this explicitly sets the bits from the properties to the provided values but leaves all other bits in the cell alone.
-   If the Value field evaluates to a [Key Format Type](key-format-types.md), and is a key into a table that uses multiple primary keys, the item name may be followed by a semicolon and an integer value that indicates the 1-based index into the set of values that together make a primary key. If no integer is specified, the value 1 is used. For example, the [Control table](control-table.md) has two primary key columns, Dialog\_ and Control. The value of an item "Item1" that is a key into the Control table will be of the form "DialogName;ControlName", where DialogName is the value in the Dialog\_ table and ControlName is the value in the Control column. To substitute just ControlName, the substitution string \[=Item1;2\] should be used.

</dd> </dl>

## Remarks

The ModuleSubstition table is used by [Configurable Merge Modules](configurable-merge-modules.md). Mergemod.dll version 2.0 or later is required to create a configurable merge module.

To ensure compatibility with versions of Mergemod.dll earlier than version 2.0, the [ModuleConfiguration table](moduleconfiguration-table.md) and ModuleSubstitution tables should be included in the [ModuleIgnoreTable table](moduleignoretable-table.md) of every module.

 

 
