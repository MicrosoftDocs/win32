---
title: FontName Property (Balloon Object)
description: FontName Property
ms.assetid: a84a19a4-9e0e-4736-b401-286e6618bc19
ms.topic: article
ms.date: 05/31/2018
---

# FontName Property (Balloon Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the font used in the word balloon for the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters("***CharacterID***").Balloon.FontName** \[ = *font*\]



| Part   | Description                                      |
|--------|--------------------------------------------------|
| *font* | A string value corresponding to the font's name. |



 

</dd> </dl>

## Remarks

The [**FontName**](fontname-property.md) property defines the font used to display text in the word balloon window of a string. The default value for the font settings of a character's word balloon are set in the Microsoft Agent Character Editor. In addition, the user can override font settings for all characters in the Microsoft Agent property sheet.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

> [!Note]  
> If you are using a character that you did not compile, check the [**FontName**](fontname-property.md) and [**FontCharSet**](fontcharset-property.md) properties for the character to determine whether they are appropriate for your locale. You may need to set these values before using the [**Speak**](speak-method.md) method to ensure appropriate text display within the word balloon.

 

 

 




