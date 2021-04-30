---
description: Indicates whether video stabilization was applied to a video frame.
ms.assetid: 13F877A3-7600-400F-9071-FE1B83027355
title: MFSampleExtension_VideoDSPMode attribute (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_VideoDSPMode attribute

Indicates whether video stabilization was applied to a video frame.

## Data type

**MFVideoDSPMode** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample)

## Remarks

The [**Video Stabilization MFT**](video-stabilization-mft.md) sets this attribute on the output samples that it produces. The value of the attribute is an [**MFVideoDSPMode**](/windows/desktop/api/wmcodecdsp/ne-wmcodecdsp-mfvideodspmode) enumeration value. If the value is **MFVideoDSPMode\_Stabilization**, it means that the MFT applied image stabilization to the frame.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Sample Attributes](sample-attributes.md)
</dt> <dt>

[Media Samples](media-samples.md)
</dt> <dt>

[**Video Stabilization MFT**](video-stabilization-mft.md)
</dt> </dl>

 

 




