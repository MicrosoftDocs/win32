---
title: FontSize Property (Commands Object)
description: FontSize Property
ms.assetid: a1113a3a-5da8-4077-8565-168963c503d2
ms.topic: article
ms.date: 05/31/2018
---

# FontSize Property (Commands Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the font size used in the character's pop-up menu.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters("***CharacterID***").Commands.FontSize** \[ = *Points*\]



| Part     | Description                                              |
|----------|----------------------------------------------------------|
| *Points* | A Long integer value specifying the font size in points. |



 

</dd> </dl>

## Remarks

The **FontSize** property defines the point size of the font used to display text in the character's pop-up menu. The default value for the font setting is based on the menu font setting for the character's **LanguageID** setting, or—if that's not set—the user default language setting.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

 

 




