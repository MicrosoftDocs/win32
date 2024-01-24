---
description: The \_Streams table lists embedded OLE data streams. This is a temporary table, created only when referenced by a SQL statement.
ms.assetid: 1e30472d-6ba5-410a-a81b-07ed225dcb69
title: '_Streams Table'
ms.topic: article
ms.date: 05/31/2018
---

# \_Streams Table

The \_Streams table lists embedded OLE data streams. This is a temporary table, created only when referenced by a SQL statement.



| Column | Type                 | Key | Nullable |
|--------|----------------------|-----|----------|
| Name   | [Text](text.md)     | Y   | N        |
| Data   | [Binary](binary.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

A unique key that identifies the stream. The maximum length of Name is 62 characters.

</dd> <dt>

<span id="Data"></span><span id="data"></span><span id="DATA"></span>Data
</dt> <dd>

The unformatted binary data.

</dd> </dl>

## Remarks

To copy an OLE data stream (for example, an object of the [Binary](binary.md) data type) from a file into a database, create a record in the \_Streams table and enter the name of the data stream into the Name column of this record and copy the data from the file into the Data column using [**MsiRecordSetStream**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetstreama). Use [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify) to insert the new record into the table.

To read a binary data stream embedded in a database, use a SQL query to find and to fetch the record containing the binary data. Use [**MsiRecordReadStream**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordreadstream) to read the binary data into a buffer.

To move a binary data stream from one database to another, first export the data to a file. Use a SQL query to find the data stream in the file and use [**MsiRecordSetStream**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetstreama) to copy the data from the file into Data column of \_Streams table of the second database. This ensures that each database has its own copy of the binary data. You cannot move binary data from one database to another simply by fetching a record with the data from the first database and inserting it into the second database.

To delete a data stream, fetch the record and set the Data column to null before updating the record. Another method is to remove the record from the table, deleting it using either [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify) or a plain SQL query. A stream should not be fetched into a record if the stream is deleted from the table.

To rename an OLE data stream, update the 'Name' column of the record.

If a hold is placed on this table using SQL (ALTER TABLE <table> HOLD) or a column is added with HOLD, the table must be released using FREE. Streams are not written until the table has been released or committed.

 

 



