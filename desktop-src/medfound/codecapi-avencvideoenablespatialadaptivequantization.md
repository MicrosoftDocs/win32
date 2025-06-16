---
description: Enables or disables spatial adaptive quantization (AQ) in an encoder MFT.
title: CODECAPI_AVEncVideoEnableSpatialAdaptiveQuantization property (Codecapi.h)
ms.topic: reference
ms.date: 06/12/2025
---

# CODECAPI\_AVEncVideoEnableSpatialAdaptiveQuantization property

Enables or disables spatial adaptive quantization (AQ) in an encoder MFT.

## Data type

**BOOL** (VT\_BOOL)

## Property GUID

**CODECAPI\_AVEncVideoEnableSpatialAdaptiveQuantization**

## Property value

If the value is **TRUE**, AQ is enabled. If the value is **FALSE**, AQ is disabled. The default value is implementation-dependent.

## Remarks

When AQ is enabled, if the implementation of AQ supports multiple AQ strengths, the default AQ strength will be used.

When AQ is enabled, the [CODECAPI_AVEncVideoEncodeQP](codecapi-avencvideoencodeqp.md) value is not strictly followed, as AQ dynamically adjusts Quantization Parameter (QP) values. When AQ is enabled, the [CODECAPI_AVEncVideoMaxQP](codecapi-avencvideomaxqp.md) and [CODECAPI_AVEncVideoMinQP](codecapi-avencvideominqp.md) values are still used as the upper and lower bounds for QP by the AQ algorithm.

Use [ICodecAPI::IsSupported](/windows/win32/api/strmif/nf-strmif-icodecapi-issupported) to check if the encoder supports this property. Use [ICodecAPI::GetValue](/windows/win32/api/strmif/nf-strmif-icodecapi-getvalue) to query the value of this property. Use [ICodecAPI::SetValue]((/windows/win32/api/strmif/nf-strmif-icodecapi-setvalue)) to configure this property.

Note that while the variant type of the CODECAPI_AVEncVideoEnableSpatialAdaptiveQuantization property is VT_BOOL, [IMFAttributes](/windows/win32/api/mfobjects/nn-mfobjects-imfattributes) does not support Boolean attributes. Therefore, you should use [SetUINT32](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-setuint32) instead. Any non-zero value is interpreted as **TRUE**. The attribute value will be automatically converted to a VT_BOOL property value when it is transferred to the encoder MFT.

## Examples

The following example demonstrates how to use the **CODECAPI_AVEncVideoEnableSpatialAdaptiveQuantization** property to configure an encoder MFT to enable or disable the spatial adaptive quantization feature.

```cpp
#include <codecapi.h> 
#include <mfapi.h> 

//  Inform an encoder MFT to enable or disable the spatial adaptive quantization feature. 
//  This function assumes that the encoder MFT supports ICodecAPI interface. 
//  It checks whether the new property CODECAPI_AVEncVideoEnableSpatialAdaptiveQuantization is supported. 
//  If not supported, it returns E_NOTIMPL. 

HRESULT ConfigureEncoderForSpatialAdaptiveQuantization(_In_ IMFTransform* encoder) 
{ 
    wil::com_ptr_nothrow<ICodecAPI> codecAPI; 
    RETURN_IF_FAILED(wil::com_query_to_nothrow(encoder, &codecAPI)); 

    // Check if the encoder supports the property for controlling the usage of spatial adaptive quantization 
    if (!codecAPI->IsSupported(&CODECAPI_AVEncVideoEnableSpatialAdaptiveQuantization)) 
    { 
        return E_NOTIMPL; 
    } 

    // Configure the encoder to enable spatial adaptive quantization 
    VARIANT value{}; 
    value.vt = VT_BOOL; 
    value.boolVal = VARIANT_TRUE; // VARIANT_FALSE: disable; VARIANT_TRUE: enable 
    return codecAPI->SetValue(&CODECAPI_AVEncVideoEnableSpatialAdaptiveQuantization, &value); 
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

 

