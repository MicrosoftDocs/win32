---
title: To Use Manual Stream Selection
description: To Use Manual Stream Selection
ms.assetid: 49ec283f-670a-4a0e-9477-c60a80919a1e
keywords:
- Advanced Systems Format (ASF),manual stream selection
- ASF (Advanced Systems Format),manual stream selection
- Advanced Systems Format (ASF),asynchronous readers
- ASF (Advanced Systems Format),asynchronous readers
- Advanced Systems Format (ASF),stream selection
- ASF (Advanced Systems Format),stream selection
- Advanced Systems Format (ASF),mutual exclusion
- ASF (Advanced Systems Format),mutual exclusion
- asynchronous readers,manual stream selection
- asynchronous readers,stream selection
- streams,manual selection
- mutual exclusion,manual stream selection
- streams,asynchronous readers
- mutual exclusion,asynchronous readers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Use Manual Stream Selection

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When delivering uncompressed samples with the reader object, you can deliver them only by output number. In the case of mutually exclusive streams, this means that you can receive samples only from one stream in the mutual exclusion at a time. The process of choosing which mutually exclusive stream to deliver is called stream selection.

For bit-rate mutual exclusion, the reader makes stream selections automatically based on the conditions on the host machine at playback. For other types of mutual exclusion, the reader will deliver samples from the default stream unless you manually select a different stream yourself. There may also be instances when you want to select a stream manually from a bit-rate mutual exclusion.

Manual stream selection is either on or off for the entire file. If a file contains bit-rate mutual exclusion and some other mutual exclusion type, you must select the bit rate based streams manually.

To select a mutually exclusive stream manually, you must perform the following steps.

1.  Retrieve a pointer to the [**IWMReaderAdvanced**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced) interface of the reader object by calling **IWMReader::QueryInterface**.
2.  Enable manual stream selection by calling [**IWMReaderAdvanced::SetManualStreamSelection**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-setmanualstreamselection).
3.  To find out if a particular stream is selected, call [**IWMReaderAdvanced::GetStreamSelected**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-getstreamselected). You must pass a pointer to a variable of the [**WMT\_STREAM\_SELECTION**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_stream_selection) enumeration type. When the call returns, the value in the variable will describe the current selection type of the stream.
4.  To select a stream, call [**IWMReaderAdvanced::SetStreamsSelected**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-setstreamsselected). This method enables you to specify multiple streams at the same time for synchronized stream switching.

## Related topics

<dl> <dt>

[**Reading Files with the Asynchronous Reader**](reading-files-with-the-asynchronous-reader.md)
</dt> </dl>

 

 




