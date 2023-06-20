---
description: MIDI Parser Filter
ms.assetid: a56576ad-f949-48fa-85e0-3e9898d2970d
title: MIDI Parser Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MIDI Parser Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The MIDI Parser filter reads MIDI data that is found in .MID and .RMI files. The filter accepts a stream from the [Async File Source](file-source--async--filter.md) or [URL File Source](file-source--url--filter.md) filters and outputs MIDI samples to the [**MIDI Renderer**](midi-renderer-filter.md) for playback.



| Label | Value |
|------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMMediaContent**](/previous-versions/windows/desktop/api/Qnetwork/nn-qnetwork-iammediacontent), [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)                           |
| Input Pin Media Types                    | MEDIATYPE\_Stream, MEDIASUBTYPE\_Midi                                                                    |
| Input Pin Interfaces                     | [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)                                         |
| Output Pin Media Types                   | MEDIATYPE\_Midi, MEDIASUBTYPE\_NULL                                                                      |
| Output Pin Interfaces                    | [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) |
| Filter CLSID                             | CLSID\_MIDIParser                                                                                        |
| Property Page CLSID                      | No property page                                                                                         |
| Executable                               | quartz.dll                                                                                               |
| [Merit](merit.md)                       | MERIT\_UNLIKELY                                                                                          |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                            |



 

## Remarks

For more information, see [**MIDI Renderer**](midi-renderer-filter.md).

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



