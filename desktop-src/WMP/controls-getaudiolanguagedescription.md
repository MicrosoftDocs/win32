---
title: Controls.getAudioLanguageDescription method
description: The getAudioLanguageDescription method retrieves the description for the audio language corresponding to the specified one-based index.
ms.assetid: 995a2568-f15f-4b92-9782-92ba5273f444
keywords:
- getAudioLanguageDescription method Windows Media Player
- getAudioLanguageDescription method Windows Media Player , Controls class
- Controls class Windows Media Player , getAudioLanguageDescription method
topic_type:
- apiref
api_name:
- Controls.getAudioLanguageDescription
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Controls.getAudioLanguageDescription method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getAudioLanguageDescription** method retrieves the description for the audio language corresponding to the specified one-based index.

## Syntax


```JScript
strRetVal = Controls.getAudioLanguageDescription(
  index
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) specifying the one-based audio language index.

</dd> </dl>

## Return value

This method returns a **String** value.

## Remarks

For Windows Media-based content, properties and methods related to language selection only support a single output.

Use the **audioLanguageCount** property to get the number of supported audio languages, and then access an audio language individually by using a one-based index.

**Windows Media Player 10 Mobile:** This method is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls Object**](controls-object.md)
</dt> <dt>

[**Controls.audioLanguageCount**](controls-audiolanguagecount.md)
</dt> <dt>

[**Controls.currentAudioLanguage**](controls-currentaudiolanguage.md)
</dt> <dt>

[**Controls.currentAudioLanguageIndex**](controls-currentaudiolanguageindex.md)
</dt> <dt>

[**Controls.getAudioLanguageID**](controls-getaudiolanguageid.md)
</dt> <dt>

[**Controls.getLanguageName**](controls-getlanguagename.md)
</dt> </dl>

 

 





