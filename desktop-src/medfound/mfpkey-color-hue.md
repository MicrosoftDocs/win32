---
description: Adjusts the hue.
ms.assetid: 8dc3c888-5ab8-40a1-8768-bec58b62eaf0
title: MFPKEY_COLOR_HUE Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_COLOR\_HUE Property

Adjusts the hue.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

## Data Type

VT\_I4

## Default Value

0

## Applies To

-   [Color Control Transform DSP](colorcontroltransform.md)

## Remarks

Hue adjustment is performed by mixing the Cb and Cr values. (If Cb and Cr are plotted in a 2-dimensional space, hue adjustment is performed by rotating around the origin.)

This property has a range of -127 to 127. Zero indicates no change in hue.

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

 

 
