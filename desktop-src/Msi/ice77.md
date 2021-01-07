---
description: ICE77 verifies that custom actions with the msidbCustomActionTypeInScript bit set are sequenced after the InstallInitialize action and before the InstallFinalize action.
ms.assetid: 291cf731-b7e6-44c2-a8ec-78e0e037d1f5
title: ICE77
ms.topic: article
ms.date: 05/31/2018
---

# ICE77

ICE77 verifies that custom actions with the **msidbCustomActionTypeInScript** bit set are sequenced after the [InstallInitialize action](installinitialize-action.md) and before the [InstallFinalize action](installfinalize-action.md). ICE77 checks the sequence in the [InstallExecuteSequence table](installexecutesequence-table.md) and [AdminExecuteSequence table](adminexecutesequence-table.md).

## Result

ICE77 posts an error if an in-script custom action is sequenced before the InstallInitialize action or after the InstallFinalize action.

ICE77 posts an error if the InstallInitialize action or the InstallFinalize action is missing.

## Example

ICE77 reports the following errors for the example:

``` syntax
InstallFinalize is missing from 'InstallExecuteSequence'. 
CA_InScriptInstall is a in-script custom action. It must be sequenced 
before the InstallFinalize action.
 
CA_InScriptAdmin is a in-script custom action.  It must be sequenced 
in between the InstallInitialize action and the InstallFinalize action 
in the AdminExecuteSequence Sequence table.
```

[CustomAction Table](customaction-table.md) (partial)



| Action              | Type |
|---------------------|------|
| CA\_InScriptInstall | 1025 |
| CA\_InScriptAdmin   | 1026 |



 

[InstallExecuteSequence Table](installexecutesequence-table.md) (partial)



| Action              | Sequence |
|---------------------|----------|
| CA\_InScriptInstall | 2000     |
| InstallInitialize   | 1500     |



 

[AdminExecuteSequence Table](adminexecutesequence-table.md) (partial)



| Action            | Sequence |
|-------------------|----------|
| CA\_InScriptAdmin | 1400     |
| InstallInitialize | 1500     |
| InstallFinalize   | 6600     |



 

To fix the errors, sequence the in-script custom actions after the InstallInitialize action and before the InstallFinalize action. The InstallInitialize and InstallFinalize actions must be present in the InstallExecuteSequence table and the AdminExecuteSequence table.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



