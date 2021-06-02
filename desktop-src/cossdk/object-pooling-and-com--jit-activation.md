---
description: COM+ JIT activation essentially strikes a compromise between greedy clients and greedy servers for the sake of getting optimal performance. Clients get to keep object references, while servers can more closely manage memory utilization.
ms.assetid: 125d39f5-af38-4a87-a649-2f77a3e77c27
title: Object Pooling and COM+ JIT Activation
ms.topic: article
ms.date: 05/31/2018
---

# Object Pooling and COM+ JIT Activation

COM+ JIT activation essentially strikes a compromise between greedy clients and greedy servers for the sake of getting optimal performance. Clients get to keep object references, while servers can more closely manage memory utilization.

You can refine this further by using [COM+ Object Pooling](com--object-pooling.md). By pooling objects that are JIT activated, you can dedicate a certain amount of memory to hold a certain number of objects active in memory, ready for immediate reuse. This makes the most sense when objects are expensive to create, as in the case where they hold multiple resources.

Pooling JIT-activated objects in this manner, you can achieve the following benefits:

-   Greatly accelerated object reactivation times.
-   Reuse of any expensive resources the objects are holding.
-   More precise governing of memory and resource use for the pooled objects.
-   Retention of administrative flexibility so that your application can scale to use available resources and adapt to changing performance requirements.

## Related topics

<dl> <dt>

[COM+ Just-in-Time Activation Concepts](com--just-in-time-activation-concepts.md)
</dt> <dt>

[COM+ Object Pooling](com--object-pooling.md)
</dt> <dt>

[Enabling JIT Activation for a Component](enabling-jit-activation-for-a-component.md)
</dt> <dt>

[Transactions and COM+ JIT Activation](transactions-and-com--jit-activation.md)
</dt> </dl>

 

 



