---
title: ContextMenu Count property
description: The Count property returns the number of MenuItem objects that are included in the ContextMenu object. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1a773536-c44e-480c-a087-523d8695872d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Count property MMC
- Count property MMC , ContextMenu object
- ContextMenu object MMC , Count property
- Count property MMC , ContextMenu interface
- ContextMenu interface MMC , Count property
topic_type:
- apiref
api_name:
- ContextMenu.Count
- ContextMenu.Count
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ContextMenu::Count property

The **Count** property returns the number of [**MenuItem**](menuitem-object.md) objects that are included in the [**ContextMenu**](contextmenu-object.md) object. This property is read-only.

## Syntax


```VB
Property Count As Long
```



## Property value

The number of [**MenuItem**](menuitem-object.md) objects contained in this context menu.

## Examples


```VB
' Retrieve the item count of the ContextMenu object.
Dim nCount As Long
nCount = objCtxMenu.Count
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_ContextMenu is defined as DAB39CE0-25E6-4E07-8362-BA9C95706545<br/>          |



## See also

<dl> <dt>

[**ContextMenu.Item**](contextmenu-item.md)
</dt> </dl>

 

 





