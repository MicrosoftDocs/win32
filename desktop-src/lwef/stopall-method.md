---
title: StopAll Method
description: StopAll Method
ms.assetid: 2ce32ff8-4908-45b1-9b83-4d558f67417c
ms.topic: article
ms.date: 05/31/2018
---

# StopAll Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Stops all animation requests or specified types of requests for the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").StopAll** \[*Type*\]



| Part   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Type* | Optional. To use this parameter you can use any of the following values. You can also specify multiple types by separating them with commas. <br/> "**Get**" <br/> To stop all queued [**Get**](get-method.md) requests.<br/> "**NonQueuedGet**" <br/> To stop all non-queued [**Get**](get-method.md) requests (**Get** method with **Queue** parameter set to **False**).<br/> "**Move**" <br/> To stop all queued [**MoveTo**](moveto-method.md) requests.<br/> "**Play**" <br/> To stop all queued [**Play**](play-method.md) requests.<br/> "**Speak**" <br/> To stop all queued [**Speak**](speak-method.md) requests.<br/> |



 

</dd> </dl>

## Remarks

If you don't set the **Type** parameter, the server stops all animations for the character, including queued and non-queued [**Get**](get-method.md) requests, and clears its animation queue. It also stops playing a character's Hiding or Showing animation.

This method will not generate a [**Request**](/windows/desktop/lwef/the-request-object) object.

## See Also

[**Stop method**](stop-method.md)


 

