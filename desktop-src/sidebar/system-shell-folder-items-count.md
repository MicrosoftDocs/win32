---
title: Items.count property
description: Gets the number of System.Shell.Item objects in the Items collection.
ms.assetid: '807f08b1-7dec-4327-81d9-18fee8dc17f0'
keywords: ["count property Windows Sidebar", "count property Windows Sidebar , Items collection", "Items collection Windows Sidebar , count property"]
topic_type:
- apiref
api_name:
- Items.count
api_location:
- Sidebar.Exe
api_type:
- COM
---

# Items.count property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the number of [**System.Shell.Item**](system-shell-item.md) objects in the [**Items**](system-shell-folder-items.md) collection.

This property is read-only.

## Syntax


```JScript
icount = Items.count
```



## Property value

An **Integer** that receives the number of items.

## Examples

The following example demonstrates how to access an item in the [**Items**](system-shell-folder-items.md) collection and get a specific property for that item.


```JScript

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

[**item**](system-shell-folder-items-item.md)
</dt> <dt>

[**System.Shell.Item**](system-shell-item.md)
</dt> <dt>

[**System.Shell.Folder**](system-shell-folder.md)
</dt> <dt>

[**Items**](system-shell-folder-items.md)
</dt> </dl>

 

 





