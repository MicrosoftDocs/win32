---
title: SoundEffects Property
description: SoundEffects Property
ms.assetid: 39e48e5f-b24e-48ce-b5a3-85467ac252e9
ms.topic: article
ms.date: 05/31/2018
---

# SoundEffects Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns a Boolean indicating whether sound effects (.WAV) files configured as part of a character's actions will play.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.AudioOutput.SoundEffects**



| Value     | Description                          |
|-----------|--------------------------------------|
| **True**  | Character sound effects are enabled. |
| **False** | Character sound effect are disabled. |



 

</dd> </dl>

## Remarks

This property reflects the Play Character Sound Effects option on the Output page of the Agent property sheet (Advanced Character Options). When the **SoundEffects** property returns **True**, sound effects included in a character's definition will be played. When **False**, the sound effects will not be played. The property setting affects all characters and is read-only; only the user can set this property value.

## See Also

[**AgentPropertyChange event**](agentpropertychange-event.md)


 

 




