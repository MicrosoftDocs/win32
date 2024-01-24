---
description: Specifies a number between 0 and 100 that indicates the tradeoff between encoding quality and encoding speed.
ms.assetid: 872140e8-fd39-446c-a84f-1e04ea95076e
title: MF_TRANSCODE_QUALITYVSSPEED attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TRANSCODE\_QUALITYVSSPEED attribute

Specifies a number between 0 and 100 that indicates the tradeoff between encoding quality and encoding speed.

## Data type

**UINT32**

The value of this property has the following range.



| Value                                                                          | Meaning                                     |
|--------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>0</dt> </dl>   | Lower quality, faster encoding.<br/>  |
| <dl> <dt>100</dt> </dl> | Higher quality, slower encoding.<br/> |



 

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

This attribute has the same GUID value as the [AVEncCommonQualityVsSpeed](../directshow/avenccommonqualityvsspeed-property.md) property defined for [**ICodecAPI**](/windows/win32/api/strmif/nn-strmif-icodecapi), and has the same interpretation.

The application can set this attribute on the transcode profile before building the transcode topology for Windows Media codecs. The value must be in the range from 0 to 100. For video stream, the transcode topology builder maps a value to the application-specified value and supplies the mapped value to the **MFPKEY\_COMPLEXITYEX** property of the encoder. Lower values enable the encoder to use less complicated encoding algorithms. Using simpler algorithms produces lower-quality output, but the encoding process is faster and requires less processing power.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Transcode API](transcode-api.md)
</dt> <dt>

[**IMFTranscodeProfile::SetVideoAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imftranscodeprofile-setvideoattributes)
</dt> </dl>

 

 
