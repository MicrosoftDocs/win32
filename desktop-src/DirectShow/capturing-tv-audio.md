---
description: Capturing TV Audio
ms.assetid: c0c62a8e-ab16-4617-936c-b64e6e3865b4
title: Capturing TV Audio
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Capturing TV Audio

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To capture audio from analog television to a file, use the [Audio Capture Filter](audio-capture-filter.md). Use the System Device Enumerator to create the Audio Capture Filter. There may be several audio capture devices on the user's system; the user must select the device that represents the sound card.

Connect the audio capture output pin to the mux filter:


```C++
hr = pBuild->RenderStream(
   &PIN_CATEGORY_CAPTURE, // Capture pin.
   &MEDIATYPE_Audio,      // Audio media type.
   pAudioCap,             // Pointer to the audio capture filter.
   NULL,                  // Optional audio compressor filter.
   pMux);                 // Pointer to the mux filter.
```



The input pins do not have to be connected to anything. Each input pin represents a physical input on the audio capture device. Use the [**IAMAudioInputMixer**](/windows/desktop/api/Strmif/nn-strmif-iamaudioinputmixer) interface to enable the input that receives the audio stream from the tuner. The input pins are identified by name, such as "Line In" or "CD Audio." Unfortunately, the names can change from one device to the next. Also, different TV tuner cards use different inputs to the sound card. Therefore, it is up to the user to identify which input to use.


```C++
IEnumPins *pEnum = NULL;
hr = pAudioCap->EnumPins(&pEnum);
if (SUCCEEDED(hr))
{
    IPin *pPin = NULL;
    while (S_OK == pEnum->Next(1, &pPin, NULL))
    {
        IAMAudioInputMixer *pMix;
        hr = pPin->QueryInterface(IID_IAMAudioInputMixer, (void**)&pMix);
        if (SUCCEEDED(hr))
        {
            // Use IPin::QueryPinInfo to get the pin name.
            pPin->Release();
            if (...) // If the user selects this pin:
            {
                pMix->put_Enable(TRUE);
                pMix->put_MixLevel(1.0);
                pMix->Release();
                break;
            }
            pMix->Release();
        }
    }
}
pEnum->Release();
```



## Related topics

<dl> <dt>

[Analog Television Audio](analog-television-audio.md)
</dt> <dt>

[Audio Capture](audio-capture.md)
</dt> </dl>

 

 



