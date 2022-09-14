---
description: Enumerating Audio Types for Specific Encoding Modes
ms.assetid: d44960eb-da5e-4379-ba9d-cb804559dc53
title: Enumerating Audio Types for Specific Encoding Modes (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Audio Types for Specific Encoding Modes (Microsoft Media Foundation)

The input and output media types accepted by the audio encoder are very structured. You must obtain supported output types by calling **IMediaObject::GetOutputType** method or **IMFTransform::GetOutputType**. After you get an output type, you must not alter it.

If you want to use an encoding mode other than one-pass CBR, you must set the mode and then enumerate the output types for that mode; the encoder changes the supported output types depending upon the mode set. The properties that control the encoding mode are [**MFPKEY\_VBRENABLED**](mfpkey-vbrenabledproperty.md) and [**MFPKEY\_PASSESUSED**](mfpkey-passesusedproperty.md). When the mode is set in the encoder, you must enumerate and select an output type, using it without alteration, just as with CBR.

## Identifying Quality Based VBR Types

The procedure for identifying quality based VBR types depends on whether the encoder is acting as a DirectX Media Object (DMO) or acting as a Media Foundation Transform (MFT). For information on when an encoder acts as a DMO or an MFT, see the individual codec reference pages under [Codec Objects](codecobjects.md).

When an audio encoder is acting as a DMO and you configure the encoder to use one-pass VBR, it enumerates all of the supported output types. However, you will typically want to select a one-pass VBR type based on the quality parameter. The encoder puts the quality value for one-pass VBR output types in the **nAvgBytesPerSec** member of the **WAVEFORMATEX** structure pointed to by **DMO\_MEDIA\_TYPE.pbFormat**.

This value is stored in the following format: 0x7FFFFFXX, where XX is the quality value (from 0 to 100). For example, the **nAvgBytesPerSec** value of 0x7FFFFF62 specifies quality level 98 (0x62 = 98).

The following example shows how to check the quality level of a format when the encoder is acting as a DMO.


```
void ShowQuality(WAVEFORMATEX* pWave)
{
    // Store the average bytes per second in a local variable
    // with a more manageable name.
    DWORD dwBps = pWave->nAvgBytesPerSec;

    // Verify that the value is a VBR quality level by using 
    // a bitmask to check for the bit pattern 0x7FFFFFXX. 
    if(dwBps & 0x7FFFFF00 == 0x7FFFFF00)
        printf("VBR Quality: %d%%\n",(dwBps & 0x000000FF));
    else // Not a valid VBR quality value.
        printf("Not a valid one-pass VBR audio format.\n");
}
```



When the encoder is acting as an MFT and it enumerates an output type on a call to **GetAvailableOutputType**, you can query the MFT for the **MFPKEY\_MOST\_RECENTLY\_ENUMERATED\_VBRQUALITY** property. The value returned indicates the VBR quality of the most recently returned output media type. Then you can use that value to set the [**MFPKEY\_DESIRED\_VBRQUALITY**](mfpkey-desired-vbrqualityproperty.md) property of the encoder.

## Setting Peak Constraints

For quality based VBR (one-pass) and unconstrained two-pass VBR, no additional settings are required after retrieving the output type. To use peak-constrained VBR, retrieve an output type with VBR enabled and two passes set. This type, without alteration, describes unconstrained VBR settings. To set peak constraints, set the [MFPKEY\_RMAX](mfpkey-rmaxproperty.md) and [MFPKEY\_BMAX](mfpkey-bmaxproperty.md) properties.

## Related topics

<dl> <dt>

[Configuring Audio Encoding](configuringaudioencoding.md)
</dt> <dt>

[Finding Audio Encoder Output Types](findingaudioencoderoutputtypes.md)
</dt> <dt>

[Using Two-Pass Encoding](usingtwoencodingpasses.md)
</dt> <dt>

[Using VBR Encoding](usingvbrencoding.md)
</dt> </dl>

 

 



