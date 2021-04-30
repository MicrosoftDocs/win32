---
description: Source Reader Attributes
ms.assetid: 312a588a-848b-4563-893a-fac49a4ca465
title: Source Reader Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Source Reader Attributes

The following attributes can be used to initialize the [Source Reader](source-reader.md).



| Attribute                                                                                                            | Description                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MF\_LOW\_LATENCY](mf-low-latency.md)                                                                               | Enables low-latency processing.                                                                                                                                                                                                    |
| [MF\_READWRITE\_DISABLE\_CONVERTERS](mf-readwrite-disable-converters.md)                                            | Enables or disables format conversions by the source reader.                                                                                                                                                                       |
| [MF\_READWRITE\_ENABLE\_HARDWARE\_TRANSFORMS](mf-readwrite-enable-hardware-transforms.md)                           | Enables the source reader to use hardware-based Media Foundation transforms (MFTs).                                                                                                                                                |
| [MF\_SOURCE\_READER\_ASYNC\_CALLBACK](mf-source-reader-async-callback.md)                                           | Contains a pointer to the application's callback interface for the source reader.                                                                                                                                                  |
| [MF\_SOURCE\_READER\_D3D\_MANAGER](mf-source-reader-d3d-manager.md)                                                 | Contains a pointer to the Microsoft [Direct3D Device Manager](direct3d-device-manager.md).                                                                                                                                        |
| [MF\_SOURCE\_READER\_DISABLE\_DXVA](mf-source-reader-disable-dxva.md)                                               | Specifies whether the source reader enables DirectX Video Acceleration (DXVA) on the video decoder.                                                                                                                                |
| [MF\_SOURCE\_READER\_DISCONNECT\_MEDIASOURCE\_ON\_SHUTDOWN](mf-source-reader-disconnect-mediasource-on-shutdown.md) | Specifies whether the source reader shuts down the media source.<br/> Applies only when the application creates the source reader from an existing media source object.<br/>                                           |
| [MF\_SOURCE\_READER\_ENABLE\_ADVANCED\_VIDEO\_PROCESSING](mf-source-reader-enable-advanced-video-processing.md)     | Enables advanced video processing by the [Source Reader](source-reader.md), including color space conversion, deinterlacing, video resizing, and frame-rate conversion.                                                           |
| [MF\_SOURCE\_READER\_ENABLE\_VIDEO\_PROCESSING](mf-source-reader-enable-video-processing.md)                        | Enables limited video processing by the source reader.                                                                                                                                                                             |
| [MF\_SOURCE\_READER\_MEDIASOURCE\_CONFIG](mf-source-reader-mediasource-config.md)                                   | Contains configuration properties for the media source.                                                                                                                                                                            |
| [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md)                                            | Contains an [**IMFFieldOfUseMFTUnlock**](/windows/desktop/api/mfidl/nn-mfidl-imffieldofusemftunlock) pointer, which is used to unlock an MFT with field-of-use restrictions. For more information, see [Field of Use Restrictions](field-of-use-restrictions.md). |



 

Use these attributes with the following methods and functions:

-   [**IMFReadWriteClassFactory::CreateInstanceFromObject**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-imfreadwriteclassfactory-createinstancefromobject)
-   [**IMFReadWriteClassFactory::CreateInstanceFromURL**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-imfreadwriteclassfactory-createinstancefromurl)
-   [**MFCreateSourceReaderFromByteStream**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfrombytestream)
-   [**MFCreateSourceReaderFromMediaSource**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfrommediasource)
-   [**MFCreateSourceReaderFromURL**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfromurl)

To use any of these attributes, first call [**MFCreateAttributes**](/windows/desktop/api/mfapi/nf-mfapi-mfcreateattributes) to create a new attribute store. Then use the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface to set the desired attributes on the attribute store. Pass the **IMFAttributes** pointer to the *pAttributes* parameter of any of the methods or functions listed previously.

## Related topics

<dl> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> <dt>

[Source Reader](source-reader.md)
</dt> <dt>

[**IMFSourceReader**](/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsourcereader)
</dt> </dl>

 

 




