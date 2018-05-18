---
title: System.Shell.Folder.Items property
description: A collection of System.Shell.Item objects.
ms.assetid: '21a7d81d-2b8e-4d53-9b2a-eccbbb5e14c0'
keywords: ["Items property Windows Sidebar", "Items property Windows Sidebar , System.Shell.Folder object", "System.Shell.Folder object Windows Sidebar , Items property"]
topic_type:
- apiref
api_name:
- System.Shell.Folder.Items
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Shell.Folder.Items property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

A collection of [**System.Shell.Item**](system-shell-item.md) objects.

> [!Note]  
> Objects of type [**System.Shell.Item**](system-shell-item.md) can only be accessed through the **Items** collection. This collection is a member of [**System.Shell.Folder**](system-shell-folder.md).

 

This property is read-only.

## Syntax


```JScript
objItems = System.Shell.Folder.Items
```



## Property value

A collection of [**System.Shell.Item**](system-shell-item.md) objects.

## Remarks

Each [**System.Shell.Item**](system-shell-item.md) in the **Items** collection corresponds to a file system object present on the machine.

## Examples

The following example demonstrates how to create an **Items** collection, select the [**System.Shell.Item**](system-shell-item.md) instance at index `3` from the **Items** collection, and access the `isFolder` property of that **System.Shell.Item** instance.


```JScript
// Create an Items Collection.
var collItems = System.Shell.Folder.Items; 
            
// Get the System.Shell.Item instance at index 3 of the collection.
var oMyShellItem = collItems.item(3);  
            
// Get the value of the IsFolder property of oMyShellItem.
var bIsFolder = oMyShellItem.IsFolder;
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**count**](system-shell-folder-items-count.md)
</dt> <dt>

[**item**](system-shell-folder-items-item.md)
</dt> <dt>

[**System.Shell.Item**](system-shell-item.md)
</dt> <dt>

[**System.Shell.Folder**](system-shell-folder.md)
</dt> </dl>

 

 





