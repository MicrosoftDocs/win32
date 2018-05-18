---
Description: 'Independent software vendors (ISVs) can extend the set of known folders on a system by registering known folders of their own.'
ms.assetid: 'bb2c63e6-7525-4d20-ac50-591b3e53dea2'
title: How to Extend Known Folders with Custom Folders
---

# How to Extend Known Folders with Custom Folders

Independent software vendors (ISVs) can extend the set of known folders on a system by registering known folders of their own. Once registered, those third-party folders are known to the system. They are found by any call to [**IKnownFolderManager::GetFolderIds**](iknownfoldermanager-getfolderids.md). Note that a known folder must be a per-machine folder. You cannot create a per-user known folder.

## Instructions

### Step 1:

Define your known folder through a [**KNOWNFOLDER\_DEFINITION**](knownfolder-definition.md) structure.

### Step 2:

Register the known folder through a call to [**IKnownFolderManager::RegisterFolder**](iknownfoldermanager-registerfolder.md).

## Remarks

If you create a known folder for your application as part of your installation procedure, you must also include [**IKnownFolderManager::UnregisterFolder**](iknownfoldermanager-unregisterfolder.md) as part of your uninstallation code.

Give consideration to why you want your folder to be included in the known folder system before you register it. You should have a valid reason for elevating your folder to that level of system visibility.

## Related topics

<dl> <dt>

[Known Folders Sample](shell.samples_knownfolders)
</dt> </dl>

 

 



