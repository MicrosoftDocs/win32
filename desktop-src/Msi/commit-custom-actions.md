---
description: Commit Custom actions are executed upon successful completion of the installation script.
ms.assetid: ad766585-e8ac-44b6-9717-7979f803886c
title: Commit Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Commit Custom Actions

Commit Custom actions are executed upon successful completion of the installation script. If the [InstallFinalize action](installfinalize-action.md) is successful, the installer will then run any existing Commit Custom actions. The only mode parameter the installer sets in this case is MSIRUNMODE\_COMMIT. See [**MsiGetMode**](/windows/desktop/api/Msiquery/nf-msiquery-msigetmode) for a description of the run mode parameters.

A commit custom action can be specified by adding an option flag to the Type field of the [CustomAction table](customaction-table.md). See [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md) for the option flag designating a commit custom action.

A commit custom action is the complement to a [rollback custom action](rollback-custom-actions.md) and can be used with rollback custom actions to reverse custom actions that make changes directly to the system.

Note that a rollback custom action may not be able to remove all of the changes made by commit custom actions. Although the installer writes both rollback and commit custom actions into the rollback script, commit custom actions only run after the installer has successfully processed the installation script. Commit custom actions are the first actions to run in the rollback script. If a commit custom action fails, the installer initiates rollback but can only rollback those operations already written to the rollback script. This means that depending on the commit custom action, a rollback may not be able to undo the changes made by the action. You can ignore failures in commit custom actions by authoring the custom action to ignore return codes.

Rollback and commit custom actions do not run when rollback is disabled. If a package author requires these types of custom actions for proper installation, they should use the [**RollbackDisabled**](rollbackdisabled.md) Property in a condition that prevents the installation from continuing when rollback is disabled.

 

 



