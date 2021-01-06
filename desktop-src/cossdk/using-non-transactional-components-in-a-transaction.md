---
description: Using Non-Transactional Components in a Transaction
ms.assetid: b83b4bab-1851-48dc-b35a-6467a6dff741
title: Using Non-Transactional Components in a Transaction
ms.topic: article
ms.date: 05/31/2018
---

# Using Non-Transactional Components in a Transaction

It is often useful to place non-transactional components into a transaction to take advantage of the [ACID properties](acid-properties.md) of transactions. For example, if you have non-transactional legacy components that you use to update passwords on a network, you can place those components in a transaction to ensure that password updates are consistent across the network.

The *transaction context object* is a generic object that allows non-transactional clients to combine the work of multiple COM objects into a single transaction, without requiring you to develop a new component specifically for that purpose. In contrast to an automatic transaction, the transaction context object requires its client to explicitly commit or abort the transaction.

By default, the transaction attribute value of the transaction context object is set to Required. COM+ aborts the transaction if the client releases the transaction context object without explicitly issuing a commit or abort call.

The following Visual Basic example shows how a non-transactional client can compose the work done by more than one object into a single transaction:


```VB
Dim objTxCtx As TransactionContext
Dim objCat As MyDLL.Ccat  ' Ccat is a user-defined component.
Dim objDog As MyDLL.Cdog  ' Cdog is a user-defined component.

' Get TransactionContext object.
Set objTxCtx = _
  CreateObject ("TxCtx.TransactionContext")

' Create instances of Cat and Dog.
Set objCat = _ 
  objTxCtx.CreateInstance ("MyDLL.Ccat")
Set objDog = _ 
  objTxCtx.CreateInstance ("MyDLL.Cdog")

' Both objects do work.
objDog.Bark
objCat.Hiss

' Commit the transaction.
objTxCtx.Commit

```



## Limitations of the Transaction Context Object

Following are some important limitations of the transaction context object:

-   When using a transaction context object, the application logic that combines the work of multiple objects into a single transaction is tied to a specific non-transactional client implementation and some advantages of using COM components are lost. These lost advantages include the following:
    -   Ability to reuse the application logic as part of an even larger transaction
    -   Imposition of declarative security
    -   Flexibility to run the logic remotely from the client
-   The transaction context object runs in-process with the non-transactional client, which means that COM+ must be available on the non-transactional client computer. This might not be a problem, for example, when the transaction context object is used from an Active Server Pages (ASP) page that is running on the same server as COM+.
-   You do not get a context for the non-transactional client when you create a transaction context object. Transactional work can only be done indirectly, through COM objects created by using the transaction context object. In particular, the non-transactional client cannot use COM+ resource dispensers (such as ODBC) and have the work included in the transaction. For example, developers may be familiar with the following syntax for doing transactional work on relational database systems:

    ``` syntax
    BEGIN TRANSACTION
      DoWork
    COMMIT TRANSACTION
    ```

    Using the transaction context object in a similar way does not yield the desired result:

    ``` syntax
    Set objTxCtx = CreateObject ("TxCtx.TransactionContext")
      DoWork
      objTxCtx.Commit
    Set objTxCtx = Nothing
    ```

    The call to DoWork in this example is not enlisted in a transaction. Instead, you must build a COM component that calls DoWork, create an object instance of that component using the transaction context object, and then call that object from the non-transactional client for the work to be part of the client-controlled transaction.

 

 



