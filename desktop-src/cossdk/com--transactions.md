---
description: COM+ Transactions
ms.assetid: 40eccce1-a362-4adc-8060-f6923b9162c9
title: COM+ Transactions
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Transactions

When you purchase a book from an online bookstore, you use a credit card to trade money for a book. After you submit your order, a series of related operations (validation of your credit card, verification of inventory availability, and so forth) ensures that you get the book and that the bookstore gets your money. If a single operation in the series fails during the exchange, the entire exchange fails. You do not get the book, and the bookstore does not get your money.

The technology responsible for making this online exchange balanced and predictable is called *transaction processing*. Programmatically, a *transaction* is a unit of work in which a series of operations occur. COM+ uses programmatic transactions to ensure that resources are not permanently updated unless all operations within the transaction complete successfully. By binding a set of related operations together in a COM+ transaction that either completely succeeds or completely fails, you can vastly simplify error recovery.

The following topics introduce general transaction processing theory, provide a closer look at transactions in COM+, and present practical tips for writing transactional components.



| Topic                                                                   | Description                                                                    |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [COM+ Transactions Concepts](com--transactions-concepts.md)<br/> | Presents basic terms and concepts.<br/>                                  |
| [COM+ Transactions Tasks](com--transactions-tasks.md)<br/>       | Provides practical information on writing transactional components.<br/> |



 

 

 




