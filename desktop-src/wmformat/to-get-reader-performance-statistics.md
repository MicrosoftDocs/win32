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
ms.date: 05/31/2018
---

# To Get Reader Performance Statistics

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

 

 




