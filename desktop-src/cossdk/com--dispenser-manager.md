---
description: The dispenser manager provides resource pooling for the resource dispensers and ensures that a resource supplied by a resource dispenser is correctly enlisted in the application objects transaction.
ms.assetid: c8986943-56a1-4668-9e80-7ab2a42333a8
title: COM+ Dispenser Manager
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Dispenser Manager

The dispenser manager provides resource pooling for the resource dispensers and ensures that a resource supplied by a resource dispenser is correctly enlisted in the application object's transaction. The dispenser manager automatically reclaims resources that are still reserved at the end of an object's lifetime, eliminating the possibility of resource "leaks." The dispenser manager can ask a resource dispenser to create a new resource or to destroy idle resources when necessary to adjust inventory levels, rather than using static settings.

> [!Note]  
> Because resource dispenser interfaces exposed to the application are not required to be COM interfaces, the dispenser manager can be used in a process without initializing COM, for example, to support the ODBC resource dispenser.

 

Upon resource creation, the resource dispenser may specify how long an idle resource is allowed to remain in the pool before it's destroyed. A thread that runs in the dispenser manager is always looking for these idle resources.

## The Inventory Statistics Manager

The dispenser manager uses the *inventory statistics manager* to manage pool resource inventory levels. The inventory statistics manager maintains a record of when each resource was used and removes resources from inventory when they have not been used for *x* seconds, where the value of *x* is set per resource when the resource is created.

## The Holder Component

The dispenser manager polls each *holder*, a component created by the dispenser manager that lists the resource inventory for each resource dispenser, every 10 seconds to allow it to readjust its resource inventory. Each holder calls the inventory statistics manager to suggest inventory levels for each type of resource. As a result, the holder may ask the resource dispenser to either create or destroy some inventory.

The holder and resource dispenser communicate to request resources of a particular type. The following relationships exist between the holder and resource dispenser:

-   The holder can request a resource from the resource dispenser. The resource dispenser either returns an available resource or creates a new one.
-   The holder can notify the resource dispenser that an application no longer needs a resource and then return it to the resource pool.
-   The holder and the resource dispenser work together to maintain the size of the resource pool.

## Related topics

<dl> <dt>

[COM+ Resource Dispenser Concepts](com--resource-dispenser-concepts.md)
</dt> </dl>

 

 



