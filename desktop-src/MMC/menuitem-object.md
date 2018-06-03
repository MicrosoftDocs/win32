---
title: MenuItem Object object
description: The MenuItem object encapsulates a single context menu item.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 43e25217-d9b5-45aa-a90c-7d5d6a50f8b0
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MenuItem Object object MMC
- MenuItem Object object MMC , described
topic_type:
- apiref
api_name:
- MenuItem Object
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# MenuItem Object object

The **MenuItem** object encapsulates a single context menu item.

## Members

The **MenuItem Object** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MenuItem Object** object has these methods.



| Method                              | Description                      |
|:------------------------------------|:---------------------------------|
| [**Execute**](menuitem-execute.md) | Executes a menu item.<br/> |



 

### Properties

The **MenuItem Object** object has these properties.



| Property                                                                       | Access type          | Description                                                                               |
|:-------------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------|
| [**DisplayName**](menuitem-displayname.md)<br/>                         | Read-only<br/> | The name of the menu item, including accelerators.<br/>                             |
| [**Enabled**](menuitem-enabled.md)<br/>                                 | Read-only<br/> | Returns the menu item's enabled status.<br/>                                        |
| [**LanguageIndependentName**](menuitem-languageindependentname.md)<br/> | Read-only<br/> | The language-independent name of the menu item; accelerators are not included.<br/> |
| [**LanguageIndependentPath**](menuitem-languageindependentpath.md)<br/> | Read-only<br/> | The language-independent path of the menu item, starting from the root.<br/>        |
| [**Path**](menuitem-path.md)<br/>                                       | Read-only<br/> | The path of the menu item, starting from the root.<br/>                             |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| IID<br/>                      | IID\_MenuItem is defined as 0178FAD1-B361-4B27-96AD-67C57EBF2E1D<br/>             |



## See also

<dl> <dt>

[**ContextMenu.Item**](contextmenu-item.md)
</dt> <dt>

[**ContextMenu object**](contextmenu-object.md)
</dt> </dl>

 

 





