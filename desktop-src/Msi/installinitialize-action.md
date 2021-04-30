---
description: The InstallInitialize action and InstallFinalize action mark the beginning and end of a sequence of actions that change the system.
ms.assetid: c2637070-3fd9-422c-9252-cf15045c6485
title: InstallInitialize Action
ms.topic: article
ms.date: 05/31/2018
---

# InstallInitialize Action

The InstallInitialize action and [InstallFinalize](installfinalize-action.md) action mark the beginning and end of a sequence of actions that change the system.

## Sequence Restrictions

The InstallInitialize action must be sequenced before any actions that change the system, such as the [InstallFiles](installfiles-action.md) action, the [WriteRegistryValues](writeregistryvalues-action.md) action, the [SelfRegModules](selfregmodules-action.md) action, and the [ProcessComponents](processcomponents-action.md) action. The InstallInitialize action must therefore be sequenced before the [InstallFinalize](installfinalize-action.md) action and the [InstallExecute](installexecute-action.md) action.

[Custom actions](custom-actions.md) that modify the Windows Installer package, for example by adding rows to a table that handles installable resources, such as the [Registry](registry-table.md) table or [DuplicateFile](duplicatefile-table.md) table, must be sequenced before InstallInitialize action.

## ActionData Messages

There are no ActionData messages.

 

 



