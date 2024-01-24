---
description: The \_Storages table lists embedded OLE data storages. This is a temporary table, created only when referenced by a SQL statement.
ms.assetid: b2f2907d-6966-4b63-9589-c1580f8db574
title: '_Storages Table'
ms.topic: article
ms.date: 05/31/2018
---

# \_Storages Table

The \_Storages table lists embedded OLE data storages. This is a temporary table, created only when referenced by a SQL statement.



| Column | Type                 | Key | Nullable |
|--------|----------------------|-----|----------|
| Name   | [Text](text.md)     | Y   | N        |
| Data   | [Binary](binary.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

A unique key that identifies the storage. The maximum length of Name is 31 characters.

</dd> <dt>

<span id="Data"></span><span id="data"></span><span id="DATA"></span>Data
</dt> <dd>

The unformatted binary data.

</dd> </dl>

## Remarks

To add an OLE storage to a database, create a new record in the \_Storages table and enter the name of the storage into the Name column. Use [**MsiRecordSetStream**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetstreama) to copy data into the Data column of this record. Finally, use [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify) to insert the record into the \_Storages table.

Data cannot be read from the \_Storages table. However, the \_Storages table can be queried to check for the existence of a specific storage. This means that it is not possible to move an OLE storage from one database to another. You must instead import the original storage file into the new database.To delete an OLE storage, fetch the record containing the binary data, set the Data column in the \_Storages table to null, and then update the record. An alternative method is to simply delete the record using either [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify) or a plain SQL query.

To rename an OLE storage, update the Name column of the record.

If a hold is placed on this table using SQL (ALTER TABLE <table> HOLD) or a column is added with HOLD, the table must be released using FREE. Storages are not written until the table has been released or committed.

 

 



