---
title: Speak Method
description: Speak Method
ms.assetid: 6267e04c-feb5-4f48-8a88-4e6ca3388bf3
ms.topic: article
ms.date: 05/31/2018
---

# Speak Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Speaks the specified text or sound file for the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Speak** \[*Text*\], \[*Url*\]



| Part   | Description                                                                                                                                                                                                                                                  |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Text* | Optional. A string that specifies what the character says.                                                                                                                                                                                                   |
| *Url*  | Optional. A string expression specifying the location of an audio file (.WAV or .LWV format). The location can be specified as a file (including a UNC path specification) or URL (when character animation data is also being retrieved via HTTP protocol). |



 

</dd> </dl>

## Remarks

Although the *Text* and *Url* parameters are optional, one of them must be supplied. To use this method with a character configured to speak only in its word balloon or using a text-to-speech (TTS) engine, simply provide the *Text* parameter. Include a space between words to define appropriate word breaks in the word balloon, even for languages that do not traditionally include spaces.

You can also include vertical bar characters (\|) in the *Text* parameter to designate alternative strings, so that the server randomly chooses a different string each time it processes the method.

Character support of TTS output is defined when the character is compiled using the Microsoft Agent Character Editor. To generate TTS output, a compatible TTS engine must already be installed before calling this method. For further information, see [Accessing Speech Services](accessing-speech-services.md).

If you use recorded sound-file (.WAV or .LWV format only) output for the character, specify the file's location in the *Url* parameter. This file specification can include a local (absolute or relative) or universal naming convention (UNC) path. The filename cannot include any characters not included in the US code page 1252. However, if you are using the HTTP protocol to access the character animation data, use the [**Get**](get-method.md) method to load the animation before calling the **Speak** method. See [Using the Microsoft Linguistic Information Sound Editing Tool](using-the-microsoft-linguistic-information-sound-editing-tool.md) for information about creative .LWV files.

When using recorded sound-file output, you can still use the *Text* parameter to specify the words that appear in the character's word balloon. However, if you specify a linguistically enhanced sound file (.LWV) for the *Url* parameter and do not specify text for the word balloon, the *Text* parameter uses the text stored in the file.

You can also vary parameters of the speech output with special tags that you include in the *Text* parameter. For more information, see [Microsoft Agent Speech Output Tags](microsoft-agent-speech-output-tags.md).

If you declare an object reference and set it to this method, it returns a [**Request**](/windows/desktop/lwef/the-request-object) object. You can use this to synchronize other parts of your code with the character's spoken output, as in the following example:


```
   Dim SpeakRequest as Object
...
   Set SpeakRequest = Genie.Speak ("And here it is.")
...
   Sub Agent1_RequestComplete (ByVal Request as Object)
   ' Make certain the request exists
   If SpeakRequest Not Nothing Then
      ' See if it was this request
      If Request = SpeakRequest Then
         ' Display the message box 
         Msgbox "Ta da!"
      End If
   End If
   End Sub
```



You can also use a [**Request**](/windows/desktop/lwef/the-request-object) object to check for certain error conditions. For example, if you use the **Speak** method to speak and do not have a compatible TTS engine installed, the server sets the **Request** object's [**Status**](status-property.md) property to "failed" with its [**Description**](description-property.md) property to "Class not registered" or "Unknown or object returned error". To determine if you have a TTS engine installed, use the [**TTSModeID**](ttsmodeid-property.md) property.

Similarly, if you have the character attempt to speak a sound file, and if the file has not been loaded or there is a problem with the audio device, the server also sets the [**Request**](/windows/desktop/lwef/the-request-object) object's [**Status**](status-property.md) property to "failed" with an appropriate error code number.

You can also include bookmark speech tags in your Speak text to synchronize your code:


```
   Dim SpeakRequest as Object
...
   Set SpeakRequest = Genie.Speak ("And here \mrk=100\it is.")
...
   Sub Agent1_Bookmark (ByVal BookmarkID As Long)
   If BookmarkID = 100 Then
      ' Display the message box 
         Msgbox "Tada!"
      End If
   End Sub
```



For more information on the bookmark speech tag, see [Speech Output Tags](mrk-tag.md).

The **Speak** method uses the last action played to determine which speaking animation to play. For example, if you preceded the **Speak** command with a [**Play**](play-method.md) "**GestureRight**", the server will play **GestureRight** and then the **GestureRight** speaking animation. If the last animation played has no speaking animation, Agent plays the animation assigned to the character's **Speaking** state.

If you call **Speak** and the audio channel is busy, the character's audio output will not be heard, but the text will display in the word balloon.

Agent's automatic word breaking in the word balloon breaks words using white-space characters (for example, Space or Tab). However, if it cannot, it may break a word to fit the balloon. In languages like Japanese, Chinese, and Thai, where spaces are not used to break words, insert a Unicode zero-width space character (0x200B) between characters to define logical word breaks.

> [!Note]  
> The word balloon's [**Enabled**](enabled-property.md) property must also be **True** for text to display.

 

> [!Note]  
> Set the character's language ID (by setting the character's **LanguageID** before using the **Speak** method to ensure appropriate text display within the word balloon.

 

## See Also

[**Bookmark event**](bookmark-event.md), [**RequestStart event**](requeststart-event.md), [**RequestComplete event**](requestcomplete-event.md)


 

 