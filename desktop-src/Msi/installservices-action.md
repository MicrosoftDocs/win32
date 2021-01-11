---
description: The InstallServices action registers a service for the system. This action queries the ServiceInstall table.
ms.assetid: bb394cdb-1310-44fb-b7e1-2ffbb976d438
title: InstallServices Action
ms.topic: article
ms.date: 05/31/2018
---

# InstallServices Action

The InstallServices action registers a service for the system. This action queries the [ServiceInstall table](serviceinstall-table.md).

## Sequence Restrictions

The services action must be used in the following sequence.

[StopServices](stopservices-action.md)

[DeleteServices](deleteservices-action.md)

Any of the following actions: [InstallFiles](installfiles-action.md), [RemoveFiles](removefiles-action.md), [DuplicateFiles](duplicatefiles-action.md), [MoveFiles](movefiles-action.md), [PatchFiles](patchfiles-action.md), and [RemoveDuplicateFiles](removeduplicatefiles-action.md) actions.

InstallServices

[StartServices](startservices-action.md)

## ActionData Messages

There are no ActionData messages.

## Remarks

This action requires that the user be an administrator or have elevated privileges with permission to install services or that the application be part of a managed installation.

 

 



