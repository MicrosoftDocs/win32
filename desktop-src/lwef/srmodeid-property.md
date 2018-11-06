---
title: SRModeID Property
description: SRModeID Property
ms.assetid: 4c784fc5-d2c2-4e5b-ba5f-f59b4507f40f
ms.topic: article
ms.date: 05/31/2018
---

# SRModeID Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the speech recognition engine the character uses.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters("***CharacterID***").SRModeID** \[ = *ModeID*\]



| Part     | Description                                                             |
|----------|-------------------------------------------------------------------------|
| *ModeID* | A string expression that corresponds to the mode ID of a speech engine. |



 

</dd> </dl>

## Remarks

The property determines the speech recognition engine used by the character for speech input. The mode ID for a speech recognition engine is a formatted string defined by the speech vendor that uniquely identifies the engine. For more information, see [Accessing a Speech Engine In Your Code](accessing-a-speech-engine-in-your-code.md).

If you specify a mode ID for a speech engine that isn't installed, if the user has disabled speech recognition (in the Microsoft Agent property sheet), or if the language of the specified speech engine doesn't match the character's [**LanguageID**](languageid-property.md) setting, the server raises an error.

If you query this property and haven't already (successfully) set the speech recognition engine, the server returns the mode ID of the engine that SAPI returns based on the character's [**LanguageID**](languageid-property.md) setting. If you haven't set the character's **LanguageID**, then Agent returns the mode ID of the engine that SAPI returns based on the user's default language ID setting. If there is no matching engine, the server returns an empty string (""). Querying this property does not require that [**SpeechInput.Enabled**](https://www.bing.com/search?q=**SpeechInput.Enabled**) be set to **True**. However, if you query the property when speech input is disabled, the server returns an empty string.

When speech input is enabled (in the Advanced Character Options window), querying or setting this property will load the associated engine (if it is not already loaded), and start speech services. That is, the Listening key is available, and the Listening Tip is displayable. (The Listening key and Listening Tip are enabled only if they are also enabled in Advanced Character Options.) However, if you query the property when speech is disabled, the server does not start speech services.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

Microsoft Agent's speech engine requirements are based on the Microsoft Speech API. Engines supporting Microsoft Agent's SAPI requirements can be installed and used with Agent.

> [!Note]  
> This property also returns the empty string if you have no compatible sound support installed on your system.

 

> [!Note]  
> Querying this property does not typically return an error. However, if the speech engine takes an abnormally long time to load, you may get an error indicating that the query timed out.

 

## See Also

[**LanguageID property**](languageid-property.md)


 

 




