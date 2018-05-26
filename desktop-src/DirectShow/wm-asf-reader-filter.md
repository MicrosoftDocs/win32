---
Description: WM ASF Reader Filter
ms.assetid: e698c0da-88b2-497a-8a25-9d3b76c85a7d
title: WM ASF Reader Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM ASF Reader Filter

The WM ASF Reader is a wrapper filter for the reader object provided with the Windows Media Format SDK and is the recommended source filter for file playback of Windows Media-based content and content created with any of the Microsoft MPEG-4 Encoder DMOs.



|                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter interfaces                        | [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), [**IFileSourceFilter**](/windows/win32/Strmif/nn-strmif-ifilesourcefilter?branch=master), [**IAMExtendedSeeking**](/windows/win32/Qnetwork/nn-qnetwork-iamextendedseeking?branch=master), **IServiceProvider**In addition, the filter exposes the following Windows Media Format SDK interfaces: [**IWMHeaderInfo**](wmformat.iwmheaderinfo), [**IWMReaderAdvanced**](wmformat.iwmreaderadvanced), [**IWMReaderAdvanced2**](wmformat.iwmreaderadvanced2), [**IWMDRMReader**](wmformat.iwmdrmreader) (through **IServiceProvider**)<br/> |
| Input pin media types                    | Not applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Input pin interfaces                     | Not applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output pin media types                   | MEDIATYPE\_Video, MEDIATYPE\_Audio, MEDIATYPE\_ScriptCommand, MEDIATYPE\_FileTransfer                                                                                                                                                                                                                                                                                                                                                                                                     |
| Output pin interfaces                    | [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [**IAMWMBufferPass**](/windows/win32/Dshowasf/nn-dshowasf-iamwmbufferpass?branch=master), **IServiceProvider**In addition, the pins expose the following Windows Media Format SDK interfaces: **IWMStreamConfig2** (through **IServiceProvider**)<br/>                                                                                                                                                                                                                                    |
| Filter CLSID                             | CLSID\_WMAsfReader                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Property Page CLSID                      | No property page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Executable                               | Qasf.dll                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Merit](merit.md)                       | MERIT\_UNLIKELY                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                                                                                                                                                                                                                                                                                                                                                             |



 

## Remarks

When given the name of an ASF file or a URL, the WM ASF Reader reads the compressed content, parses the compressed streams, and exposes an output pin for each one. This filter connects downstream to audio and/or video codecs filters, which do the decompression. Seeking is supported if the ASF file is seekable. The ASF Reader time stamps the samples before sending them downstream, but it does not modify the time stamps in any way.

Playback at speeds other than 1.0 (as specified in [**IMediaSeeking::SetRate**](/windows/win32/Strmif/nf-strmif-imediaseeking-setrate?branch=master)) is not supported.

When the Windows Media Format SDK runtime sends [**WMT\_STATUS**](wmformat.wmt_status) messages to the WM ASF Writer filter, the filter forwards any messages related to DRM license acquisition as [**EC\_WMT\_EVENT**](ec-wmt-event.md) events. For more information, see [Reading DRM-Protected ASF Files in DirectShow](reading-drm-protected-asf-files-in-directshow.md).

The WM ASF Reader partially implements the [**IWMReaderAdvanced**](wmformat.iwmreaderadvanced) and [**IWMReaderAdvanced2**](wmformat.iwmreaderadvanced2) interfaces in order to give applications access to the informational methods on the reader object. The filter's implementation simply passes the calls through to the interface on the reader object. The streaming methods are not implemented because the filter must have complete control over the streaming process. The following methods are implemented:

-   [**IWMReaderAdvanced::GetStatistics**](wmformat.iwmreaderadvanced_getstatistics)
-   [**IWMReaderAdvanced::SetClientInfo**](wmformat.iwmreaderadvanced_setclientinfo)
-   [**IWMReaderAdvanced2::GetBufferProgress**](wmformat.iwmreaderadvanced2_getbufferprogress)
-   [**IWMReaderAdvanced2::GetDownloadProgress**](wmformat.iwmreaderadvanced2_getdownloadprogress)
-   [**IWMReaderAdvanced2::GetPlayMode**](wmformat.iwmreaderadvanced2_getplaymode)
-   [**IWMReaderAdvanced2::GetProtocolName**](wmformat.iwmreaderadvanced2_getprotocolname)
-   [**IWMReaderAdvanced2::SetLogClientID**](wmformat.iwmreaderadvanced2_setlogclientid)
-   [**IWMReaderAdvanced2::SetPlayMode**](wmformat.iwmreaderadvanced2_setplaymode)

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)
</dt> </dl>

 

 




