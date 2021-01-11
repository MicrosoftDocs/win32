---
description: Specifies, on IMFTransform, the maximum macroblock processing rate, in macroblocks per second, that is supported by the hardware encoder.
ms.assetid: 1AA41DE3-C37C-41BA-9549-5F12373DDB3B
title: MF_VIDEO_MAX_MB_PER_SEC attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_VIDEO\_MAX\_MB\_PER\_SEC attribute

Specifies, on [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform), the maximum macroblock processing rate, in macroblocks per second, that is supported by the hardware encoder.

## Data type

**UINT32**

## Remarks

This is a read-only attribute.

**H.264/AVC encoders:**

This attribute is affected by the following properties:

-   [MF\_MT\_VIDEO\_LEVEL](mf-mt-video-level.md) (which is an alias of [MF\_MT\_MPEG2\_LEVEL](mf-mt-mpeg2-level-attribute.md))
-   [CODECAPI\_AVEncCommonQualityVsSpeed](../directshow/avenccommonqualityvsspeed-property.md)
-   [CODECAPI\_AVEncMPVDefaultBPictureCount](../directshow/avencmpvdefaultbpicturecount-property.md)

If the [MF\_MT\_VIDEO\_LEVEL](mf-mt-video-level.md) attribute is present, the encoder should return the processing rate for the highest bitrate and resolution supported at the specified level. If the MF\_MT\_VIDEO\_LEVEL attribute is not present then it should use a default level of 4.

If the [CODECAPI\_AVEncCommonQualityVsSpeed](../directshow/avenccommonqualityvsspeed-property.md) ICodecAPI property has been set, the encoder should return the processing rate corresponding to the value set for this property. If the CODECAPI\_AVEncCommonQualityVsSpeed attribute is not present, then it should use a default value of 0 which should be the fastest processing mode.

If the [CODECAPI\_AVEncMPVDefaultBPictureCount](../directshow/avencmpvdefaultbpicturecount-property.md) ICodecAPI property has been set to a valid and supported value, the encoder should return the processing rate corresponding the value set for this property. If the CODECAPI\_AVEncMPVDefaultBPictureCount attribute is not presen,t then it should use a default value of 0 B frames.

Only the lower 28 bits should be used by an application. The upper 4bits are reserved for future use. Applications should ignore the upper 4 bits and MFTs should set the upper 4 bits to 0.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 
