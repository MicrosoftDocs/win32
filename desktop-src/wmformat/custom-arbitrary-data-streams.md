---
title: Custom Arbitrary Data Streams
description: Custom Arbitrary Data Streams
ms.assetid: 23e93b5d-719f-47dc-9f3b-7bef14161b90
keywords:
- Windows Media Format SDK,custom arbitrary data streams
- Advanced Systems Format (ASF),custom arbitrary data streams
- ASF (Advanced Systems Format),custom arbitrary data streams
- Windows Media Format SDK,streams
- Advanced Systems Format (ASF),streams
- ASF (Advanced Systems Format),streams
- custom arbitrary data streams
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Custom Arbitrary Data Streams

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can create a stream in an ASF file to contain any sort of data. If none of the supported stream types suits your needs, you must use an arbitrary data stream. The writer object handles an arbitrary data stream just as it does any uncompressed stream; the samples are packetized and combined with the samples from other streams in the data section of the file. Of course, only a reading application that has been specifically programmed to deal with your arbitrary type will be able to handle the data after it is delivered by the reading object.

One common use of arbitrary data streams is for media data encoded by using a third-party codec. Because the objects of this SDK do not interact directly with third-party codecs, your writing application must process the samples with the encoding portion of the codec and pass the compressed samples to the writer.

## Related topics

<dl> <dt>

[**Arbitrary Streams**](arbitrary-streams.md)
</dt> <dt>

[**Configuring Custom Arbitrary Streams**](configuring-custom-arbitrary-streams.md)
</dt> </dl>

 

 




