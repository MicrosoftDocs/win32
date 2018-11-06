---
title: FontCharSet Property
description: FontCharSet Property
ms.assetid: 2f23a242-d620-4766-8f59-cf158aa55969
ms.topic: article
ms.date: 05/31/2018
---

# FontCharSet Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the character set for the font displayed in the specified character's word balloon.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Balloon.FontCharSet** \[ = *value*\]



| Part    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *value* | An integer value that specifies the character set used by the font. The following are some common settings for value: 0 Standard Windows characters (ANSI).<br/> 1 Default character set.<br/> 2 The symbol character set.<br/> 128 Double-byte character set (DBCS) unique to the Japanese version of Windows.<br/> 129 Double-byte character set (DBCS) unique to the Korean version of Windows.<br/> 134 Double-byte character set (DBCS) unique to the Simplified Chinese version of Windows.<br/> 136 Double-byte character set (DBCS) unique to the Traditional Chinese version of Windows.<br/> 255 Extended characters normally displayed by Microsoft MS-DOS applications.<br/> For other character set values, consult the Platform SDK documentation.<br/> |



 

</dd> </dl>

## Remarks

The default value for the character set of a character's word balloon is set in the Microsoft Agent Character Editor. In addition, the user can override the character-set settings for all characters in the Microsoft Agent property sheet.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

> [!Note]  
> If you are using a character that you did not compile, check the [**FontName**](fontname-property.md) and **FontCharSet** properties for the character to determine whether they are appropriate for your locale. You may need to set these values before using the [**Speak**](speak-method.md) method to ensure appropriate text display within the word balloon.

 

## See Also

[**FontName property**](fontname-property.md)


 

 





