---
description: ICE13 validates that dialogs in sequence tables appear in the AdminUISequence, or InstallUISequence tables. Dialogs must not be listed in the InstallExecuteSequence, AdminExecuteSequence, or AdvtExecuteSequence tables.
ms.assetid: 51542a8f-2fb6-4021-b52d-6f7a2b0294d6
title: ICE13
ms.topic: article
ms.date: 05/31/2018
---

# ICE13

ICE13 validates that dialogs in sequence tables appear in the [AdminUISequence](adminuisequence-table.md), or [InstallUISequence](installuisequence-table.md) tables. Dialogs must not be listed in the [InstallExecuteSequence](installexecutesequence-table.md), [AdminExecuteSequence](adminexecutesequence-table.md), or [AdvtExecuteSequence](advtexecutesequence-table.md) tables.

## Result

ICE13 posts an error message if a dialog appears in an execute sequence table.

## Example

For the following example, ICE13 posts an error message stating that the 'WelcomeDialog' cannot be listed in the 'InstallExecuteSequence' table.

[InstallExecuteSequence Table](installexecutesequence-table.md) (partial)



| Action          |
|-----------------|
| InstallFinalize |
| CostFinalize    |
| WelcomeDialog   |



 

[InstallUISequence Table](installuisequence-table.md) (partial)



| Action         |
|----------------|
| CostFinalize   |
| CostInitialize |
| BrowseDialog   |



 

[Dialog Table](dialog-table.md) (partial)



| Dialog        |
|---------------|
| BrowseDialog  |
| WelcomeDialog |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



