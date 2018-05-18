---
title: System.Shell.Item object
description: Defines the properties of each member of the Items collection.
ms.assetid: '78d971cb-4a29-42a2-a650-d9c3aa4f5b55'
keywords: ["System.Shell.Item object Windows Sidebar", "System.Shell.Item object Windows Sidebar , described"]
topic_type:
- apiref
api_name:
- System.Shell.Item
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.Item object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties of each member of the [**Items**](system-shell-folder-items.md) collection.

## Members

The **System.Shell.Item** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **System.Shell.Item** object has these methods.



| Method                                             | Description                                                                                              |
|:---------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| [**invokeVerb**](system-shell-item-invokeverb.md) | Invokes a verb associated with the item. <br/>                                                     |
| [**metadata**](system-shell-item-metadata.md)     | Retrieves the metadata value for a canonical property name key of the **System.Shell.Item**. <br/> |



 

### Properties

The **System.Shell.Item** object has these properties.



| Property                                                          | Access type          | Description                                                                                                  |
|:------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------|
| [**isFileSystem**](system-shell-item-isfilesystem.md)<br/> | Read-only<br/> | Gets whether the object is a file. <br/>                                                               |
| [**isFolder**](system-shell-item-isfolder.md)<br/>         | Read-only<br/> | Gets whether the object is a folder. <br/>                                                             |
| [**isLink**](system-shell-item-islink.md)<br/>             | Read-only<br/> | Gets whether the object is a link (or shortcut). <br/>                                                 |
| [**link**](system-shell-item-link.md)<br/>                 | Read-only<br/> | Gets a **System.Shell.Item** object that represents the linked item. <br/>                             |
| [**modifyDate**](system-shell-item-modifydate.md)<br/>     | Read-only<br/> | Gets the last modified date of the **System.Shell.Item**. <br/>                                        |
| [**name**](system-shell-item-name.md)<br/>                 | Read-only<br/> | Gets the name of the **System.Shell.Item**. <br/>                                                      |
| [**path**](system-shell-item-path.md)<br/>                 | Read-only<br/> | Gets the UNC path (with filename) of the **System.Shell.Item**. <br/>                                  |
| [**SHFolder**](system-shell-item-shfolder.md)<br/>         | Read-only<br/> | Gets a [**System.Shell.Folder**](system-shell-folder.md) object from the **System.Shell.Item**. <br/> |
| [**size**](system-shell-item-size.md)<br/>                 | Read-only<br/> | Gets the size (in bytes) of the **System.Shell.Item**. <br/>                                           |
| [**type**](system-shell-item-type.md)<br/>                 | Read-only<br/> | Gets the verbose file type (not the extension) of the Windows Shell item. <br/>                        |



 

## Remarks

Each **System.Shell.Item** in the [**Items**](system-shell-folder-items.md) collection corresponds to a file system object present on the machine.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





