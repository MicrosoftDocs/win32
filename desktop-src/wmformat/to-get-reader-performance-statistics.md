---
title: To Get Reader Performance Statistics
description: To Get Reader Performance Statistics
ms.assetid: 996abfe6-1444-48ab-8c34-ba923c4cd511
keywords:
- Advanced Systems Format (ASF),reader performance statistics
- ASF (Advanced Systems Format),reader performance statistics
- Advanced Systems Format (ASF),asynchronous readers
- ASF (Advanced Systems Format),asynchronous readers
- Advanced Systems Format (ASF),performance statistics
- ASF (Advanced Systems Format),performance statistics
- asynchronous readers,performance statistics
- performance,reader statistics
- performance,asynchronous readers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Get Reader Performance Statistics

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When reading files locally with the asynchronous reader, it is not necessary to check the performance of reading operations. If your application is reading from a streaming source however, performance statistics can be very important. Your application can respond to changes in playback performance to ensure the best possible end-user experience.

The performance information you can retrieve from the reader includes the following statistics:

-   The current bandwidth of the connection.
-   The number of packets received from the server.
-   The number of lost packets that were recovered.
-   The number of lost packets that were not recovered.
-   The percentage of the total number of packets sent that have been received.

To get reader performance statistics, perform the following steps.

1.  Before starting playback, create a [**WM\_READER\_STATISTICS**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_reader_statistics) structure. You must set the **cbSize** member to sizeof(WM\_READER\_STATISTICS).
2.  Obtain a pointer to the [**IWMReaderAdvanced**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced) interface of the reader object by calling **IWMReader::QueryInterface**.
3.  During playback, make calls to [**IWMReaderAdvanced::GetStatistics**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-getstatistics) frequently to monitor performance. Pass your **WM\_READER\_STATISTICS** structure with each call and examine the appropriate members.

## Related topics

<dl> <dt>

[**Reading Files with the Asynchronous Reader**](reading-files-with-the-asynchronous-reader.md)
</dt> </dl>

 

 




