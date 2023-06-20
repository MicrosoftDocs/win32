---
description: Setting Media Types on a DMO
ms.assetid: 9ff1542d-6a67-414d-8336-aae80c74d5d0
title: Setting Media Types on a DMO
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Setting Media Types on a DMO

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Before a DMO can process any data, the client must set the media type for each stream. (There is one minor exception to this rule; see [Optional Streams](optional-streams.md).) To find the number of streams, call the [**IMediaObject::GetStreamCount**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-getstreamcount) method:


```C++
DWORD cInput = 0, cOutput = 0;
pDMO->GetStreamCount(&cInput, &cOutput);
```



This method returns two values, the number of inputs and the number of outputs. These values are fixed for the lifetime of the DMO.

**Preferred Types**

For every stream, the DMO assigns a list of possible media types, in order of preference. For example, the preferred types might be 32-RGB, 24-bit RGB, and 16-bit RGB, in that order. When the client sets the media types, it can use these lists as a hint. To retrieve a preferred type for a stream, call the [**IMediaObject::GetInputType**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-getinputtype) method or [**IMediaObject::GetOutputType**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-getoutputtype) method. Specify the stream number and an index value for the type (starting from zero). For example, the following code retrieves the first preferred type from the first input stream:


```C++
DMO_MEDIA_TYPE mt
hr = pDMO->GetInputType(0, 0, &mt)
if (SUCCEEDED(hr))
{
    // Examine this media type (not shown).
    /* ... */

    // Free the format block.
    MoFreeMediaType(&mt);
}
```



To enumerate all of the preferred media types on a given stream, use a loop that increments the type index until the method returns DMO\_E\_NO\_MORE\_ITEMS, as shown in the following example:


```C++
DMO_MEDIA_TYPE mt;
DWORD dwType = 0;
while (hr = pDMO->GetInputType(0, dwType, &mt), SUCCEEDED(hr))
{
    // Examine this media type (not shown).
    /* ... */

    // Free the format block.
    MoFreeMediaType(&mt);
    ++dwType;
}
```



You should note the following points about preferred types:

-   The DMO might return a type that has no format block. For example, a DMO could specify a video type, such as 24-bit RGB, without providing the width and height of the image. When you set the type, however, you must provide a complete format block. (Some media types, such as MIDI, never require a format block, in which case this remark does not apply.)
-   The DMO is not required to support every combination of preferred types that it returns. For example, if a DMO has two streams, and each stream has four preferred types, there are 16 possible combinations, but not all of them are guaranteed to be valid.
-   When the client sets the media type for one stream, the DMO might update the preferred types for other streams to reflect the new state. It is not required to do so, however.
-   For some streams, the DMO might not offer any preferred types. Typically, a DMO should offer at least some preferred types on some streams.
-   The DMO is not required to offer a complete list of the media types it can accept. There might be "unadvertised" types that the DMO supports but does not offer as preferred types.

In short, the client should treat the preferred types as guidelines only. The only way to know for certain which types are supported is to test them, as described in the next section.

**Setting the Media Type on a Stream**

Use the [**IMediaObject::SetInputType**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-setinputtype) and [**IMediaObject::SetOutputType**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-setoutputtype) methods to set the type for each stream. You must provide a **DMO\_MEDIA\_TYPE** structure that contains a complete description of the media type. The following example sets the media type on input stream 0, using 44.1-kHz 16-bit stereo PCM audio:


```C++
DMO_MEDIA_TYPE mt;
ZeroMemory(&mt, sizeof(DMO_MEDIA_TYPE));
// Allocate memory for the format block.
HRESULT hr = MoInitMediaType(&mt, sizeof(WAVEFORMATEX));
if (SUCCEEDED(hr))
{
    // Set the type GUIDs.
    mt.majortype  = MEDIATYPE_Audio;
    mt.subtype    = MEDIASUBTYPE_PCM;
    mt.formattype = FORMAT_WaveFormatEx;

    // Initialize the format block.
    WAVEFORMATEX *pWave = reinterpret_cast<WAVEFORMATEX*>(mt.pbFormat);
    pWave->wFormatTag = WAVE_FORMAT_PCM;
    pWave->nChannels = 2;
    pWave->nSamplesPerSec = 44100;
    pWave->wBitsPerSample = 16;
    pWave->nBlockAlign = (pWave->nChannels * pWave->wBitsPerSample) / 8;
    pWave->nAvgBytesPerSec = pWave->nSamplesPerSec * pWave->nBlockAlign;
    pWave->cbSize = 0;

    // Set the media type.
    hr = pDMO->SetInputType(0, &mt, 0); 

    // Release the format block.
    MoFreeMediaType(&mt);
}
```



To test a media type without setting it, call **SetInputType** or **SetOutputType** with the DMO\_SET\_TYPEF\_TEST\_ONLY flag. The method returns S\_OK if the type is acceptable, or S\_FALSE otherwise:


```C++
if (S_OK == pDMO->SetInputType(0, &mt, DMO_SET_TYPEF_TEST_ONLY)
{
    // Media type is OK.
}
```



Because the settings on one stream can affect another stream, you might need to clear a stream's media type. To do this, call **SetInputType** or **SetOutputType** with the DMO\_SET\_TYPEF\_CLEAR flag.

For a decoder DMO, the client would typically set the input type first, and then choose an output type. For an encoder DMO, the client would set the output type first, and then the input type.

## Related topics

<dl> <dt>

[Directly Hosting a DMO](directly-hosting-a-dmo.md)
</dt> </dl>

 

 



