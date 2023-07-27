---
description: Frequency Tables
ms.assetid: 58a680ea-1f88-4900-8820-c30a2f3e3901
title: Frequency Tables
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Frequency Tables

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The TV Tuner filter (kstvtune.ax) has an internal list of frequency tables. Each frequency table contains a list of frequencies, and corresponds to the broadcast or cable frequencies for a given country/region. An application tunes to a particular frequency by calling the [**IAMTuner::put\_Channel**](/windows/desktop/api/Strmif/nf-strmif-iamtuner-put_channel) method with the index of the desired frequency.

For some countries/regions, the index numbers of the frequency tables map directly to channel numbers. Fixed channel numbers are not appropriate for all markets, however. For instance, the European channel numbers are not actually used by consumers. Instead, consumers expect to choose and assign their own channel numbers for the frequencies that are used by the broadcast or cable operators in their area. For these countries/regions, applications should not expose the index numbers directly to the user. Instread, the application should keep an internal mapping between channel numbers (presented to the user) and frequency indexes (for tuning).

Most non-US cable operators are free to broadcast on frequencies of their choosing, often mixing frequencies from different standards into the same channel lineup. Therefore, a "Unicable" frequency table is used for any country/region that lacks a standard cable channel standards authority. Also, a mechanism is provided to override individual frequencies in the frequency tables. This mechanism is described in the following section, [Frequency Overrides](frequency-overrides.md).

## Related topics

<dl> <dt>

[International Analog TV Tuning](international-analog-tv-tuning.md)
</dt> </dl>

 

 



