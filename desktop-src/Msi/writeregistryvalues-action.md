---
description: The WriteRegistryValues action sets up an application's registry information.
ms.assetid: ab121de3-f07d-401a-b52a-246a555c142c
title: WriteRegistryValues Action
ms.topic: article
ms.date: 05/31/2018
---

# WriteRegistryValues Action

The WriteRegistryValues action sets up an application's registry information. The registry information is gated by the [Component table](component-table.md). A registry value is written to the registry if the corresponding component has been set to be installed either locally or as run from source. For more information, see [Registry table](registry-table.md).

## Sequence Restrictions

The [InstallValidate action](installvalidate-action.md) must come before the WriteRegistryValues action. If there is a [RemoveRegistryValues action](removeregistryvalues-action.md), then it must come before the WriteRegistryValues action.

A custom action can be used to add rows to the [Registry table](registry-table.md) during an installation, uninstallation, or repair transaction. These rows do not persist in the Registry table and the information is only available during the current transaction. The custom action must therefore be run in every installation, uninstallation, or repair transaction that requires the information in these additional rows. The custom action must come before the [RemoveRegistryValues](removeregistryvalues-action.md) and WriteRegistryValues actions in the action sequence.

## ActionData Messages



| Field | Description of action data                               |
|-------|----------------------------------------------------------|
| \[1\] | Path to registry key of value written to registry.       |
| \[2\] | Formatted text string name of value written to registry. |
| \[3\] | Formatted text string of value written to registry.      |



 

 

 



