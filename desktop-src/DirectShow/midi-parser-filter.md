---
Description: MIDI Parser Filter
ms.assetid: a56576ad-f949-48fa-85e0-3e9898d2970d
title: MIDI Parser Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MIDI Parser Filter

The MIDI Parser filter reads MIDI data that is found in .MID and .RMI files. The filter accepts a stream from the [Async File Source](file-source--async--filter.md) or [URL File Source](file-source--url--filter.md) filters and outputs MIDI samples to the [**MIDI Renderer**](midi-renderer-filter.md) for playback.



|                                          |                                                                                                          |
|------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMMediaContent**](/windows/win32/Qnetwork/nn-qnetwork-iammediacontent?branch=master), [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master)                           |
| Input Pin Media Types                    | MEDIATYPE\_Stream, MEDIASUBTYPE\_Midi                                                                    |
| Input Pin Interfaces                     | [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)                                         |
| Output Pin Media Types                   | MEDIATYPE\_Midi, MEDIASUBTYPE\_NULL                                                                      |
| Output Pin Interfaces                    | [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master) |
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

 

 



