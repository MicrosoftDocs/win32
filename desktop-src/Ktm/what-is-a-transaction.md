---
description: 'A transaction is a group of operations that have the following properties: atomic, consistent, isolated, and durable (ACID).'
ms.assetid: b3da52a3-1c52-4577-a997-7e72ebc03fa8
title: What is a Transaction?
ms.topic: article
ms.date: 05/31/2018
---

# What is a Transaction?

A transaction is a group of operations that have the following properties: atomic, consistent, isolated, and durable (ACID). The support of transactions enables new types of applications to be developed, while simplifying the development process and making the application more robust. The remainder of this topic provides scenarios that demonstrate the need for these properties, then a table that defines each property.

In an *atomic* group of operations, either every operation in the group must succeed, or the effects of all of them must be undone (also known as *rolling back*). For example, a bank transfer must be an atomic set of two operations: a debit from one account and a credit to another account. The debit and credit must be implemented as an atomic group. If those two operations do not both succeed, then the transfer is either unfairly in favor of the bank or the account holder.

The requirement of *consistency* means that the data is consistent after the transaction (assuming that we started with a consistent system before the transaction). For the bank transfer example, consistency may be defined as having the combined account balance of the two accounts be a constant. To implement consistency in the bank transfer example, the debit and credit operations simply need to be for the same amount of money.

Another example of a transaction is an update to a website. An electronic commerce site requires that a new product category navigation page to appear at exactly the same time as the product detail pages that describe the new products. In this case, there is a need to update and add multiple directory entries under the control of a transaction. Not only is it necessary to have the updates be atomic, but it is also necessary that a customer who is currently shopping must not see the updates in progress. This is an example of the *isolation* property of transactions.

The property of *durability* requires that after an update is finished, its effects persist even if the system stops responding. In the previous example, durability can be provided simply by ensuring adequate data recovery so that all new file system entries that represent the addition of a new product to the site appear after a system stops responding. This requires a system with data backup, recovery, and high availability mechanisms.

The guarantee of the atomicity of a transaction, as well as the other properties, is present in the face of any number of failures, including failures that occur during the recovery phase of a prior failure. Eventually the system will reach either one of two states: all operations have been applied or none of the operations have been applied.

The properties of a transaction are summarized in the following table.



| Term                                                                                                         | Description                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| <span id="Atomic"></span><span id="atomic"></span><span id="ATOMIC"></span>Atomic<br/>                 | Either all of the operations in the transaction succeed or none of the operations persist.<br/>                             |
| <span id="Consistent"></span><span id="consistent"></span><span id="CONSISTENT"></span>Consistent<br/> | If the data are consistent before the transaction begins, then they will be consistent after the transaction finishes.<br/> |
| <span id="Isolated_"></span><span id="isolated_"></span><span id="ISOLATED_"></span>Isolated <br/>     | The effects of a transaction that is in progress are hidden from all other transactions.<br/>                               |
| <span id="Durable"></span><span id="durable"></span><span id="DURABLE"></span>Durable<br/>             | When a transaction finishes, its results are persistent and will survive a system crash.<br/>                               |



 

These properties ensure that software can handle unexpected errors, because it can simply abort a transaction when an unexpected situation prevents a successful completion. The transaction infrastructure ensures that all the effects of the aborted transaction are rolled back, returning the data to a consistent state. Therefore, a transactional system enables a graceful recovery from system failures.

To guarantee the ACID properties, a system that supports transactions must have a robust logging capability that can be used to commit or roll back transactions as necessary. For more information, see [Common Log File System](/previous-versions/windows/desktop/clfs/common-log-file-system-portal).

 

