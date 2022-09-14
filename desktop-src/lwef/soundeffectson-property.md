---
title: SoundEffectsOn Property
description: SoundEffectsOn Property
ms.assetid: 478c4748-5ca1-4237-958a-17f0a476c32c
ms.topic: article
ms.date: 05/31/2018
---

# SoundEffectsOn Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets whether sound effects are enabled for your character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent*.**Characters("***CharacterID***").SoundEffectsOn** \[ = *boolean*\]



| Part      | Description                                                                                                                                                        |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *boolean* | A Boolean expression specifying whether sound effects are enabled. **True** Sound effects are enabled.<br/> **False** Sound effects are disabled.<br/> |



 

</dd> </dl>

## Remarks

This property determines whether sound effects included as a part of a character's animations will play when an animation plays. This property's setting applies to all clients of the character.

## See Also

[**SoundEffects property**](soundeffects-property.md)


 

 





