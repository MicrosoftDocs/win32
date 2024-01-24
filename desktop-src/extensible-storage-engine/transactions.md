---
description: "Learn more about: Transactions (Windows Events)"
title: Transactions (Windows Events)
TOCTitle: Transactions
ms:assetid: 1ceb362c-1efe-439b-b10a-016c8a54f27b
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269197(v=EXCHG.10)
ms:contentKeyID: 32765500
ms.date: 04/11/2016
ms.topic: article
---

# Transactions (Windows Events)


_**Applies to:** Windows�| Windows Server_

## Transactions

ESE transactions are logical units of processing that control how an application sees and manipulates rows in the database. Your application can use transaction save points to determine whether to keep or discard a particular set of changes to the database. All transactions in ESE are atomic, consistent, isolated, and durable (ACID) as described below:

  - **Atomic:** All the updates in the transaction either appear in the database or they are discarded.

<!-- end list -->

  - **Consistent:** The database will always start in a legal state and will always end in another legal state. For ESE applications, the database engine will control some simple constraints, for example uniqueness of a unique index, but the application itself will define almost all other aspects of what it means for the database to be in a legal state.

<!-- end list -->

  - **Isolation:** Transactions are isolated from updates by other sessions. A transaction will never see a partial set of changes made by another transaction.

<!-- end list -->

  - **Durable:** After the database engine acknowledges that a transaction has been committed, its changes are persistent in the database. The durability of a transaction may be optionally waived for performance reasons.

Transactions are performed within the bounds of the calls to [JetBeginTransaction](./jetbegintransaction-function.md) and [JetCommitTransaction](./jetcommittransaction-function.md) or [JetRollback](./jetrollback-function.md). When the application enters the transaction, the database appears frozen at the instance in time that the transaction begins. This is called snapshot isolation. If the transaction is terminated by calling [JetRollback](./jetrollback-function.md), none of the operations performed in the transaction are committed to the database. If the process or the machine crashes before [JetCommitTransaction](./jetcommittransaction-function.md) is called, it is the same as calling [JetRollback](./jetrollback-function.md).

This procedure shows how to start and commit a transaction that reads and updates data in a database.

### To start and commit a transaction

1.  Call [JetBeginTransaction](./jetbegintransaction-function.md) or [JetBeginTransaction2](./jetbegintransaction2-function.md) with the session ID to start the transaction.

2.  Move the cursor to the desired record by calling [JetMove](./jetmove-function.md) with JET_MoveFirst specified in the *cRow* parameter. For more information on how to move the cursor, see the [Indexing in the Table](./indexing-in-the-table.md) topic.

3.  Call [JetGetTableColumnInfo](./jetgettablecolumninfo-function.md) on the current record with JET_ColInfo specified in the *InfoLevel* parameter to retrieve the column ID for the column. The column ID is returned in the [JET_COLUMNDEF](./jet-columndef-structure.md) structure.

4.  Call [JetSetColumn](./jetsetcolumn-function.md) with the session ID, table ID, and column ID of the column that is updated. The column data is contained in the *pvData* parameter.

5.  Call [JetCommitTransaction](./jetcommittransaction-function.md) to commit the transaction to the database.

The way in which an ESE database engine implements snapshot isolation has some important differences from traditional relational database isolation and locking models. When a transaction reads a row, it can always access the row without failing or waiting for other sessions to release a lock. When a transaction attempts to update a row, it will succeed if it is the first session to update that row, that is the first writer wins. If the session is not the first writer then it will immediately fail with a write conflict error. The session must then abort its transaction, wait (usually via a random delay), for the other transaction to commit its changes, and then retry the transaction. The database engine will not automatically cause that session to wait until the other transaction has finished its update. Usually, a transaction will test if it can update a row inside of the [JetUpdate](./jetupdate-function.md) call. If it cannot lock the row for update then [JetUpdate](./jetupdate-function.md) will fail with JET_errWriteConflict.

Sessions are limited to one thread from the time the transaction starts to the end of the transaction. It is recommended that all update and retrieve operations be performed in a transaction. ESE also supports schema modifications such as creating tables and adding columns inside the transaction. Both update and schema modifications can be performed in the same transaction. After the transaction completes with [JetCommitTransaction](./jetcommittransaction-function.md), the update is logged in the transaction log file. These files can be used to maintain a logically consistent state in the event of an unexpected process termination or system shutdown.

Transactions may be nested up to 7 levels with matching calls to [JetBeginTransaction](./jetbegintransaction-function.md) and [JetCommitTransaction](./jetcommittransaction-function.md) or [JetRollback](./jetrollback-function.md) nested within each other. This allows the application to rollback a part of the transaction without having to back out of the entire transaction. The nested call to [JetCommitTransaction](./jetcommittransaction-function.md) signifies that this level of processing is complete; however, the transaction is not committed to the database until the outer most call to commit the transaction with [JetCommitTransaction](./jetcommittransaction-function.md).

Escrow update columns can be updated concurrently by multiple sessions without failing with Jet_errWriteConflict. The [JetEscrowUpdate](./jetescrowupdate-function.md) function may only be called on escrow columns, columns that were created with Jet_bitColumnEscrowUpdate.
