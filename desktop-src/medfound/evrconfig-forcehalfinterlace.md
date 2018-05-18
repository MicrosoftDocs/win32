---
Description: 'Forces the Enhanced Video Renderer (EVR) to skip the second field of every interlaced frame.'
ms.assetid: 'b79d9230-b127-4e9b-b73b-685ce27aefa9'
title: 'EVRConfig\_ForceHalfInterlace attribute'
---

# EVRConfig\_ForceHalfInterlace attribute

Forces the Enhanced Video Renderer (EVR) to skip the second field of every interlaced frame.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Remarks

This attribute can be set on the EVR media sink. To set the attribute, use **QueryInterface** to query the EVR media sink for the [**IMFAttributes**](imfattributes.md) interface.

Setting this attribute has the same effect as setting the **MFVideoMixPrefs\_ForceHalfInterlace** flag on the EVR. See [**MFVideoMixPrefs**](mfvideomixprefs.md) for a description of this flag.

The GUID constant for this attribute is exported from strmiids.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Uuids.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[EVR Attributes](enhanced-video-renderer-attributes.md)
</dt> <dt>

[Video Quality Management](video-quality-management.md)
</dt> </dl>

 

 




