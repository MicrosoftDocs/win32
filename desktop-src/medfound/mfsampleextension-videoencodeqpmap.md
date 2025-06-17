---
description: Stores a map of the Quantization Parameter (QP) values used for each block in an encoded video frame. 
title: MFSampleExtension_VideoEncodeQPMap attribute (Mfapi.h)
ms.topic: reference
ms.date: 03/29/2024
---

# MFSampleExtension\_VideoEncodeQPMap attribute

Stores a map of the Quantization Parameter (QP) values used for each block in an encoded video frame.

## Data type

An [IMFMediaBuffer](/windows/win32/api/mfobjects/nn-mfobjects-imfmediabuffer).

## Remarks

Accessing the QP map allows developers to analyze and optimize video encoding quality. This attribute allows them to evaluate compression efficiency, detect quality inconsistencies, and fine-tune encoding settings for better visual fidelity and bitrate control.

The QP map is an array of QP values with the type of **uint8_t**. Each block has one QP value. A developer should determine the QP map’s size using [CODECAPI_AVEncVideoOutputQPMapBlockSize](codecapi-avencvideooutputqpmapblocksize.md) and video frame width and height (Divide the width/height by the block size. If the width/height is not an exact multiple of the block size, round it up to the next multiple of the block size) . This provides the number of rows and columns, ensuring proper alignment with the video frame. The map is from left to right and top to bottom. 

Use [IMFAttributes::SetUnknown](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-setunknown) to attach an **IMFMediaBuffer** containing the QP map to an output sample. Use [IMFAttributes::GetUnknown](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-getunknown) to retrieve the **IMFMediaBuffer** containing the QP map from an output sample.  

The QP map should only be reported when the entire frame has completed encoding. If the encoder uses multiple slices, the PSNR buffer should be attached to the [IMFSample](/windows/win32/api/mfobjects/nn-mfobjects-imfsample) of the last slice. 

The interpretation of the 8-bit QP values in the QP map depends on the valid QP range defined by the applicable codec specification. For higher bit depths (e.g., 10-bit), some hardware vendors (IHVs) may use the internal quantizer index range (e.g., [-12, 51] for 10-bit HEVC) instead of the final encoded QP range (e.g., [0, 63]). This internal range reflects how QP values are adjusted relative to bit depth (Qp = qpY + QpBdOffsetY) during transform and quantization steps, as specified in the codec standard. Consumers of the QP map should consult the driver documentation to correctly interpret these values and apply appropriate offset correction if necessary.

## Examples

The following example shows a helper function that can be used by implementations of an encoder MFT that supports **ICodecAPI**. The function demonstrates how to check if QP map reporting is enabled on the encoder MFT. If it is enabled, the function shows how to attach the QP map onto the output sample. This assumes that each output sample contains a complete frame. If the encoder uses multiple slices, the QP map should be attached only to the **IMFSample** of the last slice.

```cpp
#include <mfapi.h> 
#include <mfobjects.h> 
#include <codecapi.h> 
#include <wil.com.h>
#include <wil/result_macros.h>

// Function to query and attach QP map to output samples 
HRESULT ReportQPMapOnOutputSample( 
    _In_ IMFTransform* encoder,  
    _In_ IMFSample* outputSample,  
    _In_ IMFMediaBuffer* qPMap // IMFMediaBuffer could be the GPU resource for QP map if using hardware encoder 
)  

{ 
    RETURN_HR_IF_NULL(E_INVALIDARG, encoder); 
    RETURN_HR_IF_NULL(E_INVALIDARG, outputSample); 
    RETURN_HR_IF_NULL(E_INVALIDARG, qPMap); 

    // Query the encoder's codec API to check if QP Map reporting is enabled 
    wil::com_ptr_nothrow<ICodecAPI> codecAPI; 
    RETURN_IF_FAILED(wil::com_query_to_nothrow(encoder, &codecAPI)); 

    wil::unique_variant value; 
    RETURN_IF_FAILED(codecAPI->GetValue(&CODECAPI_AVEncVideoOutputQPMapBlockSize, &value)); 

    if (value.vt != VT_UI4 || !value.ulVal) { 
        return S_OK; // QP Map not enabled 
    } 

    // Attach the IMFMediaBuffer (QP Map) to the output sample's attributes 
    wil::com_ptr_nothrow<IMFAttributes> sampleAttributes; 
    RETURN_IF_FAILED(wil::com_ptr_nothrow(outputSample, &sampleAttributes)); 

    return sampleAttributes->SetUnknown(MFSampleExtension_VideoEncodeQPMap, qPMap); 
} 
```

The following example demonstrates how an app can retrieve the QP map data from the **IMFSample** objects that are produced by an encoder MFT.  

```cpp
#include <mfapi.h> 
#include <mfobjects.h> 
#include <codecapi.h> 
#include <wil.com.h>
#include <wil/result_macros.h>

// Function to retrieve the QP map from an output sample. 
HRESULT RetrieveQPMapFromOutputSample( 
    _In_ IMFSample* outputSample,  
    _COM_Outptr_result_maybenull_ IMFMediaBuffer** qPMapBuffer // Output: IMFMediaBuffer containing the QP map 
) 
{ 
    RETURN_HR_IF_NULL(E_INVALIDARG, qPMapBuffer); 
    *qPMapBuffer = nullptr; 

    RETURN_HR_IF_NULL(E_INVALIDARG, outputSample); 

    // Retrieve the sample attributes 
    wil::com_ptr_nothrow<IMFAttributes> sampleAttributes; 
    RETURN_IF_FAILED(wil::com_query_to_nothrow(outputSample, &sampleAttributes)); 

 
    // Retrieve the IMFMediaBuffer associated with the QP map 
    (void)sampleAttributes->GetUnknown(MFSampleExtension_VideoEncodeQPMap, IID_PPV_ARGS(qPMapBuffer)); 

    return S_OK; 

}
```

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client | Windows 11, build 26100   |
| Minimum supported server | Windows Server 2025   |
| Header               | mfapi.h |
