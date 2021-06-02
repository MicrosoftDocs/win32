---
description: Specifies whether to use an algorithm that produces higher-quality video, or a faster algorithm.
ms.assetid: a6760e7e-7c99-4412-bde5-05958fad89a1
title: MFPKEY_RESIZE_QUALITY Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_RESIZE\_QUALITY Property

Specifies whether to use an algorithm that produces higher-quality video, or a faster algorithm.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore).

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



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 
