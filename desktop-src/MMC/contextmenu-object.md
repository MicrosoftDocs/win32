---
title: ContextMenu Object object
description: The ContextMenu object is used to manage and iterate an MMC context menu; it serves as a collection of MenuItem objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4c94aedf-86f8-4f13-b2e2-51f402e69b0f
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ContextMenu Object object MMC
- ContextMenu Object object MMC , described
topic_type:
- apiref
api_name:
- ContextMenu Object
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ContextMenu Object object

The **ContextMenu** object is used to manage and iterate an MMC context menu; it serves as a collection of [**MenuItem**](menuitem-object.md) objects.

## Members

The **ContextMenu Object** object has these types of members:

-   [Properties](#properties)

### Properties

The **ContextMenu Object** object has these properties.



| Property                                      | Description                                                                                  |
|:----------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**Count**](contextmenu-count.md)<br/> | Number of [**MenuItem**](menuitem-object.md) objects in use by the context menu.<br/> |
| [**Item**](contextmenu-item.md)<br/>   | Retrieves a [**MenuItem**](menuitem-object.md) object by index or path.<br/>          |



 

## Examples

The **ContextMenu** object supports the "For Each" enumeration syntax, as shown in the following example.


```VB
Dim objMenuItem As MMC20.MenuItem
' objCtxMenu is a ContextMenu object.
For Each objMenuItem In objCtxMenu
   ' Use the MenuItem object.
    MsgBox (objMenuItem.DisplayName)
Next
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| IID<br/>                      | IID\_ContextMenu is defined as DAB39CE0-25E6-4E07-8362-BA9C95706545<br/>          |



## See also

<dl> <dt>

[**View.ScopeNodeContextMenu**](view-scopenodecontextmenu.md)
</dt> <dt>

[**View.SelectionContextMenu**](view-selectioncontextmenu.md)
</dt> </dl>

 

 





