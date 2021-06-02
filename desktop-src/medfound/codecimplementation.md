---
description: Codec implementation.
ms.assetid: 5ec23f95-cc7d-4c16-979a-f1d2cc485bb0
title: Codec implementation
ms.topic: article
ms.date: 05/31/2018
---

# Codec implementation

The Windows Media Audio and Video codecs are implemented as COM objects. Typically, a codec is implemented as a pair of COM objects: one for the encoder and one for the decoder. The encoder has a class identifier (CLSID) and the decoder has a different CLSID. For example, the encoder portion of the Windows Media Audio 9 codec has a CLSID represented by the constant **CLSID\_CWMAEncMediaObject**, and the decoder portion of that same codec has a CLSID represented by the constant **CLSID\_CWMADecMediaObject**.

In some cases, more than one encoder is included in a single COM object. For example, the Windows Media Video 9 encoder and the Windows Media Video 9.1 encoder are both part of the same COM object. Consequently, they both have the same CLSID, which is represented by the constant **CLSID\_CWMV9EncMediaObject**. Similarly, some COM objects include more than one decoder.

Each encoder or decoder object exposes the [**IMediaObject**](/previous-versions/ms785953%28v%3dvs.85%29) interface so that the object can be used as a DirectX Media Object (DMO) and the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface so that the object can be used as a Media Foundation Transform (MFT).

For most encoders, regardless of whether you use the encoder as a DMO or an MFT, you use the same CLSID to create an instance of the encoder. For example, to create an instance of the Windows Media Video 9 encoder, you use **CLSID\_CWMV9EncMediaObject**, regardless of whether you intend to use the encoder as a DMO or an MFT. Similarly, for most decoders, each decoder has a single CLSID regardless of whether you use the decoder as a DMO or an MFT.

> [!Note]  
> There are some exceptions to the preceding statement about using a single CLSID for both the DMO and the MFT. For example, the MPEG-4 Part 2 decoder has one CLSID when it is acting as a DMO and a different CLSID when it is acting as an MFT.

 

In addition to the core interfaces, each encoder or decoder object implements two similar interfaces for working with codec properties, **IPropertyBag** and **IPropertyStore**. Older versions of the encoder and decoder objects used **IPropertyBag**, which identifies each property by a string value containing a property name. **IPropertyStore** is a newer interface that identifies properties with a unique property key value. Support for **IPropertyStore** was added to provide support for MFTs. Most **IPropertyBag** property name strings have a corresponding **IPropertyStore** property key GUID and most of the GUIDs have a corresponding **IPropertyBag** name string, with a few exceptions.

This documentation lists the properties by property key constant, but each entry includes the property-name string constant for use with **IPropertyBag** when appropriate.

## Related topics

[Windows Media Codecs](windows-media-codecs.md)
