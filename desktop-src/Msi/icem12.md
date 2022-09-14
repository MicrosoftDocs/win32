---
description: ICEM12 verifies that in a ModuleSequence table, standard actions have sequence numbers and custom actions have BaseAction and After values.
ms.assetid: 1a168629-9865-4412-8317-8af8b9a7b8bd
title: ICEM12
ms.topic: article
ms.date: 05/31/2018
---

# ICEM12

ICEM12 verifies that in a ModuleSequence table, standard actions have sequence numbers and custom actions have BaseAction and After values.

This ICEM is available in the Mergemod.cub file provided in the Windows Installer 2.0 SDK and later. For details, see [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

## Result

ICEM12 posts an error in the following cases:

-   It finds the module contains a [standard action](standard-actions.md) without a sequence number.
-   It finds that a standard action has values entered in the BaseAction or After fields of the [ModuleAdminUISequence table](moduleadminuisequence-table.md), [ModuleAdminExecuteSequence table](moduleadminexecutesequence-table.md), [ModuleAdvtExecuteSequence table](moduleadvtexecutesequence-table.md), [ModuleInstallUISequence table](moduleinstalluisequence-table.md), or [ModuleInstallExecuteSequence table](moduleinstallexecutesequence-table.md).
-   It finds the module contains a [custom action](custom-actions.md) without any values entered into the Sequence, BaseAction or After fields of the [ModuleAdminUISequence table](moduleadminuisequence-table.md), [ModuleAdminExecuteSequence table](moduleadminexecutesequence-table.md), [ModuleAdvtExecuteSequence table](moduleadvtexecutesequence-table.md), [ModuleInstallUISequence table](moduleinstalluisequence-table.md), or [ModuleInstallExecuteSequence table](moduleinstallexecutesequence-table.md).

ICEM12 posts a warning if it finds a custom action that has a Sequence number specified, but no value in the BaseAction or After fields.

Note that all actions found in the [CustomAction table](customaction-table.md) are considered custom actions. All other action are considered standard actions.

## Example

ICEM12 posts the following error and warning messages for a module that contains the database entries shown below:

``` syntax
Error. Custom actions should use the BaseAction and After fields and not use the 
Sequence field in the Module Sequence tables. The custom action 'Action1' uses the Sequence field 
and does not use the BaseAction and After fields in the ModuleInstallExecuteSequence table. 
    
Error. Custom actions should not leave the Sequence, BaseAction, and After fields 
of the Module Sequence tables all empty. The custom action 'Action3' leaves the Sequence, 
BaseAction, and After fields empty in the ModuleAdminExecuteSequence table.

Error. Standard actions should not use the BaseAction and After fields in Module 
Sequence tables. The standard action 'Action2' has a values entered in the BaseAction 
or After fields of the ModuleAdminExecuteSequence table.

Error. Standard actions must have a entry in the Sequence field of Module Sequence 
tables. The standard action 'Action2' does not have a Sequence value in the 
ModuleExecuteSequence table.
```

[CustomAction](customaction-table.md)



| Action  | Type | Source  | Target  |
|---------|------|---------|---------|
| Action1 | 30   | source1 | target1 |
| Action3 | 30   | source3 | target3 |



 

[ModuleAdminExecuteSequence](moduleadminexecutesequence-table.md)



| Action  | Sequence | BaseAction | After | Condition |
|---------|----------|------------|-------|-----------|
| Action2 |          | Action1    | 1     | true      |
| Action3 |          |            |       | true      |



 

[ModuleInstallExecuteSequence](moduleinstallexecutesequence-table.md)



| Action  | Sequence | BaseAction | After | Condition |
|---------|----------|------------|-------|-----------|
| Action1 | 1        |            |       | true      |



 

To fix these errors try the following:

-   Remove the sequence number for the custom action Action1 and use the BaseAction and After fields instead.
-   Enter values into the Sequence, BaseAction, or After fields for the custom action Action3. Leave the BaseAction and After fields empty for standard action Action2.
-   Do not leave the Sequence field empty for standard action Action2.

## Related topics

<dl> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



