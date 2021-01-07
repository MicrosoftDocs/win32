---
description: ICEM04 verifies that the merge module's required empty tables are empty. Failure to fix an error that ICEM04 reports can result in incorrect merging of the merge module.
ms.assetid: c6f64f5e-be65-485b-8831-e377535bd335
title: ICEM04
ms.topic: article
ms.date: 05/31/2018
---

# ICEM04

ICEM04 verifies that the merge module's required empty tables are empty. Failure to fix an error that ICEM04 reports can result in incorrect merging of the merge module.

## Result

ICEM04 posts an error when the merge module's required empty tables are not empty.

## Example

ICEM04 posts the following error messages for a module that contains the database entries shown.

``` syntax
An empty FeatureComponents table is required in a Merge Module.

The Merge Module contains the 'ModuleInstallExecuteSequence' table. It 
must therefore have an empty 'InstallExecuteSequence' table.

Action 'CostInitialize' found in the AdvtExecuteSequence table. This 
table must be empty in a Merge Module
```

The following table shows you a partial [AdvtExecuteSequence Table](advtexecutesequence-table.md).



| Action         | Sequence |
|----------------|----------|
| CostInitialize | 1        |



 

The following list shows you the partial contents of MergeModule:

-   ModuleInstallExecuteSequence
-   ModuleAdvtExecuteSequence
-   InstallUISequence

The following example shows you another possible error.

``` syntax
Feature-Component '[1].[2]' found in the FeatureComponents table. The 
FeatureComponents table must be empty in a Merge Module.
```

If a merge module contains a module sequence table, it must contain the corresponding empty sequence table, whether or not the module sequence table is empty. For example, if the merge module contains the [ModuleAdminExecuteSequence Table](moduleadminexecutesequence-table.md), it must also contain an empty AdminExecuteSequence table.

The [FeatureComponents Table](featurecomponents-table.md) is required in all merge modules and must be empty.

The following procedure shows you how to fix errors.

**To fix errors**

1.  Add an empty [FeatureComponents Table](featurecomponents-table.md) to the merge module.
2.  Add an empty [InstallExecuteSequence Table](installexecutesequence-table.md) to the merge module.
3.  Remove the 'CostInitialize' action from the [AdvtExecuteSequence Table](advtexecutesequence-table.md).
    > [!Note]  
    > This table must be empty in a merge module. Actions should only appear in the ModuleAdvtExecuteSequence table.

     

## Tables Used During Execution

The following list identifies the tables that are used during execution:

-   [FeatureComponents Table](featurecomponents-table.md)
-   Module\*Sequence tables and corresponding \*Sequence tables.

## Related topics

<dl> <dt>

[About Merge Modules](about-merge-modules.md)
</dt> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



