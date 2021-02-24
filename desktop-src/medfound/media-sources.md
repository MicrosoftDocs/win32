---
description: Media Sources
ms.assetid: 65132e7d-22f6-4209-bc58-f5ea86ebd514
title: Media Sources
ms.topic: article
ms.date: 05/31/2018
---

# Media Sources

*Media sources* are objects that generate media data in the Media Foundation pipeline. This section describes the media source APIs in detail. Read this section if you are implementing a custom media source, or using a media source outside of the Media Foundation pipeline.

If your application uses the control layer, it needs to use only a limited subset of the media source APIs. For information, see the topic [Using Media Sources with the Media Session](using-media-sources-with-the-media-session.md).

## In this section



| Topic                                                                                                 | Description                                                                                                          |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [Media Source Object Model](media-source-object-model.md)<br/>                                 | This topic describes the object model for media sources in Microsoft Media Foundation<br/>                     |
| [Presentation Descriptors](presentation-descriptors.md)<br/>                                   | A *presentation descriptor* is an object that contains the description of a particular presentation.<br/>      |
| [Media Source Events](media-source-events.md)<br/>                                             | This topic lists the events that are sent by media sources and media streams.<br/>                             |
| [Writing a Custom Media Source](writing-a-custom-media-source.md)<br/>                         | This topic describes how to implement a custom media source in Media Foundation.<br/>                          |
| [Case Study: MPEG-1 Media Source](tutorial--writing-a-custom-media-source.md)<br/>             | This topic takes an in-depth look at the [MPEG-1 Media Source](mpeg1source-sample.md) SDK Sample.<br/>        |
| [Custom Metadata Providers for Media Files](custom-metadata-providers-for-media-files.md)<br/> | This topic describes how to write a custom Shell property handler for a Media Foundation media source.<br/>    |
| [Source Resolver](source-resolver.md)<br/>                                                     | The source resolver takes a URL or byte stream and creates the appropriate media source for that content.<br/> |



 

## Related topics

<dl> <dt>

[Media Foundation Pipeline](media-foundation-pipeline.md)
</dt> <dt>

[Custom Metadata Providers for Media Files](custom-metadata-providers-for-media-files.md)
</dt> <dt>

[Media Foundation Architecture](media-foundation-architecture.md)
</dt> </dl>

 

 




