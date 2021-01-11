---
description: COM+ gives developers more control over their applications by allowing configurable transaction isolation levels.
ms.assetid: a59e262c-41f2-4c80-a04c-50a39af8b009
title: Configuring Transaction Isolation Levels
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Transaction Isolation Levels

COM+ gives developers more control over their applications by allowing configurable transaction isolation levels. Versions of COM+ prior to COM+ 1.5 always used the highest level of isolation for transactions. While this level guarantees that data integrity is always preserved, it can lead to performance issues, such as time-outs, when many transactions need to be performed on a large database. With configurable isolation levels, experienced developers can increase concurrency to improve performance and scalability.

COM+ provides the following transaction isolation levels.



| Level            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Serialized       | Data read by a current transaction cannot be changed by another transaction until the current transaction finishes. No new data can be inserted that would affect the current transaction. This is the safest isolation level and is the default.                                                                                                                                                                                                                                                                                                                                                    |
| Repeatable read  | Data read by a current transaction cannot be changed by another transaction until the current transaction finishes. Any type of new data can be inserted during a transaction.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Read committed   | A transaction cannot read data that is being modified by another transaction that has not committed. This is the default isolation level in Microsoft SQL Server.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Read uncommitted | A transaction can read any data, even if it is being modified by another transaction. This is the least safe isolation level but allows the highest concurrency.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Any              | Any isolation level is supported. This setting is most commonly used by downstream components to avoid conflicts. This setting is useful because any downstream component must be configured with an isolation level that is equal to or less than the isolation level of its immediate upstream component. Therefore, a downstream component that has its isolation level configured as Any always uses the same isolation level that its immediate upstream component uses. If the root object in a transaction has its isolation level configured to Any, its isolation level becomes Serialized. |



 

> [!Note]  
> If a downstream component is configured with a higher isolation level than an upstream component and attempts to enlist in a transaction, an error results and the transaction aborts.

 

## Related topics

<dl> <dt>

[Setting the Transaction Isolation Level](setting-the-transaction-isolation-level.md)
</dt> </dl>

 

 



