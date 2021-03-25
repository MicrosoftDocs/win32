---
title: Controls.getLanguageName method
description: The getLanguageName method retrieves the name of the audio language with the specified locale identifier (LCID).
ms.assetid: 9e142c89-92bf-476f-bae7-b94f5b5ebe01
keywords:
- getLanguageName method Windows Media Player
- getLanguageName method Windows Media Player , Controls class
- Controls class Windows Media Player , getLanguageName method
topic_type:
- apiref
api_name:
- Controls.getLanguageName
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Controls.getLanguageName method

The **getLanguageName** method retrieves the name of the audio language with the specified locale identifier (LCID).

## Syntax


```JScript
strRetVal = Controls.getLanguageName(
  LCID
)
```



## Parameters

<dl> <dt>

*LCID* \[in\]
</dt> <dd>

**Number** (**long**) specifying the LCID.

</dd> </dl>

## Return value

This method returns a **String**.

## Remarks

An LCID uniquely identifies a particular language dialect, called a locale.

For Windows Media-based content, properties and methods related to language selection only support a single output.

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

[**Controls.getAudioLanguageID**](controls-getaudiolanguageid.md)
</dt> </dl>

 

 





