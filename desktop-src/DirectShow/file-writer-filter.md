---
Description: File Writer Filter
ms.assetid: 2bfbea8a-679f-4656-9ff3-fdf34aa0eb26
title: File Writer Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# File Writer Filter

The File Writer filter can be used to write files to disc regardless of format. The filter simply writes to disc whatever it receives on its input pin, so it must be connected upstream to a multiplexer that can format the file correctly. You can create a new output file with the File Writer or specify an existing file; if the file already exists, it will be completely overwritten with the new data.

The file writer filter uses the input stream's time stamps as file offsets and provides random access to the file. It supports **IStream** to allow reading and writing the file header after the graph is stopped. To improve performance it also supports unbuffered overlapped writes and handles the corresponding buffer negotiation.

> [!Note]  
> To write ASF files, use the [WM ASF Writer](wm-asf-writer-filter.md) filter.

 



|                                          |                                                                                                                                                                                                    |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMFilterMiscFlags**](/windows/win32/Strmif/nn-strmif-iamfiltermiscflags?branch=master), [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), [**IFileSinkFilter**](/windows/win32/Strmif/nn-strmif-ifilesinkfilter?branch=master), [**IFileSinkFilter2**](/windows/win32/Strmif/nn-strmif-ifilesinkfilter2?branch=master), **IPersistStream** |
| Input Pin Media Types                    | MEDIATYPE\_Stream, MEDIASUBTYPE\_NULL                                                                                                                                                              |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master), **IStream**                                                                                |
| Output Pin Media Types                   | Not applicable                                                                                                                                                                                     |
| Output Pin Interfaces                    | Not applicable                                                                                                                                                                                     |
| Filter CLSID                             | CLSID\_FileWriter                                                                                                                                                                                  |
| Property Page CLSID                      | No property page                                                                                                                                                                                   |
| Executable                               | qcap.dll                                                                                                                                                                                           |
| [Merit](merit.md)                       | MERIT\_DO\_NOT\_USE                                                                                                                                                                                |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                                                                      |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



