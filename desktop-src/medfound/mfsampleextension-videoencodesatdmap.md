---
description: Stores a map of the Sum of Absolute Differences (SATD) values used for each block in an encoded video frame. 
title: MFSampleExtension_VideoEncodeSatdMap attribute (Mfapi.h)
ms.topic: reference
ms.date: 03/29/2024
---

# MFSampleExtension\_VideoEncodeSatdMap attribute

Stores a map of the Sum of Absolute Differences (SATD) values used for each block in an encoded video frame. 

## Data type

An [IMFMediaBuffer](/windows/win32/api/mfobjects/nn-mfobjects-imfmediabuffer).

## Remarks

App developers can use the SATD map to analyze and optimize video encoding quality. The SATD values provide insight into the distortion between the original and reconstructed blocks after transformation. This information helps evaluate compression efficiency, identify quality inconsistencies, and fine-tune encoding parameters for improved visual fidelity and bitrate control.

The SATD map is a flat array of **uint32_t** values, where each value corresponds to a single block. To determine the map’s dimensions, divide the video frame width and height by the block size specified via [CODECAPI_AVEncVideoSatdMapBlockSize](codecapi-avencvideosatdmapblocksize.md). If the frame dimensions are not exact multiples of the block size, round the dimensions up to the nearest multiple. This yields the number of columns and rows. The SATD values are ordered from left to right, top to bottom, in row major fashion.


Use [IMFAttributes::SetUnknown](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-setunknown) to attach an **IMFMediaBuffer** containing the QP map to an output sample. Use [IMFAttributes::GetUnknown](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-getunknown) to retrieve the **IMFMediaBuffer** containing the QP map from an output sample.  

The SATD map is only generated when the entire frame has been encoded. If the encoder processes the frame in multiple slices, the SATD map should be attached [IMFSample](/windows/win32/api/mfobjects/nn-mfobjects-imfsample) of the final slice.

The interpretation of the 8-bit QP values in the QP map depends on the valid QP range defined by the applicable codec specification. For higher bit depths (e.g., 10-bit), some hardware vendors (IHVs) may use the internal quantizer index range (e.g., [-12, 51] for 10-bit HEVC) instead of the final encoded QP range (e.g., [0, 63]). This internal range reflects how QP values are adjusted relative to bit depth (Qp = qpY + QpBdOffsetY) during transform and quantization steps, as specified in the codec standard. Consumers of the QP map should consult the driver documentation to correctly interpret these values and apply appropriate offset correction if necessary.

## Examples

The following example shows a helper function that can be used by implementations of an encoder MFT that supports **ICodecAPI**. The function demonstrates how to check if SATD map reporting is enabled on the encoder MFT. If it is enabled, the function shows how to attach the SATD map onto the output sample. This assumes that each output sample contains a complete frame. If the encoder uses multiple slices, the SATD map should be attached only to the IMFSample of the last slice.

```cpp
#include <mfapi.h> 
#include <mfobjects.h> 
#include <codecapi.h> 
#include <wil/com.h> 
#include <wil/resource.h> 

// Function to query and attach SATD map to output samples 

HRESULT ReportSatdMapOnOutputSample( 
    _In_ IMFTransform* encoder,
    _In_ IMFSample* outputSample,
    _In_ IMFMediaBuffer* satdMap // IMFMediaBuffer could be the GPU resource for SATD map if using hardware encoder 
)  
{ 
    RETURN_HR_IF_NULL(E_INVALIDARG, encoder); 
    RETURN_HR_IF_NULL(E_INVALIDARG, outputSample); 
    RETURN_HR_IF_NULL(E_INVALIDARG, satdMap); 

    // Query the encoder's codec API to check if SATD Map reporting is enabled 
    wil::com_ptr_nothrow<ICodecAPI> codecAPI; 
    RETURN_IF_FAILED(wil::com_query_to_nothrow(encoder, &codecAPI)); 

    wil::unique_variant value;
    (void) codecAPI->GetValue(&CODECAPI_AVEncVideoSatdMapBlockSize, &value);
    if (value.vt != VT_UI4 || !value.ulVal) {
        return S_OK; // SATD Map reporting is not enabled
    }

    // Attach the IMFMediaBuffer (SATD Map) to the output sample's attributes
    wil::com_ptr_nothrow<IMFAttributes> sampleAttributes;
    RETURN_IF_FAILED(wil::com_ptr_nothrow(outputSample, &sampleAttributes));

    return sampleAttributes->SetUnknown(MFSampleExtension_VideoEncodeSatdMap, satdMap);
} 
```

The following example demonstrates how an app can retrieve the SATD map data from the **IMFSample** objects that are produced by an encoder MFT.  

```cpp
#include <mfapi.h>
#include <mfobjects.h>
#include <codecapi.h>
#include <wil/com.h>
#include <wil/resource.h>

// Function to retrieve the SATD map from an output sample.
// The output parameter will be set to a null pointer if the output sample does not have a SATD map.
HRESULT RetrieveSatdMapFromOutputSample(
    _In_ IMFSample* outputSample, 
    _COM_Outptr_result_maybenull_ IMFMediaBuffer** satdMapBuffer // Output: IMFMediaBuffer containing the SATD map
)
{
    RETURN_HR_IF_NULL(E_INVALIDARG, satdMapBuffer);
    *satdMapBuffer = nullptr;

    RETURN_HR_IF_NULL(E_INVALIDARG, outputSample);

    // Retrieve the sample attributes
    wil::com_ptr_nothrow<IMFAttributes> sampleAttributes;
    if (SUCCEEDED(wil::com_query_to_nothrow(outputSample, &sampleAttributes)))
    {
        // Retrieve the IMFMediaBuffer associated with the SATD map
        HRESULT hr = sampleAttributes->GetUnknown(MFSampleExtension_VideoEncodeSatdMap, IID_PPV_ARGS(satdMapBuffer));
        RETURN_HR_IF(hr, hr != S_OK && hr != MF_E_ATTRIBUTENOTFOUND);
    }
    return S_OK;
}
```

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client | Windows 11, build 26100   |
| Minimum supported server | Windows Server 2025   |
| Header               | mfapi.h |
