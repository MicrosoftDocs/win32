---
description: Stores a map of the absolute Quantization Parameter (QP) values provided as input to the encoder MFT. 
title: MFSampleExtension_VideoEncodeInputAbsoluteQPMap attribute (Mfapi.h)
ms.topic: reference
ms.date: 12/09/2025
---

# MFSampleExtension\_VideoEncodeInputAbsoluteQPMap attribute

Stores a map of the absolute Quantization Parameter (QP) values provided as input to the encoder MFT.

## Data type

An [IMFMediaBuffer](/windows/win32/api/mfobjects/nn-mfobjects-imfmediabuffer).

## Remarks

This attribute allows apps to provide hints to a video encoder MFT by specifying different Quantization Parameter (QP) values for different parts of a video frame. For example, a video conferencing app might know what parts of a video frame is showing a person’s face, and it can use this API to ask the encoder to use smaller QP values when encoding those parts of the video frame.

Assuming a video of resolution of 1920x1080 being encoded with HEVC standard, with the supported absolute QP block size being 32x32. There are 60x34 such blocks. The blocks will be arranged in row major ordering. The following table shows the layout of such a absolute QP map.

:::image type="content" source="images/absoluteqpmap.png" alt-text="The data format of an example absolute QP map":::

Use [IMFAttributes::SetUnknown](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-setunknown) to attach an [IMFMediaBuffer](/windows/win32/api/mfobjects/nn-mfobjects-imfmediabuffer) containing the absolute QP values. Use [IMFAttributes::GetUnknown](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-getunknown) to retrieve the **IMFMediaBuffer** containing the absolute QP values.

Absolute QP maps are provided for the entire frame at once. If the encoder uses multiple tiles or slices, the tile level or slice level encode will use the externally provided absolute QP input maps at the frame level in performing such tile or slice level encode.

There is no separation of QP values from a Chroma or Luma perspective. QP values will applied uniformly to Luma & Chroma Pixels.

Absolute QP maps give applications full control over the exact quantization parameter for each region of a frame, effectively allowing the app to override the encoder’s internal rate control in the MFT. This capability is crucial in dynamic scenarios such as live sports broadcasts with graphical overlays or picture-in-picture feeds, where different regions of the frame change in complexity from one moment to the next. Relying solely on Delta QP maps could lead to artifacts when the encoder’s automatic adjustments don’t align with the application’s quality needs.

Simultaneous usage of both delta QP and absolute QP is not supported. If an absolute QP map is attached to an [IMFSample](/windows/win32/api/mfobjects/nn-mfobjects-imfsample), any delta QP map is ignored by the encoder MFT.

[MFCreateDXGISurfaceBuffer](/windows/win32/api/mfapi/nf-mfapi-mfcreatedxgisurfacebuffer) can be used to wrap a GPU resource into an **IMFMediaBuffer**.

The data type of each element in the absolute QP map should match what is indicated in the **dataType** field of the [InputQPSettings](/windows/win32/api/mfapi/ns-mfapi-inputqpsettings) passed in the blob obtained with the [CODECAPI_AVEncVideoInputDeltaQPSettings](codecapi-avencvideoinputdeltaqpblocksettings.md) property.

Providing delta QP values may conflict and have an overriding effect on bitrate properties like [AVEncCommonMeanBitRate](/windows/win32/codecapi/avenccommonmeanbitrate-property) or [CODECAPI_AVEncCommonMaxBitRate](/windows/win32/codecapi/avenccommonmaxbitrate-property).

Encoder MFT that support **MFSampleExtension_VideoEncodeInputAbsoluteQPMap** must also support **CODECAPI_AVEncVideoInputDeltaQPSettings**.



## Examples

This example shows how to attach a delta QP map to **IMFSample** objects that are provided as input to an encoder MFT. The *deltaQPBuffer* input parameter represents the delta QP map. For information about how to write data to a media buffer, see [Working With Media Buffers](working-with-media-buffers.md).

```cpp
#include <mfapi.h>
#include <mfobjects.h>
#include <wil/com.h>
#include <wil/result_macros.h>

// Function to set absolute QP values contained within an IMFMediaBuffer to an input sample.
// The function returns a failure code if the operation fails.
HRESULT SetAbsoluteQPForInputSample(
    _In_ IMFSample* inSample, 
    _In_ IMFMediaBuffer* absoluteQPBuffer // Input: IMFMediaBuffer contains absolute QP values
)
{
    RETURN_HR_IF_NULL(E_INVALIDARG, absoluteQPBuffer);
    RETURN_HR_IF_NULL(E_INVALIDARG, inSample);

    // Retrieve the sample attributes
    wil::com_ptr_nothrow<IMFAttributes> sampleAttributes;
    RETURN_IF_FAILED(wil::com_query_to_nothrow(inSample, &sampleAttributes));

    // Set the IMFMediaBuffer with the absolute QP map
    return sampleAttributes->SetUnknown(MFSampleExtension_VideoEncodeInputAbsoluteQPMap, absoluteQPBuffer);
}
```


## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client | Windows 11, build 26100   |
| Minimum supported server | Windows Server 2025   |
| Header               | mfapi.h |
