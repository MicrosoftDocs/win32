---
description: Indicates whether MFSampleExtension\_ROIRectangle attribute set on the input sample will be honored or not.
ms.assetid: 6B3CB513-43E8-4D30-B5A0-CD2E9C9F46BA
title: CODECAPI_AVEncVideoROIEnabled property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CODECAPI\_AVEncVideoROIEnabled property

Indicates whether [MFSampleExtension\_ROIRectangle](mfsampleextension-roirectangle.md) attribute set on the input sample will be honored or not.

## Data type

**BOOL** (VT\_BOOL)

## Property GUID

**CODECAPI\_AVEncVideoROIEnabled**

## Remarks

The default value is **FALSE**. This indicates that the AAC encoder MFT will use constant bit rate encoding.  The encoded bit stream will have a certain bitrate independent of the input signal. 

If this value is set to **TRUE**, it indicates that the AAC encoder MFT will use variable bit rate encoding. The encoder adapts the bitrate of the encoded stream depending on the psychoacoustic requirements of the input signal.

Apps should set the CODECAPI_AVEncAACEnableVBR property on the encoder MFT before setting the input and output media types on the encoder MFT. This is because the VBR setting may affect which input and output media type combinations are supported by the encoder.
Setting the CODECAPI_AVEncAACEnableVBR property after setting the input or output media types, may result in an error if the input or output media types are not supported by the requested VBR setting.
When VBR encoding is enabled, the MF_MT_AVG_BITRATE attribute on the output media type specifies the average bit rate of the encoded output.


## Requirements


| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10                                   |
| Minimum supported server<br/> | Windows Server 2022     |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




