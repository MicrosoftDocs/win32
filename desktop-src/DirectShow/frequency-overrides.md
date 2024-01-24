---
description: Frequency Overrides
ms.assetid: 0e45d0a6-3c3e-462c-a8dc-c4f25b614b85
title: Frequency Overrides
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Frequency Overrides

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A significant amount of effort was spent to ensure that the broadcast frequencies and color standard assignments are correct for each country/region. Even so, there will be situations when the frequency tables are not sufficient, contain errors, or become obsolete. To address this problem, the frequencies listed in the TV Tuner filter's frequency tables may be selectively overridden, by using the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**TV System Services**\\**TVAutoTune**\\**TS0-1**

> [!Note]  
> Starting in Windows 7, the following redirected registry key is used for x86 applications running on x64 versions of Windows:

 

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Wow6432Node**\\**Microsoft**\\**TV System Services**\\**TVAutoTune**\\**TS0-1**

Frequency overrides are grouped into application-defined "tuning spaces," which are identified by number. The following example shows an example override:

``` syntax
HKEY_LOCAL_MACHINE\Software\Microsoft\TV System Services\TVAutoTune\TS0-1
"12"=dword:04022750
```

In this case, "TS0-1" indicates Tuning Space 0 for cable frequencies. The first number identifies the tuning space. The second number is either 0 for broadcast frequencies or 1 for cable frequencies.

The subkey named "12" overrides the frequency value for the frequency at index 12 in the current frequency table. The value of the subkey is a **DWORD** that specifies the frequency in Hertz (Hz). In this example, the frequency is set to 67.25 MHz. Overrides can be defined for any channel numbers in the range of 1 to 999, inclusive. If the tuning hardware does not support a given frequency, the tune request will fail.

This mechanism can also be used to create new channel numbers outside the existing range in the frequency table. The [**IAMTuner::ChannelMinMax**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-channelminmax) method will return the extended channel range. For example, if the original channel range was 1 to 158, and a channel override of "200" is added to the registry, the **ChannelMinMax** method will return 200 as the maximum channel. In this case, channel numbers in the range of 159 to 199 will have no frequencies assigned to them, so any tuning requests in that range will automatically fail.

The [**IAMTuner::put\_TuningSpace**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-put_tuningspace) method allows the application to choose which set of overrides and fine-tuning information to use. Tuning space numbers are arbitrary. It is the application's responsibility to maintain the relationship between the tuning space and the frequency table. The most straightforward approach is to use the country/region code as the tuning space number. Then, every time the application switches to a new country/region code, it also switches to the same tuning space (in that order).

## Related topics

<dl> <dt>

[International Analog TV Tuning](international-analog-tv-tuning.md)
</dt> </dl>

 

 



