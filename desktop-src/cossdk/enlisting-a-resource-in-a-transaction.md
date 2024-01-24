---
description: Enlisting a Resource in a Transaction
ms.assetid: b41fe0aa-a4cf-4d4a-9543-8eb0b38f07a2
title: Enlisting a Resource in a Transaction
ms.topic: article
ms.date: 05/31/2018
---

# Enlisting a Resource in a Transaction

After a resource is allocated, but just before returning the resource to the resource dispenser, the dispenser manager checks with COM+ to see whether the calling object is running within a transaction. If the calling object is running within a transaction, the dispenser manager calls back to the resource dispenser and asks it to enlist the resource in the transaction. Then the resource is returned to the resource dispenser, which then returns it to the calling instance.

The resource dispenser must be able to enlist in an OLE transaction with the Distributed Transaction Coordinator (DTC).

> [!Note]  
> Transaction enlistment is optional when a resource dispenser dispenses non-transactional resources, such as memory or threads.

 

When a transaction is complete, COM+ notifies the dispenser manager about whether it committed or aborted. Then the dispenser manager notifies each resource dispenser's holder that any resources enlisted in this transaction can now be moved to general inventory.

## Related topics

<dl> <dt>

[COM+ Resource Dispenser Concepts](com--resource-dispenser-concepts.md)
</dt> <dt>

[Pooled Resource States Available to COM+ Resource Dispenser](pooled-resource-states-available-to-com--resource-dispenser.md)
</dt> <dt>

[Resource Dispenser Resource Allocation Process](resource-dispenser-resource-allocation-process.md)
</dt> </dl>

 

 



