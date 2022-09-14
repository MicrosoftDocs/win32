---
title: IdleOn Property
description: IdleOn Property
ms.assetid: ba436dec-c7b4-42e8-99d6-c6ff93afd73c
ms.topic: article
ms.date: 05/31/2018
---

# IdleOn Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets a Boolean value that determines whether the server manages the specified character's **Idling** state animations.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").IdleOn** \[ = *boolean*\]

</dd> </dl> 

| Part      | Description                                                                                                                                                                                                             |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *boolean* | A Boolean expression specifying whether the server manages idle mode. **True** (Default) Server handling of the idle state is enabled. <br/> **False** Server handling of the idle state is disabled. <br/> |



 

## Remarks

The server automatically sets a time-out after the last animation played for a character. When this timer's interval is complete, the server begins the **Idling** state for a character, playing its associated **Idling** animations at regular intervals. If you want to disable the server from automatically playing the **Idling** state animations, set the property to **False** and play an animation or call the [**Stop**](stop-method.md) method. Setting this value does not affect the current animation state of the character.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

 

 





