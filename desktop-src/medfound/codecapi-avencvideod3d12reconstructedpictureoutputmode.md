---
description: Controls the output of Direct3D 12 reconstructed pictures from a D3D12-based video encoder.
title: CODECAPI_AVEncVideoD3D12ReconstructedPictureOutputMode property (Codecapi.h)
ms.topic: reference
ms.date: 05/20/2026
---

# CODECAPI\_AVEncVideoD3D12ReconstructedPictureOutputMode property

Controls the output of Direct3D 12 reconstructed pictures from a D3D12-based video encoder. The reconstructed picture is attached as an attribute on the output [IMFSample](/windows/win32/api/mfobjects/nn-mfobjects-imfsample).

## Data type

**ULONG** (VT\_UI4)

## Property GUID

**CODECAPI\_AVEncVideoD3D12ReconstructedPictureOutputMode**

## Property value

The value is a member of the [eAVEncVideoD3D12ReconstructedPictureOutputMode](/windows/win32/api/codecapi/ne-codecapi-eavencvideod3d12reconstructedpictureoutputmode) enumeration.

| Value | Meaning |
|-------|---------|
| **eAVEncVideoEncodeD3D12ReconstructedPictureMode\_None** (0) | The encoder does not return a reconstructed picture. This is the default. |
| **eAVEncVideoEncodeD3D12ReconstructedPictureMode\_Copy** (1) | The encoder returns a copy of the reconstructed picture. |
| **eAVEncVideoEncodeD3D12ReconstructedPictureMode\_Shared** (2) | The encoder returns the reconstructed picture without making a copy. The application must not modify the returned resource. |

## Remarks

This is a static property. Use [ICodecAPI::SetValue](/windows/win32/api/strmif/nf-strmif-icodecapi-setvalue) to configure this property. Use [ICodecAPI::IsSupported](/windows/win32/api/strmif/nf-strmif-icodecapi-issupported) to check if the encoder supports this property. Use [ICodecAPI::GetValue](/windows/win32/api/strmif/nf-strmif-icodecapi-getvalue) to query the value of this property.

When this property is set to a non-zero value, the encoder attaches the reconstructed picture to each output sample using the [MFSampleExtension_VideoEncodeD3D12ReconstructedPicture](mfsampleextension-videoencoded3d12reconstructedpicture.md) attribute.

The reconstructed picture is an [ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource) wrapped in an [IMFMediaBuffer](/windows/win32/api/mfobjects/nn-mfobjects-imfmediabuffer). App developers can use the reconstructed picture to show an accurate preview of the encoded video without having to decode the bitstream, or to analyze and optimize video encoding decisions for future frames.

## Examples

The following example shows how to configure a D3D12-based encoder MFT to enable or disable the reconstructed picture feature.

```cpp
#include <codecapi.h>
#include <mfapi.h>
#include <wil/com.h>

//  Inform an encoder MFT to enable or disable the reconstructed picture feature.
//  This function assumes that the encoder MFT supports ICodecAPI interface.
//  It checks whether the new property CODECAPI_AVEncVideoD3D12ReconstructedPictureOutputMode
//  is supported. If not supported, it returns E_NOTIMPL.
HRESULT ConfigureEncoderForD3D12ReconstructedPictureOutput(
    _In_ IMFTransform* encoder, uint32_t mode)
{
    RETURN_HR_IF(E_INVALIDARG, mode > 2);

    wil::com_ptr_nothrow<ICodecAPI> codecAPI;
    RETURN_IF_FAILED(wil::com_query_to_nothrow(encoder, &codecAPI));

    // Check if the encoder supports the property for reconstructed picture output mode
    if (!codecAPI->IsSupported(&CODECAPI_AVEncVideoD3D12ReconstructedPictureOutputMode))
    {
        return E_NOTIMPL;
    }

    // configure encoder
    wil::unique_variant value;
    value.vt = VT_UI4;
    value.ulVal = mode;
    return codecAPI->SetValue(
        &CODECAPI_AVEncVideoD3D12ReconstructedPictureOutputMode, &value);
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
- [MFSampleExtension_VideoEncodeD3D12ReconstructedPicture](mfsampleextension-videoencoded3d12reconstructedpicture.md)
- [eAVEncVideoD3D12ReconstructedPictureOutputMode](/windows/win32/api/codecapi/ne-codecapi-eavencvideod3d12reconstructedpictureoutputmode)
