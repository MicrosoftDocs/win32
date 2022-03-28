---
description: Represents the collection of verbs for an item in a Shell folder. This object contains properties and methods that allow you to retrieve information about the collection.
title: FolderItemVerbs object (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FolderItemVerbs
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 31badb4b-b89e-4294-9dd7-bda716e163b2

---

# FolderItemVerbs object

Represents the collection of verbs for an item in a Shell folder. This object contains properties and methods that allow you to retrieve information about the collection.

## Members

The **FolderItemVerbs** object has these types of members:

- [Methods](#methods)
- [Properties](#properties)

### Methods

The **FolderItemVerbs** object has these methods.



| Method                                        | Description                                                                                                      |
|:----------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](folderitemverbs--newenum.md) | Creates and returns a new **FolderItemVerbs** object that is a copy of this FolderItemVerbs object.<br/>   |
| [**Item**](folderitemverbs-item.md)          | Retrieves the [**FolderItemVerb**](folderitemverb.md) object for a specified item in the collection.<br/> |



 

### Properties

The **FolderItemVerbs** object has these properties.



| Property                                                      | Access type          | Description                                                |
|:--------------------------------------------------------------|:---------------------|:-----------------------------------------------------------|
| [**Application**](folderitemverbs-application.md)<br/> | Read-only<br/> | Not implemented.<br/>                                |
| [**Count**](folderitemverbs-count.md)<br/>             | Read-only<br/> | Contains the number of items in the collection.<br/> |
| [**Parent**](folderitemverbs-parent.md)<br/>           | Read-only<br/> | Not implemented.<br/>                                |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




