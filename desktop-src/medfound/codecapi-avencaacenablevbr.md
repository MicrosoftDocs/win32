---
description: Specifies whether variable bitrate (VBR) encoding is used for AAC encoding.
title: CODECAPI_AVEncAACEnableVBR property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CODECAPI\_AVEncAACEnableVBR property

Specifies whether variable bitrate (VBR) encoding is used for Advanced Audio Coding (AAC) encoding.

## Data type

**BOOL** (VT\_UI4)

## Property GUID

**CODECAPI\_AVEncAACEnableVBR**

## Property value

A boolean value specifying whether variable bitrate (VBR) encoding is used for Advanced Audio Coding (AAC) encoding.

## Remarks

The default value is **FALSE**. This indicates that the AAC encoder MFT will use constant bit rate encoding.  The encoded bit stream will have a certain bitrate independent of the input signal. 

If this value is set to **TRUE**, it indicates that the AAC encoder MFT will use variable bit rate encoding. The encoder adapts the bitrate of the encoded stream depending on the psychoacoustic requirements of the input signal.

Apps should set the CODECAPI_AVEncAACEnableVBR property on the encoder MFT before setting the input and output media types on the encoder MFT. This is because the VBR setting may affect which input and output media type combinations are supported by the encoder.

Setting the CODECAPI_AVEncAACEnableVBR property after setting the input or output media types, may result in an error if the input or output media types are not supported by the requested VBR setting.
When VBR encoding is enabled, the MF_MT_AVG_BITRATE attribute on the output media type specifies the average bit rate of the encoded output.

Note that while the variant type of the CODECAPI_AVEncAACEnableVBR property is VT_BOOL, [IMFAttributes](/windows/win32/api/mfobjects/nn-mfobjects-imfattributes) does not support Boolean attributes. Therefore, you should use [SetUINT32](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-setuint32) instead. The attribute value will be automatically converted to a VT_BOOL property value when it is transferred to the encoder MFT.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10        |
| Minimum supported server<br/> | Windows 2022<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[**ICodecAPI**](/windows/desktop/api/strmif/nn-strmif-icodecapi)
</dt> </dl>

 

