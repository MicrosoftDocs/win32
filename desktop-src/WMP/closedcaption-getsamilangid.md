---
title: ClosedCaption.getSAMILangID method
description: The getSAMILangID method retrieves the locale identifier (LCID) of a language supported by the current SAMI file.
ms.assetid: 35f8379a-a2f5-4b22-b1ad-3c5cc5bc5e3d
keywords:
- getSAMILangID method Windows Media Player
- getSAMILangID method Windows Media Player , ClosedCaption class
- ClosedCaption class Windows Media Player , getSAMILangID method
topic_type:
- apiref
api_name:
- ClosedCaption.getSAMILangID
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ClosedCaption.getSAMILangID method

The **getSAMILangID** method retrieves the locale identifier (LCID) of a language supported by the current SAMI file.

## Syntax


```JScript
retVal = ClosedCaption.getSAMILangID(
  index
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

**Number** (**long**) specifying the index of the LCID to retrieve.

</dd> </dl>

## Return value

This method returns a **Number** (**long**) containing the LCID of the language with the specified index.

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
</dt> </dl>

 

 





