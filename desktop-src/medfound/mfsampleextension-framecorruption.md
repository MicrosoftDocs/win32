---
Description: 'Specifies whether a video frame is corrupted.'
ms.assetid: '0218F6F6-6832-445C-B733-6A99E4EA2A3B'
title: 'MFSampleExtension\_FrameCorruption attribute'
---

# MFSampleExtension\_FrameCorruption attribute

Specifies whether a video frame is corrupted.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Applies to

[**IMFSample**](imfsample.md)

## Remarks

A video decoder can set this attribute on its output samples. If the value is 1, the decoder detected data corruption in the frame. If the value is 0, there is no data corruption, or none was detected.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Sample Attributes](sample-attributes.md)
</dt> <dt>

[Media Samples](media-samples.md)
</dt> </dl>

 

 




