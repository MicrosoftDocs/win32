---
Description: Represents a single verb available to an item. This object contains properties and methods that allow you to retrieve information about the verb.
title: FolderItemVerb object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FolderItemVerb
api_type: 
- COM
api_location: 
- Shell32.dll
---

# FolderItemVerb object

Represents a single verb available to an item. This object contains properties and methods that allow you to retrieve information about the verb.

## Members

The **FolderItemVerb** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **FolderItemVerb** object has these methods.



| Method                              | Description                                                                                  |
|:------------------------------------|:---------------------------------------------------------------------------------------------|
| [**DoIt**](folderitemverb-doit.md) | Executes a verb on the [**FolderItem**](folderitem.md) associated with the verb.<br/> |



 

### Properties

The **FolderItemVerb** object has these properties.



| Property                                                     | Access type          | Description                          |
|:-------------------------------------------------------------|:---------------------|:-------------------------------------|
| [**Application**](folderitemverb-application.md)<br/> | Read-only<br/> | Not implemented.<br/>          |
| [**Name**](folderitemverb-name.md)<br/>               | Read-only<br/> | Contains the verb's name.<br/> |
| [**Parent**](folderitemverb-parent.md)<br/>           | Read-only<br/> | Not implemented.<br/>          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




