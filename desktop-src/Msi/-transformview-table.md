---
description: This is a read-only temporary table used to view transforms with the transform view mode. This table is never persisted by the installer.
ms.assetid: 4763ac0e-900f-45f1-bee5-34d413c5e401
title: '_TransformView Table'
ms.topic: article
ms.date: 05/31/2018
---

# \_TransformView Table

This is a read-only temporary table used to view transforms with the transform view mode. This table is never persisted by the installer.

To invoke the transform view mode, obtain a handle and open the reference database. See [Obtaining a Database Handle](obtaining-a-database-handle.md). Call [**MsiDatabaseApplyTransform**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseapplytransforma) with MSITRANSFORM\_ERROR\_VIEWTRANSFORM. This stops the transform from being applied to the database and dumps the transform contents into the \_TransformView table. The data in the table can be accessed using SQL queries. See [Working with Queries](working-with-queries.md).

The \_TransformView table is not cleared when another transform is applied. The table reflects the cumulative effect of successive applications. To view the transforms separately you must release the table.

The \_TransformView Table has the following columns.



| Column  | Type                         | Key | Nullable |
|---------|------------------------------|-----|----------|
| Table   | [Identifier](identifier.md) | Y   | N        |
| Column  | [Text](text.md)             | Y   | N        |
| Row     | [Text](text.md)             | Y   | Y        |
| Data    | [Text](text.md)             | N   | Y        |
| Current | [Text](text.md)             | N   | Y        |



 

## Column

<dl> <dt>

<span id="Table"></span><span id="table"></span><span id="TABLE"></span>Table
</dt> <dd>

Name of an altered database table.

</dd> <dt>

<span id="Column"></span><span id="column"></span><span id="COLUMN"></span>Column
</dt> <dd>

Name of an altered table column or INSERT, DELETE, CREATE, or DROP.

</dd> <dt>

<span id="Row"></span><span id="row"></span><span id="ROW"></span>Row
</dt> <dd>

A list of the primary key values separated by tabs. Null primary key values are represented by a single space character. A Null value in this column indicates a schema change.

</dd> <dt>

<span id="Data"></span><span id="data"></span><span id="DATA"></span>Data
</dt> <dd>

Data, name of a data stream, or a column definition.

</dd> <dt>

<span id="Current"></span><span id="current"></span><span id="CURRENT"></span>Current
</dt> <dd>

Current value from reference database, or column a number.

</dd> </dl>

## Remarks

The \_TransformView is held in memory by a lock count, that can be released with the following SQL command.

"ALTER TABLE \_TransformView FREE".

The data in the table can be accessed using SQL queries. The SQL language has two main divisions: Data Definition Language (DDL) that is used to define all the objects in an SQL database, and Data Manipulation Language (DML) that is used to select, insert, update, and delete data in the objects defined using DDL.

The Data Manipulation Language (DML) transform operations are indicated as follows. Data Manipulation Language (DML) are those statements in SQL that manipulate, as opposed to define, data.



| Transform operation | SQL result                                    |
|---------------------|-----------------------------------------------|
| Modify data         | {table} {column} {row} {data} {current value} |
| Insert row          | {table} "INSERT" {row} NULL NULL              |
| Delete row          | {table} "DELETE" {row} NULL NULL              |



 

The Data Definition Language (DDL) transform operations are indicated as follows. Data Definition Language (DDL) are those statements in SQL that define, as opposed to manipulate, data.



| Transform operation | SQL result                                   |
|---------------------|----------------------------------------------|
| Add column          | {table} {column} NULL {defn} {column number} |
| Add table           | {table} "CREATE" NULL NULL NULL              |
| Drop table          | {table} "DROP" NULL NULL NULL                |



 

When the application of a transform adds this table, the Data field receives text that can be interpreted as a 16-bit integer value. The value describes the column named in the Column field. You can compare the integer value to the constants in the following table to determine the definition of the altered column.



| Bit                                                                                                       | Description                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Bits_07"></span><span id="bits_07"></span><span id="BITS_07"></span>Bits 0 7<br/>         | Hexadecimal: 0x0000 0x0100<br/> Decimal: 0 255<br/> Column width<br/>                                                                                                                                                                                                                                  |
| <span id="Bit_8"></span><span id="bit_8"></span><span id="BIT_8"></span>Bit 8<br/>                  | Hexadecimal: 0x0100<br/> Decimal: 256<br/> A persistent column. Zero means a temporary column. <br/>                                                                                                                                                                                                   |
| <span id="Bit_9"></span><span id="bit_9"></span><span id="BIT_9"></span>Bit 9<br/>                  | Hexadecimal: 0x0200<br/> Decimal: 1023<br/> A localizable column. Zero means the column cannot be localized.<br/>                                                                                                                                                                                      |
| <span id="Bits_1011"></span><span id="bits_1011"></span><span id="BITS_1011"></span>Bits 10 11<br/> | Hexadecimal: 0x0000<br/> Decimal: 0<br/> Long integer<br/> Hexadecimal: 0x0400<br/> Decimal: 1024<br/> Short integer<br/> Hexadecimal: 0x0800<br/> Decimal: 2048<br/> Binary object<br/> Hexadecimal: 0x0C00<br/> Decimal: 3072<br/> String<br/> |
| <span id="Bit_12"></span><span id="bit_12"></span><span id="BIT_12"></span>Bit 12<br/>              | Hexadecimal: 0x1000<br/> Decimal: 4096<br/> Nullable column. Zero means the column is non-nullable.<br/>                                                                                                                                                                                               |
| <span id="Bit_13"></span><span id="bit_13"></span><span id="BIT_13"></span>Bit 13<br/>              | Hexadecimal: 0x2000<br/> Decimal: 8192<br/> Primary key column. Zero means this column is not a primary key.<br/>                                                                                                                                                                                      |
| <span id="Bits_1415"></span><span id="bits_1415"></span><span id="BITS_1415"></span>Bits 14 15<br/> | Hexadecimal: 0x4000 0x8000<br/> Decimal: 16384 32768<br/> Reserved<br/>                                                                                                                                                                                                                                |



 

For a script sample that demonstrates the \_TransformView table, see [View a Transform](view-a-transform.md).

 

 




