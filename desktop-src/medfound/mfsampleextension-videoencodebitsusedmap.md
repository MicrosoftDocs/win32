---
description: Stores a map of the number of bits used for encoding each block in an encoded video frame.
title: MFSampleExtension_VideoEncodeBitsUsedMap attribute (Mfapi.h)
ms.topic: reference
ms.date: 03/29/2024
---

# MFSampleExtension\_VideoEncodeBitsUsedMap attribute

Stores a map of the number of bits used for encoding each block in an encoded video frame.

## Data type

An [IMFMediaBuffer](/windows/win32/api/mfobjects/nn-mfobjects-imfmediabuffer).

## Remarks

Accessing the bits used map allows developers to analyze bit allocation across an encoded frame. This can help diagnose inefficiencies, adjust encoding strategies, and ensure that critical regions of a video receive appropriate bit allocation.

The bits used map is an array of **uint32_t**. Each block has one **uint32_t** value that represents the number of bits used in encoding the block. A developer should determine the map’s size using [CODECAPI_AVEncVideoOutputBitsUsedMapBlockSize](codecapi-avencvideooutputbitsusedmapblocksize.md) and video frame width and height (Divide the width/height by the block size. If the width/height is not an exact multiple of the block size, round it up to the next multiple of the block size) . This provides the number of rows and columns, ensuring proper alignment with the video frame. The map is from left to right and top to bottom.

Use [IMFAttributes::SetUnknown](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-setunknown) to attach an **IMFMediaBuffer** containing the QP map to an output sample. Use [IMFAttributes::GetUnknown](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-getunknown) to retrieve the **IMFMediaBuffer** containing the QP map from an output sample.  

The bits used map should only be reported when the entire frame has completed encoding. If the encoder uses multiple slices, the PSNR buffer should be attached to the [IMFSample](/windows/win32/api/mfobjects/nn-mfobjects-imfsample) of the last slice.

## Examples

The following example demonstrates how to use the **CODECAPI_AVEncVideoOutputBitsUsedMapBlockSize** property to configure an encoder MFT to enable or disable reporting the bits used map feature. If the block size is zero, it is disabled. If it is not zero, it is enabled.

```cpp
#include <codecapi.h> 
#include <mfapi.h> 

//  Inform an encoder MFT to enable or disable reporting the bits used map feature. 
//  This function assumes that the encoder MFT supports ICodecAPI interface. 
//  It checks whether the property CODECAPI_AVEncVideoOutputBitsUsedMapBlockSize is supported. 
//  If not supported, it returns E_NOTIMPL. 

HRESULT ConfigureEncoderForBitsUsedMap(_In_ IMFTransform* encoder, uint32_t blockSize) 
{ 
    wil::com_ptr_nothrow<ICodecAPI> codecAPI; 
    RETURN_IF_FAILED(wil::com_query_to_nothrow(encoder, &codecAPI)); 

    // Check if the encoder supports the property 
    if (!codecAPI->IsSupported(&CODECAPI_AVEncVideoOutputBitsUsedMapBlockSize)) 
    { 
        return E_NOTIMPL; 
    } 

    // Configure encoder 
    wil::unique_variant value; 
    value.vt = VT_UI4; 
    value.ulVal = blockSize; // zero: disable; non-zero: enable 
    return codecAPI->SetValue(&CODECAPI_AVEncVideoOutputBitsUsedMapBlockSize, &value); 
} 
```

The following example shows a helper function that can be used by implementations of an encoder MFT that supports **ICodecAPI**. The function shows how to check if bits used map reporting is enabled on the encoder MFT. If it is enabled, the function shows how to attach the bits used map onto the output sample. This assumes that each output sample contains a complete frame. If the encoder uses multiple slices, the bits used map should be attached only to the IMFSample of the last slice.

```cpp
#include <mfapi.h> 
#include <mfobjects.h> 
#include <codecapi.h> 
#include <wrl.h> 

// Function to query and attach bits used map to output samples 

HRESULT ReportBitsUsedMapOnOutputSample( 
    _In_ IMFTransform* encoder,  
    _In_ IMFSample* outputSample,  
    _In_ IMFMediaBuffer* bitsUsedMap // IMFMediaBuffer could be the GPU resource for bits used map if using hardware encoder 
)  
{ 
    RETURN_HR_IF_NULL(E_INVALIDARG, encoder); 
    RETURN_HR_IF_NULL(E_INVALIDARG, outputSample); 
    RETURN_HR_IF_NULL(E_INVALIDARG, bitsUsedMap); 

    // Query the encoder's codec API to check if bits used Map reporting is enabled 
    wil::com_ptr_nothrow<ICodecAPI> codecAPI; 
    RETURN_IF_FAILED(wil::com_query_to_nothrow(encoder, &codecAPI)); 

    wil::unique_variant value; 
    RETURN_IF_FAILED(codecAPI->GetValue(&CODECAPI_AVEncVideoOutputBitsUsedMapBlockSize, &value)); 

    if (value.vt != VT_UI4 || !value.ulVal) { 
        return S_OK; // Bits Used Map not enabled 
    } 

    // Attach the IMFMediaBuffer (Bits Used Map) to the output sample's attributes 
    wil::com_ptr_nothrow<IMFAttributes> sampleAttributes; 
    RETURN_IF_FAILED(wil::com_query_to_nothrow(outputSample, &sampleAttributes)); 

    return sampleAttributes->SetUnknown(MFSampleExtension_VideoEncodeBitsUsedMap, bitsUsedMap); 
} 

The following example shows how an app can retrieve the bits used map data from the **IMFSample** objects that are produced by an encoder MFT.

```cpp
#include <mfapi.h> 
#include <mfobjects.h> 
#include <codecapi.h> 
#include <wrl.h> 

// Function to retrieve the bits used map data from an output sample 
HRESULT RetrieveBitsUsedMapFromOutputSample( 
    _In_ IMFSample* outputSample,  
    _COM_Outptr_result_maybenull_ IMFMediaBuffer** bitsUsedMap // Output: IMFMediaBuffer containing the bits used map 
) 
{ 

    RETURN_HR_IF_NULL(E_INVALIDARG, bitsUsedMap); 
    *bitsUsedMap = nullptr; 

    RETURN_HR_IF_NULL(E_INVALIDARG, outputSample); 

    // Retrieve the sample attributes 
    wil::com_ptr_nothrow<IMFAttributes> sampleAttributes; 
    RETURN_IF_FAILED(wil::com_query_to_nothrow(outputSample, &sampleAttributes)); 

    // Retrieve the IMFMediaBuffer associated with the bits used map 
    (void)sampleAttributes->GetUnknown(MFSampleExtension_VideoEncodeBitsUsedMap, IID_PPV_ARGS(bitsUsedMap)); 

    return S_OK; 

} 
```


## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client | Windows 11, build 26100   |
| Minimum supported server | Windows Server 2025   |
| Header               | mfapi.h |
