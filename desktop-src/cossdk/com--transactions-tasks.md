---
description: COM+ Transactions Tasks
ms.assetid: fe4374f1-2452-4316-be57-b866c438404d
title: COM+ Transactions Tasks
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Transactions Tasks

While automatic transaction processing in COM+ allows you to spend more productive development time in creating and configuring objects that you want to participate in automatic transactions, there are some programming tasks you can perform to tailor transaction behavior to your application requirements.

The following topics discuss specific programming options related to transaction processing.



| Topic                                                                                             | Description                                                                                        |
|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [Setting the Transaction Attribute](setting-the-transaction-attribute.md)<br/>             | Describes how to set transaction attribute values for your transaction objects.<br/>         |
| [Setting the Transaction Isolation Level](setting-the-transaction-isolation-level.md)<br/> | Describes how to set the transaction isolation levels for your transaction objects.<br/>     |
| [Setting the Transaction Time-Out](setting-the-transaction-time-out.md)<br/>               | Describes how to set time-out intervals for your transactions.<br/>                          |
| [Setting the Consistent and Done Flags](setting-the-consistent-and-done-flags.md)<br/>     | Shows how to use the consistent and done flags to control the outcome of a transaction.<br/> |
| [Creating BYOT Objects](creating-byot-objects.md)<br/>                                     | Describes how to create objects so you can Bring Your Own Transaction (BYOT).<br/>           |



 

> [!Note]  
> As a general rule, any component that updates persistent state should support transactions. Components that combine the operations of two or more objects into a single task should use transactions to simplify error recovery. Also, to release resources, such as database connections, transactions in COM+ should be as short as you can make them.

 

## Related topics

<dl> <dt>

[COM+ Transactions Concepts](com--transactions-concepts.md)
</dt> </dl>

 

 




