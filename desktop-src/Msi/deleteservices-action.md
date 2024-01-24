---
description: The DeleteServices action stops a service and removes its registration from the system. This action queries the ServiceControl table.
ms.assetid: c7976de9-65f4-4552-8f8c-e7a32ef4821d
title: DeleteServices Action
ms.topic: article
ms.date: 05/31/2018
---

# DeleteServices Action

The DeleteServices action stops a service and removes its registration from the system. This action queries the [ServiceControl table](servicecontrol-table.md).

## Sequence Restrictions

The services actions must be used in the following sequence:

1.  [StopServices](stopservices-action.md)
2.  DeleteServices
3.  Any of the following actions: [InstallFiles](installfiles-action.md), [RemoveFiles](removefiles-action.md), [DuplicateFiles](duplicatefiles-action.md), [MoveFiles](movefiles-action.md), [PatchFiles](patchfiles-action.md), and [RemoveDuplicateFiles](removeduplicatefiles-action.md) actions.
4.  [InstallServices action](installservices-action.md)
5.  [StartServices](startservices-action.md)

## ActionData Messages



| Field | Description of action data |
|-------|----------------------------|
| \[1\] | Service display name.      |
| \[2\] | Service name.              |



 

## Remarks

This action requires the user be an administrator or have elevated privileges with permission to delete services or that the application be part of a managed installation.

 

 



