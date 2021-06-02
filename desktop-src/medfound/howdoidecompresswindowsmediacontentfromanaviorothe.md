---
description: How do I decompress streams from an AVI file or other file about which I have no format information?
ms.assetid: 980f52f4-17a4-4871-9269-f9e0b97416c6
title: How do I decompress streams from an AVI file or other file about which I have no format information?
ms.topic: article
ms.date: 05/31/2018
---

# How do I decompress streams from an AVI file or other file about which I have no format information?

Without format information, including extended format data, you cannot decompress data that was encoded with a Windows Media codec. The codecs were designed to create data streams for use with the Advanced Systems Format (ASF) file container. The header section of an ASF file stores the format information for all of the streams in the file. When you use content encoded using one of the Windows Media Audio and Video codecs outside of an ASF file, you must ensure that the format information is available. The way to do this varies from one container to another.

## Related topics

<dl> <dt>

[Frequently Asked Questions](frequentlyaskedquestions.md)
</dt> </dl>

 

 



