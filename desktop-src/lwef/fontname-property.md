---
title: FontName Property (Commands Object)
description: Learn about the FontName Commands object property. Microsoft Agent is deprecated as of Windows 7.
ms.assetid: 7de3653e-9b4d-4a31-82d5-243f10e2743b
ms.topic: article
ms.date: 05/31/2018
---

# FontName Property (Commands Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the font used in the character's pop-up menu.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters("***CharacterID***").Commands.FontName** \[ = *Font*\]



| Part   | Description                                      |
|--------|--------------------------------------------------|
| *Font* | A string value corresponding to the font's name. |



 

</dd> </dl>

## Remarks

The **FontName** property defines the font used to display text in the character's pop-up menu. The default value for the font setting is based on the menu font setting for the character's **LanguageID** setting, or -- if that's not set -- the user default language ID setting.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

 

 




