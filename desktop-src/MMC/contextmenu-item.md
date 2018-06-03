---
title: ContextMenu Item property
description: The Item property returns the MenuItem object at a specified index or specified path. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8d8ca283-f29f-4e0c-a278-4fc240994fe3
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Item property MMC
- Item property MMC , ContextMenu object
- ContextMenu object MMC , Item property
- Item property MMC , ContextMenu interface
- ContextMenu interface MMC , Item property
topic_type:
- apiref
api_name:
- ContextMenu.Item
- ContextMenu.Item
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ContextMenu::Item property

The **Item** property returns the [**MenuItem**](menuitem-object.md) object at a specified index or specified path. This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal IndexOrPath As Variant _
) As MenuItem
```



## Property value

The [**MenuItem**](menuitem-object.md) object at the position specified by *IndexOrPath* in the set of **MenuItem** objects maintained by this collection, or **NULL** if the item does not exist.

## Examples


```VB
' Retrieve the item count of the ContextMenu object.
Dim nCount As Long
nCount = objCtxMenu.Count

Dim i As Long
Dim objMenuItem As MMC20.MenuItem
 
' Iterate the menu items using the index.
For i = 1 To nCount
    Set objMenuItem = objCtxMenu.Item(i)
    ' Use the MenuItem object. For example,
    ' display the name.
    MsgBox (objMenuItem.DisplayName)
    ' Free the object for the next iteration.
    Set objMenuItem = Nothing
Next i
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

[**ContextMenu.Count**](contextmenu-count.md)
</dt> <dt>

[**MenuItem object**](menuitem-object.md)
</dt> </dl>

 

 





