---
description: In the COM+ programming model, you can design your components to do what they do best&\#8212;enabling business logic or establishing a database connection&\#8212;and rely on the transaction processing framework of Microsoft Windows to automate transactions.
ms.assetid: 50086e6e-024b-4a09-b8be-8f55b6bfadb2
title: Managing Automatic Transactions in COM+
ms.topic: article
ms.date: 05/31/2018
---

# Managing Automatic Transactions in COM+

In the COM+ programming model, you can design your components to do what they do best—enabling business logic or establishing a database connection—and rely on the transaction processing framework of Microsoft Windows to automate transactions.

## Starting a Transaction

COM+ automatically begins a transaction when it encounters either of the following conditions:

-   When a non-transactional client calls a component that requires a transaction or requires a new transaction.
-   When a transactional client calls a component that requires a new transaction.

If COM+ determines that an object should have a new transaction, it begins the transaction first and then places the object in it. The process includes the following steps:

1.  COM+ creates a context object, sets both the [JIT activation](com--just-in-time-activation.md) and [Synchronization](com--synchronization.md) attributes to Required, and sets the [consistent and done flags](consistent-and-done-flags.md) to True and False, respectively.
2.  COM+ communicates with the Distributed Transaction Coordinator (DTC) to begin a transaction. The DTC coordinates the physical transaction.
3.  The DTC generates a transaction identifier and passes it back to COM+. The transaction identifier establishes a transaction boundary. All objects participating in the transaction share the same identifier.
4.  When the client creates the object, COM+ activates it within the transaction boundary.

## Ending a Transaction

COM+ ends an automatic transaction by committing or aborting it when one of the following conditions occurs:

-   The root object of the transaction completes its work and COM+ releases it. After the root object deactivates, the transaction attempts to commit.
-   The client releases the root object. Without a reference, the root object deactivates and the transaction attempts to commit.
-   The transaction exceeds its time-out threshold. The transaction aborts automatically if not committed within the transaction time-out period, deactivating all objects associated with the transaction. The default transaction time-out period is 60 seconds.

## Related topics

<dl> <dt>

[Consistent and Done Flags](consistent-and-done-flags.md)
</dt> <dt>

[Speeding Transactions by Notifying the Root Object](speeding-transactions-by-notifying-the-root-object.md)
</dt> <dt>

[Terminating an Automatic Transaction by Calling SetComplete](terminating-an-automatic-transaction-by-calling-setcomplete.md)
</dt> </dl>

 

 



