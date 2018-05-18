---
Description: 'Number of audio samples contained in one compressed block of audio data. This attribute can be used in compressed audio formats that have a fixed number of samples within each block.'
ms.assetid: '6ae31548-4d78-4e38-9cfc-01b611a6022d'
title: 'MF\_MT\_AUDIO\_SAMPLES\_PER\_BLOCK attribute'
---

# MF\_MT\_AUDIO\_SAMPLES\_PER\_BLOCK attribute

Number of audio samples contained in one compressed block of audio data. This attribute can be used in compressed audio formats that have a fixed number of samples within each block.

## Data type

**UINT32**

## Remarks

This attribute corresponds to the **wSamplesPerBlock** member of the [**WAVEFORMATEXTENSIBLE**](dshow.waveformatextensible) structure.

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

 

 




