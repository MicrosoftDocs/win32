---
title: Controls.currentAudioLanguageIndex
description: The currentAudioLanguageIndex property specifies or retrieves the one-based index that corresponds to the audio language for playback.
ms.assetid: 9a1ae887-4e64-4758-a8a2-bf2e10a7a5c7
keywords:
- Controls.currentAudioLanguageIndex Windows Media Player
topic_type:
- apiref
api_name:
- Controls.currentAudioLanguageIndex
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.currentAudioLanguageIndex

The **currentAudioLanguageIndex** property specifies or retrieves the one-based index that corresponds to the audio language for playback.

``` syntax
player.controls.currentAudioLanguageIndex
      
```

## Possible Values

This property is a read/write **Number** (**long**).

## Remarks

For Windows Media-based content, properties and methods related to language selection only support a single output.

Use the **audioLanguageCount** property to get the number of supported audio languages.

**Windows Media Player 10 Mobile:** This property only accepts or returns 0.

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

[**Controls.getAudioLanguageDescription**](controls-getaudiolanguagedescription.md)
</dt> <dt>

[**Controls.getAudioLanguageID**](controls-getaudiolanguageid.md)
</dt> <dt>

[**Controls.getLanguageName**](controls-getlanguagename.md)
</dt> </dl>

 

 





