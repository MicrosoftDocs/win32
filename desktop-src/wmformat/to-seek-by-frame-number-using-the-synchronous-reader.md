---
title: To Seek By Frame Number Using the Synchronous Reader
description: To Seek By Frame Number Using the Synchronous Reader
ms.assetid: 755e0124-de57-4699-af8e-c594567b5523
keywords:
- Advanced Systems Format (ASF),seeking by frame numbers
- ASF (Advanced Systems Format),seeking by frame numbers
- Advanced Systems Format (ASF),synchronous readers
- ASF (Advanced Systems Format),synchronous readers
- synchronous readers,seeking by frame numbers
- video streams,seeking by frame numbers
- video streams,synchronous readers
ms.topic: article
ms.date: 05/31/2018
---

# To Seek By Frame Number Using the Synchronous Reader

To seek for data by frame number using the synchronous reader, you specify a range for playback. A range is defined by a starting frame number in a specific video stream and a number of frames to play.

To seek data in an ASF file by frame number using the synchronous reader, perform the following steps.

1.  Set the starting frame number and number of frames to read for sample delivery by calling [**IWMSyncReader::SetRangeByFrame**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-setrangebyframe). You must specify the stream number of a frame-indexed video stream. The reader will synchronize the rest of the outputs to the presentation time of the specified frame of the specified stream and begin delivering output samples.
2.  Begin retrieving samples with calls to [**IWMSyncReader::GetNextSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getnextsample). Proceed as you normally would with the synchronous reader.

## Related topics

<dl> <dt>

[**IWMSyncReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader)
</dt> <dt>

[**Reading Files with the Synchronous Reader**](reading-files-with-the-synchronous-reader.md)
</dt> </dl>

 

 




