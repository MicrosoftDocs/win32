---
description: This section describes how to configure VBR streams.
ms.assetid: 9dd3ff5b-4c7c-41a8-b1b9-7ea380175193
title: Using VBR Encoding (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Using VBR Encoding (Microsoft Media Foundation)

As detailed in the [Encoding Methods](encodingmethods.md) topic, variable bit rate (VBR) encoding is used to improve the consistency of content quality. You configure VBR streams in the same way that you encode constant bit rate (CBR) streams, except for the buffer parameters (bit rate and buffer window). This section describes how to configure VBR streams.

## Configuring Quality Based VBR

Encoding using the quality based VBR method does not require any predefined buffer parameters. Instead, you specify a quality level (from 0 to 100) which the encoder uses to determine the appropriate buffer parameters dynamically. This encoding mode uses only one encoding pass.

You can enumerate the supported quality-based VBR output types for the audio codecs. You must use one of the types returned by the DMO when setting the output type. For more information, see [Enumerating Audio Types for Specific Encoding Modes](enumeratingaudiotypesforspecificencodingmodes.md).

To configure a quality-based VBR video stream, you must set the properties that are listed in the following table.



| Property                                            | Description                                                                                                                                             |
|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MFPKEY\_VBRENABLED](mfpkey-vbrenabledproperty.md) | Set to VARIANT\_TRUE.                                                                                                                                   |
| [MFPKEY\_VBRQUALITY](mfpkey-vbrqualityproperty.md) | Set to the desired quality value, from 0 to 100. Not all quality values represent discrete settings. See the property description for more information. |



 

## Configuring Unconstrained VBR

Unconstrained VBR encoding enables the encoder to vary the size of individual samples without any explicit buffer limits. However, the average bit rate over the duration of the resulting content must be less than or equal to the specified value. Unconstrained VBR requires two encoding passes.

You can enumerate the supported two-pass VBR output types for the audio codecs. You must use one of the types returned by the DMO when setting the output type. For more information, see [Enumerating Audio Types for Specific Encoding Modes](enumeratingaudiotypesforspecificencodingmodes.md).

To configure an unconstrained VBR video stream, you must set the properties that are listed in the following table.



| Property                                            | Description                          |
|-----------------------------------------------------|--------------------------------------|
| [MFPKEY\_VBRENABLED](mfpkey-vbrenabledproperty.md) | Set to VARIANT\_TRUE.                |
| [MFPKEY\_PASSESUSED](mfpkey-passesusedproperty.md) | Set to 2.                            |
| [MFPKEY\_RAVG](mfpkey-ravgproperty.md)             | Set to the desired average bit rate. |



 

## Configuring Peak-Constrained VBR

Peak-constrained VBR is like unconstrained VBR in that it is confined to an average bit rate over the duration of the stream. In addition, peak-constrained VBR conforms to a peak buffer. This buffer is described using a peak bit rate and a peak buffer window, just as a CBR buffer is described by an average bit rate and a buffer window. This mode gives the encoder flexibility in how it encodes individual samples while adhering to the peak limitations. This is particularly useful when decoding is performed by a chip in a device, like a DVD player, where there are hardware limitations that must be considered.

The supported peak-constrained, VBR audio encoder output types are the same types enumerated for unconstrained VBR. Set the peak values on the DMO and use the delivered type. For more information, see [Enumerating Audio Types for Specific Encoding Modes](enumeratingaudiotypesforspecificencodingmodes.md).

To configure a peak-constrained VBR video stream, you must set the properties that are listed in the following table using the **IPropertyBag::Write** method.



| Property                                            | Description                                                     |
|-----------------------------------------------------|-----------------------------------------------------------------|
| [MFPKEY\_VBRENABLED](mfpkey-vbrenabledproperty.md) | Set to VARIANT\_TRUE.                                           |
| [MFPKEY\_PASSESUSED](mfpkey-passesusedproperty.md) | Set to 2.                                                       |
| [MFPKEY\_RAVG](mfpkey-ravgproperty.md)             | Set to the desired average bit rate.                            |
| [MFPKEY\_RMAX](mfpkey-rmaxproperty.md)             | Set to the desired peak bit rate.                               |
| [MFPKEY\_BMAX](mfpkey-bmaxproperty.md)             | Set to the buffer window that corresponds to the peak bit rate. |



 

> [!Note]  
> It is recommended that you set the peak bit rate to at least twice the average bit rate. Setting the peak rate to a lower value may cause the codec to encode the content as two-pass CBR instead of peak-constrained VBR.

 

## Related topics

<dl> <dt>

[Windows Media Codecs](windows-media-codecs.md)
</dt> <dt>

[Using Two-Pass Encoding](usingtwoencodingpasses.md)
</dt> <dt>

[Working with Audio](workingwithaudio.md)
</dt> <dt>

[Working with Video](workingwithvideo.md)
</dt> </dl>

 

 



