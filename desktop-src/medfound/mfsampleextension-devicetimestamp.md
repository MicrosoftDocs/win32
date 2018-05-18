---
Description: 'Contains the time stamp from the device driver.'
ms.assetid: '8904d104-ebcc-474d-b6b5-b262b6f62ee9'
title: 'MFSampleExtension\_DeviceTimestamp attribute'
---

# MFSampleExtension\_DeviceTimestamp attribute

Contains the time stamp from the device driver.

## Data type

**UINT64**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT64**](imfattributes-getuint64.md).

To set this attribute, call [**IMFAttributes::SetUINT64**](imfattributes-setuint64.md).

## Applies to

[**IMFSample**](imfsample.md)

## Remarks

This attribute is set on media samples created by a media source for a capture device. This attribute carries the non-adjusted value of the query performance counter (QPC). This attribute is available for MFTs inserted into the capture pipeline.

To get the time stamp relative to the start of streaming, call the [**IMFSample::GetSampleTime**](imfsample-getsampletime.md) method.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
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

 

 




