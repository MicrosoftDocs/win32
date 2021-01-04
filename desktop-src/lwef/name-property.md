---
title: Name Property (Characters Object)
description: Name Property
ms.assetid: 'vs|msagent|~\pacontrol_2bxm.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Name Property (Characters Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets a string that specifies the default name of the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Name** \[ = *string*\]



| Part     | Description                                                                             |
|----------|-----------------------------------------------------------------------------------------|
| *string* | A string value corresponding to the character's name (in the current language setting). |



 

</dd> </dl>

## Remarks

A character's **Name** may depend on the character's [**LanguageID**](languageid-property.md) setting. A character's name in one language may be different or use different characters than in another. The character's default **Name** for a specific language is defined when the character is compiled with the Microsoft Agent Character Editor.

Avoid renaming a character, especially when using it in a scenario where other client applications may use the same character. Also, Agent uses the character's **Name** to automatically create commands for hiding and showing the character.

 

 




