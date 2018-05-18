---
Description: 'A transaction is an object that defines a logical unit of work.'
ms.assetid: '29661a58-ada9-4b7c-8d85-ab65b824c7cd'
title: Transactions
---

# Transactions

A transaction is an object that defines a logical unit of work. The transaction is alive as long as there is a handle referencing the transaction and it is considered active if the transaction has not yet been committed or rolled back. If a transaction is created and all handles to it have been closed before a commit or rollback occurs, the transaction will be rolled back.

Consider the case of a user-mode transactional client that creates a transaction to scope its operations, then performs updates on one or more resource managers. The following occurs:

1.  The client calls the [**CreateTransaction**](createtransaction.md) function to create the transaction and receives a handle to that transaction as the return value.

    The transaction can be opened or inherited by any number of processes; each process is thus involved in the transaction. The failure of any of these processes will cause the transaction to abort.

    This transaction may not yet be persistent. Only transactions that have reached the prepared state must be recovered across system failures if the transaction uses presumed-abort logging.

2.  The client must pass a transaction to the resource manager explicitly.
3.  The client performs all its transactional operations with one or more RMs, such as transacted file systems.
4.  The client calls the [**CommitTransaction**](committransaction.md) function.
5.  The resource manager receives notifications from KTM to prepare and commit its data.

## Transactions and Threads

Transactions are not the same as threads. Multiple threads or processes can be a part of a single transaction. Conversely, a thread can be a part of several different transactions at different times.

## Transaction Functions

The following functions are used with transactions.



| Function                                                            | Description                                                                                   |
|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [**CommitTransaction**](committransaction.md)                      | Requests that the specified transaction be committed.                                         |
| [**CommitTransactionAsync**](committransactionasync.md)            | Requests that the specified transaction be committed.                                         |
| [**CreateTransaction**](createtransaction.md)                      | Creates a new transaction object.                                                             |
| [**GetTransactionInformation**](gettransactioninformation-func.md) | Returns the requested information about the specified transaction.                            |
| [**OpenTransaction**](opentransaction.md)                          | Opens an existing transaction.                                                                |
| [**RollbackTransaction**](rollbacktransaction.md)                  | Requests that the specified transaction be rolled back.                                       |
| [**RollbackTransactionAsync**](rollbacktransactionasync.md)        | Requests that the specified transaction be rolled back. This function returns asynchronously. |
| [**SetTransactionInformation**](settransactioninformation.md)      | Sets the transaction information for the specified transaction.                               |



 

 

 



