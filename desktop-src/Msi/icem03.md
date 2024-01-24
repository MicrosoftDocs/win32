---
description: ICEM03 verifies that all actions in the module are either base actions or derive from a valid base action.
ms.assetid: 8e2b5921-32cf-45e8-9906-30002574a712
title: ICEM03
ms.topic: article
ms.date: 05/31/2018
---

# ICEM03

ICEM03 verifies that all actions in the module are either base actions or derive from a valid base action.

Merge module ICEs are stored in a merge module .cub file called Mergemod.cub and not in the .cub file containing the ICEs used for package validation.

## Result

ICEM03 posts the error messages for a module containing actions in a sequence table that is not a base action or derived from a valid base action.

## Example

ICEM03 posts the following error messages for a module containing the database entries shown below.

``` syntax
The action 'Action1' in the 'ModuleInstallExecuteSequence' table is 
orphaned. It is not a valid base action and does not derive from a 
valid base action.
The action 'Action2' in the 'ModuleInstallExecuteSequence' table is 
orphaned. It is not a valid base action and does not derive from a 
valid base action.
```

[ModuleInstallExecuteSequence Table](moduleinstallexecutesequence-table.md)



| Action  | Sequence | BaseAction | After | Condition |
|---------|----------|------------|-------|-----------|
| Action1 |          | Action2    | 0     |           |
| Action2 |          | Action1    | 0     |           |



 

ICEM03 posts errors for these two actions because they refer to each other as base actions in the ModuleInstallExecuteSequence table. All actions in the [ModuleAdminUISequence](moduleadminuisequence-table.md), [ModuleAdminExecuteSequence](moduleadminexecutesequence-table.md), [ModuleAdvtUISequence](moduleadvtuisequence-table.md), [ModuleAdvtExecuteSequence](moduleadvtexecutesequence-table.md), [ModuleInstallUISequence](moduleinstalluisequence-table.md), and [ModuleInstallExecuteSequence](moduleinstallexecutesequence-table.md) tables must either be base actions or derive their position from the combination of another action and a before and after flag.

To fix this error, determine the base actions for the two actions. Add a record for the base actions with a default sequence number. For Action1 and Action2 enter the base action names in the BaseAction column and 0 or 1 in the After column.

## Related topics

<dl> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



