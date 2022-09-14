---
title: Web Stream Playback in DirectShow
description: Web Stream Playback in DirectShow
ms.assetid: cc307c24-2bd2-43de-ba81-1cf5b05524b2
keywords:
- Windows Media Format SDK,DirectShow
- Windows Media Format SDK,Web stream playback
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- Advanced Systems Format (ASF),Web stream playback
- ASF (Advanced Systems Format),Web stream playback
- DirectShow,Web stream playback
- Web streams,DirectShow
- Web streams,playback in DirectShow
- streams,Web stream playback in DirectShow
ms.topic: article
ms.date: 05/31/2018
---

# Web Stream Playback in DirectShow

Microsoft DirectShow supports Web streams (see [Web Streams](web-streams.md) for more information) in file playback scenarios through the [WM ASF Reader](wm-asf-reader-filter.md) filter, but you must write your own DirectShow filter to capture and persist the stream.

> [!Note]  
> To play back Web streams in content that is being streamed from a server running Windows Media Services, use the Windows Media Player 9 Series ActiveX® control embedded in a Web page.

 

When given a file containing streams of type WMMEDIATYPE\_FileTransfer, the WM ASF Reader will create an output pin for it. The format block will be a [**WMT\_WEBSTREAM\_FORMAT**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_webstream_format) structure. If no downstream filter is available that can handle that media type, then the pin will remain unconnected, but the file will still play the audio and/or video streams.

It is important to understand that each media sample in a Web stream contains a [**WMT\_WEBSTREAM\_SAMPLE\_HEADER**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_webstream_sample_header) structure, which has a variable length depending on the length of its **wszURL** member. The pointer to the sample data initially points to this structure, and you must advance the pointer past the structure in order to access the actual data in the stream. Your Web stream handler filter should be based on the **CBaseRenderer** class. In the **DoRenderSample** method, the filter will need to parse the structure for information about the Web stream, and then perform the appropriate action. Typically, this will involve saving the file to disk, and then calling **CommitUrlCacheEntry** and **CreateUrlCacheEntry** to place the files into the Internet Explorer cache. The filter must handle multipart files, that is, files that are larger than one sample, and also must handle render commands, which are specified by the **WMT\_WEBSTREAM\_SAMPLE\_HEADER.wSampleType** member. The filter sends an **EC\_OLE\_EVENT** to the application, along with the text of the **WMT\_WEBSTREAM\_SAMPLE\_HEADER.wszURL** string which contains the name of the file to be rendered. The application then causes the browser to display the specified page. If the Web stream has been authored correctly, the file should already be in the cache.

For more information on **CBaseRenderer**, **DoRenderSample**, and **EC\_OLE\_EVENT**, see the DirectShow SDK documentation.

## Related topics

<dl> <dt>

[**Web Streams**](web-streams.md)
</dt> </dl>

 

 




