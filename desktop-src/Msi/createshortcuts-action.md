---
description: The CreateShortcuts action manages the creation of shortcuts.
ms.assetid: 2e8a30ec-e8e7-4855-addb-2501bf85ab54
title: CreateShortcuts Action
ms.topic: article
ms.date: 05/31/2018
---

# CreateShortcuts Action

The CreateShortcuts action manages the creation of shortcuts.

## Sequence Restrictions

The CreateShortcuts action must come after the [InstallFiles](installfiles-action.md) action and the [RemoveShortcuts](removeshortcuts-action.md) action.

## ActionData Messages



| Field | Description of action data      |
|-------|---------------------------------|
| \[1\] | Identifier of created shortcut. |



 

## Remarks

The CreateShortcuts action creates shortcuts to the key files of components of features that are selected for installation or advertisement.

## Related topics

<dl> <dt>

[Shortcut Table](shortcut-table.md)
</dt> <dt>

[MsiShortcutProperty Table](msishortcutproperty-table.md)
</dt> </dl>

 

 



