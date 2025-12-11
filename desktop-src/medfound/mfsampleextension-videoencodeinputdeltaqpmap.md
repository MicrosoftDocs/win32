---
description: Stores a map of the delta Quantization Parameter (QP) values provided as input to the encoder MFT. 
title: MFSampleExtension_VideoEncodeInputDeltaQPMap attribute (Mfapi.h)
ms.topic: reference
ms.date: 23/09/2025
---

# MFSampleExtension\_VideoEncodeInputDeltaQPMap attribute

Stores a map of the delta Quantization Parameter (QP) values provided as input to the encoder MFT.

## Data type

An [IMFMediaBuffer](/windows/win32/api/mfobjects/nn-mfobjects-imfmediabuffer).

## Remarks

This attribute allows apps to provide hints to a video encoder MFT by specifying different Quantization Parameter (QP) values for different parts of a video frame. For example, a video conferencing app might know what parts of a video frame is showing a person’s face, and it can use this API to ask the encoder to use smaller QP values when encoding those parts of the video frame.

Assuming a video of resolution of 1920x1080 being encoded with HEVC standard, with the supported delta QP block size being 16x16. There are 120x68 such blocks. The blocks will be arranged in row major ordering. The following table shows the layout of such a delta QP map.

:::image type="content" source="images/deltaqpmap.png" alt-text="The data format of an example delta QP map":::

Use [IMFAttributes::SetUnknown](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-setunknown) to attach an [IMFMediaBuffer](/windows/win32/api/mfobjects/nn-mfobjects-imfmediabuffer) containing the delta QP values. Use [IMFAttributes::GetUnknown](/windows/win32/api/mfobjects/nf-mfobjects-imfattributes-getunknown) to retrieve the **IMFMediaBuffer** containing the delta QP values.

Delta QP maps are provided for the entire frame at once. If the encoder uses multiple tiles or slices, the tile level or slice level encode will use the externally provided delta QP input maps at the frame level in performing such tile or slice level encode.

There is no separation of QP values from a Chroma or Luma perspective. QP values will applied uniformly to Luma & Chroma Pixels.

Delta QP maps allow applications to adjust bit allocation within a frame without taking over the entire rate control process from the MFT. For example, in video conferencing, an app can use a delta QP map to prioritize higher quality for the foreground (like faces) while reducing quality in the background.

Simultaneous usage of both delta QP and absolute QP is not supported. If an absolute QP map is attached to an [IMFSample](/windows/win32/api/mfobjects/nn-mfobjects-imfsample), any delta QP map is ignored by the encoder MFT.

[MFCreateDXGISurfaceBuffer](/windows/win32/api/mfapi/nf-mfapi-mfcreatedxgisurfacebuffer) can be used to wrap a GPU resource into an **IMFMediaBuffer**.

The data type of each element in the delta QP map should match what is indicated in the **dataType** field of the [InputQPSettings](/windows/win32/api/mfapi/ns-mfapi-inputqpsettings.md) passed in the blob obtained with the [CODECAPI_AVEncVideoInputDeltaQPSettings](codecapi-avencvideoinputdeltaqpblocksettings.md) property.

Providing delta QP values may conflict and have an overriding effect on bitrate properties like [AVEncCommonMeanBitRate](avenccommonmeanbitrate-property.md) or [CODECAPI_AVEncCommonMaxBitRate](/windows/win32/codecapi/avenccommonmaxbitrate-property.md).

Encoder MFT that support **MFSampleExtension_VideoEncodeInputDeltaQPMap** must also support **CODECAPI_AVEncVideoInputDeltaQPSettings**.



## Examples

This example shows how to attach a delta QP map to **IMFSample** objects that are provided as input to an encoder MFT. The *deltaQPBuffer* input parameter represents the delta QP map. For information about how to write data to a media buffer, see [Working With Media Buffers](working-with-media-buffers.md).

```cpp
#include <mfapi.h>
#include <mfobjects.h>
#include <wil/com.h>
#include <wil/result_macros.h>

// Function to set delta QP values contained within an IMFMediaBuffer on an input sample.
// The function returns a failure HRESULT code if the operation fails.
HRESULT SetDeltaQPForInputSample(
    _In_ IMFSample* inSample, 
    _In_ IMFMediaBuffer* deltaQPBuffer // Input: IMFMediaBuffer contains delta QP values
)
{
    RETURN_HR_IF_NULL(E_INVALIDARG, deltaQPBuffer);
    RETURN_HR_IF_NULL(E_INVALIDARG, inSample);

    // Retrieve the sample attributes
    wil::com_ptr_nothrow<IMFAttributes> sampleAttributes;
    RETURN_IF_FAILED(wil::com_query_to_nothrow(inSample, &sampleAttributes));

    // Set the IMFMediaBuffer with the Delta QP map
    return sampleAttributes->SetUnknown(MFSampleExtension_VideoEncodeInputDeltaQPMap, deltaQPBuffer);
}

```


## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client | Windows 11, build 26100   |
| Minimum supported server | Windows Server 2025   |
| Header               | mfapi.h |
