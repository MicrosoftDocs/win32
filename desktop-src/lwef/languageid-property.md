---
title: LanguageID Property
description: LanguageID Property
ms.assetid: f57b0fa1-b3b8-49c8-b441-2a40e564d6ea
ms.topic: article
ms.date: 05/31/2018
---

# LanguageID Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the language ID for the character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters** **("***CharacterID***").LanguageID** \[ = *LanguageID*\]



Part

Description

LanguageID

A Long integer specifying the language ID for the character. The language ID (LANGID) for a character is a 16-bit value defined by Windows, consisting of a primary language ID and a secondary language ID. The following examples are values for languages supported by Microsoft Agent. To determine the value for other languages, see the *Platform SDK documentation*.

 

Arabic

&H0401

Italian

&H0410

 

Basque

&H042D

Japanese

&H0411

 

Chinese (Simplified)

&H0804

Korean

&H0412

 

Chinese (Traditional)

&H0404

Norwegian

&H0414

 

Croatian

&H041A

Polish

&H0415

 

Czech

&H0405

Portuguese (Portugal)

&H0816

 

Danish

&H0406

Portuguese (Brazil)

&H0416

 

Dutch

&H0413

Romanian

&H0418

 

English (British)

&H0809

Russian

&H0419

 

English (US)

&H0409

Slovakian

&H041B

 

Finnish

&H040B

Slovenian

&H0424

 

French

&H040C

Spanish

&H0C0A

 

German

&H0407

Swedish

&H041D

 

Greek

&H0408

Thai

&H041E

 

Hebrew

&H040D

Turkish

&H041F

 

Hungarian

&H040E

 

 



 

</dd> </dl>

## Remarks

If you do not set the **LanguageID** for the character, its language ID will be the current system language ID if the corresponding Agent language DLL is installed, otherwise, the character's language will be English (US).

This property also determines the language for word balloon text, the commands in the character's pop-up menu, and the speech recognition engine. It also determines the default language for TTS output.

If you try to set the **LanguageID** for a character and the Agent language DLL for that language is not installed or a display font for the language ID is not available, Agent raises an error and **LanguageID** remains at its last setting.

Setting this property does not raise an error if there are no matching speech engines for the language. To determine if there is a compatible speech engine available for the **LanguageID**, check [**SRModeID**](srmodeid-property.md) or [**TTSModeID**](ttsmodeid-property.md). If you do not set **LanguageID**, it will be set to the user default language ID setting.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

> [!Note]  
> If you set **LanguageID** to a language that supports bidirectional text (such as Arabic or Hebrew), but the system running your application does not have bidirectional support installed, text in the word balloon will appear in logical rather than display order.

 

## See Also

[**SRModeID property**](srmodeid-property.md), [**TTSModeID property**](ttsmodeid-property.md)


 

 




