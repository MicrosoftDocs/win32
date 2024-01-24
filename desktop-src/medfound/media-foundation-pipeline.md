---
description: The pipeline layer in Microsoft Media Foundation is the layer of the architecture that directly generates or processes media data.
ms.assetid: d6396246-ddc4-4e24-9371-35ddbef59b8a
title: Media Foundation Pipeline
ms.topic: article
ms.date: 05/31/2018
---

# Media Foundation Pipeline

The *pipeline* layer in Microsoft Media Foundation is the layer of the architecture that directly generates or processes media data.

Most applications do not call methods directly on the pipeline components, although it is possible to do so. Read these topics if you are writing a custom pipeline component.

## In this section



| Topic                                                                     | Description                                                                                                                           |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [Media Sources](media-sources.md)<br/>                             | Media sources generate media data, typically from a file, capture device, or network stream. <br/>                              |
| [Media Foundation Transforms](media-foundation-transforms.md)<br/> | Media Foundation transforms (MFTs) process media data. For example, codecs in Media Foundation are implemented as MFTs. <br/>   |
| [Media Sinks](media-sinks.md)<br/>                                 | Media sinks consume media data. For example, a media sink might write the data to a file, or send the data over a network.<br/> |



 

## Related topics

<dl> <dt>

[Media Foundation and COM](media-foundation-and-com.md)
</dt> <dt>

[Media Foundation Architecture](media-foundation-architecture.md)
</dt> </dl>

 

 




