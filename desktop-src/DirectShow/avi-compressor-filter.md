---
Description: AVI Compressor Filter
ms.assetid: 'addde51d-2982-4964-b16a-406fea89a0ce'
title: AVI Compressor Filter
---

# AVI Compressor Filter

The AVI Compressor filter enables Video Compression Manager (VCM) codecs to join a filter graph. Each codec appears as a separate instance of the filter. You cannot directly create this filter with CoCreateInstance. Instead, you must use the system device enumerator. For more information, see [Using the System Device Enumerator](using-the-system-device-enumerator.md).

The filter's input pin connects to filters that output uncompressed video data, such as video capture filters or the [AVI Splitter Filter](avi-splitter-filter.md). The filter's output pin typically connects to a MUX filter, such as the [AVI Mux Filter](avi-mux-filter.md).

If the codec supports an old-style VFW configuration dialog box or About dialog box, an application can display it using the [**IAMVfwCompressDialogs**](iamvfwcompressdialogs.md) interface.

> [!Note]  
> MPEG compressors are never implemented as VCM codecs, but only as native DirectShow filters.

 



|                                          |                                                                                                                                                                                                                                                    |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMVfwCompressDialogs**](iamvfwcompressdialogs.md), [**IBaseFilter**](ibasefilter.md), IPersistPropertyBag, ISpecifyPropertyPages                                                                                                             |
| Input Pin Media Types                    | MEDIATYPE\_Video, MEDIASUBTYPE\_NULL                                                                                                                                                                                                               |
| Input Pin Interfaces                     | [**IMemInputPin**](imeminputpin.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md)                                                                                                                                             |
| Output Pin Media Types                   | MEDIATYPE\_Video, MEDIASUBTYPE\_NULL                                                                                                                                                                                                               |
| Output Pin Interfaces                    | [**IAMStreamConfig**](iamstreamconfig.md), [**IAMVideoCompression**](iamvideocompression.md), [**IMediaPosition**](imediaposition.md), [**IMediaSeeking**](imediaseeking.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md) |
| Filter CLSID                             | Not applicable                                                                                                                                                                                                                                     |
| Property Page CLSID                      | No property page.                                                                                                                                                                                                                                  |
| Executable                               | qcap.dll                                                                                                                                                                                                                                           |
| [Merit](merit.md)                       | MERIT\_DO\_NOT\_USE                                                                                                                                                                                                                                |
| [Filter Category](filter-categories.md) | CLSID\_VideoCompressorCategory                                                                                                                                                                                                                     |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



