---
title: Pitch Property
description: Pitch Property
ms.assetid: 98b2ada3-93c6-4fa1-bf12-353eb229c30c
ms.topic: article
ms.date: 05/31/2018
---

# Pitch Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description_"></span><span id="description_"></span><span id="DESCRIPTION_"></span>**Description** 
</dt> <dd>

Returns a Long integer for the specified character's speech output (TTS) pitch setting.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Pitch**

</dd> </dl>

## Remarks

This property applies only to characters configured for TTS output. If the character does not support TTS output, this property returns zero (0).

Although your application cannot write this value, you can include **Pit** (pitch) tags in your output text that will temporarily increase the pitch for a particular utterance. However, using the **Pit** tag to change the pitch will not change the **Pitch** property setting. For further information, see [Speech Output Tags](pit-tag.md).

 

 




