---
title: To Seek By SMPTE Time Code Using the Asynchronous Reader
description: To Seek By SMPTE Time Code Using the Asynchronous Reader
ms.assetid: 5c618f04-3761-418c-b75a-70c7bf7fa5be
keywords:
- Advanced Systems Format (ASF),seeking by SMPTE time codes
- ASF (Advanced Systems Format),seeking by SMPTE time codes
- Advanced Systems Format (ASF),asynchronous readers
- ASF (Advanced Systems Format),asynchronous readers
- Advanced Systems Format (ASF),SMPTE time codes
- ASF (Advanced Systems Format),SMPTE time codes
- asynchronous readers,seeking by SMPTE time codes
- asynchronous readers,SMPTE time codes
- SMPTE time codes,seeking
- SMPTE time codes,asynchronous readers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Seek By SMPTE Time Code Using the Asynchronous Reader

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The reader object can seek to a point in a file based on the SMPTE time code associated with a video stream. Time code data is encapsulated in [**WMT\_TIMECODE\_EXTENSION\_DATA**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_timecode_extension_data) structures that are attached to video samples as data unit extensions.

SMPTE time codes are defined by a range and a time code within that range. A range is a continuous series of time codes. Each time code is defined by hours, minutes, seconds, and frames.

To seek data in an ASF file by SMPTE time code using the asynchronous reader, perform the following steps.

1.  Obtain a pointer to the [**IWMReaderAdvanced3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced3) interface of the reader object by calling **IWMReader::QueryInterface**.
2.  Set the starting time code and duration by calling [**IWMReaderAdvanced3::StartAtPosition**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced3-startatposition). You must specify the stream number of a video stream that is indexed by time code. The reader will synchronize the rest of the outputs to the presentation time of the specified frame of the specified stream and begin delivering output samples.
3.  Handle the samples as you normally would in your implementation of the **IWMReaderCallback::OnSample** method.

## Related topics

<dl> <dt>

[**Reading Files with the Asynchronous Reader**](reading-files-with-the-asynchronous-reader.md)
</dt> <dt>

[**Working with Indexes**](working-with-indexes.md)
</dt> <dt>

[**SMPTE Time Code Support**](smpte-time-code-support.md)
</dt> </dl>

 

 




