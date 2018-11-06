---
Description: Specifies whether to use an algorithm that produces higher-quality video, or a faster algorithm.
ms.assetid: a6760e7e-7c99-4412-bde5-05958fad89a1
title: MFPKEY_RESIZE_QUALITY Property
ms.topic: article
ms.date: 05/31/2018
---

# MFPKEY\_RESIZE\_QUALITY Property

Specifies whether to use an algorithm that produces higher-quality video, or a faster algorithm.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](https://msdn.microsoft.com/en-us/library/Bb761474(v=VS.85).aspx).

## Data Type

VT\_BOOL

## Applies To

-   [Video Resizer DSP](videoresizer.md)

## Remarks

Use one of the following values:



| Value     | Description          |
|-----------|----------------------|
| VT\_FALSE | Faster algorithm     |
| VT\_TRUE  | Higher-quality video |



 

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

 

 




