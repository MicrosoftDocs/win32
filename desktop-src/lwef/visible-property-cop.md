---
title: Visible Property
description: Visible Property
ms.assetid: 80137e16-4646-4251-b1c0-bca39ff7a233
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Visible Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets whether the [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) is visible in the character's pop-up menu.

</dd> <dt>

<span id="Syntax_"></span><span id="syntax_"></span><span id="SYNTAX_"></span>**Syntax** 
</dt> <dd>

*agent***.Characters(**"*CharacterID*"**).Commands(**"*name*"**).Visible** \[ = *boolean*\]



| Part      | Description                                                                                                                                                                                                                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *boolean* | A Boolean expression specifying whether the [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441)'s caption appears in the character's pop-up menu.<br/> **True** (Default) The caption appears.<br/> **False** The caption does not appear.<br/> |



 

</dd> </dl>

## Remarks

Set this property to **False** when you want to include voice input for your own interfaces without having them appear in the pop-up menu for the character. If you set a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object's [**Caption**](caption-property.md) property to the empty string (""), the caption text will not appear in the pop-up menu (for example, as a blank line), regardless of its [**Visible**](visible-property.md) property setting.

The [**Visible**](visible-property.md) property setting of a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object's parent [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection does not affect the **Visible** property setting of the **Command**.

 

 





