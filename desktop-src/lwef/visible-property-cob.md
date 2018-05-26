---
title: Visible Property
description: Visible Property
ms.assetid: c06d623d-8997-413a-b4ab-24275eccfa10
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Visible Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns a Boolean indicating whether the character is visible.

</dd> <dt>

<span id="Syntax_"></span><span id="syntax_"></span><span id="SYNTAX_"></span>**Syntax** 
</dt> <dd>

*agent***.Characters(**"*CharacterID*"**).Visible**



| Value | Description                            |
|-------|----------------------------------------|
| True  | The character is displayed.            |
| False | The character is hidden (not visible). |



 

</dd> </dl>

## Remarks

This property indicates whether the character's frame is being displayed. It does not necessarily mean that there is an image on the screen. For example, this property returns **True** even when the character is positioned off the visible display area or when the current character frame contains no images. This property's setting applies to all clients of the character.

This property is read-only. To make a character visible or hidden, use the [**Show**](show-method.md) or [**Hide**](lwef-odhide_method) methods.

 

 




