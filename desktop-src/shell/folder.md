---
description: Represents a Shell folder. This object contains properties and methods that allow you to retrieve information about the folder.
ms.assetid: 'f1e82c61-205e-47c8-bc7c-6a52410a672e'
title: Folder object (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Folder
api_type: 
- COM
api_location: 
- Shldisp.h
---

# Folder object

Represents a Shell folder. This object contains properties and methods that allow you to retrieve information about the folder.

## Members

The **Folder** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Folder** object has these methods.



| Method                                      | Description                                                                                                                |
|:--------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| [**CopyHere**](folder-copyhere.md)         | Copies an item or items to a folder.<br/>                                                                            |
| [**GetDetailsOf**](folder-getdetailsof.md) | Retrieves details about an item in a folder. For example, its size, type, or the time of its last modification.<br/> |
| [**Items**](folder-items.md)               | Retrieves a [**FolderItems**](folderitems.md) object that represents the collection of items in the folder.<br/>    |
| [**MoveHere**](folder-movehere.md)         | Moves an item or items to this folder.<br/>                                                                          |
| [**NewFolder**](folder-newfolder.md)       | Creates a new folder.<br/>                                                                                           |
| [**ParseName**](folder-parsename.md)       | Creates and returns a [**FolderItem**](folderitem.md) object that represents a specified item.<br/>                 |



 

### Properties

The **Folder** object has these properties.



| Property                                               | Access type          | Description                                          |
|:-------------------------------------------------------|:---------------------|:-----------------------------------------------------|
| [**Application**](folder-application.md)<br/>   | Read-only<br/> | Contains the folder's Application object.<br/> |
| [**Parent**](folder-parent.md)<br/>             | Read-only<br/> | Not implemented.<br/>                          |
| [**ParentFolder**](folder-parentfolder.md)<br/> | Read-only<br/> | Contains the parent **Folder** object.<br/>    |
| [**Title**](folder-title.md)<br/>               | Read-only<br/> | Contains the title of the folder.<br/>         |



 

## Remarks

> [!Note]  
> Not all methods are implemented for all folders. For example, the [**ParseName**](folder-parsename.md) method is not implemented for the Control Panel folder (CSIDL\_CONTROLS). If you attempt to call an unimplemented method, a 0x800A01BD (decimal 445) error is raised.

 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                 |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl> |



 

 




