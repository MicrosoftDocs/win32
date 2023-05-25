---
title: Playing Files from a Network Source
description: Playing Files from a Network Source
ms.assetid: 72f2d685-56fc-4da2-8372-3774cc65f59d
keywords:
- Windows Media Format SDK,reading ASF data
- Windows Media Format SDK,playing files from network sources
- Advanced Systems Format (ASF),reading data
- ASF (Advanced Systems Format),reading data
- Advanced Systems Format (ASF),playing files from network sources
- ASF (Advanced Systems Format),playing files from network sources
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Playing Files from a Network Source

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Reading from a network is not fundamentally different from reading a local file. The application passes the URL to the reader object's [**IWMReader::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-open) method, and the reader object handles the details of the network protocols. The reader object uses intelligent buffer management to provide the smoothest playback possible. If the application needs more control over the reader object's network settings, these are available through the [**IWMReaderNetworkConfig**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadernetworkconfig) and [**IWMReaderNetworkConfig2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadernetworkconfig2) interfaces.

Content from a network source falls into one of the following two categories:

-   Streaming. The data is transmitted just in time to be played on the local machine. Servers running Windows Media Services can provide streaming data. If multiple bit rate (MBR) content is streamed, the client can request a different bit rate from the server as streaming progresses.
-   Downloaded. All the data is transmitted as quickly as possible so that it can be saved as a file on the local machine. Web servers provide downloaded data. There is no communication from the client to the server after the download begins.

When the reader object downloads a file from a Web server, it uses a technique called progressive streaming, which allows a player to begin rendering the content before downloading is complete. Data is buffered to provide an uninterrupted flow of data to the player. Information such as the transfer rate and duration of the content is used to determine how long to buffer the data before giving it to the player.

To open a file or stream over a network, call the reader object's **IWMReader::Open** method with the appropriate URL. **Open** is an asynchronous call, so it returns immediately. When the source is ready for reading, the reader object sends a WMT\_OPENED notification to the application's [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) callback method. At this point, the application can query the reader for the delivery mode by calling [**IWMReaderAdvanced2::GetPlayMode**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-getplaymode). For network content, this method will return either WMT\_PLAY\_MODE\_DOWNLOAD, indicating downloaded content, or WMT\_PLAY\_MODE\_STREAMING, indicating streamed content.

To begin reading the file or stream, call the [**IWMReader::Start**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-start) method. The reader sends a WMT\_BUFFERING\_START notification when it starts to buffer the content, and a WMT\_BUFFERING\_STOP notification when buffering is complete. While the reader is buffering content (that is, between these two notifications), you might want to display the buffering progress to the user. The [**IWMReaderAdvanced2::GetBufferProgress**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-getbufferprogress) method returns the percentage of data that has been buffered and the estimated time that remains. For downloaded content, you can also call [**IWMReaderAdvanced2::GetDownloadProgress**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-getdownloadprogress) to get the download progress. Call these methods repeatedly to update your display, until buffering has completed. Buffering can occur again during playback, due to factors such as network congestion. If this occurs, the application receives another WMT\_BUFFERING\_START notification.

When the reader object begins to play the content, it sends a WMT\_STARTED notification. As each sample is decoded and becomes available for rendering, the reader passes it to the application through the [**IWMReaderCallback::OnSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadercallback-onsample) callback method. At this point, the process is the same as it is for local file playback. When playback stops, the reader sends a WMT\_END\_OF\_STREAMING notification.

## Related topics

<dl> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> </dl>

 

 




