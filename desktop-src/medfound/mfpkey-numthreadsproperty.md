---
description: Specifies the number of threads that the encoder will use.
ms.assetid: 2f463cba-2512-455d-9ce1-8797682d4d67
title: MFPKEY_NUMTHREADS Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_NUMTHREADS Property

Specifies the number of threads that the encoder will use.

## Constant for IPropertyBag

g\_wszWMVCNumThreads

## Data Type

VT\_I4

## Default Value

1

## Remarks

This value is intended to divide encoding into multiple threads to take advantage of computers with multiple processors. Splitting encoding tasks into multiple threads can cause a slight decrease in quality as compared to a single thread.

For the video encoder (wmvencod.dll) released with Windows XP and Windows Vista, this property should be set to 1, 2, or 4. Other values will be rounded down.

For the video encoder (wmvencod.dll) released with Windows 7, this property should be set to 1, 2, 4, or 8. Other values will be rounded down.

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

 

 




