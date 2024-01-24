---
description: The InstallExecute action runs a script containing all operations in the action sequence since either the start of the installation or the last InstallExecute action or InstallExecuteAgain action.
ms.assetid: a124e9fb-f9fa-4ed3-8f32-4f1fab392530
title: InstallExecute Action
ms.topic: article
ms.date: 05/31/2018
---

# InstallExecute Action

The InstallExecute action runs a script containing all operations in the action sequence since either the start of the installation or the last InstallExecute action or [InstallExecuteAgain action](installexecuteagain-action.md). The InstallExecute action updates the system without ending the transaction.

## Sequence Restrictions

The InstallExecute action comes between the [InstallInitialize action](installinitialize-action.md) and the [InstallFinalize action](installfinalize-action.md).

## ActionData Messages

There are no ActionData messages.

## Remarks

The [InstallExecuteAgain action](installexecuteagain-action.md) does the same thing as the InstallExecute action. Because the sequence tables have only one primary key, the Action column, the same action cannot be repeated in a particular sequence table. Two actions exist that do the same thing, InstallExecute and InstallExecuteAgain, for cases where the functionality of InstallExecute is needed twice in the [InstallExecuteSequence table](installexecutesequence-table.md). For more information, see [Using a Sequence Table](using-a-sequence-table.md).

 

 



