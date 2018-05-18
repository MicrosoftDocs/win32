---
Description: 'Block alignment, in bytes, for an audio media type. The block alignment is the minimum atomic unit of data for the audio format.'
ms.assetid: '7d304826-ad81-4243-a675-2f55b668b348'
title: 'MF\_MT\_AUDIO\_BLOCK\_ALIGNMENT attribute'
---

# MF\_MT\_AUDIO\_BLOCK\_ALIGNMENT attribute

Block alignment, in bytes, for an audio media type. The block alignment is the minimum atomic unit of data for the audio format.

## Data type

**UINT32**

## Remarks

For PCM audio formats, the block alignment is equal to the number of audio channels multiplied by the number of bytes per audio sample.

This attribute corresponds to the **nBlockAlign** member of the [**WAVEFORMATEX**](dshow.waveformatex) structure.

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

 

 




