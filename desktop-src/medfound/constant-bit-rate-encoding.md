---
description: Constant Bit Rate Encoding
ms.assetid: 0f084f3f-7432-4514-ae6a-c8179a99dec7
title: Constant Bit Rate Encoding
ms.topic: article
ms.date: 05/31/2018
---

# Constant Bit Rate Encoding

In constant bit rate (CBR) encoding, the encoder knows the bit rate of the output media samples and the buffer window (leaky bucket parameters) before the encoding session begins. The encoder uses the same number of bits to encode each second of sample throughout the duration of the file to achieve the target bit rate for a stream. This limits the variation in the size of the stream samples. Also, during the encoding session the bit rate is not exactly at the specified value but remains close to the target bit rate.

CBR encoding is useful when you want to know the bit rate or approximate duration of a file without parsing the entire file. This is required in live streaming scenarios where the media content needs to be streamed at a predictable bit rate and with consistent bandwidth usage.

The disadvantage of CBR encoding is that the quality of the encoded content will not be constant. Because some content is more difficult to compress, parts of a CBR stream will be of lower quality than others. For example, a typical movie has some scenes that are fairly static and some scenes that are full of action. If you encode a movie using CBR, the scenes that are static, and therefore easy to encode efficiently, will be of higher quality than the action scenes, which would have required higher sample sizes to maintain the same quality.

In general, variations in the quality of a CBR file are more pronounced at lower bit rates. At higher bit rates, the quality of a CBR-encoded file will still vary, but the quality issues will be less noticeable to the user. When using CBR encoding, you should set the bandwidth as high as your delivery scenario allows.

-   [CBR Configuration Settings](#cbr-configuration-settings)
-   [Leaky Bucket Settings](#leaky-bucket-settings)

### CBR Configuration Settings

You must configure an encoder by specifying the type of encoding and the various stream specific settings before the encoding session.

**To configure the encoder for CBR encoding**

1.  Specify the CBR encoding mode.

    By default, the encoder is configured to use CBR encoding. Encoder configuration is set through property values. These properties are defined in wmcodecdsp.h. You can explicitly specify this mode by setting the [**MFPKEY\_VBRENABLED**](mfpkey-vbrenabledproperty.md) property to VARIANT\_FALSE. For information about how to set properties on encoders, see [Configuring the Encoder](configuring-the-encoder.md).

2.  Choose the encoding bit rate.

    For CBR encoding, you must know the bit rate at which you want to encode the stream before the encoding session begins. You must set the bit rate during while you are configuring the encoder. To do this, while you are performing media type negotiation, check the [**MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND**](mf-mt-audio-avg-bytes-per-second-attribute.md) attribute (for audio streams) or the [**MF\_MT\_AVG\_BITRATE**](mf-mt-avg-bitrate-attribute.md) attribute (for video streams) of the available output media types and choose an output media type that has the average bit rate closest to the target bit rate you want to achieve. For more information, see [Media Type Negotiation on the Encoder](media-type-negotiation-on-the-encoder.md).

The following code example shows the implementation for SetEncodingProperties. This function sets stream level encoding properties for CBR and VBR.


```C++
//-------------------------------------------------------------------
//  SetEncodingProperties
//  Create a media source from a URL.
//
//  guidMT:  Major type of the stream, audio or video
//  pProps:  A pointer to the property store in which 
//           to set the required encoding properties.
//-------------------------------------------------------------------

HRESULT SetEncodingProperties (const GUID guidMT, IPropertyStore* pProps)
{
    if (!pProps)
    {
        return E_INVALIDARG;
    }

    if (EncodingMode == NONE)
    {
        return MF_E_NOT_INITIALIZED;
    }
   
    HRESULT hr = S_OK;

    PROPVARIANT var;

    switch (EncodingMode)
    {
        case CBR:
            // Set VBR to false.
            hr = InitPropVariantFromBoolean(FALSE, &var);
            if (FAILED(hr))
            {
                goto done;
            }

            hr = pProps->SetValue(MFPKEY_VBRENABLED, var);
            if (FAILED(hr))
            {
                goto done;
            }

            // Set the video buffer window.
            if (guidMT == MFMediaType_Video)
            {
                hr = InitPropVariantFromInt32(VIDEO_WINDOW_MSEC, &var);
                if (FAILED(hr))
                {
                    goto done;
                }

                hr = pProps->SetValue(MFPKEY_VIDEOWINDOW, var);    
                if (FAILED(hr))
                {
                    goto done;
                }
            }
            break;

        case VBR:
            //Set VBR to true.
            hr = InitPropVariantFromBoolean(TRUE, &var);
            if (FAILED(hr))
            {
                goto done;
            }

            hr = pProps->SetValue(MFPKEY_VBRENABLED, var);
            if (FAILED(hr))
            {
                goto done;
            }

            // Number of encoding passes is 1.

            hr = InitPropVariantFromInt32(1, &var);
            if (FAILED(hr))
            {
                goto done;
            }

            hr = pProps->SetValue(MFPKEY_PASSESUSED, var);
            if (FAILED(hr))
            {
                goto done;
            }

            // Set the quality level.

            if (guidMT == MFMediaType_Audio)
            {
                hr = InitPropVariantFromUInt32(98, &var);
                if (FAILED(hr))
                {
                    goto done;
                }

                hr = pProps->SetValue(MFPKEY_DESIRED_VBRQUALITY, var);    
                if (FAILED(hr))
                {
                    goto done;
                }
            }
            else if (guidMT == MFMediaType_Video)
            {
                hr = InitPropVariantFromUInt32(95, &var);
                if (FAILED(hr))
                {
                    goto done;
                }

                hr = pProps->SetValue(MFPKEY_VBRQUALITY, var);    
                if (FAILED(hr))
                {
                    goto done;
                }
            }
            break;

        default:
            hr = E_UNEXPECTED;
            break;
    }    

done:
    PropVariantClear(&var);
    return hr;
}
```



### Leaky Bucket Settings

For CBR encoding, the average and the maximum leaky bucket values for the stream are the same. For more information about these parameters, see [The Leaky Bucket Buffer Model](the-leaky-bucket-buffer-model.md).

To CBR-encode audio streams, you need to set the leaky bucket values after negotiating the output media type on the encoder. The encoder calculates the buffer window internally based on the average bit rate set on the output media type.

To set leaky bucket values create an array of DWORDs can set the following values in the [**MFPKEY\_ASFSTREAMSINK\_CORRECTED\_LEAKYBUCKET**](mfpkey-asfstreamsink-corrected-leakybucket-property.md) property in the media sink's property store. For more information, see [Setting Properties in the File Sink](setting-properties-in-the-file-sink.md).

-   Average bit rate: Get the average bit rate from the output media type that is selected during media type negotiation. Use the [**MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND**](mf-mt-audio-avg-bytes-per-second-attribute.md) attribute.
-   Buffer window: Query the encoder for the [**IWMCodecLeakyBucket**](/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmcodecleakybucket) interface and then call [**IWMCodecLeakyBucket::GetBufferSizeBits**](../wmformat/iwmcodecleakybucket-getbuffersizebits.md) (wmcodecifaces.h, wmcodecdspuuid.lib).
-   Initial buffer size: Set to 0.

## Related topics

<dl> <dt>

[ASF Encoding Types](asf-encoding-types.md)
</dt> <dt>

[Tutorial: 1-Pass Windows Media Encoding](tutorial--1-pass-windows-media-encoding.md)
</dt> <dt>

[Tutorial: Writing a WMA File by Using CBR Encoding](tutorial--writing-a-wma-file-by-using-cbr-encoding.md)
</dt> </dl>

 

 
