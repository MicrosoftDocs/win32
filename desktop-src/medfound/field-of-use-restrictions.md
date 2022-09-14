---
description: Field of Use Restrictions
ms.assetid: 36f28e4c-2baf-4618-9935-5d4615f6bc77
title: Field of Use Restrictions
ms.topic: article
ms.date: 05/31/2018
---

# Field of Use Restrictions

> [!Note]  
> This topic applies to Windows 7 or later.

 

A *field-of-use* restriction is a provision that limits how a license for a particular technology can be used.

Media Foundation provides a mechanism for enforcing field-of-use restrictions on Media Foundation transforms (MFTs), particularly codecs. This mechanism requires the MFT to block its own use by applications until the application has performed a handshake with the MFT. Media Foundation does not define the handshake—typically, it would involve some sort of cryptographic exchange.

### Registration and Enumeration

If an MFT has field-of-use restrictions, set the **MFT\_ENUM\_FLAG\_FIELDOFUSE** flag when you register the MFT. This flag applies to the following MFT registration APIs:

-   [**MFTRegister**](/windows/desktop/api/mfapi/nf-mfapi-mftregister)
-   [**MFTRegisterLocal**](/windows/desktop/api/mfapi/nf-mfapi-mftregisterlocal)
-   [**MFTRegisterLocalByCLSID**](/windows/desktop/api/mfapi/nf-mfapi-mftregisterlocalbyclsid)
-   [**IMFLocalMFTRegistration::RegisterMFTs**](/windows/desktop/api/mfidl/nf-mfidl-imflocalmftregistration-registermfts)

By default, MFTs registered with this flag are excluded from enumeration results. To enumerate MFTs with field-of-use restrictions, call [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex) and specify the **MFT\_ENUM\_FLAG\_FIELDOFUSE** flag in the *Flags* parameter. The following diagram illustrates this process.

![diagram showing mft and an application sending data to the registry](images/mft-fou01.gif)

The [**MFTEnum**](/windows/desktop/api/mfapi/nf-mfapi-mftenum) function always excludes any MFTs that have field-of-use restrictions.

### Unlocking the MFT

To use an MFT with field-of-use restrictions, perform the following steps:

1.  The application implements the [**IMFFieldOfUseMFTUnlock**](/windows/desktop/api/mfidl/nn-mfidl-imffieldofusemftunlock) interface.
2.  The [**IMFFieldOfUseMFTUnlock::Unlock**](/windows/desktop/api/mfidl/nf-mfidl-imffieldofusemftunlock-unlock) method takes a pointer to the **IUnknown** interface of the MFT.
3.  In the [**Unlock**](/windows/desktop/api/mfidl/nf-mfidl-imffieldofusemftunlock-unlock) method, the application performs the required handshake, using whatever mechanism is defined by the MFT. This step is not defined by Media Foundation API.
4.  If the [**Unlock**](/windows/desktop/api/mfidl/nf-mfidl-imffieldofusemftunlock-unlock) method succeeds, the MFT unlocks itself.

The application specifies the [**IMFFieldOfUseMFTUnlock**](/windows/desktop/api/mfidl/nn-mfidl-imffieldofusemftunlock) pointer by setting the [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md) attribute. There are several different ways to set this attribute, depending on how your application creates the decoder or encoding pipeline:



| API                   | How to Unlock Field-Of-Use                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Source Reader         | If your application uses the [Source Reader](source-reader.md) to decode a media file, set the [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md) attribute in the configuration parameters. See [Source Reader Attributes](source-reader-attributes.md).                                                                                                                                                                                                                                                                         |
| Sink Writer           | If your application uses the sink writer to encode a media file, set the [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md) attribute in the configuration parameters. See [Sink Writer Attributes](sink-writer-attributes.md).                                                                                                                                                                                                                                                                                                    |
| Fast Transcode        | If your application uses the Fast Transcode feature to create an encoding topology, set the [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md) when you call [**IMFTranscodeProfile::SetContainerAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imftranscodeprofile-setcontainerattributes). For more information about the Fast Transcode feature, see [Transcode API](transcode-api.md).                                                                                                                                                                      |
| Topology              | If you create a topology directly, set the [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md) as an attribute on the topology. See [Topology Attributes](topology-attributes.md).                                                                                                                                                                                                                                                                                                                                                  |
| MFT Activation Object | If your application directly enumerates the decoders or encoders that it will use, set the [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md) on the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) pointers returned by the [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex) function. <br/> Set the attribute before calling [**IMFActivate::ActivateObject**](/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-activateobject) to create the MFT. The activation object calls [**IMFFieldOfUseMFTUnlock::Unlock**](/windows/desktop/api/mfidl/nf-mfidl-imffieldofusemftunlock-unlock) when it creates the MFT.<br/> |



 

The following diagram shows the relation between MFT activation objects and the [**IMFFieldOfUseMFTUnlock**](/windows/desktop/api/mfidl/nn-mfidl-imffieldofusemftunlock) interface.

![diagram showing an application, activation object and mft with arrows to an fou object, which has an arrow back to mft](images/mft-fou02.gif)

## Related topics

<dl> <dt>

[Media Foundation Transforms](media-foundation-transforms.md)
</dt> </dl>

 

 




