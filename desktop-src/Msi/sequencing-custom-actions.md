---
description: Custom actions are scheduled in sequence tables in the same way as standard actions.
ms.assetid: 1aea75b1-a498-405e-9208-91672455496b
title: Sequencing Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Sequencing Custom Actions

Custom actions are scheduled in sequence tables in the same way as standard actions.

**To schedule a custom action in a sequence table**

1.  Enter the custom action name (which is the primary key of the [CustomAction](customaction-table.md)) table into the Action column of the [Sequence](sequence-table-detailed-example.md) table.
2.  Enter the custom action's sequence relative to the other actions in the table into the Sequence column of the [Sequence](sequence-table-detailed-example.md) table. For more information about sequence tables, see [Using a Sequence Table](using-a-sequence-table.md).
3.  To conditionally skip the action, enter a conditional expression into the Condition column of the [Sequence](sequence-table-detailed-example.md) table. The installer skips this action if the expression evaluates to FALSE.

As in the case of standard actions, custom actions that are scheduled in the [InstallUISequence](installuisequence-table.md) or [AdminUISequence](adminuisequence-table.md) run only if the internal user interface is set to the full level. The UI level is set by using the [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui) function.

Standard and custom actions scheduled in the [InstallExecuteSequence](installexecutesequence-table.md), [AdminExecuteSequence](adminexecutesequence-table.md), or [AdvtExecuteSequence](advtexecutesequence-table.md) tables do not make system changes. Instead the installer queues up execution records in a script for subsequent execution during the install service. If there is no install service, then the actions scheduled in these tables are run in the same context as the UI sequence.

If the installer server is not registered, the custom actions are executed on the client side. If the server is registered and using the full UI mode, then the custom actions are run on the server side.

If using full UI with the server, the initial actions prior to the [InstallValidate](installvalidate-action.md) action are run on the client to allow full interaction. Execution is then switched to the server which repeats those actions and runs the script execution actions. This is followed by a return to the client for the final actions.

Note that if a product is removed by setting its top feature to absent, the [**REMOVE**](remove.md) property may not equal ALL until after the [InstallValidate](installvalidate-action.md) action. This means that any custom action that depends on REMOVE=ALL must be sequenced after the InstallValidate action. A custom action may check REMOVE to determine whether a product has been set to be completely uninstalled.

Custom actions that reference an installed file as their source, such as Custom Action Type 17 (DLL), Custom Action Type 18 (EXE), Custom Action Type 21 (JScript), and Custom Action Type 22 (VBScript), must adhere to the following sequencing restrictions.

-   The custom action must be sequenced after the [CostFinalize](costfinalize-action.md) action so that the path to the referenced file can be resolved.
-   If the source file is not already installed on the computer, deferred (in-script) custom actions must be sequenced after the [InstallFiles](installfiles-action.md).
-   If the source file is not already installed on the computer, nondeferred custom actions must be sequenced after the [InstallInitialize](installinitialize-action.md) action.

The following sequencing restrictions apply to custom actions that change or update a Windows Installer package.

-   If the custom action changes the package, such as by adding rows to a table, the action must be sequenced before the [InstallInitialize](installinitialize-action.md) action.
-   If the custom action makes changes that would affect costing, then it should be sequenced before the [CostInitialize](costfinalize-action.md) action.
-   If the custom action changes the installation state of features or components, it must be sequenced before the [InstallValidate](installvalidate-action.md) action.

 

 



