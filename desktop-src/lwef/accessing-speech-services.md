---
title: Accessing Speech Services (Microsoft Agent Server Interface)
description: Accessing Speech Services
ms.assetid: 99cf630d-3bd1-403a-833a-9173a84fe3c0
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Speech Services (Microsoft Agent Server Interface)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Although Microsoft Agent's services include support for speech input, a compatible command-and-control speech recognition engine must be installed to access Agent's speech input services. Similarly, if you want to use Microsoft Agent's speech services to support synthesized speech output for a character, you must install a compatible text-to-speech (TTS) speech engine for your character. Because Microsoft Agent's speech services are based on the Microsoft Speech API (SAPI), you can use any engines that compatibly support the required speech interfaces.

To enable speech input support in your application, define a [**Command**](https://www.bing.com/search?q=**Command**) object and set its [**Voice**](https://www.bing.com/search?q=**Voice**) property. Microsoft Agent will automatically load speech services, so that when the user presses the Listening key or you call [**Listen**](https://www.bing.com/search?q=**Listen**), the speech recognition engine will be loaded. By default the character's language ID will determine which engine is loaded. Agent attempts to load the first engine that SAPI returns as matching this language. Use **IAgentCharacterEx::SetSRModeID** if you want to load a specific engine.

To enable text-to-speech output, use the [**Speak**](https://www.bing.com/search?q=**Speak**) method. Microsoft Agent will automatically attempt to load an engine that matches the character's language ID. If the character's definition includes a specific TTS engine mode ID and that engine is available and matches the character's language ID, Agent loads that engine for the character. If not, Agent loads the first TTS engine that SAPI returns as matching the character's language setting. You can also use **IAgentCharacterEx::SetTTSModeID** to load a specific engine.

Typically, Microsoft Agent loads a speech recognition engine when the Listening mode is initiated and loads a text-to-speech engine when [**Speak**](https://www.bing.com/search?q=**Speak**) is first called. However, if you want to preload the speech engine, you can do this by querying the properties related to the speech interfaces. For example, calling **IAgentCharacterEx::GetSRModeID** or **IAgentCharacterEx::GetTTSModeID** will attempt to load that type of engine.

 

 




