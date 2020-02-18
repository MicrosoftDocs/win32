---
title: To Seek By SMPTE Time Code Using the Synchronous Reader
description: To Seek By SMPTE Time Code Using the Synchronous Reader
ms.assetid: 1fd8885c-a694-43fd-b2a2-23eb0ae7ed72
keywords:
- Advanced Systems Format (ASF),seeking by SMPTE time codes
- ASF (Advanced Systems Format),seeking by SMPTE time codes
- Advanced Systems Format (ASF),synchronous readers
- ASF (Advanced Systems Format),synchronous readers
- Advanced Systems Format (ASF),SMPTE time codes
- ASF (Advanced Systems Format),SMPTE time codes
- synchronous readers,seeking by SMPTE time codes
- synchronous readers,SMPTE time codes
- SMPTE time codes,seeking
- SMPTE time codes,synchronous readers
ms.topic: article
ms.date: 05/31/2018
---

# To Seek By SMPTE Time Code Using the Synchronous Reader

The synchronous reader object can seek to a point in a file based on the SMPTE time code associated with a video stream. Time code data is encapsulated in [**WMT\_TIMECODE\_EXTENSION\_DATA**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_timecode_extension_data) structures that are attached to video samples as data unit extensions.

SMPTE time codes are defined by a range and a time code within that range. A range is a continuous series of time codes. Each time code is defined by hours, minutes, seconds, and frames.

To seek data in an ASF file by SMPTE time code using the synchronous reader, perform the following steps.

1.  Set the starting time code and ending time code for sample delivery by calling [**IWMSyncReader::SetRangeByFrame**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-setrangebyframe). You must specify the stream number of a video stream indexed by time code. The synchronous reader will synchronize the rest of the outputs to the presentation time of the specified frame of the specified stream.
2.  Begin retrieving samples with calls to [**IWMSyncReader::GetNextSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getnextsample). Proceed as you normally would with the synchronous reader.

## Related topics

<dl> <dt>

[**Reading Files with the Synchronous Reader**](reading-files-with-the-synchronous-reader.md)
</dt> <dt>

[**SMPTE Time Code Support**](smpte-time-code-support.md)
</dt> <dt>

[**Working with Indexes**](working-with-indexes.md)
</dt> </dl>

 

 




