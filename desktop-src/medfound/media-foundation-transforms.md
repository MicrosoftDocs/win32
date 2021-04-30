---
description: Media Foundation Transforms
ms.assetid: cb23fe0a-c42c-4912-a0bf-1f0b18a6f4e0
title: Media Foundation Transforms
ms.topic: article
ms.date: 05/31/2018
---

# Media Foundation Transforms

Media Foundation transforms (MFTs) provide a generic model for processing media data. MFTs are used for decoders, encoders, and digital signal processors (DSPs). In short, anything that sits in the media pipeline between the media source and the media sink is an MFT.

This section describes the MFT programming model and how to implement an MFT, with recommendations for specific types of MFTs, such as decoders.



| Topic                                                                    | Description                                                                                                                                                                                         |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About MFTs](about-mfts.md)                                             | Provides a brief overview of MFTs                                                                                                                                                                   |
| [Basic MFT Processing Model](basic-mft-processing-model.md)             | Describes in more detail the basic model for processing data with an MFT.                                                                                                                           |
| [Asynchronous MFTs](asynchronous-mfts.md)                               | Describes an asynchronous processing model that is an alternative to the basic model.<br/> Asynchronous processing was introduced in Windows 7. Not every MFT supports this model.<br/> |
| [Registering and Enumerating MFTs](registering-and-enumerating-mfts.md) | How to register an MFT and how to enumerate MFTs in the registry.                                                                                                                                   |
| [Field of Use Restrictions](field-of-use-restrictions.md)               | Describes the mechanism for unlocking an MFT that has field-of-use restrictions.                                                                                                                    |
| [Comparison of MFTs and DMOs](comparison-of-mfts-and-dmos.md)           | Summarizes the differences between MFTs and DMOs.                                                                                                                                                   |
| [Writing a Custom MFT](writing-a-custom-mft.md)                         | Guidelines for writing a custom MFT.                                                                                                                                                                |



 

## Related topics

<dl> <dt>

[Media Foundation Pipeline](media-foundation-pipeline.md)
</dt> <dt>

[Media Foundation Architecture](media-foundation-architecture.md)
</dt> <dt>

[**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)
</dt> </dl>

 

 




