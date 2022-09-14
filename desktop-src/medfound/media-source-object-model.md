---
description: Media Source Object Model
ms.assetid: 88373028-8a34-4bf1-8300-d1a7e4c7dd75
title: Media Source Object Model
ms.topic: article
ms.date: 05/31/2018
---

# Media Source Object Model

This topic describes the object model for media sources in Microsoft Media Foundation. A media source must implement two objects:

-   A presentation descriptor, which describes the contents of the source, including the number of streams and the format of each stream. For more information about presentation descriptors, see [Presentation Descriptors](presentation-descriptors.md).
-   One or more media streams, which generate the source data.

The source does not create the streams until playback starts.

## Media Source Interfaces

A media source must expose the following interfaces through **QueryInterface**.



| Interface                                                | Description                                                                                                     |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource)                 | Required for all media sources.                                                                                 |
| [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) | Required for all media sources. The [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) interface inherits this interface. |



 

Optionally, a media source can implement the [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice) interface and implement any of the following interfaces as services:



| Service interface                                  | Description                                                       |
|----------------------------------------------------|-------------------------------------------------------------------|
| [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol)           | Controls the playback rate.                                       |
| [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport)           | Reports the range of playback rates that are supported.           |
| [**IMFQualityAdvise**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise)       | Enables the quality manager to adjust the audio or video quality. |
| [**IMFMetadataProvider**](/windows/desktop/api/mfidl/nn-mfidl-imfmetadataprovider) | Provides metadata.                                                |



 

If the media source can play at rates other than normal speed (1.0), it should expose the rate control service ([**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol) and [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport)). Otherwise, it is assumed that the source only supports playback at normal speed. For more information, see [Implementing Rate Control](implementing-rate-control.md).

For more information about service interfaces and [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice), see [Service Interfaces](service-interfaces.md).

## Media Stream Interfaces

Media streams must implement the following interfaces.



| Interface                                                | Description                                                                                                     |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**IMFMediaStream**](/windows/desktop/api/mfidl/nn-mfidl-imfmediastream)                 | Required for all media streams.                                                                                 |
| [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) | Required for all media streams. The [**IMFMediaStream**](/windows/desktop/api/mfidl/nn-mfidl-imfmediastream) interface inherits this interface. |



 

Currently no service interfaces are defined for media streams.

## Related topics

<dl> <dt>

[Media Sources](media-sources.md)
</dt> </dl>

 

 



