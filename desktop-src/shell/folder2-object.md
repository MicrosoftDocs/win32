---
description: Extends the Folder object to support offline folders.
title: Folder2 object (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Folder2
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 5b52b141-ced3-4d38-8584-7dfcfe12ab56

---

# Folder2 object

Extends the [**Folder**](folder.md) object to support offline folders.

## Members

The **Folder2** object has these types of members:

- [Methods](#methods)
- [Properties](#properties)

### Methods

The **Folder2** object has these methods.



| Method                                                                 | Description                                                                          |
|:-----------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
| [**DismissedWebViewBarricade**](folder2-dismissedwebviewbarricade.md) | Called in response to the web view barricade being dismissed by the user.<br/> |
| [**Synchronize**](folder2-synchronize.md)                             | Synchronizes all offline files in the folder.<br/>                             |



 

### Properties

The **Folder2** object has these properties.



| Property                                                                            | Access type          | Description                                                               |
|:------------------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------|
| [**HaveToShowWebViewBarricade**](folder2-havetoshowwebviewbarricade.md)<br/> | Read-only<br/> | Not currently supported.<br/>                                       |
| [**OfflineStatus**](folder2-offlinestatus.md)<br/>                           | Read-only<br/> | Contains the offline status of the folder.<br/>                     |
| [**Self**](folder2-self.md)<br/>                                             | Read-only<br/> | Contains the folder's [**FolderItem**](folderitem.md) object.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**Folder**](folder.md)
</dt> </dl>

 

 




