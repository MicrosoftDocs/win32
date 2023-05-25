---
title: Selecting Bit Rates
description: Selecting Bit Rates
ms.assetid: 466524a6-2473-4768-8ae3-0ac18807f88c
keywords:
- profiles,choosing bit rates
- profiles,bit rates
- codecs,choosing bit rates
- codecs,bit rates
- profiles,selecting bit rates
- codecs,selecting bit rates
- bit rates,selecting
- bit rates,profiles
- bit rates,codecs
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Selecting Bit Rates

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

For files that will be streamed over a network, you must consider carefully what bit rates you should use. Under most circumstances you can add the bit rates of all of the streams in a file together to get a general idea of the available bandwidth required to stream the file. However, a certain amount of overhead is also required for each stream. This overhead is summarized in the following table.



| Bit-rate range (Kbps) | Additional bandwidth required for overhead (Kbps) |
|-----------------------|---------------------------------------------------|
| 10 – 16               | 3                                                 |
| 17 – 30               | 4                                                 |
| 31 – 45               | 5                                                 |
| 46 – 70               | 6                                                 |
| 71 – 225              | 7                                                 |
| >225               | 9                                                 |



 

The normal overhead required for a stream does not take data unit extensions into account. Every data unit extension adds to the size of the sample to which it is attached. Depending upon the type of data unit extension, this can greatly increase the bit rate for the stream.

You must also consider that the theoretical maximum bandwidth available over a network connection is not a practical target bit rate. The average available bandwidth for any given connection falls well short of the bandwidth capacity of the connection, because of network traffic and many other factors.

## Related topics

<dl> <dt>

[**Designing Profiles**](designing-profiles.md)
</dt> </dl>

 

 




