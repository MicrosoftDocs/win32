---
description: Quality-Based Variable Bit Rate Encoding
ms.assetid: e07c3f31-3d53-4250-9634-f66690357f26
title: Quality-Based Variable Bit Rate Encoding
ms.topic: article
ms.date: 05/31/2018
---

# Quality-Based Variable Bit Rate Encoding

Unlike [Constant Bit Rate Encoding](constant-bit-rate-encoding.md) (CBR), where the encoder strives to maintain a particular bit rate of the encoded media, in the variable bit rate (VBR) mode, the encoder strives to achieve the best possible quality of the encoded media. The primary difference between CBR and VBR is the size of the buffer window used. VBR-encoded streams usually have large buffer windows compared to CBR-encoded streams.

The quality of encoded content is determined by the amount of data that is lost when the content is compressed. Many factors affect the loss of data in the compression process; but in general, the more complex the original data and the higher the compression ratio, the more detail is lost in the compression process.

In quality-based VBR mode, you do not define a bit rate or a buffer window that the encoder must follow. Instead, you specify a level of quality for a digital media stream instead of a bit rate. The encoder compresses the content so that all samples are of comparable quality; this ensures that quality is consistent throughout the playback duration, regardless of the buffer requirements of the resulting stream.

Quality-based VBR encoding tends to create large compressed streams. In general, this type of encoding is well suited for local playback or high bandwidth network connections (or download and play). For example, you can write an application to copy songs from CD to ASF files on a computer. Using quality-based VBR encoding would ensure that all of the songs copied are of the same quality. In those cases, the consistent quality will provide a better user experience.

The disadvantage of quality-based VBR encoding is that there is really no way to know the size or bandwidth requirements of the encoded media before the encoding session, because the encoder uses a single encoding pass. This can make quality-based VBR-encoded files inappropriate for circumstances where memory or bandwidth are restricted, such as playing content on portable media players or streaming over a low-bandwidth network.

## Configuring the Encoder for Quality-Based VBR Encoding

Encoder configuration is set through property values. These properties are defined in wmcodecdsp.h. The configuration properties must be set on the encoder before negotiating the output media type. For information about how to set properties on the encoder, see [Configuring the Encoder](configuring-the-encoder.md).

The following list shows the properties you must set for this type of encoding:

-   Specify the VBR encoding mode by setting the **MFPKEY\_VBRENABLED** property to VARIANT\_TRUE.
-   Set the **MFPKEY\_PASSESUSED** to 1 because this VBR mode uses one encoding pass.
-   Set the desired quality level (from 0 to 100) by setting the **MFPKEY\_DESIRED\_VBRQUALITY** property. Quality-based VBR does not encode the content to any predefined buffer parameters. This quality level that will be maintained for the entire stream, regardless of the bit-rate requirements that result.
-   For video streams, set the average bit rate to a nonzero value in the [**MF\_MT\_AVG\_BITRATE**](mf-mt-avg-bitrate-attribute.md) attribute on the output media type of the encoder. The accurate bit rate is updated after the encoding session is complete.

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



## Related topics

<dl> <dt>

[ASF Encoding Types](asf-encoding-types.md)
</dt> </dl>

 

 



