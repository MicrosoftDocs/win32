---
description: Sink Writer Attributes
ms.assetid: f27b9beb-f35f-400e-a337-50d9de21e91e
title: Sink Writer Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Sink Writer Attributes

The following attributes can be used to initialize the sink writer.



| Attribute                                                                                  | Description                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MF\_LOW\_LATENCY](mf-low-latency.md)                                                     | Enables low-latency processing.                                                                                                                                                                                                    |
| [MF\_READWRITE\_DISABLE\_CONVERTERS](mf-readwrite-disable-converters.md)                  | Enables or disables format conversions by the sink writer.                                                                                                                                                                         |
| [MF\_READWRITE\_ENABLE\_HARDWARE\_TRANSFORMS](mf-readwrite-enable-hardware-transforms.md) | Enables the sink writer to use hardware-based Media Foundation transforms (MFTs).                                                                                                                                                  |
| [MF\_SINK\_WRITER\_ASYNC\_CALLBACK](mf-sink-writer-async-callback.md)                     | Contains a pointer to the application's callback interface for the sink writer.                                                                                                                                                    |
| [MF\_SINK\_WRITER\_DISABLE\_THROTTLING](mf-sink-writer-disable-throttling.md)             | Specifies whether the sink writer limits the rate of incoming data.                                                                                                                                                                |
| [MF\_TRANSCODE\_CONTAINERTYPE](mf-transcode-containertype.md)                             | Specifies the container type of the output file.                                                                                                                                                                                   |
| [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md)                  | Contains an [**IMFFieldOfUseMFTUnlock**](/windows/desktop/api/mfidl/nn-mfidl-imffieldofusemftunlock) pointer, which is used to unlock an MFT with field-of-use restrictions. For more information, see [Field of Use Restrictions](field-of-use-restrictions.md). |
| [MF\_SINK\_WRITER\_D3D\_MANAGER](mf-sink-writer-d3d-manager.md)                           | Use this attribute to provide a Direct3D device for any video encoders or media sinks loaded by the sink writer.                                                                                                                   |



 

Use these attributes with the following methods and functions:

-   [**IMFReadWriteClassFactory::CreateInstanceFromObject**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-imfreadwriteclassfactory-createinstancefromobject)
-   [**IMFReadWriteClassFactory::CreateInstanceFromURL**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-imfreadwriteclassfactory-createinstancefromurl)
-   [**MFCreateSinkWriterFromMediaSink**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfrommediasink)
-   [**MFCreateSinkWriterFromURL**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfromurl)

To use any of these attributes, first call [**MFCreateAttributes**](/windows/desktop/api/mfapi/nf-mfapi-mfcreateattributes) to create a new attribute store. Then use the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface to set the desired attributes on the attribute store. Pass the **IMFAttributes** pointer to the *pAttributes* parameter of any of the methods or functions listed previously.

## Related topics

<dl> <dt>

[**IMFSinkWriter**](/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsinkwriter)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 



