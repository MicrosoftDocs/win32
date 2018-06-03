---
title: Items.item property
description: Gets a System.Shell.Item from the Items collection.
ms.assetid: 976518af-616e-497f-a2a6-ced9082c67c8
keywords:
- item property Windows Sidebar
- item property Windows Sidebar , Items collection
- Items collection Windows Sidebar , item property
topic_type:
- apiref
api_name:
- Items.item
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Items.item property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets a [**System.Shell.Item**](system-shell-item.md) from the [**Items**](system-shell-folder-items.md) collection.

This property is read-only.

## Syntax


```JScript
objitem = Items.item
```



## Property value

An **Object** that receives a [**System.Shell.Item**](system-shell-item.md) at the specified index.

## Examples

The following example demonstrates how to access an item in the [**Items**](system-shell-folder-items.md) collection and get a specific property for that item.


```JScript

```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**System.Shell.Item**](system-shell-item.md)
</dt> <dt>

[**System.Shell.Folder**](system-shell-folder.md)
</dt> <dt>

[**Items**](system-shell-folder-items.md)
</dt> <dt>

[**count**](system-shell-folder-items-count.md)
</dt> </dl>

 

 





