---
title: WM ASF Reader Filter (Windows Media Format 11 SDK)
description: Learn about WM ASF Reader filter for the Windows Media Format 11 SDK. Review filter information and see related topics.
ms.assetid: 3d5ca88a-86bd-4d84-b4f4-782564ced58d
keywords:
- Windows Media Format SDK,WM ASF Reader
- DirectShow,WM ASF Reader
- QASF filters,WM ASF Reader
- WM ASF Reader
- Advanced Systems Format (ASF),WM ASF Reader
- ASF (Advanced Systems Format),WM ASF Reader
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WM ASF Reader Filter (Windows Media Format 11 SDK)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When given the name of an ASF file or a URL, the WM ASF Reader reads the compressed content, parses the streams, and exposes an output pin for each one. This filter connects downstream to the Windows Media Audio or Windows Media Video DMOs, which do the decompression. Seeking is supported if the ASF file is seekable. The WM ASF Reader applies time stamps to the media samples based on the time stamp in the ASF file, but it does not modify the time stamps in any way. Internally, the filter uses the Windows Media Format reader object to read the Windows Media–based content.

> [!Note]  
> In the DirectX SDK, this filter is not the default source filter for ASF files, so with that SDK you cannot use this filter with the **RenderFile** method; you must explicitly add it to the filter graph by using its class identifier (CLSID). This behavior is different with the Windows Media Format SDK. When you install the Windows Media Format SDK runtime libraries, the WM ASF Reader is registered as the default filter for ASF files.

 

The following table contains information about the WM ASF Reader filter, such as the interfaces and media types it supports.



|  Filter Information                      |  Types                                                                                                                                                                                                                                             |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter interfaces      | **IBaseFilter**, **IFileSourceFilter**, **IServiceProvider**, **IWMHeaderInfo**, **IWMReaderAdvanced** (partially implemented. See Remarks.), **IWMReaderAdvanced2** (partially implemented), **IWMDRMReader** (through **IServiceProvider**) |
| Input pin media types  | Not applicable                                                                                                                                                                                                                                |
| Input pin interfaces   | Not applicable                                                                                                                                                                                                                                |
| Output pin media types | MEDIATYPE\_Video, MEDIATYPE\_Audio, MEDIATYPE\_ScriptCommand, MEDIATYPE\_FileTransfer                                                                                                                                                         |
| Format type            | **VIDEOINFOHEADER2** if content is [*interlaced*](wmformat-glossary.md), otherwise **VIDEOINFOHEADER**                                                                                                                    |
| Output pin interfaces  | **IMediaSeeking**, **IAMWMBufferPass**, **IServiceProvider**, **IWMStreamConfig2** (through **IServiceProvider**)                                                                                                                             |
| Filter CLSID           | CLSID\_WMAsfReader                                                                                                                                                                                                                            |
| Property Page CLSID    | No property page                                                                                                                                                                                                                              |
| Executable             | Qasf.dll                                                                                                                                                                                                                                      |
| Merit                  | MERIT\_UNLIKELY                                                                                                                                                                                                                               |
| Filter Category        | CLSID\_LegacyAmFilterCategory                                                                                                                                                                                                                 |



 

## Remarks

The WM ASF Reader partially implements the **IWMReaderAdvanced** and **IWMReaderAdvanced2** interfaces in order to give applications access to the informational methods on the reader object. The filter's implementation simply passes the calls through to the interface on the reader object. The streaming methods are not implemented because the filter must have complete control over the streaming process. The following **IWMReaderAdvanced** and **IWMReaderAdvanced2** methods are implemented:

-   [**IWMReaderAdvanced::GetStatistics**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-getstatistics)
-   [**IWMReaderAdvanced::SetClientInfo**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-setclientinfo)
-   [**IWMReaderAdvanced2::GetBufferProgress**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-getbufferprogress)
-   [**IWMReaderAdvanced2::GetDownloadProgress**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-getdownloadprogress)
-   [**IWMReaderAdvanced2::GetPlayMode**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-getplaymode)
-   [**IWMReaderAdvanced2::GetProtocolName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-getprotocolname)
-   [**IWMReaderAdvanced2::SetLogClientID**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-setlogclientid)
-   [**IWMReaderAdvanced2::SetPlayMode**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-setplaymode)

## Related topics

<dl> <dt>

[**DirectShow QASF Reference**](directshow-qasf-reference.md)
</dt> <dt>

[**Reading ASF Files in DirectShow**](reading-asf-files-in-directshow.md)
</dt> </dl>

 

 




