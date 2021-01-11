---
description: "Learn more about: Reading Data from the Database"
title: Reading Data from the Database
TOCTitle: Reading Data from the Database
ms:assetid: c3c48918-ccd6-4c34-849c-93bd7533ce92
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294080(v=EXCHG.10)
ms:contentKeyID: 32765695
ms.date: 04/11/2016
ms.topic: article
---

# Reading Data from the Database


_**Applies to:** Windows | Windows Server_

## Reading Data from the Database

Reading data from the database should be performed within a transaction.

The following procedure shows how to perform a simple read operation in the database.

### To read data from a database

1.  Call [JetBeginTransaction](./jetbegintransaction-function.md) or [JetBeginTransaction2](./jetbegintransaction2-function.md) with the session ID to start the transaction.

2.  Move the cursor to the desired record by calling [JetMove](./jetmove-function.md) with JET_MoveFirst in the *cRow* parameter. For more information on how to move the cursor, see the [Indexing in the Table](./indexing-in-the-table.md) topic.

3.  Call [JetGetTableColumnInfo](./jetgettablecolumninfo-function.md) on the current record with JET_ColInfo specified in the *InfoLevel* parameter to retrieve the column ID for the column. The column ID is returned in the [JET_COLUMNDEF](./jet-columndef-structure.md) structure.

4.  Read the data from the column by calling [JetRetrieveColumn](./jetretrievecolumn-function.md) with the column ID retrieved in step 3 in the columnid parameter. The *pvData* parameter contains the type of data specified in the [JET_COLUMNDEF](./jet-columndef-structure.md) structure retrieved in step 3.

5.  Call [JetCommitTransaction](./jetcommittransaction-function.md) to commit the transaction to the database.
