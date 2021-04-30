---
description: ICE84 checks the AdvtExecuteSequence table, AdminExecuteSequence table, and the InstallExecuteSequence table to verify that the following standard actions have not been set with conditions in the Condition field.
ms.assetid: 0d1bbf4b-ffab-409e-a292-891dfa823433
title: ICE84
ms.topic: article
ms.date: 05/31/2018
---

# ICE84

ICE84 checks the [AdvtExecuteSequence table](advtexecutesequence-table.md), [AdminExecuteSequence table](adminexecutesequence-table.md), and the [InstallExecuteSequence table](installexecutesequence-table.md) to verify that the following [standard actions](standard-actions.md) have not been set with conditions in the Condition field.

-   [CostInitialize action](costinitialize-action.md)
-   [CostFinalize action](costfinalize-action.md)
-   [FileCost action](filecost-action.md)
-   [InstallValidate action](installvalidate-action.md)
-   [InstallInitialize action](installinitialize-action.md)
-   [InstallFinalize action](installfinalize-action.md)
-   [ProcessComponents action](processcomponents-action.md)
-   [PublishFeatures action](publishfeatures-action.md)
-   [PublishProduct action](publishproduct-action.md)
-   [RegisterProduct action](registerproduct-action.md)
-   [UnpublishFeatures action](unpublishfeatures-action.md)

If conditions are found, ICE84 posts a warning.

## Result

ICE84 posts the following warning.



| ICE84 error                                                             | Description                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------|
| Action '\[1\]' found in %s table is a required action with a condition. | A required action has been authored with a condition. |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



