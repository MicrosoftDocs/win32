---
title: TTSModeID Property
description: TTSModeID Property
ms.assetid: 9205c37e-e006-466a-9b33-b98408c01ed7
ms.topic: article
ms.date: 05/31/2018
---

# TTSModeID Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the TTS engine mode used for the character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").TTSModeID** \[ = *ModeID*\]



| Part     | Description                                                             |
|----------|-------------------------------------------------------------------------|
| *ModeID* | A string expression that corresponds to the mode ID of a speech engine. |



 

</dd> </dl>

## Remarks

This property determines the TTS (text-to-speech) engine mode ID for a character's spoken output. The mode ID for a TTS engine is a formatted string defined by the speech vendor that uniquely identifies the engine's mode. For more information, see [Accessing a Speech Engine in Your Code](accessing-a-speech-engine-in-your-code.md).

Setting this property overrides the server's attempt to load an engine based on the character's compiled TTS setting and the character's current [**LanguageID**](languageid-property.md) setting. However, if you specify a mode ID for an engine that isn't installed or if the user has disabled speech output in the Microsoft Agent property sheet (**AudioOutput.Enabled = False**), the server raises an error.

If you do not (or have not successfully) set a TTS mode ID for the character, the server checks to see if the character's compiled TTS mode setting matches the character's [**LanguageID**](languageid-property.md) setting, and that the associated TTS engine is installed. If so, the TTS mode used by the character for spoken output and this property returns that mode ID. If not, the server requests a compatible SAPI speech engine that matches the **LanguageID** of the character, as well as the gender and age set for the character's compiled mode ID. If you have not set the character's **LanguageID**, its **LanguageID** is the current user language. If no matching engine can be found, querying for this property returns an empty string for the engine's mode ID. Similarly, if you query this property when the user has disabled speech output in the Microsoft Agent property sheet (**AudioOutput.Enabled = False**), the value will be an empty string.

Querying or setting this property will load the associated engine (if it is not already loaded). However, if the engine specified in the character's compiled TTS setting is installed and matches the character's language ID setting, the engine will be loaded when the character loads.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

Microsoft Agent's speech engine requirements are based on the Microsoft Speech API. Engines supporting Microsoft Agent's SAPI requirements can be installed and used with Agent.

> [!Note]  
> This property also returns the empty string if you have no compatible sound support installed on your system.

 

> [!Note]  
> Setting the **TTSModeID** can fail if Speech.dll is not installed and the engine you specify does not match the character's compiled TTS mode setting.

 

> [!Note]  
> Querying this property does not typically return an error. However, if the speech engine takes an abnormally long time to load, you may get an error indicating that the query timed out.

 

## See Also

[**LanguageID property**](languageid-property.md)


 

 




