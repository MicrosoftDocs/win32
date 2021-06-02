---
description: This section describes the general design of Microsoft Media Foundation. For information about using Media Foundation for specific programming tasks, see Media Foundation Programming Guide.
ms.assetid: 33820c6a-859d-4df6-a605-4e0f64f45c5b
title: Media Foundation Architecture
ms.topic: article
ms.date: 05/31/2018
---

# Media Foundation Architecture

This section describes the general design of Microsoft Media Foundation. For information about using Media Foundation for specific programming tasks, see [Media Foundation Programming Guide](media-foundation-programming-guide.md).

## In this section



| Topic                                                                                                         | Description                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Overview of the Media Foundation Architecture](overview-of-the-media-foundation-architecture.md)<br/> | Gives a high-level overview of the Media Foundation architecture.<br/>                                                                                                                                                                                                               |
| [Media Foundation Primitives](media-foundation-primitives.md)<br/>                                     | Describes some basic interfaces that are used throughout Media Foundation.<br/> Almost all Media Foundation applications will use these interfaces.<br/>                                                                                                                       |
| [Media Foundation Platform APIs](media-foundation-platform-apis.md)<br/>                               | Describes core Media Foundation functions, such as asynchronous callbacks and work queues.<br/> Some applications might use platform-level interfaces. Also, custom plug-ins, such as media sources and MFTs, use these interfaces.<br/>                                       |
| [Media Foundation Pipeline](media-foundation-pipeline.md)<br/>                                         | The Media Foundation pipeline layer consists of media sources, MFTs, and media sinks. Most applications do not call methods directly on the pipeline layer. Instead, applications use one of the higher layers, such as the Media Session or the Source Reader and Sink Writer.<br/> |
| [Media Session](media-session.md)<br/>                                                                 | The Media Session manages data flow in the Media Foundation pipeline.<br/>                                                                                                                                                                                                           |
| [Source Reader](source-reader.md)<br/>                                                                 | The Source Reader enables an application to get data from a media source, without the applicating needing to call the media source APIs directly. The Source Reader can also perform decoding of compressed streams.<br/>                                                            |
| [Protected Media Path](protected-media-path.md)<br/>                                                   | The protected media path (PMP) provides a protected environment for playing premium video content. It is not necessary to use the PMP when writing a Media Foundation application. <br/>                                                                                             |



 

## Related topics

<dl> <dt>

[About Media Foundation](about-the-media-foundation-sdk.md)
</dt> <dt>

[Media Foundation: Essential Concepts](media-foundation-programming--essential-concepts.md)
</dt> <dt>

[Media Foundation and COM](media-foundation-and-com.md)
</dt> <dt>

[Media Foundation Programming Guide](media-foundation-programming-guide.md)
</dt> </dl>

 

 




