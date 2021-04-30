---
title: Enabled Property (AudioOutput Object)
description: Enabled Property
ms.assetid: 6526f249-be13-4732-b79e-a9952489461f
ms.topic: article
ms.date: 05/31/2018
---

# Enabled Property (AudioOutput Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns a Boolean indicating whether audio (spoken) output is enabled.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.AudioOutput.Enabled**



| Value     | Description                               |
|-----------|-------------------------------------------|
| **True**  | (Default) Spoken audio output is enabled. |
| **False** | Spoken audio output is disabled.          |



 

</dd> </dl>

## Remarks

This property reflects the Play Audio Output option on the Output page of the Agent property sheet (Advanced Character Options). When the [**Enabled**](enabled-property.md) property returns **True**, the [**Speak**](speak-method.md) method produces audio output if a compatible TTS engine is installed or you use sound files for spoken output. When it returns **False**, it means that speech output is not installed or has been disabled by the user. The property setting applies to all Agent characters and is read-only; only the user can set this property value.

## See Also

[AgentPropertyChange Event](agentpropertychange-event.md)


 

 




