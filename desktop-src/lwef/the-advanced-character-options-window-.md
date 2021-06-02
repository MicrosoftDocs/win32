---
title: Advanced Character Options Window (Voice Commands Window)
description: The Advanced Character Options Window
ms.assetid: c2f784e9-d1c5-4fa3-b3f7-5061c9b7e6d9
ms.topic: article
ms.date: 05/31/2018
---

# Advanced Character Options Window (Voice Commands Window)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The Advanced Character Options window provides options for users to adjust their interaction with all characters. For example, users can disable speech input or change input parameters. Users can also change the output settings for the word balloon. These settings override any set by a client application or set as part of the character definition. Your application cannot change or disable these options, because they apply to the general user preferences for operation of all characters. However, the server will notify your application ([**DefaultCharacterChange**](defaultcharacterchange-event.md)) when the user changes and applies an option. You can also display or close the window using the window's [**Visible**](visible-property.md) property and access its location through its [**Top**](top-property.md) and [**Left**](left-property.md) properties.

In addition to supporting the animation of a character, Microsoft Agent supports audio output for the character. This includes spoken output and sound effects. For spoken output, the server automatically lip-syncs the character's defined mouth images to the output. You can choose text-to-speech (TTS) synthesis, recorded audio, or only word balloon text output.

 

 




