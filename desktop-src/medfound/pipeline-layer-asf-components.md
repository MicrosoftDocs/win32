---
description: In Media Foundations pipeline model, a media source is connected to a transform which is further connected to a media sink.
ms.assetid: 55ab3a53-d9fd-438c-998c-8888f99958ce
title: Pipeline Layer ASF Components
ms.topic: article
ms.date: 05/31/2018
---

# Pipeline Layer ASF Components

In Media Foundation's pipeline model, a media source is connected to a transform which is further connected to a media sink. The data contained in the source flows through the transform and generates output media samples in the sink for the purpose of playback or encoding. Depending on whether the application wants to playback ASF content or encode to an ASF file, the application must build the pipeline differently.

The following topics contain information about the pipeline layer components.

-   [ASF Media Source](asf-media-source.md)
-   [Windows Media Encoders](windows-media-encoders.md)
-   [ASF Media Sinks](asf-media-sinks.md)

The three main components of an ASF pipeline for playback are as follows:

-   ASF media source is provided by Media Foundation that represents an ASF file.
-   Audio resamplers, video image resizers, etc., (transform)
-   Audio and Video renderer (sinks)

For information about building a playback pipeline, see [Creating Playback Topologies](creating-playback-topologies.md).

The three main components of an ASF pipeline for encoding are as follows:

-   Media source representing the data in a format that needs to be converted. This component can be one of the default media sources provided by Media Foundation or a custom source that exposes the [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) interface.
-   Windows Media encoders (transform) that perform the format conversion.
-   ASF media sinks provided by Media Foundation that write ASF objects and media samples in an output file specified by the application.

The pipeline is represented in a topology and each object in the pipeline is represented by a topology node. Both for playback and encoding, all of the pipeline operations are handled by the Media Session. One of responsibilities of the Media Session is to make sure that the pipeline has all the components required to generate output. For example, in an encoding pipeline, if the audio source format is different than the target format, the Media Session inserts additional transform components such as the resampler that performs appropriate sample rate conversions. The data flow control through the pipeline is also managed by the Media Session. In a playback scenario, starting the Media Session the Media Session sends samples to SAR and EVR, which renders them on the output device. For encoding, starting the Media Session begins the encoding process. The session asynchronously notifies the application when the encoding is complete.

The following topic contains step-by-step instructions about using the pipeline layer components to build an encoding topology. components for reading and writing ASF files.

-   [Tutorial: 1-Pass Windows Media Encoding](tutorial--1-pass-windows-media-encoding.md)

## Related topics

<dl> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> </dl>

 

 



