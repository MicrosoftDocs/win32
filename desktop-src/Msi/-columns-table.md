---
description: The \_Columns table is a read-only system table that contains the column catalog. It lists the columns for all the tables. You can query this table to find out if a given column exists.
ms.assetid: 1ddde4e2-90a9-4dd8-a4f9-b6802d0b11cf
title: '_Columns Table'
ms.topic: article
ms.date: 05/31/2018
---

# \_Columns Table

The \_Columns table is a read-only system table that contains the column catalog. It lists the columns for all the tables. You can query this table to find out if a given column exists.

The \_Columns table has the following columns.



| Column | Type                   | Key | Nullable |
|--------|------------------------|-----|----------|
| Table  | [Text](text.md)       | Y   | N        |
| Number | [Integer](integer.md) | Y   | N        |
| Name   | [Text](text.md)       | N   | N        |



 

## Columns

<dl> <dt>

<span id="Table"></span><span id="table"></span><span id="TABLE"></span>Table
</dt> <dd>

The name of the table that contains the column.

</dd> <dt>

<span id="Number"></span><span id="number"></span><span id="NUMBER"></span>Number
</dt> <dd>

The order of the column within the table.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

The name of the column.

</dd> </dl>

## Remarks

Because the \_Columns table is a system table that cannot be modified through SQL queries, you cannot obtain the primary keys with the [**MsiDatabaseGetPrimaryKeys**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasegetprimarykeysa) function or the [**PrimaryKeys property**](database-primarykeys.md).

Only persistent columns are stored in the \_Columns table. To determine if a temporary column exists one would need to create a view using a SELECT \* statement against the table, then loop through all fields in a record returned by the [**MsiViewGetColumnInfo**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewgetcolumninfo) function with the MSICOLINFO\_NAMES option.

 

 



