---
description: ICE12 validates the CustomAction, Directory, AdminExecuteSequence, AdminUISequence, AdvtExecuteSequence, InstallExecuteSequence, and InstallUISequence tables of the Windows Installer database.
ms.assetid: c1576aff-ff05-49be-8679-a8bfd01977f5
title: ICE12
ms.topic: article
ms.date: 05/31/2018
---

# ICE12

ICE12 queries the [CustomAction](customaction-table.md), [Directory](directory-table.md), [AdminExecuteSequence](adminexecutesequence-table.md), [AdminUISequence](adminuisequence-table.md), [AdvtExecuteSequence](advtexecutesequence-table.md), [InstallExecuteSequence](installexecutesequence-table.md), and [InstallUISequence](installuisequence-table.md) tables to validate the following:

-   That the [CostFinalize action](costfinalize-action.md) occurs in any sequence table containing actions of the type [Custom Action Type 35](custom-action-type-35.md) or [Custom Action Type 51](custom-action-type-51.md).
-   That every [Custom Action Type 35](custom-action-type-35.md) comes after the [CostFinalize action](costfinalize-action.md). in the sequence tables.
-   That every [Custom Action Type 51](custom-action-type-51.md) that has a foreign key to the Directory table in the Source column of the CustomAction table comes before the [CostFinalize action](costfinalize-action.md) in the sequence tables.

Note that ICE12 does not validate the formatted text in the Target column of the CustomAction table.

## Result

ICE12 posts an error message if validation of the custom actions that set a directory property fails.

## Example

ICE12 would post three errors for the example shown.

-   For CA1, Folder 'MyFolder' not found in Directory table
-   For CA2, Sequence '80' comes before CostFinalize in the InstallExecuteSequence table. It must come after (CF@100)
-   For CA3, Sequence '125' comes after CostFinalize in the InstallExecuteSequence table. It must come before (CF@100)

[CustomAction Table](customaction-table.md) (partial)



| Action | Type | Source        |
|--------|------|---------------|
| CA1    | 35   | MyFolder      |
| CA2    | 35   | WindowsFolder |
| CA3    | 51   | WindowsFolder |



 

[Directory Table](directory-table.md)



| Directory     | Directory\_Parent | DefaultDir    |
|---------------|-------------------|---------------|
| TARGETDIR     |                   | SourceDir     |
| WindowsFolder | TARGETDIR         | WindowsFolder |



 

[InstallExecuteSequence Table](installexecutesequence-table.md) (partial)



| Action       | Sequence |
|--------------|----------|
| CostFinalize | 100      |
| CA2          | 80       |
| CA3          | 125      |



 

To fix the error for CA1 change its entry in its Source column in the CustomAction table to an existing entry in the Directory table or add MyFolder to the Directory table.

To fix the error for CA2, change its sequence in the InstallExecuteSequence table such that it comes after the CostFinalize action.

To fix the error for CA3, change its sequence in the InstallExecuteSequence table such that it comes before the CostFinalize action.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



