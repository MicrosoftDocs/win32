---
description: How to find the duration of a media file.
ms.assetid: 88ecde0c-328f-4ca7-9d26-836e4df06563
title: How to Find the Duration of a Media File
ms.topic: article
ms.date: 05/31/2018
---

# How to Find the Duration of a Media File

To find the duration of a media file, perform the following steps:

1.  Use the [Source Resolver](source-resolver.md) to create a media source that can parse the media file.
2.  Call [**IMFMediaSource::CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor) on the media source. This method returns presentation descriptor that describes the contents of the media file.
3.  Query the presentation descriptor for the [MF\_PD\_DURATION](mf-pd-duration-attribute.md) attribute by calling the [**IMFAttributes::GetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint64) method. The value of the attribute, if present, is the file duration in 100-nanosecond units.


```C++
HRESULT GetSourceDuration(IMFMediaSource *pSource, MFTIME *pDuration)
{
    *pDuration = 0;

    IMFPresentationDescriptor *pPD = NULL;

    HRESULT hr = pSource->CreatePresentationDescriptor(&pPD);
    if (SUCCEEDED(hr))
    {
        hr = pPD->GetUINT64(MF_PD_DURATION, (UINT64*)pDuration);
        pPD->Release();
    }
    return hr;
}
```



## Related topics

<dl> <dt>

[Audio/Video Playback](audio-video-playback.md)
</dt> </dl>

 

 



