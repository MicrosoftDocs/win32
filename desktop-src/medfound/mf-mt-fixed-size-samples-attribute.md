---
Description: 'Specifies for a media type whether the samples have a fixed size.'
ms.assetid: '2d67864a-fd2f-400d-8a1e-e71dc1920593'
title: 'MF\_MT\_FIXED\_SIZE\_SAMPLES attribute'
---

# MF\_MT\_FIXED\_SIZE\_SAMPLES attribute

Specifies for a media type whether the samples have a fixed size.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

If this attribute is **TRUE**, every sample in the stream is the same size (in bytes). Otherwise, samples might vary in size.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[**IMFMediaType**](imfmediatype.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




