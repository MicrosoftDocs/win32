---
description: Custom actions intended to change the system state must be deferred execution custom actions.
ms.assetid: 48707ae1-9488-4bbb-8447-b24e383affb7
title: Changing the System State Using a Custom Action
ms.topic: article
ms.date: 05/31/2018
---

# Changing the System State Using a Custom Action

Custom actions intended to change the system state must be deferred execution custom actions. Custom actions that set properties, feature states, component states, or target directories, or schedule system operations by inserting rows into sequence tables can use immediate execution safely. However, custom actions that change the system directly or call another system service must be deferred to the time when the installation script is executed. For more information, see [Deferred Execution Custom Actions](deferred-execution-custom-actions.md).

You should not attempt to use an immediate execution custom action to change the system state, because every custom action that changes the state needs to have a corresponding rollback custom action to undo the system state change on an installation rollback. All rollback custom actions are also deferred custom actions and must precede the action they undo. For more information, see [Rollback Custom Actions](rollback-custom-actions.md).

 

 



