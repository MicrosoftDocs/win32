---
description: This article contains general guidance for using the Direct3D 12 video APIs.
ms.assetid: 
title: Direct3D 12 Video Overview
ms.topic: article
ms.date: 06/03/2019
---

# Direct3D 12 Video Overview

This article contains general guidance for using the Direct3D 12 video APIs.

## About Direct3D 12 Video

The Direct3D 12 video interface provides a new way for apps to implement video decoding and process. The Direct3D 12 interface is different from the previous Direct3D 11 interface because it was designed to be consistent with the Direct3D 12 principles and style, which includes the following:

- Give developers more control
 - Allocation of hardware-accessible memory
 - CPU threads used to generate & submit commands
   - Independent generation and submission
   - Non-blocking
 - Scheduling of hardware work
- Covers existing functionality, including most Direct3D 11 video functionality, but at the same time, keeps simplicity and ease of use in mind
- Power and performance of main Direct3D 12 applications equal to or better than Direct3D 11
- Consistency with other Direct3D 12 APIs
- Interoperability with existing graphics APIs


## Video decoding

The following sections describe some of the tasks involved in implementing Direct3D 12 video decoding.

### Query for decoding capabilities

Call [ID3D12VideoDevice::CheckFeatureSupport](/windows/desktop/api/d3d12video/nf-d3d12video-id3d12videodevice-checkfeaturesupport) to check for the support details for Direct3D 12 video decoding operations. Pass a value from the [D3D12_FEATURE_VIDEO](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_feature_video) enumeration to specify the feature for which you are requesting support information.

### Create the video decoder

Call [ID3D12VideoDevice::CreateVideoDecoder](/windows/desktop/api/d3d12video/nf-d3d12video-id3d12videodevice-createvideodecoder) to create an instance of the [ID3D12VideoDecoder](/windows/desktop/api/d3d12video/nn-d3d12video-id3d12videodecoder) interface. The decoder holds state for a decode session, including reference-related data such as motion vectors.  In the event of a resolution change or a [MaxDecodePictureBufferCount](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decoder_heap_desc) change, the decoder object is recreated. The decode width and height specify the native stream resolution before any scale.  The maximum Decode Picture Buffer (DPB) count specifies the largest DPB count that can be used without recreating the video decoder.

The decoder may be used to record commands from multiple command lists, but may only be associated with one command list at a time.  The application is responsible for synchronizing access to the decoder.

### Create the video decoder heap 

Call [ID3D12VideoDevice::CreateVideoDecoderHeap](/windows/desktop/api/d3d12video/nf-d3d12video-id3d12videodevice-createvideodecoderheap) to create an instance of the [ID3D12VideoDecoderHeap](/windows/desktop/api/d3d12video/nn-d3d12video-id3d12videodecoderheap) interface. This object contains the resolution-dependent driver resources and state.

### Decoding a frame

All input and output parameters for the video processing operations are organized into an input parameter structure, [D3D12_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_input_stream_arguments), and an output parameter structure, [D3D12_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_output_stream_arguments).
The application manages the reference frames, and as such, needs to set the reference frames for every decoding operation.
When the command list is properly recorded, call [ID3D12CommandQueue::ExecuteCommandLists](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-executecommandlists) on the video command queue to submit the frame decoding to the GPU.


### Enabling decoder output conversions
If the decoder supports conversion, then enable the desired conversions by properly filling the [D3D12_VIDEO_DECODE_CONVERSION_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_decode_conversion_arguments) structure. The format and resolutions of the desired output versus the native output of the decoder are communicated via the difference in color space and resolutions specified in the conversion parameters.

##	Querying decoding status 
Use the methods [ID3D12VideoDecodeCommandList::BeginQuery](/windows/desktop/api/d3d12video/nf-d3d12video-id3d12videodecodecommandlist-beginquery) and [ID3D12VideoDecodeCommandList::EndQuery](/windows/desktop/api/d3d12video/nf-d3d12video-id3d12videodecodecommandlist-endquery) to query the status of the decoding operation.

The [D3D12_QUERY_DATA_VIDEO_DECODE_STATISTICS](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_query_data_video_decode_statistics) structure is used to describe video decode statistics. To get an instance of this structure call [ID3D12VideoDecodeCommandList::EndQuery](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodecodecommandlist-endquery), passing in the heap query type value of [D3D12_QUERY_TYPE_VIDEO_DECODE_STATISTIC](/windows/win32/api/d3d12/ne-d3d12-d3d12_query_type). Note that this query does not use [ID3D12VideoDecodeCommandList::BeginQuery](/windows/desktop/api/d3d12video/nf-d3d12video-id3d12videodecodecommandlist-beginquery).

## Video processing

Direct3D 12 video APIs take a streamlined approach to video processing, eliminating features of Direct3D 11 that weren't widely used and removing capability checks for features that are mandatory across devices. The enumeration process for video processing is eliminated. Instead, call [ID3D12VideoDevice::CheckFeatureSupport](/windows/desktop/api/d3d12video/nf-d3d12video-id3d12videodevice-checkfeaturesupport) which allows an app to identify the capabilities of the video processor. The desired video, interlace, stereo formats and rates are provided as as input to **CheckFeatureSupport**.

### Removed capabilities

The following capabilities from Direct3D 11 are not supported in Direct3D 12 video processing:
- Custom rates.  Instead, there is an input and output rate given during the [ID3D12VideoProcessCommandList::ProcessFrames](/windows/desktop/api/d3d12video/nf-d3d12video-id3d12videoprocesscommandlist-processframes) command recording.
- There are just two deinterlacing modes available now: [BOB](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_process_deinterlace_flags) and [CUSTOM](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_process_deinterlace_flags). Other modes have been eliminated. CUSTOM is a high-quality deinterlacing mode provided by the hardware vendor.
- All of the optional stereo formats in [D3D11_VIDEO_PROCESSOR_STEREO_CAPS](/windows/desktop/api/d3d11/ne-d3d11-d3d11_video_processor_stereo_caps) are no longer supported. Instead, [nono](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_frame_stereo_format), [horizontal](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_frame_stereo_format), [vertical](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_frame_stereo_format), and [separate](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_frame_stereo_format) are mandatory for all hardware devices if stereo is supported.
- There is no equivalent for [D3D11_VIDEO_PROCESSOR_FORMAT_CAPS](/windows/desktop/api/d3d11/ne-d3d11-d3d11_video_processor_format_caps) or [D3D11_VIDEO_PROCESSOR_AUTO_STREAM_CAPS](/windows/desktop/api/d3d11/ne-d3d11-d3d11_video_processor_auto_stream_caps). Instead, input and output formats are arguments to the creation of the video processor, and at that time, it should be known if the video processor can or cannot perform the operation with the given format. The [D3D12_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_process_auto_processing_flags) is used to indicate if auto processing features are available.
- There is no equivalent for [D3D11_VIDEO_PROCESSOR_CAPS_LEGACY](/windows/desktop/api/d3d11/ne-d3d11-d3d11_video_processor_feature_caps).
- There is no equivalent for [D3D11_VIDEO_PROCESSOR_CAPS_CONSTRICTION](/windows/desktop/api/d3d11/ne-d3d11-d3d11_video_processor_feature_caps).
- When converting from stereo to mono, we assume the baseline view is 0.
- Direct3D 12 video processing does not support converting mono to stereo and there is no support for mono offset. 


### Creating a video processor

Call [ID3D12VideoDevice::CreateVideoProcessor](/windows/desktop/api/d3d12video/nf-d3d12video-id3d12videodevice-createvideoprocessor) to create an instance of the [ID3D12VideoProcessor](/windows/desktop/api/d3d12video/nn-d3d12video-id3d12videoprocessor). The video processor holds state for a video processing session, including required intermediate memory, cached processing data, or other temporary working space. The video processor creation arguments specify which operations are performed or are available at [ID3D12VideoProcessCommandList1::ProcessFrames1](/windows/desktop/api/d3d12video/nf-d3d12video-id3d12videoprocesscommandlist1-processframes1) time.  Driver allocations to perform the video process operation (e.g. intermediates) are allocated at video processor creation time.  Use [D3D12_FEATURE_VIDEO_PROCESSOR_SIZE](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_feature_video) to determine the allocation size of the video processor in advance.

The video processor may only be used to record commands from multiple command lists, but may only be associated with one command list at a time.  The application is responsible for synchronizing access to the video processor.  The application must also record video processing commands against the video procoessor in the order that they are executed on the GPU.

All input and output arguments for the video processing operations are organized into an input argument structure, [D3D12_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_input_stream_arguments), and an output argument structure, [D3D12_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS](/windows/desktop/api/d3d12video/ns-d3d12video-d3d12_video_process_output_stream_arguments). The application must call [ID3D12VideoProcessCommandList::ProcessFrames](/windows/desktop/api/d3d12video/nf-d3d12video-id3d12videoprocesscommandlist-processframes) to record the video processing operation it wants to execute. 

When the command list is recorded, call [ID3D12CommandQueue::ExecuteCommandLists](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-executecommandlists) on the video command queue to submit the frame processing to the GPU.


## Tiers

Direct3D 12 video defines tiers that group the capabilities of hardware devices, so that the app can have fewer code paths to cater to the variety of hardware. The tiers are specified with the [D3D12_VIDEO_DECODE_TIER](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_decode_tier) enumeration.

In all the tiers, the following will be available:

- No need for decoder recreation on resolution changes. Only the decoder heap needs to be recreated on resolution change.
- All reference frames will be managed by the app. This allows the system to save memory since we do not need to allocate the maximum number of DPBs at decoder creation time in some tiers, and gives apps flexibility in resolution changing scenarios.

Note that the tiers are supersets. An app may decide to do tier 1, and not use the higher level features, which is allowed but may not provide optimal performace. For more information on the capabilities associated with different tier levels, see [D3D12_VIDEO_DECODE_TIER](/windows/desktop/api/d3d12video/ne-d3d12video-d3d12_video_decode_tier).

## Reference frames

With Direct3D 12 video, reference frames are passed explicitly. This allows for clear usage of array of textures or texture arrays when we are decoding frames. The app is not required to pass the exact same resource handle when using it as a reference; it may, for instance, decide to copy one resource to another and then pass the copy instead of the original one. The DXVA *RefFrameList* and *CurrPic* indices are still used by the driver to store relevant data for each decoded frame.


## DirectX 12 fences

In DirectX 12, the app is responsible for synchronizing the access to their buffers. For the decoding case, there will be the need for adding fences to the input buffers and to the output buffers. Each fence has a value associated with it, and are used for synchronization of the CPU and the hardware engines. For more information, see [Using Resource Barriers to Synchronize Resource States in Direct3D 12](/windows/desktop/direct3d12/using-resource-barriers-to-synchronize-resource-states-in-direct3d-12).

A typical implementation will have a fence for each input buffer. In the case of input buffers, it is possible that the buffer may be available before the whole decoding process is done. The system will ignore this case and assume that the input buffer is available when decoding is done.
An implementation will also usually have a fence for each output buffer. In the case of sending the output to the compositor, for instance, a fence is needed that is signaled when that presentation of that frame is finally done, indicating that the output is again available for the decoder.


## Related topics

<dl> <dt>
 
[Direct3D 12 Video APIs](direct3d-12-video-apis.md)
</dt> <dt>
 
[Media Foundation Programming Guide](media-foundation-programming-guide.md)
</dt> </dl>

 

 
