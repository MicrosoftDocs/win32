---
description: Using Media Sources with the Media Session
ms.assetid: b50d3d6e-728b-4ba5-9b79-413d2108ade1
title: Using Media Sources with the Media Session
ms.topic: article
ms.date: 05/31/2018
---

# Using Media Sources with the Media Session

If you are using the Media Session to control playback, the set of methods that you should call on a media source is restricted. This section describes how to use media source in conjunction with the Media Session.

Here are the basic steps your application will perform:

1.  Create the media source. To create a media source, use the source resolver. For more information, see [Source Resolver](source-resolver.md). The source resolver returns a pointer to the source's [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource) interface. (If you have written a custom media source, you can provide a custom creation method instead.)

2.  Configure the presentation. To configure the source's presentation, call [**IMFMediaSource::CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor). You can modify this copy, but the changes do not become active until the playback starts. Do not modify the presentation descriptor during playback. For more information, see [Presentation Descriptors](presentation-descriptors.md).

3.  Create a topology that contains the media source. For more information, see [Topologies](topologies.md).

4.  Use the Media Session to control playback. The Media Session calls methods on the media source. The application should not call any methods on the media source at this time.

5.  Before releasing the media source, call [**IMFMediaSource::Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-shutdown) to shut down the source.

    > [!Note]  
    > If you are using the sequencer source, the sequencer source handles shutting down the segment sources. For more information, see [Sequencer Source](sequencer-source.md).

     

If you use the Media Session, the only methods that you should call on the media source are [**CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor), [**GetCharacteristics**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-getcharacteristics), and [**Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-shutdown). In particular:

-   Do not call [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start), [**Pause**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-pause), or [**Stop**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-stop); these methods should be called only by the Media Session.

-   Do not call any [**IMFMediaStream**](/windows/desktop/api/mfidl/nn-mfidl-imfmediastream) methods.

-   Do not retrieve events directly from the media source or any of the streams. The Media Session must receive these events for the pipeline to function correctly. The Media Session forwards any events that are needed by the application.

## Related topics

<dl> <dt>

[Media Session](media-session.md)
</dt> </dl>

 

 



