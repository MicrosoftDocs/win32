---
title: Controls.audioLanguageCount
description: The audioLanguageCount property retrieves the count of supported audio languages.
ms.assetid: a6dda8bf-db8c-4e97-9277-5a23dfa93156
keywords:
- Controls.audioLanguageCount Windows Media Player
topic_type:
- apiref
api_name:
- Controls.audioLanguageCount
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.audioLanguageCount

The **audioLanguageCount** property retrieves the count of supported audio languages.

``` syntax
player.controls.audioLanguageCount
      
```

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

For Windows Media-based content, properties and methods related to language selection only support a single output.

**Windows Media Player 10 Mobile:** This property always returns 1.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls Object**](controls-object.md)
</dt> <dt>

[**Controls.currentAudioLanguage**](controls-currentaudiolanguage.md)
</dt> <dt>

[**Controls.currentAudioLanguageIndex**](controls-currentaudiolanguageindex.md)
</dt> <dt>

[**Controls.getAudioLanguageDescription**](controls-getaudiolanguagedescription.md)
</dt> <dt>

[**Controls.getAudioLanguageID**](controls-getaudiolanguageid.md)
</dt> <dt>

[**Controls.getLanguageName**](controls-getlanguagename.md)
</dt> </dl>

 

 





