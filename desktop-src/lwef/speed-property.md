---
title: Speed Property
description: Speed Property
ms.assetid: 43d0480b-d3a5-4992-a2a5-80eba37221e4
ms.topic: article
ms.date: 05/31/2018
---

# Speed Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns a Long integer that specifies the current speed of the character's speech output.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Speed**

</dd> </dl>

## Remarks

This property returns the current speaking output speed setting for the character. For characters using TTS output, the property returns the actual TTS output setting for the character. If TTS is not enabled or the character does not support TTS output, the setting reflects the user setting for output speed.

Although your application cannot write this value, you can include **Spd** (speed) tags in your output text that will temporarily speed up the output for a particular utterance. However, using the **Spd** tag to change the character's spoken output does not affect the **Speed** property setting. For further information, see [Speech Output Tags](microsoft-agent-speech-output-tags.md).

 

 




