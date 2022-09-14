---
title: Accessing Speech Services (Microsoft Agent Control)
description: Learn about accessing speech services with Microsoft Agent Control. Microsoft Agent is deprecated as of Windows 7.
ms.assetid: c6c10f2a-a433-4a8e-a069-48e3c2032fb8
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Speech Services (Microsoft Agent Control)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Although Microsoft Agent's services include support for speech input, a compatible command-and-control speech recognition engine must be installed to access Agent's speech input services. Similarly, if you want to use Microsoft Agent's speech services to support synthesized speech output for a character, you must install a compatible text-to-speech (TTS) speech engine for your character.

To enable speech input support in your application, define a [**Command**](https://www.bing.com/search?q=**Command**) object and set its [**Voice**](https://www.bing.com/search?q=**Voice**) property. Agent will automatically load speech services, so that when the user presses the Listening key or you call [**Listen**](https://www.bing.com/search?q=**Listen**), the speech recognition engine will be loaded. By default the character's [**LanguageID**](https://www.bing.com/search?q=**LanguageID**) will determine which engine is loaded. Agent attempts to load the first engine that the Microsoft Speech API (SAPI) returns as matching this language. Use [**SRModeID**](https://www.bing.com/search?q=**SRModeID**) if you want to load a specific engine.

To enable text-to-speech output, use the [**Speak**](https://www.bing.com/search?q=**Speak**) method. Agent will automatically attempt to load an engine that matches the character's [**LanguageID**](https://www.bing.com/search?q=**LanguageID**). If the character's definition includes a specific TTS engine mode ID and that engine is available and matches the character's **LanguageID**, Agent loads that engine for the character. If it is not, it loads the first TTS engine that SAPI returns as matching the character's language setting. You can also use the [**TTSModeID**](https://www.bing.com/search?q=**TTSModeID**) to load a specific engine.

Typically, Agent loads speech recognition when the Listening mode is initiated and a text-to-speech engine when [**Speak**](https://www.bing.com/search?q=**Speak**) is first called. However, if you want to preload the speech engine, you query the properties related to the speech interfaces. For example, querying [**SRModeID**](https://www.bing.com/search?q=**SRModeID**) or [**TTSModeID**](https://www.bing.com/search?q=**TTSModeID**) will attempt to load that type of engine.

Because Microsoft Agent's speech services are based on the Microsoft Speech API, you can use any engines that support the required speech interfaces.

 

 




