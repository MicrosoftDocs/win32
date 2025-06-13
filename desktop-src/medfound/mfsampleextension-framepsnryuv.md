---
description: Stores Peak Signal-to-Noise Ratio (PSNR) values for the Y, U, and V planes of an encoded video frame.
title: MFSampleExtension_FramePsnrYuv attribute (Mfapi.h)
ms.topic: reference
ms.date: 03/29/2024
---

# MFSampleExtension\_FramePsnrYuv attribute

Stores Peak Signal-to-Noise Ratio (PSNR) values for the Y, U, and V planes of an encoded video frame.

## Data type

An [IMFMediaBuffer](/windows/win32/api/mfobjects/nn-mfobjects-imfmediabuffer) containing a [MFSampleExtensionPsnrYuv](/windows/win32/api/mfapi/ns-mfapi-mfsampleextensionpsnryuv.md) structure.

## Remarks

Use [IMFAttributes::SetUnknown](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-setunknown) to attach an **IMFMediaBuffer** containing the PSNR values to an output sample. Use [IMFAttributes::GetUnknown](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-getunknown) to retrieve the **IMFMediaBuffer** containing the PSNR values from an output sample. The **IMFMediaBuffer** contains memory that matches the size of the **MFSampleExtensionPsnrYuv** structure. 

PSNR should only be reported when the entire frame has completed encoding. If the encoder uses multiple slices, the PSNR buffer should be attached to the [IMFSample](/windows/win32/api/mfobjects/nn-mfobjects-imfsample) of the last slice. 

If the encoder only supports PSNR for the Y plane, the *psnrU* and *psnrV* fields shall be zero. 

[MFCreateDXGISurfaceBuffer](/windows/win32/api/mfapi/nf-mfapi-mfcreatedxgisurfacebuffer) can be used to convert a GPU resource into an **IMFMediaBuffer**.

## Examples

The following sample shows a helper function that can be used by implementations of an encoder MFT that supports **ICodecAPI**. The function shows how to check if quality metrics reporting is enabled on the encoder MFT. If it is enabled, the function shows how to attach the quality metrics onto the output sample. This assumes that each output sample contains a complete frame. If the encoder uses multiple slices, the quality metrics should be attached only to the **IMFSample** of the last slice.

```cpp
#include <mfapi.h> 
#include <mfobjects.h> 
#include <codecapi.h> 
#include <wrl.h> 

// Function to query and attach PSNR values to output samples 
HRESULT ReportPsnrOnOutputSample( 
    _In_ IMFTransform* encoder,  
    _In_ IMFSample* outputSample,  
    _In_ IMFMediaBuffer* psnrBuffer // Pre-created buffer containing PSNR values 
) 
{

    RETURN_HR_IF_NULL(E_INVALIDARG, encoder); 
    RETURN_HR_IF_NULL(E_INVALIDARG, outputSample); 
    RETURN_HR_IF_NULL(E_INVALIDARG, psnrBuffer); 

    // Check if quality metrics (Frame PSNR) are enabled 
    wil::com_ptr_nothrow<ICodecAPI> codecAPI; 
    RETURN_IF_FAILED(wil::com_query_to_nothrow(encoder, &codecAPI)); 

    wil::unique_variant value; 
    RETURN_IF_FAILED(codecAPI->GetValue(&CODECAPI_AVEncVideoEnableFramePsnrYuv, &value)); 

    if (value.vt != VT_BOOL || !value.boolVal) {
        return S_OK; // Frame PSNR metric not enabled 
    } 

    // Retrieve the sample attributes 
    wil::com_ptr_nothrow<IMFAttributes> sampleAttributes; 
    RETURN_IF_FAILED(wil::com_query_to_nothrow(outputSample, &sampleAttributes)); 

    // Attach the pre-created IMFMediaBuffer to the sample's attributes 
    return sampleAttributes->SetUnknown(MFSampleExtension_FramePsnrYuv, psnrBuffer); 
```

The following example demonstrates how an app can retrieve the quality metrics data from the **IMFSample** objects that are produced by an encoder MFT.

```cpp
#include <mfapi.h> 
#include <mfobjects.h> 
#include <wrl.h> 

 

// Function to retrieve the quality metrics from an IMFSample that an encoder MFT has provided as its 
// output. 
// The function sets the output parameter "found", to true, if quality metrics were retrieved. 

HRESULT RetrievePsnrFromOutputSample( 
    _In_ IMFSample* outputSample,  
    _Out_ MFSampleExtensionPsnrYuv* psnrValues, 
    _Out_ bool* found 
) 
{ 
    RETURN_HR_IF_NULL(E_INVALIDARG, psnrValues); 
    *psnrValues = {}; 
    *found = false; 

    RETURN_HR_IF_NULL(E_INVALIDARG, outputSample); 

    // Retrieve the sample attributes 
    wil::com_ptr_nothrow<IMFAttributes> sampleAttributes; 
    RETURN_IF_FAILED(wil::com_query_to_nothrow(outputSample, &sampleAttributes)); 

    // Retrieve the IMFMediaBuffer containing the PSNR values 
    wil::com_ptr_nothrow<IMFMediaBuffer> psnrBuffer; 

    if (SUCCEEDED(sampleAttributes->GetUnknown(MFSampleExtension_FramePsnrYuv, IID_PPV_ARGS(&psnrBuffer)))) 
    { 
        BYTE* bufferData; 
        DWORD bufferSize; 
        RETURN_IF_FAILED(psnrBuffer->Lock(&bufferData, nullptr, &bufferSize)); 

        // Validate that the size if of the data contained in the IMFMediaBuffer matches what we expect. 
        // In this code sample, we choose to return an error if fail to retrieve the quality metrics. 

        if (bufferSize <!= (DWORD)sizeof(*psnrValues)) 
        {
            psnrBuffer->Unlock(); 
            RETURN_HR(MF_E_BUFFERTOOSMALLFAIL); 
        } 

        memcpy(psnrValues, bufferData, sizeof(*psnrValues)); 
        psnrBuffer->Unlock(); 
        *found = true;
    } 

    return S_OK; 

} 
```

## Requirements

| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 24H2<br/>                          |
| Minimum supported server<br/> | None.                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |