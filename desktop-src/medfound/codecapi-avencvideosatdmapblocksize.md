---
description: Specifies the block size used in generating the Sum of Absolute Differences (SATD) map that the video encoder attaches to output IMFSamples.
title: CODECAPI_AVEncVideoSatdMapBlockSize property (Codecapi.h)
ms.topic: reference
ms.date: 06/12/2025
---

# CODECAPI\_AVEncVideoSatdMapBlockSize property

Specifies the block size used in generating the Sum of Absolute Differences (SATD) map that the video encoder attaches to output IMFSamples.

## Data type

**ULONG** (VT\_UI4)

## Property GUID

**CODECAPI\_AVEncVideoSatdMapBlockSize**

## Property value

The block size used in generating the Sum of Absolute Differences (SATD) map that the video encoder attaches to output IMFSamples. The value must be a power of 2, such as 16 or 32. Setting the block size to 0 disables SATD map reporting. SATD map reporting is disabled by default.

## Remarks

The block size enables apps to determine the number of columns and rows SATD map. This is done by dividing the video frame width and height by the block size. For example, if the block size is 16 and the video frame has the size of 1920x1080, the SATD map has 120 columns and 68 rows. If the video frame width or height is not an exact multiple of the block size, the value should be rounded up to the next multiple of the block size. For example, for a frame with a resolution of 1920x1080 example, 1080 is not an exact multiple of 16, so the frame size id rounded up to 1088 to produce 68 rows. The extra pixels resulting from the rounding contribute a sum of zero to the SATD.

Use [ICodecAPI::IsSupported](/windows/win32/api/strmif/nf-strmif-icodecapi-issupported) to check if the encoder supports this property. Use [ICodecAPI::GetValue](/windows/win32/api/strmif/nf-strmif-icodecapi-getvalue) to query the value of this property. Use [ICodecAPI::SetValue](/windows/win32/api/strmif/nf-strmif-icodecapi-setvalue) to configure this property. Values that are not a power of 2, or 0, result in an **E_INVALIDARG** return value from **SetValue**.

## Examples

The following example demonstrates how to use the **CODECAPI_AVEncVideoSatdMapBlockSize** property to configure an encoder MFT to enable or disable the SATD map reporting feature. If the block size value is zero, it is disabled. If the block size value is not zero, it is enabled.

```cpp
#include <codecapi.h>
#include <mfapi.h>
#include <wil/com.h>

//  Inform an encoder MFT to enable or disable the SATD map reporting feature.
//  This function assumes that the encoder MFT supports ICodecAPI interface.
//  It checks whether the new property CODECAPI_AVEncVideoSatdMapBlockSize is supported.
//  If not supported, it returns E_NOTIMPL.
//  If CODECAPI_AVEncVideoSatdMapBlockSize is supported and block size is none zero, it is enabled.
//  Otherwise, it is disabled.
HRESULT ConfigureEncoderForSatdMap(_In_ IMFTransform* encoder, uint32_t blockSize)
{
    wil::com_ptr_nothrow<ICodecAPI> codecAPI;

    RETURN_IF_FAILED(wil::com_query_to_nothrow(encoder, &codecAPI));
    
    // Check if the encoder supports the property for SATD map
    if (!codecAPI->IsSupported(&CODECAPI_AVEncVideoSatdMapBlockSize))
    {
        return E_NOTIMPL;
    }
    
    // configure encoder
    wil::unique_variant value;
    value.vt = VT_UI4;
    value.ulVal = blockSize; // zero: disable; non-zero: enable
    return codecAPI->SetValue(&CODECAPI_AVEncVideoSatdMapBlockSize, &value);
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

 

