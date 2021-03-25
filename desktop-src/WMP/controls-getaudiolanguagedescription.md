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
ms.date: 05/31/2018
---

# Controls.getAudioLanguageDescription method

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

 

 





