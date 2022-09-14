---
description: Specifies the number of video frames encoded by the codec.
ms.assetid: 4a812609-137f-4f7f-aa55-89e26d7f1972
title: MFPKEY_CODEDFRAMES Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_CODEDFRAMES Property

Specifies the number of video frames encoded by the codec.

## Constant for IPropertyBag

g\_wszWMVCCodedFrames

## Data Type

VT\_I4

## Remarks

This value is equal to [MFPKEY\_TOTALFRAMES](mfpkey-totalframesproperty.md) minus any frames that were dropped due to bit-rate constraints. You can get this value after you are finished passing samples.

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

 

 




