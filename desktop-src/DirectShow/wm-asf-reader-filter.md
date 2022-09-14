---
description: Learn about the WM ASF Reader filter for DirectShow. This is a wrapper filter for the reader object that's provided with the Windows Media Format SDK.
ms.assetid: '82b9f849-b9dc-439b-8ca7-9dcd992338ab'
title: WM ASF Reader Filter (DirectShow)
ms.topic: article
ms.date: 05/31/2018
---

# WM ASF Reader Filter (DirectShow)

The WM ASF Reader is a wrapper filter for the reader object provided with the Windows Media Format SDK and is the recommended source filter for file playback of Windows Media-based content and content created with any of the Microsoft MPEG-4 Encoder DMOs.



| Label | Value |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter interfaces                        | [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**IFileSourceFilter**](/windows/desktop/api/Strmif/nn-strmif-ifilesourcefilter), [**IAMExtendedSeeking**](/previous-versions/windows/desktop/api/Qnetwork/nn-qnetwork-iamextendedseeking), **IServiceProvider**In addition, the filter exposes the following Windows Media Format SDK interfaces: [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo), [**IWMReaderAdvanced**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced), [**IWMReaderAdvanced2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2), [**IWMDRMReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader) (through **IServiceProvider**)<br/> |
| Input pin media types                    | Not applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Input pin interfaces                     | Not applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output pin media types                   | MEDIATYPE\_Video, MEDIATYPE\_Audio, MEDIATYPE\_ScriptCommand, MEDIATYPE\_FileTransfer                                                                                                                                                                                                                                                                                                                                                                                                     |
| Output pin interfaces                    | [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [**IAMWMBufferPass**](/previous-versions/windows/desktop/api/Dshowasf/nn-dshowasf-iamwmbufferpass), **IServiceProvider**In addition, the pins expose the following Windows Media Format SDK interfaces: **IWMStreamConfig2** (through **IServiceProvider**)<br/>                                                                                                                                                                                                                                    |
| Filter CLSID                             | CLSID\_WMAsfReader                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Property Page CLSID                      | No property page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Executable                               | Qasf.dll                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Merit](merit.md)                       | MERIT\_UNLIKELY                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Filter Category](filter-categories.md) | CLSID\_LegacyAmFilterCategory                                                                                                                                                                                                                                                                                                                                                                                                                                                             |



 

## Remarks

When given the name of an ASF file or a URL, the WM ASF Reader reads the compressed content, parses the compressed streams, and exposes an output pin for each one. This filter connects downstream to audio and/or video codecs filters, which do the decompression. Seeking is supported if the ASF file is seekable. The ASF Reader time stamps the samples before sending them downstream, but it does not modify the time stamps in any way.

Playback at speeds other than 1.0 (as specified in [**IMediaSeeking::SetRate**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setrate)) is not supported.

When the Windows Media Format SDK runtime sends [**WMT\_STATUS**](/previous-versions/windows/desktop/api/wmsdkidl/ne-wmsdkidl-wmt_status) messages to the WM ASF Writer filter, the filter forwards any messages related to DRM license acquisition as [**EC\_WMT\_EVENT**](ec-wmt-event.md) events. For more information, see [Reading DRM-Protected ASF Files in DirectShow](reading-drm-protected-asf-files-in-directshow.md).

The WM ASF Reader partially implements the [**IWMReaderAdvanced**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced) and [**IWMReaderAdvanced2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2) interfaces in order to give applications access to the informational methods on the reader object. The filter's implementation simply passes the calls through to the interface on the reader object. The streaming methods are not implemented because the filter must have complete control over the streaming process. The following methods are implemented:

-   [**IWMReaderAdvanced::GetStatistics**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-getstatistics)
-   [**IWMReaderAdvanced::SetClientInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-setclientinfo)
-   [**IWMReaderAdvanced2::GetBufferProgress**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-getbufferprogress)
-   [**IWMReaderAdvanced2::GetDownloadProgress**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-getdownloadprogress)
-   [**IWMReaderAdvanced2::GetPlayMode**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-getplaymode)
-   [**IWMReaderAdvanced2::GetProtocolName**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-getprotocolname)
-   [**IWMReaderAdvanced2::SetLogClientID**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-setlogclientid)
-   [**IWMReaderAdvanced2::SetPlayMode**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-setplaymode)

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)
</dt> </dl>

 

 
