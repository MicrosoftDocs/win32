---
description: File Writer Filter
ms.assetid: 2bfbea8a-679f-4656-9ff3-fdf34aa0eb26
title: File Writer Filter
ms.topic: article
ms.date: 05/31/2018
---

# File Writer Filter

The File Writer filter can be used to write files to disc regardless of format. The filter simply writes to disc whatever it receives on its input pin, so it must be connected upstream to a multiplexer that can format the file correctly. You can create a new output file with the File Writer or specify an existing file; if the file already exists, it will be completely overwritten with the new data.

The file writer filter uses the input stream's time stamps as file offsets and provides random access to the file. It supports **IStream** to allow reading and writing the file header after the graph is stopped. To improve performance it also supports unbuffered overlapped writes and handles the corresponding buffer negotiation.

> [!Note]  
> To write ASF files, use the [WM ASF Writer](wm-asf-writer-filter.md) filter.

 



| Label | Value |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMFilterMiscFlags**](/windows/desktop/api/Strmif/nn-strmif-iamfiltermiscflags), [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**IFileSinkFilter**](/windows/desktop/api/Strmif/nn-strmif-ifilesinkfilter), [**IFileSinkFilter2**](/windows/desktop/api/Strmif/nn-strmif-ifilesinkfilter2), **IPersistStream** |
| Input Pin Media Types                    | MEDIATYPE\_Stream, MEDIASUBTYPE\_NULL                                                                                                                                                              |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol), **IStream**                                                                                |
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

 

 



