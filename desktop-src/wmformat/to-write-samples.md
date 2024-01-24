---
title: To Write Samples
description: To Write Samples
ms.assetid: 9ce10a77-9e80-45e0-a7e7-2ffdf8b57773
keywords:
- Advanced Systems Format (ASF),writing samples
- ASF (Advanced Systems Format),writing samples
- Advanced Systems Format (ASF),passing samples to the writer
- ASF (Advanced Systems Format),passing samples to the writer
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Write Samples

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When you have identified and configured the inputs for the file you are writing, you can begin passing samples to the writer. You should pass samples in presentation-time order, if possible, to make the writing process more efficient.

Before passing any samples, you must set the writer to accept them by calling [**IWMWriter::BeginWriting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-beginwriting).

To pass a sample to the writer, perform the following steps:

1.  Allocate a buffer and retrieve a pointer to the [**INSSBuffer**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer) interface by calling [**IWMWriter::AllocateSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-allocatesample).
2.  Retrieve the address of the buffer created in step 1 by calling [**INSSBuffer::GetBuffer**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer-getbuffer).
3.  Copy your sample data to the buffer location, making sure that the sample passed will fit in the allocated buffer. You can use any memory copying function to copy your data. A common choice is memcpy, which is included in the standard C run-time library.
4.  Update the amount of data used in the buffer to reflect the actual size of the sample by calling [**INSSBuffer::SetLength**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer-setlength).
5.  Pass the buffer interface to the writer along with the input number and sample time using the [**IWMWriter::WriteSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-writesample) method. All audio samples for an input represent the same duration of content, so you can figure the sample time by adding the sample duration to a running total. For video, you need to calculate the time based on the frame rate.

**WriteSample** works asynchronously and might not finish writing the data from the buffer before your application is ready to call the method again. Therefore, it is important to call **AllocateSample** once for each call to **WriteSample**. However, you can release the **INSSBuffer** interface immediately after calling **WriteSample**.

When you have finished passing samples, call [**IWMWriter::EndWriting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-endwriting).

**Note** It is important that samples from all streams in the file are passed to the writer in synchronization with one another. That is, whenever possible you should pass samples to the writer in presentation-time order within the sync tolerance specified in [**IWMWriterAdvanced::SetSyncTolerance**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-setsynctolerance). Best results are achieved when data is delivered to each stream in units of one second or less.

Streams should also end at approximately the same time. For example, you should not write a file with an audio stream that is 45 seconds long and a video stream that is 50 seconds long. If you encode such a file with unaltered inputs, some of the audio data at the end of the stream will be dropped (even though it is the shorter stream). To make the file encoding work, you should add 5 seconds of silence to the audio input so that one stream does not end several seconds before another. It is not necessary for stream types with intermittent samples, like text or image streams, to be padded in this way. Script command streams should also follow all these rules.

## Related topics

<dl> <dt>

[**INSSBuffer Interface**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer)
</dt> <dt>

[**IWMWriter Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriter)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




