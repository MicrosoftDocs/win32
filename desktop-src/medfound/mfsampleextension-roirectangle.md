---
description: Specifies the bounds of the region of interest which indicates the region of the frame that requires different quality.
ms.assetid: F06CACF0-AE75-4707-8CD0-7BA7D51BB80A
title: MFSampleExtension_ROIRectangle attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_ROIRectangle attribute

Specifies the bounds of the region of interest which indicates the region of the frame that requires different quality.

## Data type

**[**ROI\_AREA**](/windows/desktop/api/mfapi/ns-mfapi-roi_area)** stored as **BLOB**

## Remarks

After successfully setting [CODECAPI\_AVEncVideoROIEnabled](codecapi-avencvideoroienabled.md) to a non-zero value on an encoder MFT, the application can set this attribute on input samples and expect it to be honored.

If [CODECAPI\_AVEncVideoROIEnabled](codecapi-avencvideoroienabled.md) is not set to a non-zero value, the MFSampleExtension\_ROIRectangle attribute is ignored on input samples.

MFSampleExtension\_ROIRectangle is set on an input sample and is only applied to the current input sample.

The **QPDelta** field on the [**ROI\_AREA**](/windows/desktop/api/mfapi/ns-mfapi-roi_area) structure specifies the quantization parameter delta for the specified region from the rest of the frame. If **QPDelta** is positive, this indicates the application wants the rectangle to have lower quality than the rest of the frame.

**H.264/AVC encoders:** **QPDelta** shall be between \[-25, +25\]. The encoder shall ensure that the final QP is in a valid range for the video standard.

The specified region is not required to be MB aligned. Encoders have flexibility to decide the actual boundary. It is recommended to cover the entire specified region.

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

 

 




