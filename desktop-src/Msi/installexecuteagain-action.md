---
description: The InstallExecuteAgain action runs a script containing all operations in the action sequence since either the start of the installation or the last InstallExecuteAgain action or the last InstallExecute action.
ms.assetid: 60ff844f-f8bf-4a55-9523-ba526dac9e29
title: InstallExecuteAgain Action
ms.topic: article
ms.date: 05/31/2018
---

# InstallExecuteAgain Action

The InstallExecuteAgain action runs a script containing all operations in the action sequence since either the start of the installation or the last InstallExecuteAgain action or the last [InstallExecute action](installexecute-action.md). The InstallExecute action updates the system without ending the transaction. InstallExecuteAgain performs the same operation as the [InstallExecute action](installexecute-action.md) but should only be used after InstallExecute.

InstallExecuteAgain should always be set so that it does not run during removal. For information, see [Using Properties in Conditional Statements](using-properties-in-conditional-statements.md).

## Sequence Restrictions

The InstallExecute action comes between the [InstallInitialize action](installinitialize-action.md) and the [InstallFinalize action](installfinalize-action.md).

## ActionData Messages

There are no ActionData messages.

## Remarks

The InstallExecuteAgain action does the same thing as the [InstallExecute action](installexecute-action.md). Because the sequence tables have only one primary key, the Action column, the same action cannot be repeated in a particular sequence table. Two actions exist that do the same thing, InstallExecute and InstallExecuteAgain, for cases where the functionality of InstallExecute is needed twice in the [InstallExecuteSequence table](installexecutesequence-table.md). For more information, see [Using a Sequence Table](using-a-sequence-table.md).

 

 



