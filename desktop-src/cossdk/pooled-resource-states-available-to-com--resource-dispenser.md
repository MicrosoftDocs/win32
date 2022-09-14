---
description: Pooled Resource States Available to COM+ Resource Dispenser
ms.assetid: 5037f11c-d113-49b0-b26f-0e3bc59ae8b3
title: Pooled Resource States Available to COM+ Resource Dispenser
ms.topic: article
ms.date: 05/31/2018
---

# Pooled Resource States Available to COM+ Resource Dispenser

At any one time, a resource is either in use or not in use and is either enlisted or not enlisted in a transaction. This yields four possible resource states, as follows:

-   **Resources in unenlisted inventory.** A resource that is not in use by an object and not enlisted in a transaction is in unenlisted inventory. A resource in general inventory is available for assignment.

-   **Resources in enlisted inventory.** A resource that is not in use by an object but is enlisted in a transaction is in enlisted inventory. Such a resource is available for assignment only to objects running in the same transaction. A resource moves from enlisted inventory to unenlisted inventory when COM+ notifies the dispenser manager that the transaction is complete.

-   **Resources in unenlisted use.** If a resource is assigned to an object and the instance is not running in a transaction or the resource dispenser has identified the resource as non-transactional, this resource is in unenlisted use.

-   **Resources in enlisted use.** If a resource is assigned to an object, the instance is running in a transaction, and the resource dispenser has successfully enlisted the resource in the transaction, this resource is in enlisted use.

## Related topics

<dl> <dt>

[COM+ Resource Dispenser Concepts](com--resource-dispenser-concepts.md)
</dt> <dt>

[Enlisting a Resource in a Transaction](enlisting-a-resource-in-a-transaction.md)
</dt> </dl>

 

 



