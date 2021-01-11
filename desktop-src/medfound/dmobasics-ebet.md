---
description: DMO Basics
ms.assetid: eaf453d2-69f8-432a-8a58-1ed70778f182
title: DMO Basics (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# DMO Basics (Microsoft Media Foundation)

This topic provides a brief overview of DMOs as they relate to Windows Media Codecs. For more information about DMOs, see [DirectX Media Objects](../directshow/directx-media-objects.md).

A DMO is a COM object that transforms data. You pass data to it, and it returns the transformed data. In the case of a codec encoder DMO, you input uncompressed media data and the DMO delivers compressed media data. The primary advantage of using DMOs is that they all implement the same base interface, [**IMediaObject**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobject), which simplifies working with them because you can use the same object, regardless of the type of transformation being performed.

Because there are variables involved in any sort of data transformation, audio and video transformation must take into account the wide range of possible media configurations. The Windows Media Audio and Video codecs also support a number of special features that you must be able to configure by using the DMO.

In general, the variable information that is needed by the codec DMOs to compress and decompress digital media is conveyed in one of three ways:

-   Set the input type on the DMO to convey the characteristics of the uncompressed media that you pass to an encoder DMO, and the characteristics of the compressed media that you pass to a decoder DMO.
-   Set the output type on the DMO to convey the characteristics of the compressed media that are delivered by an encoder DMO, and the characteristics of the uncompressed media that are delivered by a decoder DMO.
-   Using the methods of the **IPropertyBag** interface, configure other settings that support the various features of the codec DMOs as properties. **IPropertyBag** is a standard COM interface that is supported by all of the codec DMOs.

Additionally, some codec features are managed by using other interfaces that are specific to the codec DMOs. These interfaces are listed for each codec in the section [Codec Objects](codecobjects.md).

Input and output types are specific to input and output streams. Each stream represents a discrete representation of the content. For example, the Windows Media Video encoder DMO has a single input stream, and two output streams. The input stream accepts uncompressed video samples. The first of the two output streams delivers compressed samples; the other provides uncompressed samples. The individual samples in one output stream represent the same content as the corresponding samples in the other stream, but each stream delivers those samples in a different format.

Each stream (input or output) supports one or more types of media. A media type, or format, is described by a [**DMO\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/mediaobj/ns-mediaobj-dmo_media_type) structure. You can query the DMO for the types that are supported by an output stream by calling [**IMediaObject::GetOutputType**](/previous-versions/windows/desktop/api/mediaobj/nf-mediaobj-imediaobject-getoutputtype). This method returns a valid (though in some cases partially incomplete) output type for that stream. You can enumerate the supported media types for an output stream by making repeated calls to **GetOutputType**, incrementing the type parameter with each call. When the type index that you pass is out of bounds, the method returns **DMO\_E\_NO\_MORE\_ITEMS**. Input formats can be enumerated in the same way by using the [**IMediaObject::GetInputType**](/previous-versions/windows/desktop/api/mediaobj/nf-mediaobj-imediaobject-getinputtype) method.

The types that are enumerated by the DMO are only the "preferred" types, however, other types may be supported. You can validate an output type by calling [**IMediaObject::SetOutputType**](/previous-versions/windows/desktop/api/mediaobj/nf-mediaobj-imediaobject-setoutputtype). Use [**IMediaObject::SetInputType**](/previous-versions/windows/desktop/api/mediaobj/nf-mediaobj-imediaobject-setinputtype) to validate an input type. Both methods will return **DMO\_E\_TYPE\_NOT\_ACCEPTED** if the [**DMO\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/mediaobj/ns-mediaobj-dmo_media_type) structure you passed is invalid. Some DMOs require you to set an output type before enumerating any input types. The Windows Media Audio and Video codec DMOs all have inputs and outputs that have interdependent validation. That is, the output type you set will set the validation criteria for the input type. There are also some properties that, when set, alter the valid input and output types. For this reason, you should set all of the desired properties on the DMO before enumerating types.

When you have set the output and input types for the DMO, you can begin processing samples. Each input sample is passed to the codec using a call to [**IMediaObject::ProcessInput**](/previous-versions/windows/desktop/api/mediaobj/nf-mediaobj-imediaobject-processinput), and each output sample is delivered by the codec when you make a call to [**IMediaObject::ProcessOutput**](/previous-versions/windows/desktop/api/mediaobj/nf-mediaobj-imediaobject-processoutput).

## Related topics

<dl> <dt>

[Working with Codec DMOs](workingwithcodecdmos.md)
</dt> </dl>

 

 
