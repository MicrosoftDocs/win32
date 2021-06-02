---
description: The MsiConfigureServices action configures a service for the system. This action queries the MsiServiceConfig and the MsiServiceConfigFailureActions tables.
ms.assetid: 63bd4690-0649-4e23-a8cd-527b3c517dae
title: MsiConfigureServices Action
ms.topic: article
ms.date: 05/31/2018
---

# MsiConfigureServices Action

The MsiConfigureServices action configures a service for the system. This action queries the [MsiServiceConfig](msiserviceconfig-table.md) and the [MsiServiceConfigFailureActions](msiserviceconfigfailureactions-table.md) tables.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This action is available beginning with Windows Installer 5.0.

> [!IMPORTANT]
>
> Windows Services provides the ability to automatically perform predefined actions in response to a failure in a service. To support programmatically setting up these **Recovery Actions** when a service fails, [MsiServiceConfigFailureActions](msiserviceconfigfailureactions-table.md) was added to MSI in version MSI 5.0. However, this functionality is not working as expected.
>
> To workaround this issue, an application developer should use the **Custom Action** functionality in MSI to run **sc.exe** and set the **Recovery Options** appropriately.

 

## Sequence Restrictions

This standard action must be used in the following sequence.

[StopServices](stopservices-action.md)

[DeleteServices](deleteservices-action.md)

Any of the following actions: [InstallFiles](installfiles-action.md), [RemoveFiles](removefiles-action.md), [DuplicateFiles](duplicatefiles-action.md), [MoveFiles](movefiles-action.md), [PatchFiles](patchfiles-action.md), and [RemoveDuplicateFiles](removeduplicatefiles-action.md) actions.

[InstallServices](installservices-action.md)

MsiConfigureServices

[StartServices](startservices-action.md)

## ActionData Messages

There are no ActionData messages.

## Remarks

This action requires that the user be an administrator or have elevated privileges with permission to install services or that the application be part of a managed installation.

 

 



