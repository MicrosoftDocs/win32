---
description: Types Used in COM+ Resource Dispenser Interfaces
ms.assetid: f4b3a828-3d66-455c-9b0c-30086f3ffe23
title: Types Used in COM+ Resource Dispenser Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Types Used in COM+ Resource Dispenser Interfaces

The following types are used in the resource dispenser interfaces.



| Type           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **RESTYPID**   | A **DWORD** that identifies a type of resource, not a particular resource. A **RESTYPID** is usually a pointer to a structure in the dispenser's memory that describes the resource type. The dispenser manager does not understand (and does not need to understand) this structure within the resource dispenser's memory. The dispenser manager uses **RESTYPID** only to refer to a resource type within a resource dispenser.                                                                                                                                   |
| **RESID**      | A **DWORD** that identifies a particular resource, as opposed to a type of resource. A **RESID** is usually a (**void \***) that points to a structure in the resource dispenser's memory that represents the resource. The dispenser manager does not need to understand this structure within the resource dispenser's memory. The dispenser manager uses **RESID** to refer to a particular resource within a resource dispenser.                                                                                                                                 |
| **SRESID**     | A Unicode string version of **RESID**, used in the [**IHolder::TrackResourceS**](/windows/desktop/api/ComSvcs/nf-comsvcs-iholder-trackresources) and [**IHolder::UntrackResourceS**](/windows/desktop/api/ComSvcs/nf-comsvcs-iholder-untrackresources) methods. Strings are sometimes useful when only a small amount of information needs to be recorded about a resource and the entire description of the resource can be contained in the **SRESID**. In particular, using the **SRESID** can sometimes eliminate the need for a map in the resource dispenser when the resource represents a relationship between two (or more) things. |
| **TRANSID**    | Identifies a transaction. This type may be cast to the **ITransaction** interface.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **TIMEINSECS** | Indicates how long a resource can be inactive before it is destroyed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |



 

## Related topics

<dl> <dt>

[COM+ Resource Dispenser Concepts](com--resource-dispenser-concepts.md)
</dt> <dt>

[COM+ Resource Dispenser Interfaces](com--resource-dispenser-interfaces.md)
</dt> </dl>

 

 



