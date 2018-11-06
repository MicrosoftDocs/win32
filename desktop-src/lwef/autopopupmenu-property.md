---
title: AutoPopupMenu Property
description: AutoPopupMenu Property
ms.assetid: 499092cb-0990-4edb-915c-12e3011de142
ms.topic: article
ms.date: 05/31/2018
---

# AutoPopupMenu Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets whether right-clicking the character or its taskbar icon automatically displays the character's pop-up menu.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters****("***CharacterID***").AutoPopupMenu** \[ = *boolean*\]



| Part      | Description                                                                                                                                                                                                                                           |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *boolean* | A Boolean expression specifying whether the server automatically displays the character's pop-up menu on right-click. **True** (Default) Displays the menu on right-click. <br/> **False** Does not display the menu on right-click.<br/> |



 

</dd> </dl>

## Remarks

By setting this property to **False**, you can create your own menu-handling behavior. To display the menu after setting this property to **False**, use the [**ShowPopupMenu**](showpopupmenu-method.md) method.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**ShowPopupMenu method**](showpopupmenu-method.md)


 

 





