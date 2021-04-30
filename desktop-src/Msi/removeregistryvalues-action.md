---
description: The RemoveRegistryValues action can only remove values from the system registry that have been authored into the Registry table or the RemoveRegistry table.
ms.assetid: aa05eb75-15f2-4e2a-a8e2-a770ad078b41
title: RemoveRegistryValues Action
ms.topic: article
ms.date: 05/31/2018
---

# RemoveRegistryValues Action

The RemoveRegistryValues action can only remove values from the system registry that have been authored into the [Registry table](registry-table.md) or the [RemoveRegistry table](removeregistry-table.md). This action removes a registry value that has been authored into the Registry table if the associated component was installed locally or as run from source and is now set to be uninstalled. This action removes a registry value that has been authored into the RemoveRegistry table if the associated component is set to be installed locally or as run from source.

## Sequence Restrictions

The [InstallValidate](installvalidate-action.md) action must be called before calling RemoveRegistryValues. If a [WriteRegistryValues](writeregistryvalues-action.md) action is used, it must come after RemoveRegistryValues. RemoveRegistryValues must come before [UnregisterMIMEInfo](unregistermimeinfo-action.md) or [UnregisterProgIDInfo](unregisterprogidinfo-action.md).

A custom action can be used to add rows to the [Registry table](registry-table.md) during an installation, uninstallation, or repair transaction. These rows do not persist in the Registry table and the information is only available during the current transaction. The custom action must therefore be run in every installation, uninstallation, or repair transaction that requires the information in these additional rows. The custom action must come before the RemoveRegistryValues and [WriteRegistryValues](writeregistryvalues-action.md) actions in the action sequence.

## ActionData Messages



| Field | Description of action data                          |
|-------|-----------------------------------------------------|
| \[1\] | Registry path to key of removed registry value.     |
| \[2\] | Formatted string of name of removed registry value. |



 

## Remarks

To remove a registry value, record the value in the Value column of the Registry table. If the WriteRegistryValues action has attached REG\_MULTI\_SZ strings to the value in the [Registry table](registry-table.md), then the RemoveRegistryValues action removes only those strings from the registry value.

 

 



