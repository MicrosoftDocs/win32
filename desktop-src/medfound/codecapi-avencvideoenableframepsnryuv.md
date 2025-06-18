---
description: Enables or disables quality metrics reporting by an encoder MFT.
title: CODECAPI_AVEncVideoEnableFramePsnrYuv property (Codecapi.h)
ms.topic: reference
ms.date: 06/12/2025
---

# CODECAPI\_AVEncVideoEnableFramePsnrYuv

Enables or disables quality metrics reporting by an encoder MFT.

## Data type

**BOOL** (VT\_BOOL)

## Property GUID

**CODECAPI\_AVEncVideoEnableFramePsnrYuv**

## Property value

If the value is **TRUE**, quality metrics reporting is enabled. If the value is **FALSE**, quality metrics reporting is disabled. The default value is **FALSE**.

## Remarks

When enabled, [Peak Signal-to-Noise Ratio (PSNR)](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio) quality metrics are included in the encoder’s output samples. The [MFSampleExtension_FramePsnrYuv](mfsampleextension-framepsnryuv.md) MF attribute is used to carry the quality metrics.

Use [ICodecAPI::IsSupported](/windows/win32/api/strmif/nf-strmif-icodecapi-issupported) to check if the encoder supports this property. Use [ICodecAPI::GetValue](/windows/win32/api/strmif/nf-strmif-icodecapi-getvalue) to query the value of this property. Use [ICodecAPI::SetValue](/windows/win32/api/strmif/nf-strmif-icodecapi-setvalue) to configure this property.

Note that while the variant type of the CODECAPI_AVEncVideoEnableFramePsnrYuv property is VT_BOOL, [IMFAttributes](/windows/win32/api/mfobjects/nn-mfobjects-imfattributes) does not support Boolean attributes. Therefore, you should use [SetUINT32](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-setuint32) instead. Any non-zero value is interpreted as **TRUE**. The attribute value will be automatically converted to a VT_BOOL property value when it is transferred to the encoder MFT.

## Example

The following example demonstrates using the CODECAPI_AVEncVideoEnableFramePsnrYuv property to configure an encoder MFT to enable or disable the frame PSNR of YUV planes feature.

```cpp
#include <codecapi.h> 
#include <mfapi.h>
#include <wil.com.h>
#include <wil/result_macros.h>

//  Enable or disable the quality metrics feature for an encoder MFT. 
//  This function assumes that the encoder MFT supports ICodecAPI interface. 
//  It checks whether the property CODECAPI_AVEncVideoEnableFramePsnrYuv is supported. 
//  If not supported, it returns E_NOTIMPL. 

HRESULT ConfigureEncoderForFramePsnrYuv(_In_ IMFTransform* encoder) 
{ 
    wil::com_ptr_nothrow<ICodecAPI> codecAPI; 

    RETURN_IF_FAILED(wil::com_query_to_nothrow(encoder, &codecAPI)); 

    // Check if the encoder supports quality metrics reporting 
    if (!codecAPI->IsSupported(&CODECAPI_AVEncVideoEnableFramePsnrYuv)) 
    { 
        return E_NOTIMPL; 
    } 

    // Configure the encoder to enable quality metrics reporting 
    wil::unique_variant valueVARIANT value{}; 
    value.vt = VT_BOOL; 
    value.boolVal = VARIANT_TRUE; // VARIANT_FALSE: disable; VARIANT_TRUE: enable 

    return codecAPI->SetValue(&CODECAPI_AVEncVideoEnableFramePsnrYuv, &value); 
} 
```

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client | Windows 11, build 26100   |
| Minimum supported server | Windows Server 2025   |
| Header               | Codecapi.h |



## See also

- [Media Foundation Properties](media-foundation-properties.md)
- [**ICodecAPI**](/windows/desktop/api/strmif/nn-strmif-icodecapi)


 

