---
Description: This article contains guidance for motion vector estimation with Direct3D 12 video APIs.
ms.assetid: 
title: Direct3D video motion estimation
ms.topic: article
ms.date: 08/19/2019
---

# Direct3D video motion estimation

This article contains guidance for motion vector estimation with Direct3D 12 video APIs. This feature was introduced in Windows 10, version 2004 (10.0; Build 19041) and is intended to be used for the optimization of video encoders.

## The motion estimator context object

The [ID3D12VideoMotionEstimator](/windows/win32/api/d3d12video/nn-d3d12video-id3d12videomotionestimator) object maintains context for video motion estimation operations. Create a new instance of this interface by calling [ID3D12VideoDevice1::CreateVideoMotionEstimator](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodevice1-createvideomotionestimator).


## Estimate motion in a command list

Call the [EstimateMotion](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videoencodecommandlist-estimatemotion) from a [ID3D12VideoEncodeCommandList](/windows/win32/api/d3d12video/nn-d3d12video-id3d12videoencodecommandlist) to invoke the motion estimation operation.

## Storage of motion vectors

The [ID3D12VideoMotionVectorHeap](/windows/win32/api/d3d12video/nn-d3d12video-id3d12videomotionvectorheap) stores motion vectors. This interface is used by the [D3D12_VIDEO_MOTION_ESTIMATOR_OUTPUT](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_motion_estimator_output) structure returned from [ID3D12VideoEncodeCommandList::EstimateMotion](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videoencodecommandlist-estimatemotion). Call [ID3D12VideoEncodeCommandList::ResolveMotionVectorHeap](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videoencodecommandlist-resolvemotionvectorheap) to translates the motion vector output of **EstimateMotion** from hardware-dependent formats into a consistent format defined by the video motion estimation APIs.

 **ID3D12VideoMotionVectorHeap** is also used to supply hint vectors in the [D3D12_VIDEO_MOTION_ESTIMATOR_INPUT](/windows/win32/api/d3d12video/ns-d3d12video-d3d12_video_motion_estimator_input) structure.


## Protected resources

Direct3D 12 motion vector estimation supports reading from and writing to hardware DRM protected resources when supported by the driver. If the input resources are hardware DRM protected, the output is also a hardware DRM protected resource.The methods used to create the motion estimation context object and the motion vector heap,  [ID3D12VideoDevice1::CreateVideoMotionEstimator](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodevice1-createvideomotionestimator) and [ID3D12VideoDevice1::CreateVideoMotionVectorHeap](/windows/win32/api/d3d12video/nf-d3d12video-id3d12videodevice1-createvideomotionvectorheap), both accept a [ID3D12ProtectedResourceSession](/windows/win32/api/d3d12/nn-d3d12-id3d12protectedresourcesession) that is used to manage access to protected resources. 

Use [ID3D12VideoMotionEstimator::GetProtectedResourceSession](/windows/win32/api/d3d12/nf-d3d12video-id3d12videomotionestimator-getprotectedresourcesession) and [ID3D12VideoMotionVectorHeap::GetProtectedResourceSession](/windows/win32/api/d3d12/nf-d3d12video-id3d12videomotionvectorheap-getprotectedresourcesession) to retrieve the **ID3D12ProtectedResourceSession** objects provided when the objects were created.



## Related topics

<dl> <dt>
[Direct3D 12 Video APIs](direct3d-12-video-apis.md)
[Media Foundation Programming Guide](media-foundation-programming-guide.md)
</dt> </dl>

 

 




