---
title: MPEG-2 Video Analyzer Filter
description: MPEG-2 Video Analyzer Filter
ms.assetid: fc3ed646-2644-4dc3-b84b-a00fef95df66
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MPEG-2 Video Analyzer Filter

This topic applies only to Windows XP Service Pack 1 or later.

The MPEG-2 Video Analyzer filter enables playback rates faster than 4x and reverse playback when the Stream Buffer Engine is streaming an MPEG-2 source. Insert this filter directly between the [MPEG-2 Demultiplexer](https://msdn.microsoft.com/library/windows/desktop/dd390715) and the [Stream Buffer Sink](stream-buffer-sink-filter.md) filter.



|                        |                                                                                                              |
|------------------------|--------------------------------------------------------------------------------------------------------------|
| Filter Interfaces      | [**IBaseFilter**](https://msdn.microsoft.com/library/windows/desktop/dd389526)                                                                         |
| Input Pin Media Types  | MEDIATYPE\_Video, MEDIASUBTYPE\_MPEG2\_VIDEO                                                                 |
| Input Pin Interfaces   | [**IMemInputPin**](https://msdn.microsoft.com/library/windows/desktop/dd407073), [**IPin**](https://msdn.microsoft.com/library/windows/desktop/dd390397), [**IQualityControl**](https://msdn.microsoft.com/library/windows/desktop/dd376912) |
| Output Pin Media Types | Must match input type.                                                                                       |
| Output Pin Interfaces  | [**IQualityControl**](https://msdn.microsoft.com/library/windows/desktop/dd376912), [**IPin**](https://msdn.microsoft.com/library/windows/desktop/dd390397)                                         |
| Filter CLSID           | CLSID\_Mpeg2VideoStreamAnalyzer                                                                              |
| Property Page CLSID    | Not applicable                                                                                               |
| Executable             | Sbe.dll                                                                                                      |
| Merit                  | MERIT\_DO\_NOT\_USE                                                                                          |
| Category               | CLSID\_LegacyAmFilterCategory                                                                                |



 

## Related topics

<dl> <dt>

[Creating Stream Buffer Graphs](creating-stream-buffer-graphs.md)
</dt> <dt>

[Stream Buffer Engine Filters](stream-buffer-engine-filters.md)
</dt> </dl>

 

 




