---
title: To Retrieve Compressed Samples with the Synchronous Reader
description: To Retrieve Compressed Samples with the Synchronous Reader
ms.assetid: 1f6da1aa-c26a-486a-bb44-cc4305c71979
keywords:
- Advanced Systems Format (ASF),retrieving compressed samples
- ASF (Advanced Systems Format),retrieving compressed samples
- Advanced Systems Format (ASF),synchronous readers
- ASF (Advanced Systems Format),synchronous readers
- Advanced Systems Format (ASF),compressed samples
- ASF (Advanced Systems Format),compressed samples
- synchronous readers,retrieving compressed samples
- synchronous readers,compressed samples
- compressed samples,retrieving
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Retrieve Compressed Samples with the Synchronous Reader

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Like the asynchronous reader, the synchronous reader can also retrieve compressed samples. Compressed samples should be used when copying streams from one file to another.

The Windows Media Format SDK does not provide any methods for decoding data after it has been extracted from an ASF file. If you receive compressed samples and later want to decompress them, you will have to provide your own code to do so. One way to get around this limitation is to write the compressed samples to a new ASF file and then re-read them into normal, uncompressed samples.

To receive compressed samples with the synchronous reader, call [**IWMSyncReader::SetReadStreamSamples**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-setreadstreamsamples) before or during playback. Pass true for *fCompressed*.

> [!Note]  
> Image streams are not valid for compressed stream delivery. If you copy an image stream from one file to another, it will not work in the new file. To copy an image stream from file to file, retrieve the image stream samples by output number and include them in the new file as if including a new image stream.

 

## Related topics

<dl> <dt>

[**Reading Files with the Synchronous Reader**](reading-files-with-the-synchronous-reader.md)
</dt> </dl>

 

 




