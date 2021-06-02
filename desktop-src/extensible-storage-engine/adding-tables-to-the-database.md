---
description: "Learn more about: Adding Tables to the Database"
title: Adding Tables to the Database
TOCTitle: Adding Tables to the Database
ms:assetid: 176d4fea-c856-441b-bd58-165b37c35095
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269195(v=EXCHG.10)
ms:contentKeyID: 32765498
ms.date: 04/11/2016
ms.topic: article
---

# Adding Tables to the Database


_**Applies to:** Windows | Windows Server_

## Adding Tables to the Database

Tables are a heterogeneous collection of records that physically and logically group the data in the database. Tables are uniquely identified by their name. The table ID ([JET_TABLEID](./jet-tableid.md)) is a handle to a cursor that is used to update and navigate tables. You may open multiple [JET_TABLEID](./jet-tableid.md) on the same table.

An existing table is opened in the call to [JetOpenTable](./jetopentable-function.md), and a new table is created without rows or columns with [JetCreateTable](./jetcreatetable-function.md). To atomically create a table with an initial set of columns and indices, call [JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md) or [JetCreateTableColumnIndex2](./jetcreatetablecolumnindex2-function.md). The initial size of the table is given in the *lPages* parameter in [JetCreateTable](./jetcreatetable-function.md) or the **ulPages** member of the [JET_TABLECREATE](./jet-tablecreate-structure.md) structure in the call to [JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md). Tables grow automatically when data is added to the table. The growth is proportional to the initial size of the table. Columns may be added to the table at any time with [JetAddColumn](./jetaddcolumn-function.md). When the application no longer needs to access the table, the cursor can be closed with [JetCloseTable](./jetclosetable-function.md). The table may be deleted via a call to [JetDeleteTable](./jetdeletetable-function.md).

Table operations should be performed within the context of a transaction.

## See Also

[Transactions](./transactions.md)
