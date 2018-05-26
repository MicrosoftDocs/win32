---
Description: Number of audio samples per second in an audio media type.
ms.assetid: f640016d-595e-4b20-8ce8-23a029c2b064
title: MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND attribute

Number of audio samples per second in an audio media type.

## Data type

**UINT32**

## Remarks

This attribute corresponds to the **nSamplesPerSec** member of the [**WAVEFORMATEX**](dshow.waveformatex) structure.

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

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[**MF\_MT\_AUDIO\_FLOAT\_SAMPLES\_PER\_SECOND**](mf-mt-audio-float-samples-per-second-attribute.md)
</dt> </dl>

 

 




