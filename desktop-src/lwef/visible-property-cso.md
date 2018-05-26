---
title: Visible Property
description: Visible Property
ms.assetid: 0178a789-141b-4d4c-ba7c-05c7995f13bc
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

Returns or sets a value that determines whether your [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection's caption appears in the character's pop-up menu.

</dd> <dt>

<span id="Syntax_"></span><span id="syntax_"></span><span id="SYNTAX_"></span>**Syntax** 
</dt> <dd>

*agent***.Characters(**"*CharacterID*"**).Commands.Visible** \[ = *boolean*\]



| Part      | Description                                                                                                                                                                                                                             |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *boolean* | A Boolean expression specifying whether your [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) object appears in the character's pop-up menu. <br/> **True** The caption appears.<br/> **False** The caption does not appear.<br/> |



 

</dd> </dl>

## Remarks

For the caption to appear in the character's pop-up menu when your application is not the input-active client, this property must be set to **True** and the [**Caption**](caption-property.md) property set for your Commands collection. In addition, this property must be set to **True** for commands in your collection to appear in the pop-up menu when your application is input-active.

 

 





