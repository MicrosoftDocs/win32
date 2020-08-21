---
title: Listen Method
description: Listen Method
ms.assetid: ceb3b62f-2a33-4a13-b608-4cfa800be38a
ms.topic: article
ms.date: 05/31/2018
---

# Listen Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Turns on Listening mode (speech recognition) for a timed period.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters****("***CharacterID***").Listen** *State*



| Part    | Description                                                                                                                                                                      |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *State* | Required. A Boolean value that determines whether to turn Listening mode on or off. **True** Turns Listening mode on. <br/> **False** Turns Listening mode off.<br/> |



 

</dd> </dl>

## Remarks

Setting this method to **True** enables Listening mode (turns on speech recognition) for a fixed period of time (10 seconds). While you cannot set the value of the time-out, you can turn off Listening mode before the time-out expires. If you (or another client) successfully set Listening mode on and you attempt to set this property to **True** before the time-out expires, the method succeeds and resets the time-out. However, if the Listening mode is on because the user is pressing the Listening key, the method succeeds, but the time-out is ignored and the Listening mode ends based on the user's interaction with the Listening key.

This method succeeds only when called by the input-active client and if speech services have been started. To ensure that speech services have been started, query or set the [**SRModeID**](srmodeid-property.md) or set the [**Voice**](voice-property.md) setting for a [**Command**](/windows/desktop/lwef/the-command-object) before you call **Listen** otherwise the method will fail. To detect the success of this method, call it as a function and it will return a Boolean value indicating whether the method succeeded.


```
   If Genie.Listen(True) Then
      'The method succeeded

   Else
      ' The method failed

   End If
```



The method also fails if the user is pressing the Listening key and you attempt to set **Listen** to **False**. However, if the user has released the Listening key and Listening mode has not timed out, it will succeed.

**Listen** also fails if there is no compatible speech engine available that matches the character's [**LanguageID**](languageid-property.md) setting, the user has disabled speech input using the Microsoft Agent property sheet, or the audio device is busy.

When you successfully set this method to **True**, the server triggers the [**ListenStart**](listenstart-event.md) event. The server sends [**ListenComplete**](listencomplete-event.md) when the Listening mode time-out completes or when you set **Listen** to **False**.

This method does not automatically call [**Stop**](stop-method.md) and play a Listening state animation as the server does when the Listening key is pressed. This enables you to determine whether to interrupt the current animation using the [**ListenStart**](listenstart-event.md) animation by calling **Stop** and playing your own appropriate animation. However, the server does call **Stop** and plays a Hearing state animation when a user utterance is detected.

## See Also

[**LanguageID property**](languageid-property.md), [**ListenComplete event**](listencomplete-event.md), [**ListenStart event**](listenstart-event.md)


 

