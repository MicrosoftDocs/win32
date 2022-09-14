---
description: Coined by transaction processing pioneers, the acronym ACID stands for atomic, consistent, isolated, and durable.
ms.assetid: 857d145c-710d-4097-8ed6-df11e8d52228
title: ACID Properties
ms.topic: article
ms.date: 05/31/2018
---

# ACID Properties

Coined by transaction processing pioneers, the acronym ACID stands for atomic, consistent, isolated, and durable. To ensure predictable behavior, all transactions must possess these basic properties, reinforcing the role of mission-critical transactions as all-or-none propositions.

The following list contains a definition and a description of each ACID property:

<dl> <dt>

<span id="Atomic"></span><span id="atomic"></span><span id="ATOMIC"></span>Atomic
</dt> <dd>

A transaction must execute exactly once and must be atomic—either all of the work is done or none of it is. Operations within a transaction usually share a common intent and are interdependent. By performing only a subset of these operations, the system could compromise the overall intent of the transaction. Atomicity eliminates the chance of processing only a subset of operations.

</dd> <dt>

<span id="Consistent"></span><span id="consistent"></span><span id="CONSISTENT"></span>Consistent
</dt> <dd>

A transaction must preserve the consistency of data, transforming one consistent state of data into another consistent state of data. Much of the responsibility for maintaining consistency falls to the application developer.

</dd> <dt>

<span id="Isolated"></span><span id="isolated"></span><span id="ISOLATED"></span>Isolated
</dt> <dd>

A transaction must be a unit of isolation, which means that concurrent transactions should behave as if each were the only transaction running in the system. Because a high degree of isolation can limit the number of concurrent transactions, some applications reduce the isolation level in exchange for better throughput. See [Configuring Transaction Isolation Levels](configuring-transaction-isolation-levels.md) for more information.

</dd> <dt>

<span id="Durable"></span><span id="durable"></span><span id="DURABLE"></span>Durable
</dt> <dd>

A transaction must be recoverable and therefore must have durability. If a transaction commits, the system guarantees that its updates can persist even if the computer crashes immediately after the commit. Specialized logging allows the system's restart procedure to complete unfinished operations required by the transaction, making the transaction durable.

</dd> </dl>

 

 



