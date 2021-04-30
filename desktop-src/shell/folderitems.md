---
description: Represents the collection of items in a Shell folder. This object contains properties and methods that allow you to retrieve information about the collection.
title: FolderItems object (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FolderItems
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: b99201b3-95e8-4ddd-b338-dee8d107d0a0
api_name: 
 - FolderItems
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# FolderItems object

Represents the collection of items in a Shell folder. This object contains properties and methods that allow you to retrieve information about the collection.

## Members

The **FolderItems** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FolderItems** object has these methods.



| Method                                    | Description                                                                                              |
|:------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](folderitems--newenum.md) | Not implemented.<br/>                                                                              |
| [**Item**](folderitems-item.md)          | Retrieves the [**FolderItem**](folderitem.md) object for a specified item in the collection.<br/> |



 

### Properties

The **FolderItems** object has these properties.



| Property                                                  | Access type          | Description                                                                                                   |
|:----------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------|
| [**Application**](folderitems-application.md)<br/> | Read-only<br/> | Contains the [**Application**](folderitems-application.md) object of the folder items collection.<br/> |
| [**Count**](folderitems-count.md)<br/>             | Read-only<br/> | Contains the number of items in the collection.<br/>                                                    |
| [**Parent**](folderitems-parent.md)<br/>           | Read-only<br/> | Not implemented.<br/>                                                                                   |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




