---
description: The \_Validation table is a system table that contains the column names and the column values for all of the tables in the database.
ms.assetid: 52b1c537-efb6-4bb8-9e7f-b4848be52a71
title: '_Validation Table'
ms.topic: article
ms.date: 05/31/2018
---

# \_Validation Table

The \_Validation table is a system table that contains the column names and the column values for all of the tables in the database. It is used during the database validation process to ensure that all columns are accounted for and have the correct values. This table is not shipped with the installer database.

The \_Validation table has the following columns.



| Column      | Type                               | Key | Nullable |
|-------------|------------------------------------|-----|----------|
| Table       | [Identifier](identifier.md)       | Y   | N        |
| Column      | [Identifier](identifier.md)       | Y   | N        |
| Nullable    | [Text](text.md)                   | N   | N        |
| MinValue    | [DoubleInteger](doubleinteger.md) | N   | Y        |
| MaxValue    | [DoubleInteger](doubleinteger.md) | N   | Y        |
| KeyTable    | [Identifier](identifier.md)       | N   | Y        |
| KeyColumn   | [Integer](integer.md)             | N   | Y        |
| Category    | [Text](text.md)                   | N   | Y        |
| Set         | [Text](text.md)                   | N   | Y        |
| Description | [Text](text.md)                   | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Table"></span><span id="table"></span><span id="TABLE"></span>Table
</dt> <dd>

Used to identify a particular table. This key and the Column key form the primary key of the \_Validation table.

</dd> <dt>

<span id="Column"></span><span id="column"></span><span id="COLUMN"></span>Column
</dt> <dd>

Used to identify a particular column of the table. This key and the Table key form the primary key of the \_Validation table.

</dd> <dt>

<span id="Nullable"></span><span id="nullable"></span><span id="NULLABLE"></span>Nullable
</dt> <dd>

Identifies whether the column may contain a Null value.

This column may have one of the following values.



| String | Meaning                                   |
|--------|-------------------------------------------|
| Y      | Yes, the column may have a Null value.    |
| N      | No, the column may not have a Null value. |



 

</dd> <dt>

<span id="MinValue"></span><span id="minvalue"></span><span id="MINVALUE"></span>MinValue
</dt> <dd>

This field applies to columns having numeric value. The field contains the minimum permissible value. This can be the minimum value for an integer or the minimum value for a date or version string.

</dd> <dt>

<span id="MaxValue"></span><span id="maxvalue"></span><span id="MAXVALUE"></span>MaxValue
</dt> <dd>

This field applies to columns having numeric value. The field is the maximum permissible value. This may be the maximum value for an integer or the maximum value for a date or version string.

</dd> <dt>

<span id="KeyTable"></span><span id="keytable"></span><span id="KEYTABLE"></span>KeyTable
</dt> <dd>

This field applies to columns that are external keys. The field identified in Column must link to the column number specified by KeyColumn in the table named in KeyTable. This can be a list of tables separated by semicolons.

</dd> <dt>

<span id="KeyColumn"></span><span id="keycolumn"></span><span id="KEYCOLUMN"></span>KeyColumn
</dt> <dd>

This field applies to table columns that are external keys. The field identified in Column must link to the column number specified by KeyColumn in the table named in KeyTable. The permissible range of the KeyColumn field is 1-32.

</dd> <dt>

<span id="Category"></span><span id="category"></span><span id="CATEGORY"></span>Category
</dt> <dd>

This is the type of data contained by the database field specified by the Table and Column columns of the \_Validation table. If this is a type having a numeric value, such as [Integer](integer.md), [DoubleInteger](doubleinteger.md) or [Time/Date](time-date.md), then enter null into this field and specify the value's range using the MinValue and MaxValue columns. Use the Category column to specify the non-numeric data types described in [Column Data Types](column-data-types.md).

</dd> <dt>

<span id="Set"></span><span id="set"></span><span id="SET"></span>Set
</dt> <dd>

This is a list of permissible values for this field separated by semicolons. This field is usually used for enumerations.

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

A description of the data that is stored in the column.

</dd> </dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
</dl>

## Remarks

The Category field of this table only applies to string data. If the Column field refers to a column with binary data, the binary data type must be specified in the Category field. Integer data Column types ignore the Category field during validation.

 

 



