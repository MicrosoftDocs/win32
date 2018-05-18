---
title: MenuItem LanguageIndependentName property
description: The LanguageIndependentName property returns the language-independent name of the menu item or the display name, without accelerator key coding, if there is no language-independent name. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '27cdb135-08e5-478e-bd24-a76fe18f3cea'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["LanguageIndependentName property MMC", "LanguageIndependentName property MMC , MenuItem object", "MenuItem object MMC , LanguageIndependentName property", "LanguageIndependentName property MMC , MenuItem interface", "MenuItem interface MMC , LanguageIndependentName property"]
topic_type:
- apiref
api_name:
- MenuItem.LanguageIndependentName
- MenuItem.LanguageIndependentName
api_location:
- Mmcndmgr.dll
api_type:
- COM
---

# MenuItem::LanguageIndependentName property

The **LanguageIndependentName** property returns the language-independent name of the menu item or the display name, without accelerator key coding, if there is no language-independent name. This property is read-only.

## Syntax


```VB
Property LanguageIndependentName As String
```



## Property value

The language-independent name for the menu item if it exists; otherwise, the return value is the display name with any accelerator key coding removed.

## Examples


```VB
' Display the MenuItem's LanguageIndependentName property.
MsgBox ("LanguageIndependentName: " _
        & objMenuItem.LanguageIndependentName)
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_MenuItem is defined as 0178FAD1-B361-4B27-96AD-67C57EBF2E1D<br/>             |



## See also

<dl> <dt>

[**MenuItem.DisplayName**](menuitem-displayname.md)
</dt> <dt>

[**MenuItem.LanguageIndependentPath**](menuitem-languageindependentpath.md)
</dt> <dt>

[**ContextMenu.Item**](contextmenu-item.md)
</dt> <dt>

[**ContextMenu object**](contextmenu-object.md)
</dt> </dl>

 

 





