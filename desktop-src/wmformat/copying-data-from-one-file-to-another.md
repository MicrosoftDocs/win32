---
title: Copying Data from One File to Another
description: Copying Data from One File to Another
ms.assetid: 1403c396-46ea-48b1-a535-922ffca31bc2
keywords:
- Windows Media Format SDK,copying data
- Advanced Systems Format (ASF),copying data
- ASF (Advanced Systems Format),copying data
- streams,copying data
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Copying Data from One File to Another

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

At the most basic level, copying a stream from one ASF file to another is fairly straightforward. However, there are issues to consider when working with streams from multiple input files or when copying streams that you first decompress and re-encode.

The following sections describe copying streams.



| Section                                                                                              | Descripiton                                                                                    |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [Copying Streams Without Decompressing the Data](copying-streams-without-decompressing-the-data.md) | Describes how to copy streams using compressed samples to preserve the quality of the content. |
| [Copying Streams Using Decompressed Samples](copying-streams-using-decompressed-samples.md)         | Describes the difficulties in copying streams using decompressed samples.                      |



 

## Related topics

<dl> <dt>

[**Profile Manager Object**](profile-manager-object.md)
</dt> <dt>

[**Stream Configuration Object**](stream-configuration-object.md)
</dt> <dt>

[**Synchronous Reader Object**](synchronous-reader-object.md)
</dt> <dt>

[**Writer Object**](writer-object.md)
</dt> </dl>

 

 




