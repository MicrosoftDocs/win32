---
title: MenuItem Path property
description: The Path property returns the path of the menu item.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 12574172-0cba-4d50-bcfd-bbffe0848163
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Path property MMC
- Path property MMC , MenuItem object
- MenuItem object MMC , Path property
- Path property MMC , MenuItem interface
- MenuItem interface MMC , Path property
topic_type:
- apiref
api_name:
- MenuItem.Path
- MenuItem.Path
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MenuItem::Path property

The **Path** property returns the path of the menu item.

The path starts at the root, and the menu items are separated by "-&gt;". This property is read-only.

## Syntax


```VB
Property Path As String
```



## Property value

The path of the menu item, starting from the root.

## Examples


```VB
' Display the MenuItem's Path property.
MsgBox ("Path: " & objMenuItem.Path)
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_MenuItem is defined as 0178FAD1-B361-4B27-96AD-67C57EBF2E1D<br/>             |



## See also

<dl> <dt>

[**MenuItem.LanguageIndependentPath**](menuitem-languageindependentpath.md)
</dt> </dl>

 

 





