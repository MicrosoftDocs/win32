---
description: Collecting Fine-Tuning Information
ms.assetid: 0d9ea896-e0a9-411b-9a10-e366e3686a34
title: Collecting Fine-Tuning Information
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Collecting Fine-Tuning Information

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Although cable frequencies are generally expected to be exact, broadcast frequencies may be adjusted up or down several kHz by the broadcast station to reduce potential interference with neighboring channels.

When the TV Tuner filter tunes to a channel, it scans for the most precise signal. To save this information in the registry for subsequent tuning operations, do the following:

1.  Call [**IAMTuner::ChannelMinMax**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-channelminmax) to determine the range of frequency entries in the current frequency table.
2.  Call the [**IAMTuner::put\_Channel**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-put_channel) method once for each frequency index in the range.
3.  Call [**IAMTVTuner::StoreAutoTune**](/windows/desktop/api/Strmif/nf-strmif-iamtvtuner-storeautotune) to save the fine-tuning information in the registry. The information is stored under the registry key for the current tuning space.

The following code shows these steps:


```C++
long lMin = 0, lMax = 0;
hr = pTuner->ChannelMinMax(&lMin, &lMax);
if (SUCCEEDED(hr))
{
    for (long i = lMin; i <= lMax; i++)
    {
        pTuner->put_Channel(i, AMTUNER_SUBCHAN_DEFAULT,
            AMTUNER_SUBCHAN_DEFAULT)
    }
    pTuner->StoreAutoTune();
}
```



With earlier versions of the TV Tuner filter, the [**IAMTVTuner::AutoTune**](/windows/desktop/api/Strmif/nf-strmif-iamtvtuner-autotune) method was recommended for fine-tuning. However, this method ignores any frequency overrides, so its use is no longer recommended. The following code is equivalent to the **AutoTune** method, but works correctly with frequency overrides:


```C++
HRESULT MyAutoTune(IAMTVTuner *pTuner, long lIndex, long *plFoundSignal)
{
    long SignalStrength = AMTUNER_NOSIGNAL;
    HRESULT hr;
    hr = pTuner->put_Channel(lIndex, AMTUNER_SUBCHAN_DEFAULT, AMTUNER_SUBCHAN_DEFAULT);
    if (NOERROR == hr)
        pTuner->SignalPresent(&SignalStrength);
    *plFoundSignal = (SignalStrength != AMTUNER_NOSIGNAL);
        return hr;
}
```



With broadcast reception, it is not always possible to get a horizontal lock, although the picture is viewable. In these cases, the tuner hardware will have a frequency lock, but the decoder will not have horizontal lock. This condition can be detected when using [**put\_Channel**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-put_channel) or [**AutoTune**](/windows/desktop/api/Strmif/nf-strmif-iamtvtuner-autotune) by examining the return code.



| Value    | Description                                                                                                                                                                               |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| S\_OK    | The tune operation succeeded and the tuner got a frequency lock.                                                                                                                          |
| S\_FALSE | There were no errors during the tune operation, but the tuner was not able to get a frequency lock. It is highly unlikely that there is a viewable channel resulting from this operation. |



 

Any other return code indicates that some error occurred.

A return value of S\_OK does not guarantee that the decoder has a horizontal lock. The [**AutoTune**](/windows/desktop/api/Strmif/nf-strmif-iamtvtuner-autotune) method updates the *FoundSignal* parameter to indicate whether or not horizontal lock was achieved. The [**IAMTuner::SignalPresent**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-signalpresent) method returns the same information.

When the return value is S\_OK, however, the application has the option of ignoring the *FoundSignal* parameter, because the tuner is reporting a frequency lock. There is the possibility of a frequency lock on noise, but this possibility should be weighed against the possibility of skipping viewable channels.

## Registry Conversion

To support frequency overrides, the internal format of the registry key that holds fine-tuning information has changed. The original format is still supported for backward compatibility, but it does not support frequency overrides.

The old registry format is converted to the new format whenever the [**IAMTVTuner::StoreAutoTune**](/windows/desktop/api/Strmif/nf-strmif-iamtvtuner-storeautotune) method is called. If your application adds frequency overrides, it should call the **StoreAutoTune** method to convert to the new registry format. It is not necessary to collect any fine-tuning information before calling **StoreAutoTune**.

## Related topics

<dl> <dt>

[International Analog TV Tuning](international-analog-tv-tuning.md)
</dt> </dl>

 

 



