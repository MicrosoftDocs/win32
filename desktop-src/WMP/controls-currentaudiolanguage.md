---
title: Controls.currentAudioLanguage
description: The currentAudioLanguage property specifies or retrieves the locale identifier (LCID) of the audio language for playback.
ms.assetid: 628845df-add3-4068-9c3d-b4a9b818808c
keywords:
- Controls.currentAudioLanguage Windows Media Player
topic_type:
- apiref
api_name:
- Controls.currentAudioLanguage
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.currentAudioLanguage

The **currentAudioLanguage** property specifies or retrieves the locale identifier (LCID) of the audio language for playback.

``` syntax
player.controls.currentAudioLanguage
      
```

## Possible Values

This property is a read/write **Number** (**long**).

## Remarks

An LCID uniquely identifies a particular language dialect, called a locale.

For Windows Media-based content, properties and methods related to language selection only support a single output.

When working with DVD content, specifying an LCID will cause the first available audio track having the specified language ID to be selected.

**Windows Media Player 10 Mobile:** This property only accepts or returns the language-neutral LCID (0).

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

[**Controls.currentAudioLanguageIndex**](controls-currentaudiolanguageindex.md)
</dt> <dt>

[**Controls.getAudioLanguageDescription**](controls-getaudiolanguagedescription.md)
</dt> <dt>

[**Controls.getAudioLanguageID**](controls-getaudiolanguageid.md)
</dt> <dt>

[**Controls.getLanguageName**](controls-getlanguagename.md)
</dt> </dl>

 

 





