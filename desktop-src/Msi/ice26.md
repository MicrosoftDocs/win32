---
description: ICE26 validates sequence tables in a Windows Installer database.
ms.assetid: 7ea47452-3147-4d39-961d-a10eca8328c9
title: ICE26
ms.topic: article
ms.date: 05/31/2018
---

# ICE26

ICE26 validates that each of the following [*sequence tables*](s-gly.md) contain the actions that are required by the table and does not contain any actions disallowed in the table:

-   [AdminUISequence table](adminuisequence-table.md)
-   [AdminExecuteSequence table](adminexecutesequence-table.md)
-   [InstallUISequence table](installuisequence-table.md)
-   [InstallExecuteSequence table](installexecutesequence-table.md)

## Result

ICE26 posts an error message if the installation package has a sequence table that lacks a required action or that contains an action that is disallowed for the table.

## Example



| ICE26 error                                                                   | Description                                                                                                                                                                    |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action: 'Action1' is required in the InstallExecuteSequence Sequence table.   | A required action is missing from the indicated sequence table. See the template.msi or the suggested sequence tables in [Using a Sequence Table](using-a-sequence-table.md). |
| Action: 'Action2' is prohibited in the InstallExecuteSequence Sequence table. | This action cannot be in the indicated sequence table. Remove this action from the sequence table.                                                                             |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



