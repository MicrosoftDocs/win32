---
title: MenuItem DisplayName property
description: The DisplayName property returns the display name of the menu item. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 67e0ace5-6fe9-47eb-a4e7-75b748361733
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- DisplayName property MMC
- DisplayName property MMC , MenuItem object
- MenuItem object MMC , DisplayName property
- DisplayName property MMC , MenuItem interface
- MenuItem interface MMC , DisplayName property
topic_type:
- apiref
api_name:
- MenuItem.DisplayName
- MenuItem.DisplayName
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MenuItem::DisplayName property

The **DisplayName** property returns the display name of the menu item. This property is read-only.

## Syntax


```VB
Property DisplayName As String
```



## Property value

The display name of the menu item.

## Remarks

The display name returned by this property includes any accelerator key coding. For example, the string "&Properties ALT+ENTER" may be returned. The ampersand ("&") causes the letter "P" to be underlined when the menu is displayed to the user (as well as invoking the menu item if the user presses the letter P while the menu is active). The ALT+ENTER represents the shortcut key sequence (accelerator) that can be used to invoke the menu command.

## Examples


```VB
Dim objMenuItem As MMC20.MenuItem
' Retrieve the first MenuItem in the ContextMenu object.
' objCtxMenu is an MMC20.ContextMenu object.
Set objMenuItem = objCtxMenu.Item(1)
 
' Display the MenuItem's DisplayName property.
MsgBox ("DisplayName: " & objMenuItem.DisplayName)
 
' Free the object when done.
Set objMenuItem = Nothing
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

[**MenuItem.LanguageIndependentName**](menuitem-languageindependentname.md)
</dt> <dt>

[**MenuItem.LanguageIndependentPath**](menuitem-languageindependentpath.md)
</dt> <dt>

[**ContextMenu.Item**](contextmenu-item.md)
</dt> <dt>

[**ContextMenu object**](contextmenu-object.md)
</dt> </dl>

 

 





