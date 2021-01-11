---
description: Specifies the frame types (I, P, or B) that the quantization parameter (QP) is applied to.
ms.assetid: 6331033F-7EEB-41B3-B166-29686D4AADB6
title: CODECAPI_AVEncVideoEncodeFrameTypeQP property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CODECAPI\_AVEncVideoEncodeFrameTypeQP property

Specifies the frame types (I, P, or B) that the quantization parameter (QP) is applied to.

## Data type

**ULONGULONG** (VT\_UI8)

## Property GUID

**CODECAPI\_AVEncVideoEncodeFrameTypeQP**

## Remarks

For encoders which support setting a quantization parameter (QP) for different frame types (I, P, B), they shall expose this API in addition to [CODECAPI\_AVEncVideoEncodeQP](codecapi-avencvideoencodeqp.md). If an encoder supports only a single QP for all frame types, they shall support only CODECAPI\_AVEncVideoEncodeQP.

This is a dynamic encoding property meaning that a new value can be set any time during the encoding session.

**H.264/AVC encoders:**

Encoder shall support [**GetValue**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getvalue), [**SetValue**](/windows/desktop/api/strmif/nf-strmif-icodecapi-setvalue), and [**GetParameterRange**](/windows/desktop/api/strmif/nf-strmif-icodecapi-getparameterrange).

A set of four 16-bit fields are used to specify the frame QPs in fixed-QP encoding. The fields are:

-   **Bits 0-15:** QP used for I frames, valid range \[0, 51\].
-   **Bits 16-31:** QP used for P frames, valid range \[0, 51\].
-   **Bits 32-47:** QP used for B frames, valid range \[0, 51\]
-   **Bits 48-63:** reserved

When this CodecAPI is supported, encoders shall support QP setting on frame type of I, P, and B.

Default value shall be 0x0000001a001a001a. QP equal to 26 for I, P and B.

When [CODECAPI\_AVEncVideoSelectLayer](codecapi-avencvideoselectlayer.md) selects a specific temporal layer, [**SetValue**](/windows/desktop/api/strmif/nf-strmif-icodecapi-setvalue) of CODECAPI\_AVEncVideoEncodeFrameTypeQP shall set QP for I, P, and B frames on that temporal layer. By default, it sets QP for I, P, and B frames on base temporal layer temporal layer 0.

[CODECAPI\_AVEncVideoMaxQP](codecapi-avencvideomaxqp.md) and [CODECAPI\_AVEncVideoMinQP](codecapi-avencvideominqp.md) shall be used to define and limit the QP range for QPs of all picture types, I, P and B.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

