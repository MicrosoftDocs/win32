---
title: ClosedCaption.getSAMIStyleName method
description: The getSAMIStyleName method retrieves the name of a style supported by the current SAMI file.
ms.assetid: c2ffedf8-4622-44fe-9d92-b52ed3bf3b9a
keywords:
- getSAMIStyleName method Windows Media Player
- getSAMIStyleName method Windows Media Player , ClosedCaption class
- ClosedCaption class Windows Media Player , getSAMIStyleName method
topic_type:
- apiref
api_name:
- ClosedCaption.getSAMIStyleName
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ClosedCaption.getSAMIStyleName method

The **getSAMIStyleName** method retrieves the name of a style supported by the current SAMI file.

## Syntax


```JScript
strRetVal = ClosedCaption.getSAMIStyleName(
  index
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) specifying the index of the style name to retrieve.

</dd> </dl>

## Return value

This method returns a **String** containing the name of the style as specified in the SAMI file.

## Remarks

The styles in a SAMI file are indexed in the order shown in the file, starting with zero.

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

[**ClosedCaption.SAMIStyle**](closedcaption-samistyle.md)
</dt> </dl>

 

 





