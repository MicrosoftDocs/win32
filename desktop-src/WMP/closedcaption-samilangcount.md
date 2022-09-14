---
title: ClosedCaption.SAMILangCount
description: The SAMILangCount property retrieves the number of languages supported by the current SAMI file.
ms.assetid: ad2e776a-b430-46ee-9705-18d279e8715e
keywords:
- ClosedCaption.SAMILangCount Windows Media Player
topic_type:
- apiref
api_name:
- ClosedCaption.SAMILangCount
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# ClosedCaption.SAMILangCount

The **SAMILangCount** property retrieves the number of languages supported by the current SAMI file.

``` syntax
player.closedCaption.SAMILangCount
```

## Possible Values

This property is a read-only **Number** (**long**).

## Remarks

This method cannot be used until a digital media file is open (*Player*.**openState** is equal to 13).

**Windows Media Player 10 Mobile:** This property always returns 0.

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

[**ClosedCaption.getSAMILangName**](closedcaption-getsamilangname.md)
</dt> <dt>

[**ClosedCaption.SAMILang**](closedcaption-samilang.md)
</dt> </dl>

 

 





