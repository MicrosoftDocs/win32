---
description: When the installer processes the installation script, it simultaneously generates a rollback script.
ms.assetid: 5b9bfc5a-6a78-4b0e-aed8-f25aba089af1
title: Rollback Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Rollback Custom Actions

When the installer processes the installation script, it simultaneously generates a rollback script. In addition to the rollback script, the installer saves a copy of every file it deletes during the installation. These files are kept in a hidden system directory. Once the installation is complete, the rollback script and the saved files are deleted. If an installation is unsuccessful, the installer attempts to rollback the changes made during the installation and restore the original state of the computer.

Although custom actions that schedule system operations by inserting rows into database table are reversed by a rollback of the installation, custom actions that change the system directly, or that issue commands to other system services, cannot always be reversed by a rollback. A rollback custom action is an action that the installer executes only during an installation rollback, and its purpose is to reverse a custom action that has made changes to the system.

A rollback custom action is a type of [deferred execution custom action](deferred-execution-custom-actions.md), because its execution is deferred when it is invoked during the installation sequence. It differs from a regular deferred custom action in that it is only executed during a rollback. A rollback custom action must always precede the deferred custom action it rolls back in the action sequence. A rollback custom action should also handle the case where the deferred custom action is interrupted in the middle of execution. For example, if the user were to press the Cancel button while the custom action was executing.

Note that Rollback Custom Actions cannot run asynchronously. See [Synchronous and Asynchronous Custom Actions](synchronous-and-asynchronous-custom-actions.md).

The complement to a rollback custom action is a [commit custom action](commit-custom-actions.md). The installer executes a commit custom action during the installation sequence, copies the custom action into the rollback script, but does not execute the action during rollback.

Note that a rollback custom action may not be able to remove all of the changes made by commit custom actions. Although the installer writes both rollback and commit custom actions into the rollback script, commit custom actions only run after the installer has successfully processed the installation script. Commit custom actions are the first actions to run in the rollback script. If a commit custom action fails, the installer initiates rollback but can only rollback those operations already written to the rollback script. This means that depending on the commit custom action, a rollback may not be able to undo the changes made by the action. You can ignore failures in commit custom actions by authoring the custom action to ignore return codes.

When the installer runs a rollback custom action, the only mode parameter it will set is MSIRUNMODE\_ROLLBACK. See [**MsiGetMode**](/windows/desktop/api/Msiquery/nf-msiquery-msigetmode) for a description of the run mode parameters.

A rollback custom action can be specified by adding an option flag to the Type field of the [CustomAction table](customaction-table.md). See [Custom Action In-Script Execution Options](custom-action-in-script-execution-options.md) for the option flag designating a rollback custom action.

Rollback and commit custom actions do not run when rollback is disabled. If a package author requires these types of custom actions for proper installation, they should use the [**RollbackDisabled**](rollbackdisabled.md) property in a condition that prevents the installation from continuing when rollback is disabled. For information on how to disable rollback see [Rollback Installation (Windows Installer)](rollback-installation.md).

 

 



