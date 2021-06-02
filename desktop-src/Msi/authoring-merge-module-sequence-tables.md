---
description: Include the MergeModuleSequence tables in the .msm file if the merge module must modify the action sequence tables of the target .msi file. Merging does not add these tables to the .msi file. These tables only occur in merge modules.
ms.assetid: 9efb75d2-43f9-404c-8e7f-918d056190cf
title: Authoring Merge Module Sequence Tables
ms.topic: article
ms.date: 05/31/2018
---

# Authoring Merge Module Sequence Tables

Include the MergeModuleSequence tables in the .msm file if the merge module must modify the action [*sequence tables*](s-gly.md) of the target .msi file. Merging does not add these tables to the .msi file. These tables only occur in merge modules.

If any of the ModuleSequence tables are present in an .msm file, an empty copy of the corresponding installer sequence table must also be authored into the merge module. For example, if a merge module contains a ModuleAdminExecuteSequence table, the merge module must also include an empty AdminExecuteSequence table. During a merge, these empty tables provide the merge tool with necessary schema guidelines.

When using [standard actions](standard-actions.md) in merge module sequence tables, the value in the Sequence column should be the recommended action sequence number for the standard action. See the suggested action sequences given below for the recommended sequence numbers in each sequence table. If the sequence number in the merge module sequence table differs from the sequence number for the same action in the .msi file, the merge tool uses the sequence number in the .msi file during the merge.



| MergeModuleSequence table                                                    | Recommended action sequences                                             |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [ModuleAdminUISequence](moduleadminuisequence-table.md)                     | [Suggested AdminUISequence](suggested-adminuisequence.md)               |
| [ModuleAdminExecuteSequence](moduleadminexecutesequence-table.md)           | [Suggested AdminExecuteSequence](suggested-adminexecutesequence.md)     |
| [ModuleAdvtUISequence](moduleadvtuisequence-table.md)                       | [Suggested AdvtUISequence](suggested-advtuisequence.md)                 |
| [ModuleAdvtExecuteSequence](moduleadvtexecutesequence-table.md)             | [Suggested AdvtExecuteSequence](suggested-advtexecutesequence.md)       |
| [ModuleInstallUISequence](moduleinstalluisequence-table.md)                 | [Suggested InstallUISequence](suggested-installuisequence.md)           |
| [ModuleInstallExecuteSequence table](moduleinstallexecutesequence-table.md) | [Suggested InstallExecuteSequence](suggested-installexecutesequence.md) |



 

If a [standard action](standard-actions.md) is used in the Action column of a merge module sequence table, the BaseAction and After columns of that record must be Null.

If a custom action or dialog is entered into the Action column, the Sequence column must be Null.

If an action returning a termination flag is entered into the Action column, the Sequence column should contain the negative value for that flag and the BaseAction and After columns of that record must be Null. The following negative values indicate that the action is called if the installer returns the termination flag.



| Termination flag          | Value | Description              |
|---------------------------|-------|--------------------------|
| msiDoActionStatusSuccess  | -1    | Successful completion.   |
| msiDoActionStatusUserExit | -2    | User terminates install. |
| msiDoActionStatusFailure  | -3    | Fatal exit terminates.   |
| msiDoActionStatusSuspend  | -4    | Install is suspended.    |



 

The BaseAction column can contain a standard action, a custom action specified in the merge module's custom action table, or a dialog specified in the module's dialog table. The BaseAction column is a key into the Action column of this table. It cannot be a foreign key into another merge table or table in the .msi file. This means that every standard action, custom action, or dialog listed in the BaseAction column must also be listed in the Action column of another record in this table.

 

 



