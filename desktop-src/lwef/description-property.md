---
title: Description Property (Legacy Windows Environment Features)
description: Description Property
ms.assetid: 81ac4bc7-ef0c-4e7c-b57e-acc4ad315515
ms.topic: article
ms.date: 05/31/2018
---

# Description Property (Legacy Windows Environment Features)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets a string that specifies the description for the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent*.**Characters("***CharacterID***").Description** \[ = *string*\]



| Part     | Description                                                                                    |
|----------|------------------------------------------------------------------------------------------------|
| *string* | A string value corresponding to the character's description (in the current language setting). |



 

</dd> </dl>

## Remarks

A character's **Description** may depend on the character's **LanguageID** setting. A character's name in one language may be different or use different characters than in another. The character's default **Description** for a specific language is defined when the character is compiled with the Microsoft Agent Character Editor.

> [!Note]  
> The **Description** property setting is optional and may not be supplied for all characters.

 

 

 




