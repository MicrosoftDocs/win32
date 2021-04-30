---
description: Instantiating an Encoder MFT
ms.assetid: 50b71c00-b7cf-4c38-8114-bb36b358fda5
title: Instantiating an Encoder MFT
ms.topic: article
ms.date: 05/31/2018
---

# Instantiating an Encoder MFT

In Microsoft Media Foundation, encoders are implemented as [Media Foundation transforms](media-foundation-transforms.md) (MFTs). Before creating an encoder, you must first find the encoder that is most suited to your needs.

-   Windows Media audio codecs

    Category: **MFT\_CATEGORY\_AUDIO\_ENCODER**

    Major type: MFMediaType\_Audio

    SubType: MFAudioFormat\_WMAudioV9, MFAudioFormat\_WMAudioV8, MFAudioFormat\_WMAudio\_Lossless, MFAudioFormat\_WMASPDIF

-   Windows Media video codecs

    Category: **MFT\_CATEGORY\_VIDEO\_ENCODER**

    Major type: MFMediaType\_Video

    SubType: MFVideoFormat\_WVC1, MFVideoFormat\_WMV3, MFVideoFormat\_WMV2, MFVideoFormat\_WMV1

Media Foundation provides several functions that your application can call to enumerate the various encoders available in your system. Encoders are registered as COM objects and the registry entry follows the standard format for COM class factories. The registry maintains the CLSIDs for the encoders, which are categorized by the media format (audio or video). The class identifiers of the Windows Media encoders are defined as constants in the wmcodecdsp.h header file. In Media Foundation, the encoders can be registered through calls to [**MFTRegisterLocal**](/windows/desktop/api/mfapi/nf-mfapi-mftregisterlocal) or [**MFTRegisterLocalByCLSID**](/windows/desktop/api/mfapi/nf-mfapi-mftregisterlocalbyclsid) by specifying the catergory, the supported input types, and the supported output types. Upon successful registration through these functions, the MFTs are considered by the Media Foundation enumeration functions.

For creating an instance of an encoder MFT, an application has the following choices.

-   Create the encoder MFT directly and receive a pointer to the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface. For more information, see [Creating an Encoder by Using CoCreateInstance](using-an-encoder-s-imftransform--interface.md).
-   Create an instance of the activation object for the encoder MFT and receive a pointer to the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) interface. For more information, see [Using an Encoder's Activation Objects](using-an-encoder-s-activation-objects.md).

If your application is using [Pipeline Layer ASF Components](pipeline-layer-asf-components.md) to encode a file to ASF format, you must insert the encoder MFT into the pipeline as a transform node. While creating the transform node in the encoding topology, you can either set the object type as a pointer to the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface or the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) object. Media Foundation provides activation objects for Windows Media encoders so that they can be conveniently set as the transform node in the encoding topology. When the topology is resolved, the Media Session uses the activation object to create an instance of the encoder MFT.

## Related topics

<dl> <dt>

[Windows Media Encoders](windows-media-encoders.md)
</dt> </dl>

 

 



