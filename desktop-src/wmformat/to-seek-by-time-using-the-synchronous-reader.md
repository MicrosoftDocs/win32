---
title: To Seek By Time Using the Synchronous Reader
description: To Seek By Time Using the Synchronous Reader
ms.assetid: 143f72b0-9d71-4efa-b8d4-5cde53a2aa2a
keywords:
- Advanced Systems Format (ASF),seeking by time
- ASF (Advanced Systems Format),seeking by time
- Advanced Systems Format (ASF),synchronous readers
- ASF (Advanced Systems Format),synchronous readers
- synchronous readers,seeking by time
ms.topic: article
ms.date: 05/31/2018
---

# To Seek By Time Using the Synchronous Reader

To seek for data using the synchronous reader, you specify a range for playback. A range is defined by a starting presentation time and a duration, both in 100-nanosecond units.

To seek data in an ASF file by presentation time using the synchronous reader, perform the following steps.

1.  Specify a starting time and duration for sample delivery by calling [**IWMSyncReader::SetRange**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-setrange). This method does not require you to specify a stream number because the presentation times of each stream should already be synchronized.
2.  Begin retrieving samples with calls to [**IWMSyncReader::GetNextSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getnextsample). Proceed as you normally would with the synchronous reader.

## Related topics

<dl> <dt>

[**IWMSyncReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader)
</dt> <dt>

[**Reading Files with the Synchronous Reader**](reading-files-with-the-synchronous-reader.md)
</dt> </dl>

 

 




