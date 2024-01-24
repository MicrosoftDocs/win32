---
title: Microsoft Agent Speech Output Tags
description: Microsoft Agent Speech Output Tags
ms.assetid: b7939974-bc54-4dd8-8e79-3ebd24e76215
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Agent Speech Output Tags

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The Microsoft Agent services support modifying speech output through special tags inserted in the speech text string. These tags help you change the characteristics of the output expression of the character.

Speech output tags use the following rules of syntax:

-   All tags begin and end with a backslash character (\\).
-   The single backslash character is not enabled within a tag. To include a backslash character in a text parameter of a tag, use a double backslash (\\\\).
-   Tags are case-insensitive. For example, \\pit\\ is the same as \\PIT\\.
-   Tags are whitespace-dependent. For example, \\Rst\\ is not the same as \\ Rst \\.

Unless otherwise specified or modified by another tag, the speech output retains the characteristic set by the tag within the text specified in a single [**Speak**](speak-method.md) method. Speech output is automatically reset through the user-defined parameters after a **Speak** method is completed.

Some tags include quoted strings. For some programming languages, such as Visual Basic Scripting Edition (VBScript) and Visual Basic, this means that you may have to use two quote marks to designate the tag's parameter or concatenate a double-quote character as part of the string. The latter is shown in this Visual Basic example:


```
Agent1.Characters("Genie").Speak "This is \map=" + chr(34) + "Spoken text" _
+ chr(34) + "=" + chr(34) + "Balloon text" + chr(34) + "\."
```



For C, C++, and Java™ programming, precede backslashes and double quotes with a backslash. For example:


```
BSTR bszSpeak = SysAllocString(L"This is \\map=\"Spoken text\"=\"Balloon text\"\\");

pCharacter->Speak(bszSpeak, ......);
```



For foreign languages that support double-byte character set (DBCS) characters, you can use double-byte characters to specify string parameters. However, use single-byte characters for all other parameters and characters that are used to define the tag, including the tag itself.

The following tags are supported:

-   [**Chr**](chr-tag.md)
-   [**Ctx**](ctx-tag.md)
-   [**Emp**](emp-tag.md)
-   [**Lst**](lst-tag.md)
-   [**Map**](map-tag.md)
-   [**Mrk**](mrk-tag.md)
-   [**Pau**](pau-tag.md)
-   [**Pit**](pit-tag.md)
-   [**Rst**](rst-tag.md)
-   [**Spd**](spd-tag.md)
-   [**Vol**](vol-tag.md)

The tags are primarily designed for adjusting text-to-speech (TTS)-generated output. Only the [**Mrk**](mrk-tag.md) and [**Map**](map-tag.md) tags can be used with sound file-based spoken output.

> [!Note]  
> Microsoft Agent does not support all the tags documented in the Microsoft Speech SDK. Parameters may also vary depending on the TTS engine selected. You can set a specific TTS engine using [**TTSModeID**](ttsmodeid-property.md).

 

 

 




