---
description: Here is an example of a sequence table.
ms.assetid: 25b3667a-1478-48c4-9c41-4defd25a0103
title: Sequence Table Detailed Example
ms.topic: article
ms.date: 05/31/2018
---

# Sequence Table Detailed Example

Here is an example of a sequence table.



| Action                                          | Condition                                                       | Sequence |
|-------------------------------------------------|-----------------------------------------------------------------|----------|
| [LaunchConditions](launchconditions-action.md) |                                                                 |          |
| [AppSearch](appsearch-action.md)               |                                                                 | 200      |
| [CCPSearch](ccpsearch-action.md)               | CCP\_TEST                                                       | 300      |
| CCPDialog                                       | NOT\_CCP\_SUCCESS                                               | 400      |
| MyCustomConfig                                  | NOT [**Installed**](installed.md)                              | 500      |
| [CostInitialize](costinitialize-action.md)     |                                                                 | 600      |
| [FileCost](filecost-action.md)                 |                                                                 | 700      |
| [CostFinalize](costfinalize-action.md)         |                                                                 | 800      |
| InstallDialog                                   | NOT [**Installed**](installed.md)                              | 900      |
| MaintenanceDialog                               | [**Installed**](installed.md) AND NOT [**Resume**](resume.md) | 1000     |
| ActionDialog                                    |                                                                 | 1100     |
| [RegisterProduct](registerproduct-action.md)   |                                                                 | 1200     |
| [InstallValidate](installvalidate-action.md)   |                                                                 | 1300     |
| [InstallFiles](installfiles-action.md)         |                                                                 | 1400     |
| MyCustomAction                                  | $MyComponent > 2                                             | 1500     |
| [InstallFinalize](installfinalize-action.md)   |                                                                 | 1600     |



 

The following actions in this sequence table are defined by the installer and are examples of standard actions:

[LaunchConditions](launchconditions-action.md)

 

[AppSearch](appsearch-action.md)

 

[CCPSearch](ccpsearch-action.md)

 

[CostInitialize](costinitialize-action.md)

 

[FileCost](filecost-action.md)

 

[CostFinalize](costfinalize-action.md)

 

[RegisterProduct](registerproduct-action.md)

 

[InstallFiles](installfiles-action.md)

 

[InstallFiles](installfiles-action.md)

 

[InstallValidate](installvalidate-action.md)

The following actions were defined by the table's author and are examples of [custom actions](custom-actions.md) and must be listed in the [CustomAction table](customaction-table.md):

MyCustomConfig

 

MyCustomAction

The remaining entries in the Action field are foreign keys into the [Dialog table](dialog-table.md). They specify the names of dialog boxes that will displayed if the condition field evaluates to True.

CCPDialog

 

InstallDialog

 

MaintenanceDialog

 

ActionDialog

The Condition column causes the installer to skip the action if the property or expression in this field is False. The [**Installed**](installed.md) property and the [**RESUME**](resume.md) property are example of properties that are set by the installer. The [**Installed**](installed.md) property is set to true if the product is already installed and the [**RESUME**](resume.md) property is set if resuming a suspended installation. The CCP\_TEST and the NOT\_CCP\_SUCCESS properties are examples of properties that can be set at the command line by the user installing the application.

All actions run in sequence with the following conditional steps:

-   The CPPSearch is run only if CCP\_TEST is set.
-   CCPDialog is run only if NOT\_CCP\_SUCCESS is set.
-   MaintenanceDialog is run only if this product is already installed and if this is not an installation that is being resume after being suspended.
-   MyCustomAction is run only if the expression in the Condition column is True. The expression $MyComponent > 2 refers to the action state of the component called MyComponent. This condition indicates that MyCustomAction should only be run if MyComponent is set to be installed. For more information on Action states and Selection states, see the [**FeatureRequestState**](session-featurerequeststate.md) property, the [Feature table](feature-table.md), and the [InstallFiles action](installfiles-action.md).

## Related topics

<dl> <dt>

[Using Properties](using-properties.md)
</dt> <dt>

[Conditional Statement Syntax](conditional-statement-syntax.md)
</dt> </dl>

 

 



