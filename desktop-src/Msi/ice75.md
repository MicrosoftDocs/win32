---
description: ICE75 verifies that all Custom Action Type 17 (DLL), Custom Action Type 18 (EXE), Custom Action type 21 (JScript), and Custom Action Type 22 (VBScript) custom actions are sequenced after the CostFinalize action.
ms.assetid: 831de042-bea6-42da-90a0-3847bb447414
title: ICE75
ms.topic: article
ms.date: 05/31/2018
---

# ICE75

ICE75 verifies that all [Custom Action Type 17](custom-action-type-17.md) (DLL), [Custom Action Type 18](custom-action-type-18.md) (EXE), [Custom Action type 21](custom-action-type-21.md) (JScript), and [Custom Action Type 22](custom-action-type-22.md) (VBScript) custom actions are sequenced after the [CostFinalize action](costfinalize-action.md). These types of custom action use an installed file as their source. ICE75 checks the [InstallUISequence Table](installuisequence-table.md), [InstallExecuteSequence Table](installexecutesequence-table.md), [AdminUISequence Table](adminuisequence-table.md), and [AdminExecuteSequence Table](adminexecutesequence-table.md). Note that the CostFinalize action is required in these sequence tables.

## Result

ICE75 posts an error if it finds a custom action using an installed file as a source file that is not sequenced after the CostFinalize action.

## Example

ICE75 reports the following errors for the example shown:

``` syntax
CostFinalize is missing from 'AdminUISequence'. CA_FileExe is a custom
 action whose source is an installed file. It must be sequenced after 
the CostFinalize action.
 
CA_FileDLL is a custom action whose source is an installed file.  It 
must be sequenced after the CostFinalize action in the 
AdminExecuteSequence table
```

[CustomAction Table](customaction-table.md) (partial)



| Action      | Type | Source  |
|-------------|------|---------|
| CA\_FileExe | 18   | FileExe |
| CA\_FileDLL | 17   | FileDLL |



 

[AdminUISequence Table](adminuisequence-table.md) (partial)



| Action      | Sequence |
|-------------|----------|
| CA\_FileExe | 1100     |



 

[AdminExecuteSequence Table](adminexecutesequence-table.md) (partial)



| Action       | Sequence |
|--------------|----------|
| CA\_FileDLL  | 800      |
| CostFinalize | 1000     |



 

To fix the errors, sequence the custom actions after the CostFinalize action.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



