---
Description: Configuring Codec DMOs
ms.assetid: 431b33f1-ceb0-4f1b-a9f2-72e88b63f973
title: Configuring Codec DMOs
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Codec DMOs

This topic describes the process of configuring the codec DMOs. Each codec has specific procedures, but the information common to all is described here.

## Configuring DMO Inputs and Outputs

Every DMO supports specific input and output types. You can retrieve supported types for inputs and outputs by calling [**IMediaObject::GetInputType**](https://msdn.microsoft.com/en-us/library/Dd406952(v=VS.85).aspx) for inputs and [**IMediaObject::GetOutputType**](https://msdn.microsoft.com/en-us/library/Dd406956(v=VS.85).aspx) for outputs. You can enumerate the supported formats by making repeated calls to either method, incrementing the type index with each call. When the index exceeds that of the final supported type, the call returns DMO\_E\_NO\_MORE\_ITEMS.

For the video codecs, only one output type or input type is enumerated for a given media subtype. For the audio codecs, each individual supported type is enumerated. For more information about supported types for individual codecs, see [Working with Audio](workingwithaudio.md) and [Working with Video](workingwithvideo.md).

After you configure the media types for the input and output streams, set them by calling [**IMediaObject::SetInputType**](https://msdn.microsoft.com/en-us/library/Dd406962(v=VS.85).aspx) and [**IMediaObject::SetOutputType**](https://msdn.microsoft.com/en-us/library/Dd406963(v=VS.85).aspx) respectively. Both of these methods return **DMO\_E\_TYPE\_NOT\_ACCEPTED** if the specified type is invalid.

## Configuring the Codec DMOs for Encoding

All of the Windows Media Audio and Video codecs support a variety of encoding features. These features are generally configured by setting properties on the DMO by using the methods of the **IPropertyBag** interface. Some properties are configured using specialized codec interfaces. These interfaces are listed for each codec in the section [Codec Objects](codecobjects.md).

The general order of operations for configuring an encoding DMO is as follows:

1.  Configure codec features as desired by using the methods of **IPropertyBag**.
2.  Use the codec DMO interfaces to configure additional features, if needed.
3.  Configure the input and output types. The order in which the types should be configured varies for individual codecs. For more information, see [Working with Audio](workingwithaudio.md) and [Working with Video](workingwithvideo.md).

## Configuring the Codec DMOs for Decoding

Decoding is simpler than encoding, as fewer decoder features are supported.

The general order of operations for configuring a decoding DMO is as follows:

1.  Configure decoder features as desired by using the methods of **IPropertyBag**.
2.  Set the input type to the type used for the encoder output.
3.  Configure the output type. The supported output types are different for different inputs.

> [!Note]  
> It is important to use the same media type for the decoder input as was used for the encoder output. This is because the Windows Media Audio and Video codecs use media formats with extra data. This data is appended to the structure pointed to by the **pbFormat** member of the [**DMO\_MEDIA\_TYPE**](https://msdn.microsoft.com/en-us/library/Dd375504(v=VS.85).aspx) structure (usually [**VIDEOINFOHEADER**](https://msdn.microsoft.com/en-us/library/Dd407325(v=VS.85).aspx) or [**WAVEFORMATEX**](https://msdn.microsoft.com/library/Dd390970(v=VS.85).aspx)). For some types the extra data is part of the enumerated encoder output type. Other types require you to append this data manually. Without the extended format data, you cannot decode the compressed content.

 

## Related topics

<dl> <dt>

[Working with Codec DMOs](workingwithcodecdmos.md)
</dt> </dl>

 

 



