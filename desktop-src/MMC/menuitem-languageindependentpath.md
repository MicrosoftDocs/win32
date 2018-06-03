---
title: MenuItem LanguageIndependentPath property
description: The LanguageIndependentPath property returns the language-independent path of the menu item.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6c2037dd-4c92-47a4-91a7-13bb00be6503
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- LanguageIndependentPath property MMC
- LanguageIndependentPath property MMC , MenuItem object
- MenuItem object MMC , LanguageIndependentPath property
- LanguageIndependentPath property MMC , MenuItem interface
- MenuItem interface MMC , LanguageIndependentPath property
topic_type:
- apiref
api_name:
- MenuItem.LanguageIndependentPath
- MenuItem.LanguageIndependentPath
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MenuItem::LanguageIndependentPath property

The **LanguageIndependentPath** property returns the language-independent path of the menu item.

The language-independent path starts at the root, and the menu items are separated by "-&gt;". This property is read-only.

## Syntax


```VB
Property LanguageIndependentPath As String
```



## Property value

The language-independent path of the menu item, starting from the root.

## Examples


```VB
' Display the MenuItem's LanguageIndependentPath property.
MsgBox ("LanguageIndependentPath: " _
        & objMenuItem.LanguageIndependentPath)
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

[**MenuItem.DisplayName**](menuitem-displayname.md)
</dt> <dt>

[**MenuItem.LanguageIndependentName**](menuitem-languageindependentname.md)
</dt> <dt>

[**MenuItem.Path**](menuitem-path.md)
</dt> <dt>

[**ContextMenu.Item**](contextmenu-item.md)
</dt> <dt>

[**ContextMenu object**](contextmenu-object.md)
</dt> </dl>

 

 





