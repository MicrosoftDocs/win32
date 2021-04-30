---
description: The StopServices action stops system services. This action queries the ServiceControl table.
ms.assetid: 1ad01205-f8b6-400f-be1d-c00a5b71ccfd
title: StopServices Action
ms.topic: article
ms.date: 05/31/2018
---

# StopServices Action

The StopServices action stops system services. This action queries the [ServiceControl table](servicecontrol-table.md).

## Sequence Restrictions

The services actions must be used in the following sequence:

-   StopServices
-   [DeleteServices](deleteservices-action.md)

Any of the following actions:

-   [InstallFiles](installfiles-action.md)
-   [RemoveFiles](removefiles-action.md)
-   [DuplicateFiles](duplicatefiles-action.md)
-   [MoveFiles](movefiles-action.md)
-   [PatchFiles](patchfiles-action.md)
-   [RemoveDuplicateFiles](removeduplicatefiles-action.md)
-   [InstallServices](installservices-action.md)
-   [StartServices](startservices-action.md)

## ActionData Messages



| Field | Description of action data |
|-------|----------------------------|
| \[1\] | Service display name.      |
| \[2\] | Service name.              |



 

## Remarks

This action requires that the user be an administrator or have elevated privileges with permission to control services or that the application be part of a managed installation.

 

 



