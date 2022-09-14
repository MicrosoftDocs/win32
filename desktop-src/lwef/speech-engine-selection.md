---
title: Speech Engine Selection
description: Speech Engine Selection
ms.assetid: f5afedc6-093f-4247-a5c8-277d6b2d646c
ms.topic: article
ms.date: 05/31/2018
---

# Speech Engine Selection

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

A character's language ID setting determines its default speech input language; Microsoft Agent requests SAPI for an installed engine that matches that language. If a client application does not specify a language preference, Microsoft Agent will attempt to find a speech recognition engine that matches the user default language ID (using the major language ID, then the minor language ID). If no engine is available matching this language, speech is disabled for that character.

You can also request a specific speech recognition engine by specifying its mode ID (using the character [**SRModeID**](srmodeid-property.md) property). However, if the language ID for that mode ID does not match the client's language setting, the call will fail (raise an error in the control). The speech recognition engine will then remain the last successfully set engine by the client, or if none, the engine that matches the current system language ID. If there is still no match, speech input is not available for that client.

Microsoft Agent automatically loads a speech recognition engine when speech input is initiated by a user pressing the Listening hotkey or the input-active client calls the [**Listen**](listen-method.md) method. However, an engine may also be loaded when setting or querying its mode ID, setting or querying the properties of the Voice Commands Window, querying [**SRStatus**](srstatus-property.md), or when speech is enabled and the user displays the Speech Input page of the Advanced Character Options. However, Microsoft Agent only keeps loaded the speech engines that clients are using.

 

 




