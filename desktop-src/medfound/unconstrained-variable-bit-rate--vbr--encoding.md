---
description: Unconstrained Variable Bit Rate Encoding
ms.assetid: 35fb4bd7-87c5-4f46-ae71-10278670ef9c
title: Unconstrained Variable Bit Rate Encoding
ms.topic: article
ms.date: 05/31/2018
---

# Unconstrained Variable Bit Rate Encoding

In unconstrained variable bit rate (VBR) encoding mode, the content is encoded to the highest possible quality while maintaining a specified bit rate.

Unconstrained VBR encoding uses two encoding passes. When using unconstrained VBR encoding, you specify a bit rate for the stream, as you would with [Constant Bit Rate Encoding](constant-bit-rate-encoding.md). However, the encoder uses this value only as the average bit rate for the stream and encodes so that the quality is as high as possible while maintaining the average. Individual samples produced by the encoder varies in size without any explicit buffer limits. However, the average bit rate during the encoding session and the duration of the stream must be no more than the value specified by you. The actual bit rate at any point in the encoded stream can vary greatly from the average value. You do not set a buffer window for unconstrained VBR encoding. Instead, the encoder computes the size of the required buffer window based on the requirements of the encoded samples. This means that there is no limit to the size of individual samples in the stream, as long as the average bit rate is less than or equal to the value you set.

The advantage of unconstrained VBR encoding is that the compressed stream has the highest possible quality while staying within a predictable average bandwidth. Use this when you need to specify a bandwidth but fluctuations around the specified bandwidth are acceptable; for example, for local files or downloading only.

The disadvantage of this mode of encoding is that the encoder can set the buffer window to whatever value is required after encoding, giving you no control over the buffer size. In most cases, if you are not concerned about the size of the buffer or the consistency of bandwidth usage, you should use [Quality-Based Variable Bit Rate Encoding](quality-based-variable-bit-rate--vbr--encoding.md)

### Configuring the Encoder for Unconstrained VBR

Encoder configuration is set through property values. These properties are defined in wmcodecdsp.h. The configuration properties must be set on the encoder before negotiating the output media type. For information about how to set properties on the encoder, see [Configuring the Encoder](configuring-the-encoder.md). Based on the specified property values, you can enumerate the supported VBR output types and select the required one on the encoder [Media Foundation Transform](media-foundation-transforms.md) (MFT) based on the average bit rate.

The following list shows the properties you must set for this type of encoding:

-   Specify the VBR encoding mode by setting the MFPKEY\_VBRENABLED property to VARIANT\_TRUE.
-   Set the MFPKEY\_PASSESUSED to 2 because unconstrained VBR mode uses two encoding passes.
-   While enumerating the output media type, check the [**MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND**](mf-mt-audio-avg-bytes-per-second-attribute.md) attribute (for audio streams) or the [**MF\_MT\_AVG\_BITRATE**](mf-mt-avg-bitrate-attribute.md) attribute (for video streams) of the available output media types. Choose an output media type that has the average bit rate closest to the desired average bit rate that you want the encoder to maintain in the encoded content. For more information about selecting the output media type, see [Media Type Negotiation on the Encoder](media-type-negotiation-on-the-encoder.md).

To get the buffer window value is set by the encoder, call **IWMCodecLeakyBucket::GetBufferSizeBits**, defined in wmcodecifaces.h and wmcodecdspuuid.lib, after the encoding session. To add unconstrained VBR support for the streams, you must set this value in the [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET1**](mf-asfstreamconfig-leakybucket1-attribute.md) attribute (average leaky bucket values) on the stream configuration object while configuring the ASF profile.

The following modifies the SetEncodingType method of the sample class CEncoder to set up the unconstrained VBR mode. For information about this class, see [Encoder Example Code](encoder-example-code.md). For information about the helper macros used in this example, see Using the Media Foundation Code Examples.


```
//////////////////////////////////////////////////////////////////////////
//  Name: SetEncodingType
//  Description: Sets the encoding type to unconstrained VBR
//
/////////////////////////////////////////////////////////////////////////

HRESULT CEncoder::SetEncodingType(EncodeMode mode)
{
    if (!m_pMFT)
    {
        return MF_E_NOT_INITIALIZED;
    }

    HRESULT hr = S_OK;

    IPropertyStore* pProp = NULL;

    PROPVARIANT var;
    PropVariantInit(&var);

    //Query the encoder for its property store
    CHECK_HR(hr = m_pMFT->QueryInterface(__uuidof(IPropertyStore), (void**)&pProp));
    
    if (mode == EncodeMode_VBR_Unconstrained)
    {
        //Set the VBR property to TRUE, which indicates VBR encoding
        var.vt = VT_BOOL;
        var.boolVal = TRUE;
        CHECK_HR(hr = pProp->SetValue(MFPKEY_VBRENABLED, var));
        PropVariantClear(&var);

        //Set number of passes
        var.vt = VT_I4;
        var.lVal  =2;
        CHECK_HR(hr = pProp->SetValue(MFPKEY_PASSESUSED, var));
        PropVariantClear(&var);
    }

done:
    PropVariantClear(&var);
    SAFE_RELEASE (pProp);
    return hr;
    
}
```



## Related topics

<dl> <dt>

[ASF Encoding Types](asf-encoding-types.md)
</dt> <dt>

[The Leaky Bucket Buffer Model](the-leaky-bucket-buffer-model.md)
</dt> <dt>

[How to Create a Topology for Two-Pass Windows Media Encoding](how-to-create-a-topology-for-2-pass-windows-media-encoding.md)
</dt> </dl>

 

 



