---
description: The StartServices action starts system services. This action queries the ServiceControl table.
ms.assetid: 53791b1c-5fd5-45d8-817b-098566ab4f9c
title: StartServices Action
ms.topic: article
ms.date: 05/31/2018
---

# StartServices Action

The StartServices action starts system services. This action queries the [ServiceControl table](servicecontrol-table.md).

## Sequence Restrictions

The services actions must be used in the following sequence:

-   [StopServices](stopservices-action.md)
-   [DeleteServices](deleteservices-action.md)

Any of the following actions:

-   [InstallFiles](installfiles-action.md)
-   [RemoveFiles](removefiles-action.md)
-   [DuplicateFiles](duplicatefiles-action.md)
-   [MoveFiles](movefiles-action.md)
-   [PatchFiles](patchfiles-action.md)
-   [RemoveDuplicateFiles](removeduplicatefiles-action.md)
-   [InstallServices](installservices-action.md)
-   StartServices

## ActionData Messages



| Field | Description of action data |
|-------|----------------------------|
| \[1\] | Service display name.      |
| \[2\] | Service name.              |



 

## Remarks

This action requires that the user be an administrator or have elevated privileges with permission to control services or that the application be part of a managed installation.

 

 



