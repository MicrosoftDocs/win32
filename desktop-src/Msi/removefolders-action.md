---
description: The RemoveFolders action removes any folders linked to components set to be removed or run from source. These folders are removed only if they are empty. If a folder is removed, it is unregistered with the appropriate component identifier.
ms.assetid: 0f68458e-ae9a-4ca5-bc60-06d4de91e2e9
title: RemoveFolders Action
ms.topic: article
ms.date: 05/31/2018
---

# RemoveFolders Action

The RemoveFolders action removes any folders linked to components set to be removed or run from source. These folders are removed only if they are empty. If a folder is removed, it is unregistered with the appropriate component identifier.

## Sequence Restrictions

The RemoveFolders action must come after the [RemoveFiles](removefiles-action.md) action or any action that may remove files from folders.

## ActionData Messages



| Field | Description of action data    |
|-------|-------------------------------|
| \[1\] | Identifier of removed folder. |



 

## Remarks

The installer does not automatically remove the folders created by the [CreateFolders action](createfolders-action.md) during an uninstallation of the application. The installer must be instructed to remove these folders by authoring the RemoveFolders action into the action sequence.

To specify the name and location of the folder, use the Directory\_ column of the [CreateFolder table](createfolder-table.md). Each folder name in the CreateFolder table is assumed to be a property defining the folder location.

To specify the component owning the folder, use the ComponentId column of the [Component table](component-table.md).

 

 



