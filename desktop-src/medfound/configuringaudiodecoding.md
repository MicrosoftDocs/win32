---
description: Configuring Audio Decoding
ms.assetid: 362bd3bc-1474-4132-a8a8-e5dc0bba80e7
title: Configuring Audio Decoding (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Audio Decoding (Microsoft Media Foundation)

Decoding Windows Media Audio content is much easier than encoding it. After creating an audio decoder object, set the input type by using the **IMediaObject::SetInputType** or **IMFTransform::SetInputType** method. The media type that you use for the decoder input must match the output type that was used when the content was encoded. This includes the extended format data appended to the **WAVEFORMATEX** structure. You must ensure that this data is correct, because the decoder cannot process samples without it.

After setting the input type, you can configure any decoder features you want to use. Decoder features, like those used for encoding, are set using the methods of **IPropertyBag** or **IPropertyStore**.

After the input type is set and all decoder features are configured, you can enumerate the output types supported by the decoder by making calls to **IMediaObject::GetOutputType** or **IMFTransform::GetOutputType**.

## Related topics

<dl> <dt>

[Working with Audio](workingwithaudio.md)
</dt> </dl>

 

 



