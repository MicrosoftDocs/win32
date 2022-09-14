---
title: IAgentCharacter Speak
description: IAgentCharacter Speak
ms.assetid: 3c4baf83-9e69-4048-bdaf-4ead8ea8e7cd
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::Speak

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Speak(
   BSTR bszText,    // text to speak
   BSTR bszURL,     // URL of a file to speak
   long * pdwReqID  // address of a request ID
);
```

Speaks the text or sound file.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszText"></span><span id="bsztext"></span><span id="BSZTEXT"></span>*bszText*
</dt> <dd>

The text the character is to speak.

</dd> <dt>

<span id="bszURL"></span><span id="bszurl"></span><span id="BSZURL"></span>*bszURL*
</dt> <dd>

The URL (or file specification) of a sound file to use for spoken output. This can be a standard sound file (.WAV) or linguistically enhanced sound file (.LWV).

</dd> <dt>

<span id="pdwReqID"></span><span id="pdwreqid"></span><span id="PDWREQID"></span>*pdwReqID*
</dt> <dd>

Address of a variable that receives the [**Speak**](/windows/desktop/lwef/iagentcharacter--speak) request ID.

</dd> </dl>

To use this method with a character configured to speak using a text-to-speech (TTS) engine; simply provide the *bszText* parameter. You can include vertical bar characters (\|) in the *bszText* parameter to designate alternative strings, so that each time the server processes the method, it randomly choose a different string. Support of TTS output is defined when the character is compiled using the Microsoft Agent Character Editor.

If you want to use sound file output for the character, specify the location for the file in the *bszURL* parameter. When using the HTTP protocol to download a sound file, use the [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare) method to ensure the availability of the file before using this method. You can use the *bszText* parameter to specify the words that appear in the character's word balloon. If you specify a linguistically enhanced sound file (.LWV) for the *bszURL* parameter and do not specify text, the *bszText* parameter uses the text stored in the file.

The [**Speak**](/windows/desktop/lwef/iagentcharacter--speak) method uses the last animation played to determine which speaking animation to play. For example, if you precede the **Speak** command with an [**IAgentCharacter::Play**](iagentcharacter--play.md) "**GestureRight**", the server will play **GestureRight** and then the **GestureRight** speaking animation. If the last animation played has no speaking animation, then Microsoft Agent plays the animation assigned to the character's **Speaking** state.

If you call [**Speak**](/windows/desktop/lwef/iagentcharacter--speak) and the audio channel is busy, the character's audio output will not be heard, but the text will display in the word balloon. The word balloon's [Enabled](enabled-property.md) property must also be **True** for the text to display.

Microsoft Agent's automatic word breaking in the word balloon, breaks words using white-space characters (for example, space and tab). However, it may break a word to fit the balloon as well. In languages like Japanese, Chinese, and Thai, where spaces are not used to break words, insert a Unicode zero width space character (0x200B) between characters to define logical word breaks.

> [!Note]  
> Set the character's language ID (using [**IAgentCharacterEx::SetLanguageID**](iagentcharacterex--setlanguageid.md) before using the [**Speak**](/windows/desktop/lwef/iagentcharacter--speak) method to ensure appropriate text display within the word balloon.

 

## See Also

[**IAgentCharacter::Play**](iagentcharacter--play.md), [**IAgentBalloon::GetEnabled**](iagentballoon--getenabled.md), [**IAgentCharacter::Prepare**](iagentcharacter--prepare.md)


 

 