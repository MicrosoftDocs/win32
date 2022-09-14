---
title: To Retrieve Stream Samples with the Synchronous Reader
description: To Retrieve Stream Samples with the Synchronous Reader
ms.assetid: d5cc4bb7-5fcf-4e1e-80dc-f03feed4dc8a
keywords:
- Advanced Systems Format (ASF),retrieving stream samples
- ASF (Advanced Systems Format),retrieving stream samples
- Advanced Systems Format (ASF),synchronous readers
- ASF (Advanced Systems Format),synchronous readers
- synchronous readers,retrieving stream samples
- streams,retrieving samples
ms.topic: article
ms.date: 05/31/2018
---

# To Retrieve Stream Samples with the Synchronous Reader

Like the asynchronous reader, the synchronous reader can retrieve samples by stream number. Unlike the asynchronous reader, the synchronous reader can deliver stream samples either compressed or uncompressed.

To receive stream samples, perform the following steps.

1.  Any time before or during playback, call [**IWMSyncReader::SetReadStreamSamples**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-setreadstreamsamples) passing the desired stream number.
2.  Retrieve samples with continued calls to [**IWMSyncReader::GetNextSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getnextsample).

You can check whether a stream is selected for sample delivery by calling [**IWMSyncReader::GetReadStreamSamples**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getreadstreamsamples).

## Related topics

<dl> <dt>

[**IWMSyncReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader)
</dt> <dt>

[**Reading Files with the Synchronous Reader**](reading-files-with-the-synchronous-reader.md)
</dt> </dl>

 

 




