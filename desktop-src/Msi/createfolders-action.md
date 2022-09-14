---
description: The CreateFolders action creates empty folders for components that are set to be installed.
ms.assetid: 3982eac8-8272-4fb4-870c-390a0b6bd9a1
title: CreateFolders Action
ms.topic: article
ms.date: 05/31/2018
---

# CreateFolders Action

The CreateFolders action creates empty folders for components that are set to be installed. The installer creates folders both for components that run locally and run from source. Newly created folders are registered with the appropriate component identifier.

The CreateFolders action queries the [CreateFolder table](createfolder-table.md) and the [Component table](component-table.md).

## Sequence Restrictions

The CreateFolders action must be executed either before the [InstallFiles](installfiles-action.md) action or before any action that adds files to folders.

## ActionData Messages



| Field | Description of action data description |
|-------|----------------------------------------|
| \[1\] | Directory identifier of folder.        |



 

## Remarks

The installer does not automatically remove folders created by the CreateFolders action during an uninstallation of the application. The installer only removes folders if the [RemoveFolders action](removefolders-action.md) is included in the action sequence.

 

 



