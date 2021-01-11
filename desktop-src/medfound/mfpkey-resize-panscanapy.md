---
description: Specifies the y-coordinate of the upper-left corner of the pan/scan region.
ms.assetid: 9286d9eb-b390-4e7b-b0e8-3cd35dfab60c
title: MFPKEY_RESIZE_PANSCANAPY Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_RESIZE\_PANSCANAPY Property

Specifies the y-coordinate of the upper-left corner of the pan/scan region.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_I4

## Applies To

-   [Video Resizer DSP](videoresizer.md)

## Remarks

The value is a fixed-point real number. The integer portion of the number is stored in the higher 2 bytes and the fractional part is stored in the lower 2 bytes.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 
