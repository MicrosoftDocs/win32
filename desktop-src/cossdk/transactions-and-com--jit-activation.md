---
description: Transactions and COM+ JIT Activation
ms.assetid: f7fad383-4081-4a49-aa03-59861fcefc97
title: Transactions and COM+ JIT Activation
ms.topic: article
ms.date: 05/31/2018
---

# Transactions and COM+ JIT Activation

COM+ JIT Activation is closely bound to automatic transactions. When you configure a component so that it requires a transaction or requires a new transaction, JIT Activation is automatically enabled as well. The two features naturally work in conjunction. Transactional, JIT-activated components share the following characteristics:

-   Statelessness. You would not hold state that would violate transaction isolation nor would you hold state that would be lost on object deactivation.

-   Rapid use. The canonical use pattern for an object performing work in an automatic transaction is to do some small unit of work, vote, and exit.

    > [!Note]  
    > The ways that you vote in COM+ transactions and signal doneness for JIT Activation are also closely bound together. For more information, see [Setting the Done Bit](setting-the-done-bit.md).

     

-   Repeated use. When transactional work is properly broken up, clients use the same objects over and over to perform little parcels of atomic work.

-   Deactivated on commit or abort. In COM+, all objects within the transaction boundary are deactivated when the transaction commits or aborts.

In conjunction with COM+ transactional components, JIT activation serves as a big performance enhancement by keeping the channel open as clients hold long-lived references to transactional objects. As further enhancements, you can elect to pool the transactional objects to reuse the resources they hold, speed object reactivation time, and closely manage how you use memory resources for given objects.

## Related topics

<dl> <dt>

[COM+ Just-in-Time Activation Concepts](com--just-in-time-activation-concepts.md)
</dt> <dt>

[Enabling JIT Activation for a Component](enabling-jit-activation-for-a-component.md)
</dt> <dt>

[Object Pooling and COM+ JIT Activation](object-pooling-and-com--jit-activation.md)
</dt> </dl>

 

 



