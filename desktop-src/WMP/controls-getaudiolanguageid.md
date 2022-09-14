---
title: Controls.getAudioLanguageID method
description: The getAudioLanguageID method retrieves the locale identifier (LCID) for a specified audio language index.
ms.assetid: 8134a7ce-bdc7-46b2-b10e-2bf1215b0de1
keywords:
- getAudioLanguageID method Windows Media Player
- getAudioLanguageID method Windows Media Player , Controls class
- Controls class Windows Media Player , getAudioLanguageID method
topic_type:
- apiref
api_name:
- Controls.getAudioLanguageID
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.getAudioLanguageID method

The **getAudioLanguageID** method retrieves the locale identifier (LCID) for a specified audio language index.

## Syntax


```JScript
retVal = Controls.getAudioLanguageID(
  index
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) specifying the audio language index.

</dd> </dl>

## Return value

This method returns a **Number** (**long**).

## Remarks

An LCID uniquely identifies a particular language dialect, called a locale.

For Windows Media-based content, properties and methods related to language selection only support a single output.

**Windows Media Player 10 Mobile:** This property always returns the language-neutral LCID (0).

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

[**Controls.getAudioLanguageDescription**](controls-getaudiolanguagedescription.md)
</dt> <dt>

[**Controls.getLanguageName**](controls-getlanguagename.md)
</dt> </dl>

 

 





