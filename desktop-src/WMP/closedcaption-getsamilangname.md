---
title: ClosedCaption.getSAMILangName method
description: The getSAMILangName method retrieves the name of a language supported by the current SAMI file.
ms.assetid: 20cf8faf-3a8c-4d7b-9bd1-2366672f0e67
keywords:
- getSAMILangName method Windows Media Player
- getSAMILangName method Windows Media Player , ClosedCaption class
- ClosedCaption class Windows Media Player , getSAMILangName method
topic_type:
- apiref
api_name:
- ClosedCaption.getSAMILangName
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ClosedCaption.getSAMILangName method

The **getSAMILangName** method retrieves the name of a language supported by the current SAMI file.

## Syntax


```JScript
strRetVal = ClosedCaption.getSAMILangName(
  index
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) specifying the index of the language name to retrieve.

</dd> </dl>

## Return value

This method returns a **String** containing the name of the language as specified in the SAMI file.

## Remarks

The languages in a SAMI file are indexed in the order shown in the file, starting with zero.

This method cannot be used until a digital media file is open (*Player*.**openState** is equal to 13).

**Windows Media Player 10 Mobile:** This method is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Adding Closed Captions to Digital Media**](adding-closed-captions-to-digital-media.md)
</dt> <dt>

[**ClosedCaption Object**](closedcaption-object.md)
</dt> <dt>

[**ClosedCaption.SAMILang**](closedcaption-samilang.md)
</dt> </dl>

 

 





