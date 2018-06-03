---
Description: WM ASF Reader Filter
ms.assetid: e698c0da-88b2-497a-8a25-9d3b76c85a7d
title: WM ASF Reader Filter
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM ASF Reader Filter

The WM ASF Reader is a wrapper filter for the reader object provided with the Windows Media Format SDK and is the recommended source filter for file playback of Windows Media-based content and content created with any of the Microsoft MPEG-4 Encoder DMOs.



|                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**IFileSourceFilter**](/windows/desktop/api/Strmif/nn-strmif-ifilesourcefilter), [**IAMExtendedSeeking**](/windows/desktop/api/Qnetwork/nn-qnetwork-iamextendedseeking), **IServiceProvider**In addition, the filter exposes the following Windows Media Format SDK interfaces: [**IWMHeaderInfo**](https://msdn.microsoft.com/windows/desktop/649f9a73-c70a-4524-b577-366ade969f2f), [**IWMReaderAdvanced**](https://msdn.microsoft.com/windows/desktop/a7a20f87-6f21-4fe8-8889-1b6689daf833), [**IWMReaderAdvanced2**](https://msdn.microsoft.com/windows/desktop/5d741e49-9fdf-4f8d-9ea1-faaecf879be4), [**IWMDRMReader**](https://msdn.microsoft.com/windows/desktop/bf4ff0f3-1f78-43c4-be4d-c74209176e58) (through **IServiceProvider**)<br/> |
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

When the Windows Media Format SDK runtime sends [**WMT\_STATUS**](https://msdn.microsoft.com/windows/desktop/ebf77e8a-65e8-4da9-bb21-a1e2bf427bbf) messages to the WM ASF Writer filter, the filter forwards any messages related to DRM license acquisition as [**EC\_WMT\_EVENT**](ec-wmt-event.md) events. For more information, see [Reading DRM-Protected ASF Files in DirectShow](reading-drm-protected-asf-files-in-directshow.md).

The WM ASF Reader partially implements the [**IWMReaderAdvanced**](https://msdn.microsoft.com/windows/desktop/a7a20f87-6f21-4fe8-8889-1b6689daf833) and [**IWMReaderAdvanced2**](https://msdn.microsoft.com/windows/desktop/5d741e49-9fdf-4f8d-9ea1-faaecf879be4) interfaces in order to give applications access to the informational methods on the reader object. The filter's implementation simply passes the calls through to the interface on the reader object. The streaming methods are not implemented because the filter must have complete control over the streaming process. The following methods are implemented:

-   [**IWMReaderAdvanced::GetStatistics**](https://msdn.microsoft.com/windows/desktop/9ed2a3fe-c31d-42fc-9ee9-27dd9aef7e06)
-   [**IWMReaderAdvanced::SetClientInfo**](https://msdn.microsoft.com/windows/desktop/dec93690-8285-4672-bf70-63f3c10294bf)
-   [**IWMReaderAdvanced2::GetBufferProgress**](https://msdn.microsoft.com/windows/desktop/e0419f53-9962-4d81-9153-0538c60861eb)
-   [**IWMReaderAdvanced2::GetDownloadProgress**](https://msdn.microsoft.com/windows/desktop/06bff83f-c3f2-4eca-85dd-7e7b93cfd73d)
-   [**IWMReaderAdvanced2::GetPlayMode**](https://msdn.microsoft.com/windows/desktop/45c7e2c2-fff4-41a9-b5ce-76d8d6257e77)
-   [**IWMReaderAdvanced2::GetProtocolName**](https://msdn.microsoft.com/windows/desktop/056d5f3f-79bf-4e21-9f2c-cda05eaca13d)
-   [**IWMReaderAdvanced2::SetLogClientID**](https://msdn.microsoft.com/windows/desktop/818b7a0e-bbf4-42b2-a5a4-75078834c9f6)
-   [**IWMReaderAdvanced2::SetPlayMode**](https://msdn.microsoft.com/windows/desktop/d1b20a0c-fedf-46d4-a76b-7596dcf8fcf8)

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)
</dt> </dl>

 

 




