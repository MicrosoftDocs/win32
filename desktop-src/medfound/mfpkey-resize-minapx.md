---
Description: Specifies the x-coordinate of the upper-left corner of the minimum display aperture.
ms.assetid: eb9e5330-fd89-4bca-ae8c-62985f9b2373
title: MFPKEY\_RESIZE\_MINAPX Property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFPKEY\_RESIZE\_MINAPX Property

Specifies the x-coordinate of the upper-left corner of the minimum display aperture.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](https://msdn.microsoft.com/e995aaa1-d4c9-475f-b1fa-b9123cd5b653).

## Data Type

VT\_I4

## Applies To

-   [Video Resizer DSP](videoresizer.md)

## Remarks

The value is a fixed-point real number. The integer portion of the number is stored in the higher 2 bytes and the fractional part is stored in the lower 2 bytes.

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

 

 




