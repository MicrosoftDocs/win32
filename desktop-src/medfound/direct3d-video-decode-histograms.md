---
description: This article contains guidance for generating histograms while decoding video using Direct3D 11 or 12 video APIs.
ms.assetid: 
title: Direct3D video decode histograms
ms.topic: article
ms.date: 08/19/2019
---

# Direct3D video decode histograms

This article contains guidance for generating histograms while decoding video using Direct3D 11 or 12 video APIs.

## Checking the video device for histogram capabilities

Before attempting to generated histograms, you must check to see if the current video device supports the video decode histogram feature.

### Direct3D 12

Call [ID3D12VideoDevice::CheckFeatureSupport](/windows/desktop/api/d3d12video/nf-d3d12video-id3d12videodevice-checkfeaturesupport) to check for the support details for Direct3D 12 video decoding operations. Pass the **D3D12_FEATURE_VIDEO_DECODE_HISTOGRAM** value from the [D3D12_FEATURE_VIDEO](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_feature_video) enumeration to specify that you are requesting support for video decode histograms.

### Direct3D 11

Call [ID3D11VideoDevice2::CheckFeatureSupport](/windows/win32/api/d3d11_4/nf-d3d11_4-id3d11videodevice2-checkfeaturesupport) and pass in the **D3D11_FEATURE_VIDEO_DECODER_HISTOGRAM** value of the [D3D11_FEATURE_VIDEO](/windows/win32/api/d3d11_4/ne-d3d11_4-d3d11_feature_video) to determine if histograms are supported for the current device.

## Enabling histogram during decode

The collection of histogram data is enabled by the caller providing the buffers in which the histogram data is stored.  A null histogram output buffer for a given component indicates that histogram collection is disabled.

### Direct3D 12

In order to provide output buffers to receive histogram data using Direct3D 12, you should create your decode command list using the [ID3D12VideoDecodeCommandList1::DecodeFrame1](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodecodecommandlist1-decodeframe1) method. This method takes a [D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS1](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_decode_output_stream_arguments1) structure as an argument. **D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS1** has a field of type [D3D12_VIDEO_DECODE_OUTPUT_HISTOGRAM](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_decode_output_histogram), which allows you to specify an [ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource) into which histogram data is output.

### Direct3D 11

The [ID3D11VideoContext3](/windows/win32/api/d3d11_4/nn-d3d11_4-id3d11videocontext3) interface provides the [DecoderBeginFrame1](/windows/win32/api/d3d11_4/nf-d3d11_4-id3d11videocontext3-decoderbeginframe1) method, which allows you to provide one or more [ID3D11Buffer](/windows/win32/api/d3d11/nn-d3d11-id3d11buffer) interfaces into which the histogram data will be output. The [D3D11_VIDEO_DECODER_HISTOGRAM_COMPONENT](/windows/win32/api/d3d11_4/ne-d3d11_4-d3d11_video_decoder_histogram_component) to specify the components for which you want histogram data to be generated.


## Buffer format

The decode histogram output is written to a buffer as an integer counter per component.  The buffer format is a 32-bit value per bin.  A device may use an integer counter bit depth that is smaller than 32 bits, but must be 16, 24, or 32 bits.  If so, the counter value is stored in the lower bits and the upper unused bits are zero.  When the count for a bin would exceed the max value, the device sets the max value instead. Devices report the number of bins supported, which must be a value that is a power of 2.  The minimum number of bins required for devices that support this feature is 64. 

You must supply a buffer with a 256-byte aligned offset and a size that is the supported number of bins multiplied by the bin size (4 bytes) for each component requested.  Bin placement is determined by:

`binIndex = floor(value / [max value of channel + 1] * (countBins))`


When a format defines the useful bits of a component as less than the number of storage bits (for example, P010 uses the top 10 bits of 16 bits of component storage), only the useful bits are considered (P010 is treated as a 10 bit value). 

The video device reports which components are supported.  If the caller does not want a histogram for a given component, they specify nullptr.  If the driver does not support a histogram for a given component, that component's histogram buffer must be nullptr.

When multiple components are supported, the application may request any combination of components per frame decode.  For example,if the hardware reports support for Y, U, and V components, the application may request the Y histogram only for frame one, the U histogram only for frame two, and the V histogram only for frame 3.  They may also request any combination of two components or all three components.

Applications supply a separate offset and buffer pointer/handle for each component requested.  This pointer may point to the same resource as another component or a separate resource.  The offset allows placing multiple components in the same buffer, but the output region specified by the offset and the histogram size must not overlap another histogram component output.  The histogram may also be written to the same buffer as other unrelated content such as when being used in a resource sub-allocation strategy.


The D3D runtime validates that callers only enable histogram for supported components, that the buffer offset is aligned, and that buffer size is sufficient for the reported number of bins.


## Protected content

The Histogram buffers are required to have the same surface protection as the decode output surface. If the decode output surface is not a protected resource, the histogram buffer must not be a protected resource. If the decode output surface is protected resource, the histogram must be a protected resource.








## Related topics

<dl> <dt>
[Direct3D 12 Video APIs](direct3d-12-video-apis.md)
[Media Foundation Programming Guide](media-foundation-programming-guide.md)
</dt> </dl>

 

 




