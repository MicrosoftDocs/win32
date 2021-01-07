---
description: ICE29 validates that truncated stream names remain unique. Any table having a Binary or Object column is validated. See the Binary column data type.
ms.assetid: a51b641d-992b-4b6b-a208-d94bc7d05115
title: ICE29
ms.topic: article
ms.date: 05/31/2018
---

# ICE29

ICE29 validates that truncated stream names remain unique. Any table having a Binary or Object column is validated. See the [Binary](binary.md) column data type.

Handling of streams by the Win32 OLE structured storage implementation limits stream names. See [OLE Limitations on Streams](ole-limitations-on-streams.md). The installer can compress stream names up to 62 characters in length. Names longer than this are truncated.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



