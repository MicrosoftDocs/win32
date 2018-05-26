---
Description: File Source (Async) Filter
ms.assetid: 0cf6e7ab-b1fe-42f9-b682-c5484ef48c71
title: File Source (Async) Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# File Source (Async) Filter

The Async File Source filter opens and reads local files of many different data formats and passes the data to a parser filter.

To download media files from the web through HTTP, use the [File Source (URL)](file-source--url--filter.md) filter. To read ASF files, use the [WM ASF Reader](wm-asf-reader-filter.md) filter.



|                                          |                                                                                                                                      |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), [**IFileSourceFilter**](/windows/win32/Strmif/nn-strmif-ifilesourcefilter?branch=master)                                                   |
| Input Pin Media Types                    | Not applicable                                                                                                                       |
| Input Pin Interfaces                     | Not applicable                                                                                                                       |
| Output Pin Media Types                   | **MEDIATYPE\_Stream**. The subtype depends on the media format. (**MEDIASUBTYPE\_NULL** if the filter doesn't recognize the format.) |
| Output Pin Interfaces                    | [**IAMAsyncReaderTimestampScaling**](/windows/win32/Strmif/nn-strmif-iamasyncreadertimestampscaling?branch=master), [**IAsyncReader**](/windows/win32/Strmif/nn-strmif-iasyncreader?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master) |
| Filter CLSID                             | **CLSID\_AsyncReader**                                                                                                               |
| Property Page CLSID                      | No property page                                                                                                                     |
| Executable                               | quartz.dll                                                                                                                           |
| [Merit](merit.md)                       | **MERIT\_UNLIKELY**                                                                                                                  |
| [Filter Category](filter-categories.md) | **CLSID\_LegacyAmFilterCategory**                                                                                                    |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



