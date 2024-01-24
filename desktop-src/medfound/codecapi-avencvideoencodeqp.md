---
description: Specifies the quantization parameter (QP) for video encoding.
ms.assetid: 9E3B5E2D-3583-4C89-BC2A-4AC3C5545673
title: CODECAPI_AVEncVideoEncodeQP property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CODECAPI\_AVEncVideoEncodeQP property

Specifies the quantization parameter (QP) for video encoding.

## Data type

**ULONGLONG** (VT\_UI8)

## Property GUID

**CODECAPI\_AVEncVideoEncodeQP**

## Property value

A set of four 16-bit fields used to specify the frame QPs in fixed-QP encoding.

The fields are:

-   Bits 0-15: Default QP
-   Bits 16-31: QP used for I frames
-   Bits 32-47: QP used for P frames
-   Bits 48-63: QP used for B frames

## Remarks

This property is also used with [H.264 UVC 1.5 camera encoders](camera-encoder-h264-uvc-1-5.md).

To insure consistent usage across different encoders, you should assume encoders will only look at the default QP and can ignore QP values for I/P/B pictures.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[**ICodecAPI**](/windows/desktop/api/strmif/nn-strmif-icodecapi)
</dt> </dl>

 

