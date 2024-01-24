---
description: Source Resolver
ms.assetid: 93eecf10-308b-4bb4-92f9-fd32d6ecdb04
title: Source Resolver
ms.topic: article
ms.date: 05/31/2018
---

# Source Resolver

The source resolver takes a URL or byte stream and creates the appropriate media source for that content. The source resolver is the standard way for the applications to create media sources.

Internally, the source resolver uses *handler* objects:

-   *Scheme handlers* take a URL and create a media source or a byte stream.
-   *Byte stream handlers* take a byte stream and create a media source.

You can implement a custom handler and add it to the registry. Scheme handlers are registered by URL scheme, and byte stream handlers are registered by file name extension or MIME type.

This topic contains the following sections:

-   [Using the Source Resolver](using-the-source-resolver.md)
-   [Configuring a Media Source](configuring-a-media-source.md)
-   [Scheme Handlers and Byte-Stream Handlers](scheme-handlers-and-byte-stream-handlers.md)

## Related topics

<dl> <dt>

[Media Sources](media-sources.md)
</dt> </dl>

 

 



