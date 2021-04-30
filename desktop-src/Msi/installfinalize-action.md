---
description: The InstallFinalize action runs a script that contains all operations in the action sequence since either the start of the installation or the execution of the InstallExecute or InstallExecuteAgain actions.
ms.assetid: ed0e3c4f-d1ee-43b7-84a2-f4afe3ec28c6
title: InstallFinalize Action
ms.topic: article
ms.date: 05/31/2018
---

# InstallFinalize Action

The InstallFinalize action runs a script that contains all operations in the action sequence since either the start of the installation or the execution of the [InstallExecute](installexecute-action.md) or [InstallExecuteAgain](installexecuteagain-action.md) actions. This action marks the end of a transaction that begins with the [InstallInitialize](installinitialize-action.md) action.

## Sequence Restrictions

The [InstallInitialize](installinitialize-action.md) action must come before the InstallFinalize action.

## ActionData Messages

There are no ActionData messages.

## Remarks

If it is detected that the product is marked for complete removal, operations are automatically added to the script to remove the **Add/Remove Programs** in the **Control Panel** information for the product, to unregister and unpublish the product, and to remove the cached local database from %WINDOWS%, if it exists.

System changes made before the action may not be restored after the InstallFinalize action is executed. The InstallFinalize action updates the system with all operations determined to that point and then ends the transaction.

 

 



