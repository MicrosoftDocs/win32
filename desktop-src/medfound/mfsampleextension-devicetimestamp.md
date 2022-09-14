---
description: Contains the time stamp from the device driver.
ms.assetid: 8904d104-ebcc-474d-b6b5-b262b6f62ee9
title: MFSampleExtension_DeviceTimestamp attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_DeviceTimestamp attribute

Contains the time stamp from the device driver.

## Data type

**UINT64**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint64).

To set this attribute, call [**IMFAttributes::SetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint64).

## Applies to

[**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample)

## Remarks

This attribute is set on media samples created by a media source for a capture device. This attribute's value is in the [**MFTIME**](mftime.md) domain, sharing an epoch with query performance counter (QPC) time and always expressed in 100ns units. This attribute is available for MFTs inserted into the capture pipeline.

To get the time stamp relative to the start of streaming, call the [**IMFSample::GetSampleTime**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-getsampletime) method.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Audio/Video Capture in Media Foundation](audio-video-capture-in-media-foundation.md)
</dt> <dt>

[Sample Attributes](sample-attributes.md)
</dt> </dl>

 

 




