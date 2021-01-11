---
description: ICE63 checks for proper sequencing of the RemoveExistingProducts action.
ms.assetid: 4dd67bb0-c08a-4a44-b687-0394a3afc2c4
title: ICE63
ms.topic: article
ms.date: 05/31/2018
---

# ICE63

ICE63 checks for proper sequencing of the [RemoveExistingProducts action](removeexistingproducts-action.md). The RemoveExistingProducts action may be placed:

1.  Between InstallValidate and InstallInitialize
2.  Immediately after InstallInitialize, or after InstallInitialize if the actions between InstallInitialize and RemoveExistingProducts do not generate any script actions.
3.  Immediately after InstallExecute or InstallExecuteAgain and before InstallFinalize (the same restriction as above applies).
4.  After InstallFinalize.

Failure to fix a warning or error reported by ICE63 leads to failure of the upgrade.

## Result

ICE63 posts a warning or error if the sequencing of the RemoveExistingProducts action is not correct.

## Example

ICE63 reports the following error for the example shown.

``` syntax
WARNING: Some action falls between InstallInitialize and RemoveExistingProducts.
```

The action 'MyCustomAction' occurs between InstallInitialize and RemoveExistingProducts. If MyCustomAction generates any actions in the script, this causes problems in the installation.

To fix this error, verify that MyCustomAction does not generate any script actions or resequence the actions.

[InstallExecuteSequence Table](installexecutesequence-table.md)



| Action                 | Condition | Sequence |
|------------------------|-----------|----------|
| InstallInitialize      |           | 1000     |
| MyCustomAction         |           | 1010     |
| RemoveExistingProducts |           | 1020     |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



