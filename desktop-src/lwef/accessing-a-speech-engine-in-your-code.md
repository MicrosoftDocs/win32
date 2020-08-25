---
title: Accessing a Speech Engine in Your Code
description: Accessing a Speech Engine in Your Code
ms.assetid: ddfe0552-a29e-4ce4-b608-c131efbe300b
ms.topic: article
ms.date: 05/31/2018
---

# Accessing a Speech Engine in Your Code

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

To use a particular speech engine in your code, use the Agent API to set the engine. For speech input engines, use [**SRModeID**](https://www.bing.com/search?q=**SRModeID**), specifying the mode ID for the engine. However, note that the engine must be installed. To determine if the engine is present, you can query **SRModeID**. The engine must match the character's [**LanguageID**](https://www.bing.com/search?q=**LanguageID**) setting. For example, you cannot set **SRModeID** to a German speech recognition engine mode ID for a character whose **LanguageID** is French.

**Speech Input Engine Mode IDs**



| Voice                                    | Mode IDs                             |
|------------------------------------------|--------------------------------------|
| Microsoft Speech Recognition Engine v4.0 | {D8905400-B5C8-11D0-B968020AFDB1B9C} |



 

Check and set the character's [**LanguageID**](https://www.bing.com/search?q=**LanguageID**) and [**SRModeID**](https://www.bing.com/search?q=**SRModeID**) in your code before you attempt to define grammar for the voice parameters of **Command** objects your application. Also consider checking the browser or system language so you can be certain to match your users' configuration. The engine may fail if you attempt to define a grammar for a language that the engine does not match.

A character set for text-to-speech (TTS) output can be compiled with a default speech output engine's mode ID preference. When the character is loaded, if the engine is installed and matches the character's [**LanguageID**](https://www.bing.com/search?q=**LanguageID**), Agent will attempt to load that mode ID for speech output. If the engine is not present or has a different **LanguageID**, Agent will attempt to load the first mode ID it finds that matches the character's **LanguageID**, but still sets the character's compiled speed and pitch setting.

Note that since all Microsoft Agent supplied characters are compiled to use the Lernout & Hauspie TruVoice American English engine as the default speech output engine, the characters' speed and pitch setting are tuned for this language and engine. Therefore when using other TTS engines or engines of other languages the characters may not speak at the optimal pitch or speed. Although your application or webpage cannot write the [**Pitch**](/previous-versions/ms809428(v=msdn.10)) and [**Speed**](https://www.bing.com/search?q=**Speed**) property values, you can include [Pit](pit-tag.md) (pitch) and [Spd](spd-tag.md) (speed) tags in your output text that will temporarily change the pitch and speed for a particular utterance. However, using the Pit and Spd tags will not change the **Pitch** and **Speed** properties. See [Programming the Microsoft Agent Control](programming-the-microsoft-agent-control.md) and the [Microsoft Agent Speech Output Tags](microsoft-agent-speech-output-tags.md) for details.

You also need to install the SAPI 4.0a runtime binaries (SPCHAPI.exe) when using other SAPI-compliant TTS engines than the L&H TruVoice American English engine with the Microsoft Agent supplied characters so that the engines are enumerated properly. From your webpage, include the following Object tag to automatically install the component:

``` syntax
<OBJECT width=0 height=0
CLASSID="CLSID:0C7F3F20-8BAB-11d2-9432-00C04F8EF48F"
CODEBASE="#VERSION=4,0,0,0">
</OBJECT>
```

To query for or set an engine's mode ID, use [**TTSModeID**](https://www.bing.com/search?q=**TTSModeID**). With **TTSModeID** you can set a mode ID that is different from the character's [**LanguageID**](https://www.bing.com/search?q=**LanguageID**). For instance, you can set a German character to speak using a French mode ID. Speech output engine mode IDs not only define which engine you use, but also correspond to specific voices supported for an engine. You can also use the Microsoft Agent Character Editor or the tools included in the [Microsoft Speech SDK documentation](https://msdn.microsoft.com/library/ee705648.aspx) to query for the mode IDs of TTS engines installed on your system.

**Speech Output Mode IDs**



| Voice                                       | Mode IDs                               |
|---------------------------------------------|----------------------------------------|
| Adult Female \#1, US English, L&H TruVoice  | {CA141FD0-AC7F-11D1-97A3-006008273008} |
| Adult Female \#2, US English, L&H TruVoice  | {CA141FD0-AC7F-11D1-97A3-006008273009} |
| Adult Male \#1, US English, L&H TruVoice    | {CA141FD0-AC7F-11D1-97A3-006008273000} |
| Adult Male \#2, US English, L&H TruVoice    | {CA141FD0-AC7F-11D1-97A3-006008273001} |
| Adult Male \#3, US English, L&H TruVoice    | {CA141FD0-AC7F-11D1-97A3-006008273002} |
| Adult Male \#4, US English, L&H TruVoice    | {CA141FD0-AC7F-11D1-97A3-006008273003} |
| Adult Male \#5, US English, L&H TruVoice    | {CA141FD0-AC7F-11D1-97A3-006008273004} |
| Adult Male \#6, US English, L&H TruVoice    | {CA141FD0-AC7F-11D1-97A3-006008273005} |
| Adult Male \#7, US English, L&H TruVoice    | {CA141FD0-AC7F-11D1-97A3-006008273006} |
| Adult Male \#8, US English, L&H TruVoice    | {CA141FD0-AC7F-11D1-97A3-006008273007} |
| Carol, British English, L&H TTS3000         | {227A0E40-A92A-11d1-B17B-0020AFED142E} |
| Peter, British English, L&H TTS3000         | {227A0E41-A92A-11d1-B17B-0020AFED142E} |
| Linda, Dutch, L&H TTS3000                   | {A0DDCA40-A92C-11d1-B17B-0020AFED142E} |
| Alexander, Dutch, L&H TTS3000               | {A0DDCA41-A92C-11d1-B17B-0020AFED142E} |
| Véronique, French, L&H TTS3000              | {0879A4E0-A92C-11d1-B17B-0020AFED142E} |
| Pierre, French, L&H TTS3000                 | {0879A4E1-A92C-11d1-B17B-0020AFED142E} |
| Anna, German, L&H TTS3000                   | {3A1FB760-A92B-11d1-B17B-0020AFED142E} |
| Stefan, German, L&H TTS3000                 | {3A1FB761-A92B-11d1-B17B-0020AFED142E} |
| Barbara, Italian, L&H TTS3000               | {7EF71700-A92D-11d1-B17B-0020AFED142E} |
| Stefano, Italian, L&H TTS3000               | {7EF71701-A92D-11d1-B17B-0020AFED142E} |
| Naoko, Japanese, L&H TTS3000                | {A778E060-A936-11d1-B17B-0020AFED142E} |
| Kenji, Japanese, L&H TTS3000                | {A778E061-A936-11d1-B17B-0020AFED142E} |
| Shin-Ah, Korean, L&H TTS3000                | {12E0B720-A936-11d1-B17B-0020AFED142E} |
| Jun-Ho, Korean, L&H TTS3000                 | {12E0B721-A936-11d1-B17B-0020AFED142E} |
| Juliana, Portuguese (Brazil), L&H TTS3000   | {8AA08CA0-A1AE-11d3-9BC5-00A0C967A2D1} |
| Alexandre, Portuguese (Brazil), L&H TTS3000 | {8AA08CA1-A1AE-11d3-9BC5-00A0C967A2D1} |
| Svetlana, Russian, L&H TTS3000              | {06377F80-D48E-11d1-B17B-0020AFED142E} |
| Boris, Russian, L&H TTS3000                 | {06377F81-D48E-11d1-B17B-0020AFED142E} |
| Carmen, Spanish, L&H TTS3000                | {2CE326E0-A935-11d1-B17B-0020AFED142E} |
| Julio, Spanish, L&H TTS3000                 | {2CE326E1-A935-11d1-B17B-0020AFED142E} |



 

> [!Note]  
> There is a difference between a speech engine's installation CLSID and its mode ID. Similarly, a speech engine also has an engine ID, but this ID is not applicable in the Agent API.

 

 

 