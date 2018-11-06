---
Description: WM ASF Reader Filter
ms.assetid: '82b9f849-b9dc-439b-8ca7-9dcd992338ab'
title: WM ASF Reader Filter
ms.topic: article
ms.date: 05/31/2018
---

# WM ASF Reader Filter

The WM ASF Reader is a wrapper filter for the reader object provided with the Windows Media Format SDK and is the recommended source filter for file playback of Windows Media-based content and content created with any of the Microsoft MPEG-4 Encoder DMOs.



|                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**IFileSourceFilter**](/windows/desktop/api/Strmif/nn-strmif-ifilesourcefilter), [**IAMExtendedSeeking**](/windows/desktop/api/Qnetwork/nn-qnetwork-iamextendedseeking), **IServiceProvider**In addition, the filter exposes the following Windows Media Format SDK interfaces: [**IWMHeaderInfo**](https://msdn.microsoft.com/en-us/library/Dd798504(v=VS.85).aspx), [**IWMReaderAdvanced**](https://msdn.microsoft.com/en-us/library/Dd757429(v=VS.85).aspx), [**IWMReaderAdvanced2**](https://msdn.microsoft.com/en-us/library/Dd757430(v=VS.85).aspx), [**IWMDRMReader**](https://msdn.microsoft.com/en-us/library/Dd798339(v=VS.85).aspx) (through **IServiceProvider**)<br/> |
| Input pin media types                    | Not applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Input pin interfaces                     | Not applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output pin media types                   | MEDIATYPE\_Video, MEDIATYPE\_Audio, MEDIATYPE\_ScriptCommand, MEDIATYPE\_FileTransfer                                                                                                                                                                                                                                                                                                                                                                                                     |
| Output pin interfaces                    | [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [**IAMWMBufferPass**](/windows/desktop/api/Dshowasf/nn-dshowasf-iamwmbufferpass), **IServiceProvider**In addition, the pins expose the following Windows Media Format SDK interfaces: **IWMStreamConfig2** (through **IServiceProvider**)<br/>                                                                                                                                                                                                                                    |
| Filter CLSID                             | CLSID\_WMAsfReader                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Property Page CLSID                      | No property page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Executable                               | Qasf.dll                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Merit](merit.md)                       | MERIT\_UNLIKELY                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                                                                                                                                                                                                                                                                                                                                                             |



 

## Remarks

When given the name of an ASF file or a URL, the WM ASF Reader reads the compressed content, parses the compressed streams, and exposes an output pin for each one. This filter connects downstream to audio and/or video codecs filters, which do the decompression. Seeking is supported if the ASF file is seekable. The ASF Reader time stamps the samples before sending them downstream, but it does not modify the time stamps in any way.

Playback at speeds other than 1.0 (as specified in [**IMediaSeeking::SetRate**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setrate)) is not supported.

When the Windows Media Format SDK runtime sends [**WMT\_STATUS**](https://msdn.microsoft.com/en-us/library/Dd757854(v=VS.85).aspx) messages to the WM ASF Writer filter, the filter forwards any messages related to DRM license acquisition as [**EC\_WMT\_EVENT**](ec-wmt-event.md) events. For more information, see [Reading DRM-Protected ASF Files in DirectShow](reading-drm-protected-asf-files-in-directshow.md).

The WM ASF Reader partially implements the [**IWMReaderAdvanced**](https://msdn.microsoft.com/en-us/library/Dd757429(v=VS.85).aspx) and [**IWMReaderAdvanced2**](https://msdn.microsoft.com/en-us/library/Dd757430(v=VS.85).aspx) interfaces in order to give applications access to the informational methods on the reader object. The filter's implementation simply passes the calls through to the interface on the reader object. The streaming methods are not implemented because the filter must have complete control over the streaming process. The following methods are implemented:

-   [**IWMReaderAdvanced::GetStatistics**](https://msdn.microsoft.com/en-us/library/Dd743477(v=VS.85).aspx)
-   [**IWMReaderAdvanced::SetClientInfo**](https://msdn.microsoft.com/en-us/library/Dd743483(v=VS.85).aspx)
-   [**IWMReaderAdvanced2::GetBufferProgress**](https://msdn.microsoft.com/en-us/library/Dd757431(v=VS.85).aspx)
-   [**IWMReaderAdvanced2::GetDownloadProgress**](https://msdn.microsoft.com/en-us/library/Dd757432(v=VS.85).aspx)
-   [**IWMReaderAdvanced2::GetPlayMode**](https://msdn.microsoft.com/en-us/library/Dd757435(v=VS.85).aspx)
-   [**IWMReaderAdvanced2::GetProtocolName**](https://msdn.microsoft.com/en-us/library/Dd757436(v=VS.85).aspx)
-   [**IWMReaderAdvanced2::SetLogClientID**](https://msdn.microsoft.com/en-us/library/Dd757441(v=VS.85).aspx)
-   [**IWMReaderAdvanced2::SetPlayMode**](https://msdn.microsoft.com/en-us/library/Dd757443(v=VS.85).aspx)

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)
</dt> </dl>

 

 




