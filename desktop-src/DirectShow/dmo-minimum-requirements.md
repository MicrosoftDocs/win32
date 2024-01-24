---
description: DMO Minimum Requirements
ms.assetid: cd342f0f-a3dc-4623-a18f-c45071795ef4
title: DMO Minimum Requirements
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DMO Minimum Requirements

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Every DMO should meet the following minimum requirements:

-   It must support aggregation.
-   It must expose the [**IMediaObject**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-imediaobject) interface.
-   The threading model must be 'both'. DMOs must function correctly in a free-threaded environment.

Audio effect DMOs should support the [**IMediaObjectInPlace**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobjectinplace) interface, for use in DirectMusic and DirectSound.

The following interfaces are documented elsewhere, but are useful for many DMOs. They are not required, however.

-   **ISpecifyPropertyPages**, **IPropertyPage**: These interfaces enable a DMO to provide a property page, for the user to set properties.
-   **IPersistStream**: This interface enables the DMO to save its state to persistent storage.
-   [**IAMStreamConfig**](/windows/desktop/api/Strmif/nn-strmif-iamstreamconfig), [**IAMVideoCompression**](/windows/desktop/api/Strmif/nn-strmif-iamvideocompression): These interfaces enable a client to configure an encoder's output format and compression settings. (These two interfaces are part of the DirectShow API, but are also recommended for DMOs.)

## Related topics

<dl> <dt>

[Writing a DMO](writing-a-dmo.md)
</dt> </dl>

 

 



