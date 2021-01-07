---
description: ICE27 validates the sequence tables of an installation package for valid actions, action sequence restrictions, and organization in Search, Costing, Selection, and Execution sections.
ms.assetid: c5292a3c-57bb-4203-96a1-6d747f554178
title: ICE27
ms.topic: article
ms.date: 05/31/2018
---

# ICE27

ICE27 validates the [*sequence tables*](s-gly.md) of an installation package for valid actions, action sequence restrictions, and organization in Search, Costing, Selection, and Execution sections.

The ICE27 custom action validates the following:

-   That the actions listed in the Action column of the sequence tables are a [standard actions](standard-actions.md), a custom action listed in the [CustomAction table](customaction-table.md), or a dialog box listed in the [Dialog table](dialog-table.md).
-   That actions subject to sequencing restrictions are in the correct relative order to each other in the action sequence. Sequencing restrictions result when one action is dependent on another.
-   That actions restricted to a particular section of the sequence are located where they belong. ICE27 validates the following organization of the sequence tables. Note that not every sequence table has every section. See the suggested sequence tables in [Using a Sequence Table](using-a-sequence-table.md).



| Sequence table section | Range in action sequence                                                                       | Actions belonging to section                                                                                                                                                                                                                     |
|------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Search                 | {start} to [CostInitialize](costinitialize-action.md)                                         | Actions that search for existing applications. [AppSearch](appsearch-action.md)<br/> [CCPSearch](ccpsearch-action.md)<br/>                                                                                                         |
| Costing                | [CostInitialize](costinitialize-action.md) to [CostFinalize action](costfinalize-action.md)  | Actions that do [file costing](file-costing.md). [CostInitialize](costinitialize-action.md)<br/> [FileCost](filecost-action.md)<br/> [CostFinalize](costfinalize-action.md)<br/>                                           |
| Selection              | [CostFinalize](costfinalize-action.md) to [InstallValidate](installvalidate-action.md)       | Actions that set folders or feature states. [SetODBCFolders action](setodbcfolders-action.md)<br/>                                                                                                                                        |
| Execution              | [InstallValidate](installvalidate-action.md) to [InstallFinalize](installfinalize-action.md) | Script actions, such as Registration, Publication, Installation (where you copy files). Note the [InstallFinalize action](installfinalize-action.md) must be in the table if and only if there are actions in the Execution section.<br/> |
| PostExecution          | [InstallFinalize](installfinalize-action.md) to {end}                                         | [RemoveExistingProducts](removeexistingproducts-action.md)                                                                                                                                                                                      |



 

ICE27 validates the following tables:

-   [AdvtExecuteSequence](advtexecutesequence-table.md)
-   [AdminUISequence](adminuisequence-table.md)
-   [AdminExecuteSequence](adminexecutesequence-table.md)
-   [InstallUISequence](installuisequence-table.md)
-   [InstallExecuteSequence](installexecutesequence-table.md)

## Result

ICE27 posts an error message if there are sequence tables in the package with invalid action sequencing or organization.

## Example



| ICE27 error                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unknown action: 'Action1' of InstallExecuteSequnence table. Not a standard action and not found in CustomAction or Dialog tables    | There is an action listed in the sequence table indicated that is not a [standard actions](standard-actions.md), a custom action listed in the [CustomAction table](customaction-table.md), or a dialog box listed in the [Dialog table](dialog-table.md).                                                                                                                                                                                                                                                                       |
| 'Action2' in InstallExecute table in wrong place. Current: Search, Correct: Costing                                                 | There is an action in a sequence table that is incorrectly placed with respect to the sequence number in the Sequence column. "Current" indicates the current placement of the action in the Search, Costing, Selection, or Execution sections of the indicated sequence table.<br/> "Correct" indicates in which section the action belongs.<br/> To fix this error, change the sequence number of the action to inside the correct section. Note that some action can be located in more than one section.<br/> |
| 'InstallFinalize' Action in InstallExecuteSequence table can only be called when script operations exist to be executed             | There is an [InstallFinalize action](installfinalize-action.md) in a sequence table that does not contain any script operations in the Execution section of the table. Add actions to the Execution section or remove the InstallFinalize action from the table.<br/>                                                                                                                                                                                                                                                        |
| InstallFinalize must be called in InstallExecuteSequence table as script operations exist to be executed                            | There is a sequence table containing actions in the Execution section that does not include the [InstallFinalize action](installfinalize-action.md). Add the InstallFinalize action to this sequence table and give it the greatest sequence number to place it last in the action sequence.<br/>                                                                                                                                                                                                                            |
| Action: 'Action3' in InstallExecuteSequence table must come before the 'Action5' action. Current seq\#: 1200. Dependent seq\#: 1100 | There is an action in the indicated sequence table that is sequenced after a dependent action. Change the sequence number on the dependent action so that it comes before the action.<br/>                                                                                                                                                                                                                                                                                                                                    |
| Action: 'Action4' in InstallExecuteSequence table must come after the 'Action6' action.                                             | There is an action in the indicated sequence table that is sequenced before an action that it is dependent upon. Change the sequence number on the action so that it comes after its dependent action.<br/>                                                                                                                                                                                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 




