---
description: Analog Television Tuning
ms.assetid: f4ae76e3-0f61-4a33-8ea4-ef14a117df6a
title: Analog Television Tuning
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Analog Television Tuning

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Tuning is controlled by the TV Tuner filter, through the [**IAMTVTuner**](/windows/desktop/api/Strmif/nn-strmif-iamtvtuner) interface. The IAMTVTuner interface inherits IAMTuner. To obtain a pointer to the interface, call the [**ICaptureGraphBuilder2::FindInterface**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-findinterface) method as follows:


```C++
IAMTVTuner *pTuner = NULL;
hr = pBuild->FindInterface(
    &LOOK_UPSTREAM_ONLY,  // Look upstream from pCap.
    NULL,                 // No particular media type.
    pCap,                 // Pointer to the capture filter.
    IID_IAMTVTuner, (void**)&pTuner);
if (SUCCEEDED(hr))
{
    // Use pTuner ...
    pTuner->Release();
}
```



The first parameter indicates to search upstream from the capture filter.

Frequency Tables

Internally, the TV Tuner filter keeps a list of frequency tables. Each frequency table corresponds to the broadcast or cable frequencies for a given country/region. There is also a generic "Unicable" frequency table, which is used when a country/region does not have a standard set of frequency assignments.

Each frequency table contains a list of tuning frequencies. For some countries/regions, the indexes in the table correspond directly to channel numbers — in other words, the frequency for channel n is the n th entry in the table. For some countries/regions, however, there is no direct correspondence between channel numbers and frequencies. In that case, the application must keep a list that maps channel numbers (typically chosen by the user) to frequency table entries. For example, what the user sees as "channel 5" might be entry number 12 in the frequency table.

For details, see [International Analog TV Tuning](international-analog-tv-tuning.md).

Basic Tuning Operations

If the tuner supports multiple reception modes, such as television and FM radio, call [**IAMTuner::put\_Mode**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-put_mode) to select the mode. The [**IAMTuner::GetAvailableModes**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-getavailablemodes) method returns all of the modes that the tuner supports. For example, the following code checks whether the tuner supports FM radio, and if so, switches to that mode.


```C++
// Check whether the mode is supported.
long lModes = 0;
hr = m_pTuner->GetAvailableModes(&lModes);
if (SUCCEEDED(hr) && (lModes & AMTUNER_MODE_FM_RADIO))
{
    // Set the mode.
    hr = pTuner->put_Mode(AMTUNER_MODE_FM_RADIO);
}
```



To set the country/region, call the [**IAMTuner::put\_CountryCode**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-put_countrycode) method. The tuner uses this value to select the appropriate frequency table. See [Country/Region Assignments](country-region-assignments.md) for more information.

To set the channel, call the [**IAMTuner::put\_Channel**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-put_channel) method. The argument to this method is actually not a channel number, but rather an index into the current frequency table. As described previously, the index number may or may not correspond to a channel number. The [**IAMTuner::ChannelMinMax**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-channelminmax) method returns the minimum and maximum index values for the current frequency table.

Overriding Frequency Entries

It is possible that some entries in the frequency tables might be incorrect or become obsolete. Therefore, a mechanism is provided for overriding individual entries using registry keys.

The specifics are explained in the topic [International Analog TV Tuning](international-analog-tv-tuning.md). Each registry key defines a "tuning space" which contains one or more subkeys. Each subkey overrides one frequency entry. To set the current tuning space, use the [**IAMTuner::put\_TuningSpace**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-put_tuningspace) method. Activating the tuning space overrides the frequency entries in the current frequency table. Therefore, it is up to the application to maintain a correspondence between tuning spaces and countries/regions. The best approach is simply to use the country/region identifier as the name of the tuning space.

Fine Tuning the Frequency Entries

Broadcast frequencies may be adjusted up or down several kHz by the broadcast station to reduce potential interference with neighboring channels. Given the nominal frequency, the tuner card can scan for the exact frequency. The TV Tuner filter has a mechanism for saving the adjusted frequencies in the registry.

For each entry in the frequency table, call the put\_Channel method to tune to that frequency. The tuner will scan for the most precise frequency. You can check whether the tuner achieved a horizontal lock by calling [**IAMTuner::SignalPresent**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-signalpresent). The TV Tuner filter also stores the result internally.

After scanning all of the frequencies, call the [**IAMTVTuner::StoreAutoTune**](/windows/desktop/api/Strmif/nf-strmif-iamtvtuner-storeautotune) method to write the updated values into the registry. The updated values are stored under the registry entry for the current tuning space.

## Related topics

<dl> <dt>

[Analog Television](analog-television.md)
</dt> </dl>

 

 



