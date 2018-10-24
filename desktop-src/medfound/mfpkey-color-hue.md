---
Description: Adjusts the hue.
ms.assetid: 8dc3c888-5ab8-40a1-8768-bec58b62eaf0
title: MFPKEY_COLOR_HUE Property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFPKEY\_COLOR\_HUE Property

Adjusts the hue.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](https://msdn.microsoft.com/en-us/library/Bb761474(v=VS.85).aspx).

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



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




