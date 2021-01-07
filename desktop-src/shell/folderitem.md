---
description: Represents an item in a Shell folder. This object contains properties and methods that allow you to retrieve information about the item.
title: FolderItem object (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FolderItem
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 38c0e049-2f9f-43bc-8bf2-1b7becf16e66
api_name: 
 - FolderItem
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# FolderItem object

Represents an item in a Shell folder. This object contains properties and methods that allow you to retrieve information about the item.

## Members

The **FolderItem** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FolderItem** object has these methods.



| Method                                      | Description                                                                                                                                                 |
|:--------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**InvokeVerb**](folderitem-invokeverb.md) | Executes a verb on the item.<br/>                                                                                                                     |
| [**Verbs**](folderitem-verbs.md)           | Retrieves the item's [**FolderItemVerbs**](folderitemverbs.md) object. This object is the collection of verbs that can be executed on the item.<br/> |



 

### Properties

The **FolderItem** object has these properties.



| Property                                                   | Access type           | Description                                                                                                                                                                                                        |
|:-----------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Application**](folderitem-application.md)<br/>   | Read-only<br/>  | Contains the [**Application**](folderitem-application.md) object of the folder item.<br/>                                                                                                                   |
| [**GetFolder**](folderitem-getfolder.md)<br/>       | Read-only<br/>  | Contains the item's [**Folder**](folder.md) object, if the item is a folder.<br/>                                                                                                                           |
| [**GetLink**](folderitem-getlink.md)<br/>           | Read-only<br/>  | Contains the item's [**ShellLinkObject**](shelllinkobject-object.md) object, if the item is a shortcut.<br/>                                                                                                |
| [**IsBrowsable**](folderitem-isbrowsable.md)<br/>   | Read-only<br/>  | Indicates if the item can be hosted inside a browser or Windows Explorer frame.<br/>                                                                                                                         |
| [**IsFileSystem**](folderitem-isfilesystem.md)<br/> | Read-only<br/>  | Indicates if the item is part of the file system.<br/>                                                                                                                                                       |
| [**IsFolder**](folderitem-isfolder.md)<br/>         | Read-only<br/>  | Indicates if the item is a folder.<br/>                                                                                                                                                                      |
| [**IsLink**](folderitem-islink.md)<br/>             | Read-only<br/>  | Indicates whether the item is a shortcut.<br/>                                                                                                                                                               |
| [**ModifyDate**](folderitem-modifydate.md)<br/>     | Read/write<br/> | Sets or gets the date and time that a file was last modified. [**ModifyDate**](folderitem-modifydate.md) can be used to retrieve the date and time that a folder was last modified, but cannot set it.<br/> |
| [**Name**](folderitem-name.md)<br/>                 | Read/write<br/> | Sets or gets the item's name.<br/>                                                                                                                                                                           |
| [**Parent**](folderitem-parent.md)<br/>             | Read-only<br/>  | Gets an object that represents the parent of the item.<br/>                                                                                                                                                  |
| [**Path**](folderitem-path.md)<br/>                 | Read-only<br/>  | Contains the item's full path and name.<br/>                                                                                                                                                                 |
| [**Size**](folderitem-size.md)<br/>                 | Read-only<br/>  | Contains the item's size.<br/>                                                                                                                                                                               |
| [**Type**](folderitem-type.md)<br/>                 | Read-only<br/>  | Contains a string representation of the item's type.<br/>                                                                                                                                                    |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




