---
description: A transaction is a series of modifications of a data store (such as a database or a file system) guaranteed either to be all successfully executed or not to be executed at all.
ms.assetid: 1567d9d3-7839-42f0-9507-7bbf61d8eaf2
title: Transactional Message Queuing
ms.topic: article
ms.date: 05/31/2018
---

# Transactional Message Queuing

A *transaction* is a series of modifications of a data store (such as a database or a file system) guaranteed either to be all successfully executed or not to be executed at all. To implement a transaction, a record is kept of the state of the data store before the transaction begins and, if one of the modifications fails, the transaction returns failure and the initial state is restored (or rolled back). Transactions are used to maintain data integrity and consequently play an important role in business software programming.

Often, applications can be developed using a business transaction or workflow that is split into several smaller transactions or activities. These activities are separated in time and then connected using reliable message queues.

1.  The first transaction involves the order entry database. [Message Queuing](/previous-versions/windows/desktop/legacy/ms711472(v=vs.85)) moves the message from one queue to another queue, exactly one time, using transaction capabilities. If the database is updated, there is a message on the queue. If the message doesn't reach the queue, it is aborted and the database is rolled back.
2.  Sometime later, Message Queuing discovers that the server is available. There is no application polling for the existence of the server. This is the second transaction.
3.  The third transaction involves a shipping database query and the update of the shipping database. If the server fails in the middle of this transaction, the modification is rolled back and the message is returned to the input queue. This ensures that the integrity of the data and databases is maintained during the transactions.

 

 



