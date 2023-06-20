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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Retrieve Stream Samples with the Synchronous Reader

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




