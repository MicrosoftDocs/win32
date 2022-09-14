---
title: ClosedCaption.SAMIStyleCount
description: The SAMIStyleCount property retrieves the number of styles supported by the current SAMI file.
ms.assetid: 57a85e5d-1598-4cb3-b47d-a6d8f22adfff
keywords:
- ClosedCaption.SAMIStyleCount Windows Media Player
topic_type:
- apiref
api_name:
- ClosedCaption.SAMIStyleCount
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# ClosedCaption.SAMIStyleCount

The **SAMIStyleCount** property retrieves the number of styles supported by the current SAMI file.

``` syntax
player.closedCaption.SAMIStyleCount
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

[**ClosedCaption.getSAMIStyleName**](closedcaption-getsamistylename.md)
</dt> <dt>

[**ClosedCaption.SAMIStyle**](closedcaption-samistyle.md)
</dt> </dl>

 

 





