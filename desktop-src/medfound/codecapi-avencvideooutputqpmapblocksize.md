---
description: Specifies the block size used in generating the output metadata quantization parameter (QP) map from the encoder.
title: CODECAPI_AVEncVideoOutputQPMapBlockSize property (Codecapi.h)
ms.topic: reference
ms.date: 06/12/2025
---

# CODECAPI\_AVEncVideoOutputQPMapBlockSize property

Specifies the block size used in generating the output metadata quantization parameter (QP) map from the encoder.

## Data type

**ULONG** (VT\_UI4)

## Property GUID

**CODECAPI\_AVEncVideoOutputQPMapBlockSize**

## Property value

The block size. The value must be a power of 2, such as 16 or 32. Setting the block size to 0 disables QP map block size reporting. QP map block size reporting is disabled by default.

## Remarks

The block size used in generating the output metadata QP map from the encoder. With the block size, applications can derive the columns and rows of the output metadata QP map by the video frame width and height divided by the block size. For example, if the block size is 16 and the video frame has the size of 1920x1080, the QP map has 120 columns and 68 rows. If the video frame width/height is not an exact multiple of the block size, round up the width/height to the next multiple of the block size. For example, if the frame size is 1916x1076 and block size is 16, the rounded up frame size is 1920x1088.

Use [ICodecAPI::IsSupported](/windows/win32/api/strmif/nf-strmif-icodecapi-issupported) to check if the encoder supports this property. Use [ICodecAPI::GetValue](/windows/win32/api/strmif/nf-strmif-icodecapi-getvalue) to query the value of this property. Use [ICodecAPI::SetValue]((/windows/win32/api/strmif/nf-strmif-icodecapi-setvalue)) to configure this property. Values that are not a power of 2, or 0, result in an **E_INVALIDARG** return value from **SetValue**.

## Examples

The following example demonstrates how to use the **CODECAPI_AVEncVideoOutputQPMapBlockSize** property to configure an encoder MFT to enable or disable the QP map reporting feature. If the block size value is zero, it is disabled. If the block size value is not zero, it is enabled.

```cpp
#include <codecapi.h> 
#include <mfapi.h> 

//  Inform an encoder MFT to enable or disable the QP map reporting feature. 
//  This function assumes that the encoder MFT supports ICodecAPI interface. 
//  It checks whether the new property CODECAPI_AVEncVideoOutputQPMapBlockSize is supported. 
//  If not supported, it returns E_NOTIMPL. 
//  If CODECAPI_AVEncVideoOutputQPMapBlockSize is supported and block size is none zero, it is enabled. 
//  Otherwise, it is disabled. 

HRESULT ConfigureEncoderForQPMap(_In_ IMFTransform* encoder, uint32_t blockSize) 
{ 

    wil::com_ptr_nothrow<ICodecAPI> codecAPI; 
    RETURN_IF_FAILED(wil::com_query_to_nothrow(encoder, &codecAPI)); 

    // Check if the encoder supports the property for QP map 
    if (!codecAPI->IsSupported(&CODECAPI_AVEncVideoOutputQPMapBlockSize)) 
    { 
        return E_NOTIMPL; 
    } 

    // configure encoder 
    wil::unique_variant value; 
    value.vt = VT_UI4; 
    value.ulVal = blockSize; // zero: disable; non-zero: enable 

    return codecAPI->SetValue(&CODECAPI_AVEncVideoOutputQPMapBlockSize, &value); 
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

 

