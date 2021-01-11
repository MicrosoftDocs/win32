---
description: 'In the peak-constrained variable bit rate (VBR), the content is encoded to a specified bit rate and peak values: a peak bit rate and a peak buffer window.'
ms.assetid: bc37362e-d66d-4552-8357-d22093d5d0ad
title: Peak-Constrained Variable Bit Rate Encoding
ms.topic: article
ms.date: 05/31/2018
---

# Peak-Constrained Variable Bit Rate Encoding

In the peak-constrained variable bit rate (VBR), the content is encoded to a specified bit rate and *peak values*: a peak bit rate and a peak buffer window. These peak values are also called the *peak leaky bucket values*. The file is encoded to conform to a buffer described by the peak values, such that the overall average bit rate of the stream is equal to or less than the average bit rate value you specified.

Typically, the peak bit rate is quite high. The encoder ensures that the average bit rate value specified is maintained over the duration of the stream (average bit rate >= (total stream size in bits / stream duration in seconds)). Consider the following example: You configure a stream with an average bit rate of 16,000 bits per second, a peak bit rate of 48,000 bits per second, and a peak buffer window of 3,000 (3 seconds). The size of the buffer used for the stream is 144,000 bits (48,000 bits per second \* 3 seconds) as determined by the peak values. The encoder compresses the data to conform to that buffer. Additionally, the average bit rate of the stream must be 16,000 or less. If the encoder must create large samples to handle a complex segment of content, it can take advantage of the large buffer size. But other parts of the stream must be encoded at a lower bit rate to bring the average down to the specified level. Peak-constrained VBR encoding is useful for playback devices with a finite buffer capacity and data rate constraints. A common example of this is the encoding used for DVDs when decoding is performed by a chip in a device, where there are hardware limitations that must be considered.

### Configuring the Encoder for Peak-Constrained VBR

Peak-constrained VBR is like [unconstrained VBR](unconstrained-variable-bit-rate--vbr--encoding.md) in that it is confined to an average bit rate over the duration of the stream. In addition, peak-constrained VBR conforms to a peak buffer. This buffer is described using a peak bit rate and a peak buffer window. This mode uses two encoding passes and gives the encoder flexibility in how it encodes individual samples while adhering to the peak limitations.

Encoder configuration is set through property values. These properties are defined in wmcodecdsp.h. The configuration properties must be set on the encoder before negotiating the output media type. For information about how to set properties on the encoder, see [Configuring the Encoder](configuring-the-encoder.md). Based on the specified property values, you can enumerate the supported VBR output types and select the required one on the encoder [Media Foundation transform](media-foundation-transforms.md) (MFT) based on the average bit rate.

You must set the following propertiesfor this type of encoding:

-   Specify the VBR encoding mode by setting the MFPKEY\_VBRENABLED property to VARIANT\_TRUE.
-   Set the MFPKEY\_PASSESUSED to 2 because peak-constrained VBR mode uses two encoding passes.
-   Set MFPKEY\_RMAX to specify the peak bit rate and set MFPKEY\_BMAX to specify the peak buffer window.
-   While enumerating the output media type, check the [**MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND**](mf-mt-audio-avg-bytes-per-second-attribute.md) attribute (for audio streams) or the [**MF\_MT\_AVG\_BITRATE**](mf-mt-avg-bitrate-attribute.md) attribute (for video streams) of the available output media types and choose an output media type that has the average bit rate closest to the desired average bit rate that you want the encoder to maintain in the encoded content. For more information about selecting the output media type, see [Media Type Negotiation on the Encoder](media-type-negotiation-on-the-encoder.md).

> [!Note]  
> It is recommended that you set the peak bit rate to at least twice the average bit rate. Setting the peak rate to a lower value may cause the encoder to encode the content as two-pass CBR instead of peak-constrained VBR.

 

To get the buffer window value set by the encoder, call **IWMCodecLeakyBucket::GetBufferSizeBits**, defined in wmcodecifaces.h, wmcodecdspuuid.lib, after the encoding session. To add unconstrained VBR support for the streams, you must set this value in the [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET2**](mf-asfstreamconfig-leakybucket2-attribute.md) attribute (peak leaky bucket values) on the stream configuration object while configuring the ASF profile.

The following code sample modifies the SetEncodingType method of the sample class CEncoder to set up the peak-constrained VBR mode. For information about this class, see [Encoder Example Code](encoder-example-code.md). For information about the helper macros used in this example, see Using the Media Foundation Code Examples.


```
//////////////////////////////////////////////////////////////////////////
//  Name: SetEncodingType
//  Description: Sets the encoding type to peak-constrained VBR mode.
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

    // Query the encoder for its property store.
    CHECK_HR(hr = m_pMFT->QueryInterface(__uuidof(IPropertyStore), (void**)&pProp));
    
    if (mode == EncodeMode_VBR_Peak)
    {
        // Set the VBR property to TRUE, which indicates VBR encoding.
        var.vt = VT_BOOL;
        var.boolVal = TRUE;
        CHECK_HR(hr = pProp->SetValue(MFPKEY_VBRENABLED, var));
        PropVariantClear(&var);

        // Set number of passes.
        var.vt = VT_I4;
        var.lVal  =2;
        CHECK_HR(hr = pProp->SetValue(MFPKEY_PASSESUSED, var));
        PropVariantClear(&var);

        // Set the peak bit rate.
        var.vt = VT_I4;
        var.lVal  =48000;
        CHECK_HR(hr = pProp->SetValue(MFPKEY_RMAX, var));
        PropVariantClear(&var);

        // Set the peak buffer window.
        var.vt = VT_I4;
        var.lVal  =3000;
        CHECK_HR(hr = pProp->SetValue(MFPKEY_BMAX, var));
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

 

 



