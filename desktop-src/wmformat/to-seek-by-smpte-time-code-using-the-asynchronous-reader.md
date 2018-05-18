---
title: To Seek By SMPTE Time Code Using the Asynchronous Reader
description: To Seek By SMPTE Time Code Using the Asynchronous Reader
ms.assetid: '5c618f04-3761-418c-b75a-70c7bf7fa5be'
keywords: ["Advanced Systems Format (ASF),seeking by SMPTE time codes", "ASF (Advanced Systems Format),seeking by SMPTE time codes", "Advanced Systems Format (ASF),asynchronous readers", "ASF (Advanced Systems Format),asynchronous readers", "Advanced Systems Format (ASF),SMPTE time codes", "ASF (Advanced Systems Format),SMPTE time codes", "asynchronous readers,seeking by SMPTE time codes", "asynchronous readers,SMPTE time codes", "SMPTE time codes,seeking", "SMPTE time codes,asynchronous readers"]
---

# To Seek By SMPTE Time Code Using the Asynchronous Reader

The reader object can seek to a point in a file based on the SMPTE time code associated with a video stream. Time code data is encapsulated in [**WMT\_TIMECODE\_EXTENSION\_DATA**](wmt-timecode-extension-data.md) structures that are attached to video samples as data unit extensions.

SMPTE time codes are defined by a range and a time code within that range. A range is a continuous series of time codes. Each time code is defined by hours, minutes, seconds, and frames.

To seek data in an ASF file by SMPTE time code using the asynchronous reader, perform the following steps.

1.  Obtain a pointer to the [**IWMReaderAdvanced3**](iwmreaderadvanced3.md) interface of the reader object by calling **IWMReader::QueryInterface**.
2.  Set the starting time code and duration by calling [**IWMReaderAdvanced3::StartAtPosition**](iwmreaderadvanced3-startatposition.md). You must specify the stream number of a video stream that is indexed by time code. The reader will synchronize the rest of the outputs to the presentation time of the specified frame of the specified stream and begin delivering output samples.
3.  Handle the samples as you normally would in your implementation of the **IWMReaderCallback::OnSample** method.

## Related topics

<dl> <dt>

[**Reading Files with the Asynchronous Reader**](reading-files-with-the-asynchronous-reader.md)
</dt> <dt>

[**Working with Indexes**](working-with-indexes.md)
</dt> <dt>

[**SMPTE Time Code Support**](smpte-time-code-support.md)
</dt> </dl>

 

 




