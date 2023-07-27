---
description: ASF Web Stream Playback in DirectShow
ms.assetid: c7818c62-24af-4eac-84b8-f76be4ca6c09
title: ASF Web Stream Playback in DirectShow
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ASF Web Stream Playback in DirectShow

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Microsoft DirectShow supports web streams in file playback scenarios through the [WM ASF Reader](wm-asf-reader-filter.md) filter, but you must write your own DirectShow filter to capture and persist the stream.

> [!Note]  
> To play back web streams in content that is being streamed from a server running Windows Media Services, use the Windows Media Player 9 Series ActiveX® control embedded in a web page.

 

When given a file containing streams of type WMMEDIATYPE\_FileTransfer, the WM ASF Reader will create an output pin for it. The format block will be a [**WMT\_WEBSTREAM\_FORMAT**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmt_webstream_format) structure. (This structure is documented in the Windows Media Format SDK documentation.) If no downstream filter is available that can handle that media type, then the pin will remain unconnected, but the file will still play the audio and/or video streams.

Each media sample in a web stream contains a [**WMT\_WEBSTREAM\_SAMPLE\_HEADER**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmt_webstream_sample_header) structure, which is documented in the Windows Media Format SDK documentation. The structure has a variable length depending on the length of its **wszURL** member. The pointer to the sample data initially points to this structure, and you must advance the pointer past the structure in order to access the actual data in the stream.

Your web stream handler filter should be based on the [**CBaseRenderer**](cbaserenderer.md) class. In the [**CBaseRenderer::DoRenderSample**](cbaserenderer-dorendersample.md) method, the filter will need to parse the structure for information about the web stream, and then perform the appropriate action. Typically, this will involve saving the file to disk, and then calling the [**CreateUrlCacheEntry**](/windows/desktop/api/wininet/nf-wininet-createurlcacheentrya) and [**CommitUrlCacheEntryW**](/windows/desktop/api/wininet/nf-wininet-commiturlcacheentryw) or [**CommitUrlCacheEntryA**](/windows/desktop/api/wininet/nf-wininet-commiturlcacheentrya) functions to place the files into the Internet Explorer cache. The filter must handle multipart files, that is, files that are larger than one sample, and also must handle render commands, which are specified by the **WMT\_WEBSTREAM\_SAMPLE\_HEADER.wSampleType** member. The filter sends an [**EC\_OLE\_EVENT**](ec-ole-event.md) event to the application, along with the text of the **WMT\_WEBSTREAM\_SAMPLE\_HEADER.wszURL** string which contains the name of the file to be rendered. The application then causes the browser to display the specified page. If the web stream has been authored correctly, the file should already be in the cache.

For more information on WMT\_WEBSTREAM\_FORMAT and WMT\_WEBSTREAM\_SAMPLE\_HEADER, see the Windows Media Format SDK documentation.

## Related topics

<dl> <dt>

[Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)
</dt> </dl>

 

 
