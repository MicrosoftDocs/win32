---
description: Bring Your Own Transaction (BYOT)
ms.assetid: 492875cb-52a7-484f-810e-bd838373b603
title: Bring Your Own Transaction (BYOT)
ms.topic: article
ms.date: 05/31/2018
---

# Bring Your Own Transaction (BYOT)

BYOT allows a component to be created with or to inherit an external transaction. That is, a component that does not already have an associated transaction can acquire a transaction. Currently, MTS transactions are automatic; whether a component instance lives in a transaction is determined at creation time. The transactional attributes of a component and its creator determine what transaction is associated with a given instance. In all cases, MTS controls transaction lifetimes. COM+ extends this to allow setting an arbitrary pre-existing DTC or TIP transaction as the transaction property of a new component's context. This allows configured components to be associated with transactions whose lifetimes are controlled by a TP monitor, OTS, or DBMS.

> [!Note]  
> BYOT transactions must be used with caution. In certain situations, they can result in a transaction spanning multiple synchronization domains—that is, they allow parallelism with a transaction, causing a deadlock condition. Automatic transactions, rather than BYOT transactions, are the preferred programming model for writers of business components.

 

The interfaces for BYOT transactions include the [**ICreateWithTransactionEx**](/windows/desktop/api/ComSvcs/nn-comsvcs-icreatewithtransactionex) interface and the [**ICreateWithTipTransactionEx**](/windows/desktop/api/ComSvcs/nn-comsvcs-icreatewithtiptransactionex) interface. The **ICreateWithTransactionEx** interface creates an object that is enlisted within a manual transaction. The **ICreateWithTipTransactionEx** interface creates an object that is enlisted within a manual transaction using the Transaction Internet Protocol (TIP).

## Related topics

<dl> <dt>

[Inheriting Manual Transactions](inheriting-manual-transactions.md)
</dt> </dl>

 

 



