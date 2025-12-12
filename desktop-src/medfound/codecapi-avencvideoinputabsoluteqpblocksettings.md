---
description: Read-only property that specifies the settings that the encoder MFT supports for absolute QP input values.
title: CODECAPI_AVEncVideoInputAbsoluteQPBlockSettings property (Codecapi.h)
ms.topic: reference
ms.date: 12/09/2025
---

# CODECAPI\_AVEncVideoInputAbsoluteQPBlockSettings property

Read-only property that specifies the settings that the encoder MFT supports for absolute QP input values.

## Data type

[InputQPSettings](/windows/win32/api/mfapi/ns-mfapi-inputqpsettings) (VT\_BLOB)

## Property GUID

**CODECAPI\_AVEncVideoInputAbsoluteQPBlockSettings**

## Property value

The value of this property is an **InputQPSettings** structure. If the property is present, the video encoder MFT supports receiving absolute QP values that conform to the settings provided by the **InputQPSettings** structure. If the property is missing, the video encoder MFT does not support receiving absolute QP values.

When supported, absolute QP values can be provided as input for the video encoder MFT to apply during the quantization step of the encoding process. The [MFSampleExtension_VideoEncodeInputAbsoluteQPMap](mfsampleextension-videoencodeinputabsoluteqpmap.md) attribute is used to provide the QP values.


## Remarks

Each element in the QP map represents a square block of pixels, with a side of N pixels, making the total number of pixels contained within such a block N2 (NxN). The block size is specified as the number of pixels on one side of the square block (i.e., the value N.) The size of such blocks maps to Luma pixels.

Use [ICodecAPI::IsSupported](/windows/win32/api/icodecapi/nf-icodecapi-icodecapi-issupported) to check if the encoder supports receiving absolute QP values.

Use [ICodecAPI::GetValue](/windows/win32/api/icodecapi/nf-icodecapi-icodecapi-getvalue) to obtain the values represented within the **InputQPSettings** struct using the VT_BLOB interface. This is a ready-only property and therefore calling [ICodecAPI::SetValue](/windows/win32/api/icodecapi/nf-icodecapi-icodecapi-getvalue) will have no effect.

The **minBlockSize** and **maxBlockSize** fields of the **InputQPSettings** structure may have the same value, indicating that the encoder only supports a single block size.

Rectangular blocks of size MxN (e.g., 32x16), are not supported.

Providing absolute QP values may conflict and have an overriding effect on bitrate properties like [AVEncCommonMeanBitRate](/windows/win32/codecapi/avenccommonmeanbitrate-property) or [CODECAPI_AVEncCommonMaxBitRate](/windows/win32/codecapi/avenccommonmaxbitrate-property).


## Examples

The following example demonstrates how to use the **CODECAPI_AVEncVideoInputAbsoluteQPSettings** property to check if an encoder MFT supports receiving absolute QP maps. The function prints the minimum and maximum supported block sizes, and the stepping value. This information can be used by the app to choose an appropriate block size for the absolute QP map.

```cpp
#include <mfapi.h>
#include <codecapi.h>
#include <stdio.h>
#include <wil/resource.h>
#include <wil/result_macros.h>


//  This function assumes that the encoder MFT supports ICodecAPI interface.
//  It checks whether the property CODECAPI_AVEncVideoInputAbsoluteQPBlockSettings is supported.
HRESULT PrintEncoderAbsoluteQPMinMaxDataType(_In_ IMFTransform* encoder)
{
    wil::com_ptr_nothrow<ICodecAPI> codecAPI;
    RETURN_IF_FAILED(wil::com_query_to_nothrow(encoder, &codecAPI));
    
    // Check if the encoder supports Absolute QP Block Settings reporting
    if (!codecAPI->IsSupported(&CODECAPI_AVEncVideoInputAbsoluteQPBlockSettings))
    {
        printf("The encoder does not support receiving absolute QP maps.\n");
        return S_OK;
    }

    // Retrieve the InputQPSettings blob via GetValue (VT_BLOB)
    wil::unique_variant var;
    RETURN_IF_FAILED(codecAPI->GetValue(&CODECAPI_AVEncVideoInputAbsoluteQPBlockSettings, &var));
    RETURN_HR_IF(E_UNEXPECTED, var.vt != VT_BLOB || var.blob.cbSize < sizeof(InputQPSettings));

    // Cast blob data to InputQPSettings
    const InputQPSettings* settings = reinterpret_cast<const InputQPSettings*>(var.blob.pBlobData);

    // Print QP value range and steps
    printf("QP Min   = %d\n", settings->minValue);
    printf("QP Max   = %d\n", settings->maxValue);
    printf("QP Step  = %u\n", settings->steps);

    // Decode and print dataType enum
    printf("QP Data Type = 0x%08X (", settings->dataType);
    switch (settings->dataType)
    {
    	case CODEC_API_QP_MAP_INT8:   printf("INT8");   break;
    	case CODEC_API_QP_MAP_INT16:  printf("INT16");  break;
    	case CODEC_API_QP_MAP_INT32:  printf("INT32");  break;
    	case CODEC_API_QP_MAP_UINT8:  printf("UINT8");  break;
    	case CODEC_API_QP_MAP_UINT16: printf("UINT16"); break;
    	case CODEC_API_QP_MAP_UINT32: printf("UINT32"); break;
    	default:                      printf("Unknown");break;
    }
    printf(")\n");
    PropVariantClear(&var);
    return S_OK;
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

 

