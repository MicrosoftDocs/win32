---
description: This section contains info about the enumerations provided by DXGI.
ms.assetid: c4574c89-dee2-4841-9318-5383cf417111
title: DXGI Enumerations
ms.topic: article
ms.date: 05/31/2018
---

# DXGI Enumerations

This section contains info about the enumerations provided by DXGI.

## In this section



| Topic                                                                                                         | Description                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DXGI\_ADAPTER\_FLAG**](/windows/desktop/api/dxgi/ne-dxgi-dxgi_adapter_flag)<br/>                                          | Identifies the type of DXGI adapter.<br/>                                                                                                                                   |
| [**DXGI\_ADAPTER\_FLAG3**](/windows/desktop/api/dxgi1_6/ne-dxgi1_6-dxgi_adapter_flag3)<br/>                                        | Identifies the type of DXGI adapter.<br/>                                                                                                                                   |
| [**DXGI\_ALPHA\_MODE**](/windows/desktop/api/DXGI1_2/ne-dxgi1_2-dxgi_alpha_mode)<br/>                                                       | Identifies the alpha value, transparency behavior, of a surface.<br/>                                                                                                       |
| [**DXGI\_COLOR\_SPACE\_TYPE**](/windows/desktop/api/dxgicommon/ne-dxgicommon-dxgi_color_space_type)<br/>                                          | Specifies color space types.<br/>                                                                                                                                           |
| [**DXGI\_COMPUTE\_PREEMPTION\_GRANULARITY**](/windows/desktop/api/DXGI1_2/ne-dxgi1_2-dxgi_compute_preemption_granularity)<br/>              | Identifies the granularity at which the graphics processing unit (GPU) can be preempted from performing its current compute task.<br/>                                      |
| [**DXGI\_DEBUG\_RLO\_FLAGS**](/windows/desktop/api/DXGIDebug/ne-dxgidebug-dxgi_debug_rlo_flags)<br/>                                            | Flags used with [**ReportLiveObjects**](/windows/desktop/api/DXGIDebug/nf-dxgidebug-idxgidebug-reportliveobjects) to specify the amount of info to report about an object's lifetime. <br/>                         |
| [**DXGI\_FEATURE**](/windows/desktop/api/DXGI1_5/ne-dxgi1_5-dxgi_feature)<br/>                                                              | Specifies a range of hardware features, to be used when checking for feature support.<br/>                                                                                  |
| [**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format)<br/>                                                       | Resource data formats, including fully-typed and typeless formats. A list of modifiers at the bottom of the page more fully describes each format type. <br/>               |
| [**DXGI\_FRAME\_PRESENTATION\_MODE**](/windows/desktop/api/dxgi1_3/ne-dxgi1_3-dxgi_frame_presentation_mode)<br/>                            | Indicates options for presenting frames to the swap chain. <br/>                                                                                                            |
| [**DXGI\_GPU\_PREFERENCE**](/windows/desktop/api/dxgi1_6/ne-dxgi1_6-dxgi_gpu_preference)<br/>                                               | The preference of GPU for the app to run on.<br/>                                                                                                                           |
| [**DXGI\_GRAPHICS\_PREEMPTION\_GRANULARITY**](/windows/desktop/api/DXGI1_2/ne-dxgi1_2-dxgi_graphics_preemption_granularity)<br/>            | Identifies the granularity at which the GPU can be preempted from performing its current graphics rendering task.<br/>                                                      |
| [**DXGI\_HARDWARE\_COMPOSITION\_SUPPORT\_FLAGS**](/windows/desktop/api/dxgi1_6/ne-dxgi1_6-dxgi_hardware_composition_support_flags)<br/>     | Describes which levels of hardware composition are supported.<br/>                                                                                                          |
| [**DXGI\_HDR\_METADATA\_TYPE**](/windows/desktop/api/dxgi1_5/ne-dxgi1_5-dxgi_hdr_metadata_type)<br/>                                        | Specifies the header metadata type.<br/>                                                                                                                                    |
| [**DXGI\_INFO\_QUEUE\_MESSAGE\_CATEGORY**](/windows/desktop/api/DXGIDebug/ne-dxgidebug-dxgi_info_queue_message_category)<br/>                   | Values that specify categories of debug messages.<br/>                                                                                                                      |
| [**DXGI\_INFO\_QUEUE\_MESSAGE\_SEVERITY**](/windows/desktop/api/DXGIDebug/ne-dxgidebug-dxgi_info_queue_message_severity)<br/>                   | Values that specify debug message severity levels for an information queue.<br/>                                                                                            |
| [**DXGI\_MEMORY\_SEGMENT\_GROUP**](/windows/desktop/api/dxgi1_4/ne-dxgi1_4-dxgi_memory_segment_group)<br/>                                  | Specifies the memory segment group to use.<br/>                                                                                                                             |
| [**DXGI\_MODE\_ROTATION**](/previous-versions/windows/desktop/legacy/bb173065(v=vs.85))<br/>                                        | Flags that indicate how the back buffers should be rotated to fit the physical rotation of a monitor.<br/>                                                                  |
| [**DXGI\_MODE\_SCALING**](/previous-versions/windows/desktop/legacy/bb173066(v=vs.85))<br/>                                          | Flags indicating how an image is stretched to fit a given monitor's resolution.<br/>                                                                                        |
| [**DXGI\_MODE\_SCANLINE\_ORDER**](/previous-versions/windows/desktop/legacy/bb173067(v=vs.85))<br/>                           | Flags indicating the method the raster uses to create an image on a surface.<br/>                                                                                           |
| [**DXGI\_MULTIPLANE\_OVERLAY\_YCbCr\_FLAGS**](/windows/desktop/api/dxgi1_3/ne-dxgi1_3-dxgi_multiplane_overlay_ycbcr_flags)<br/>             | Options for swap-chain color space.<br/>                                                                                                                                    |
| [**DXGI\_OFFER\_RESOURCE\_FLAGS**](/windows/desktop/api/dxgi1_5/ne-dxgi1_5-dxgi_offer_resource_flags)<br/>                                  | Specifies flags for the [**OfferResources1**](/windows/desktop/api/dxgi1_5/nf-dxgi1_5-idxgidevice4-offerresources1) method.<br/>                                                                                |
| [**DXGI\_OFFER\_RESOURCE\_PRIORITY**](/windows/desktop/api/dxgi1_2/ne-dxgi1_2-dxgi_offer_resource_priority)<br/>                           | Identifies the importance of a resource s content when you call the [**IDXGIDevice2::OfferResources**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgidevice2-offerresources) method to offer the resource. <br/> |
| [**DXGI\_OUTDUPL\_POINTER\_SHAPE\_TYPE**](/windows/desktop/api/DXGI1_2/ne-dxgi1_2-dxgi_outdupl_pointer_shape_type)<br/>                     | Identifies the type of pointer shape.<br/>                                                                                                                                  |
| [**DXGI\_OVERLAY\_COLOR\_SPACE\_SUPPORT\_FLAG**](/windows/desktop/api/DXGI1_4/ne-dxgi1_4-dxgi_overlay_color_space_support_flag)<br/>        | Specifies support for overlay color space.<br/>                                                                                                                             |
| [**DXGI\_OVERLAY\_SUPPORT\_FLAG**](/windows/desktop/api/DXGI1_3/ne-dxgi1_3-dxgi_overlay_support_flag)<br/>                                  | Specifies overlay support to check for in a call to [**IDXGIOutput3::CheckOverlaySupport**](/windows/desktop/api/DXGI1_3/nf-dxgi1_3-idxgioutput3-checkoverlaysupport).<br/>                                     |
| [**DXGI\_RECLAIM\_RESOURCE\_RESULTS**](/windows/desktop/api/dxgi1_5/ne-dxgi1_5-dxgi_reclaim_resource_results)<br/>                          | Specifies result flags for the [**ReclaimResources1**](/windows/desktop/api/dxgi1_5/nf-dxgi1_5-idxgidevice4-reclaimresources1) method.<br/>                                                                     |
| [**DXGI\_RESIDENCY**](/windows/desktop/api/dxgi/ne-dxgi-dxgi_residency)<br/>                                                 | Flags indicating the memory location of a resource.<br/>                                                                                                                    |
| [**DXGI\_SCALING**](/windows/desktop/api/DXGI1_2/ne-dxgi1_2-dxgi_scaling)<br/>                                                              | Identifies resize behavior when the back-buffer size does not match the size of the target output.<br/>                                                                     |
| [**DXGI\_SWAP\_CHAIN\_COLOR\_SPACE\_SUPPORT\_FLAG**](/windows/desktop/api/DXGI1_4/ne-dxgi1_4-dxgi_swap_chain_color_space_support_flag)<br/> | Specifies color space support for the swap chain.<br/>                                                                                                                      |
| [**DXGI\_SWAP\_CHAIN\_FLAG**](/windows/desktop/api/dxgi/ne-dxgi-dxgi_swap_chain_flag)<br/>                                   | Options for swap-chain behavior.<br/>                                                                                                                                       |
| [**DXGI\_SWAP\_EFFECT**](/windows/desktop/api/DXGI/ne-dxgi-dxgi_swap_effect)<br/>                                                     | Options for handling pixels in a display surface after calling [**IDXGISwapChain1::Present1**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgiswapchain1-present1). <br/>                                         |



 

## Related topics

<dl> <dt>

[DXGI Reference](d3d10-graphics-reference-dxgi.md)
</dt> </dl>

 

