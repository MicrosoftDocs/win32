---
Description: 'This section contains info about the enumerations provided by DXGI.'
ms.assetid: 'c4574c89-dee2-4841-9318-5383cf417111'
title: DXGI Enumerations
---

# DXGI Enumerations

This section contains info about the enumerations provided by DXGI.

## In this section



| Topic                                                                                                         | Description                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DXGI\_ADAPTER\_FLAG**](https://msdn.microsoft.com/library/windows/desktop/ff471327)<br/>                                          | Identifies the type of DXGI adapter.<br/>                                                                                                                                   |
| [**DXGI\_ADAPTER\_FLAG3**](https://msdn.microsoft.com/library/windows/desktop/mt825227)<br/>                                        | Identifies the type of DXGI adapter.<br/>                                                                                                                                   |
| [**DXGI\_ALPHA\_MODE**](dxgi-alpha-mode.md)<br/>                                                       | Identifies the alpha value, transparency behavior, of a surface.<br/>                                                                                                       |
| [**DXGI\_COLOR\_SPACE\_TYPE**](dxgi-color-space-type.md)<br/>                                          | Specifies color space types.<br/>                                                                                                                                           |
| [**DXGI\_COMPUTE\_PREEMPTION\_GRANULARITY**](dxgi-compute-preemption-granularity.md)<br/>              | Identifies the granularity at which the graphics processing unit (GPU) can be preempted from performing its current compute task.<br/>                                      |
| [**DXGI\_DEBUG\_RLO\_FLAGS**](dxgi-debug-rlo-flags.md)<br/>                                            | Flags used with [**ReportLiveObjects**](idxgidebug-reportliveobjects.md) to specify the amount of info to report about an object's lifetime. <br/>                         |
| [**DXGI\_FEATURE**](dxgi-feature.md)<br/>                                                              | Specifies a range of hardware features, to be used when checking for feature support.<br/>                                                                                  |
| [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059)<br/>                                                       | Resource data formats, including fully-typed and typeless formats. A list of modifiers at the bottom of the page more fully describes each format type. <br/>               |
| [**DXGI\_FRAME\_PRESENTATION\_MODE**](dxgi-frame-presentation-mode.md)<br/>                            | Indicates options for presenting frames to the swap chain. <br/>                                                                                                            |
| [**DXGI\_GPU\_PREFERENCE**](dxgi-gpu-preference.md)<br/>                                               | The preference of GPU for the app to run on.<br/>                                                                                                                           |
| [**DXGI\_GRAPHICS\_PREEMPTION\_GRANULARITY**](dxgi-graphics-preemption-granularity.md)<br/>            | Identifies the granularity at which the GPU can be preempted from performing its current graphics rendering task.<br/>                                                      |
| [**DXGI\_HARDWARE\_COMPOSITION\_SUPPORT\_FLAGS**](dxgi-hardware-composition-support-flags.md)<br/>     | Describes which levels of hardware composition are supported.<br/>                                                                                                          |
| [**DXGI\_HDR\_METADATA\_TYPE**](dxgi-hdr-metadata-type.md)<br/>                                        | Specifies the header metadata type.<br/>                                                                                                                                    |
| [**DXGI\_INFO\_QUEUE\_MESSAGE\_CATEGORY**](dxgi-info-queue-message-category.md)<br/>                   | Values that specify categories of debug messages.<br/>                                                                                                                      |
| [**DXGI\_INFO\_QUEUE\_MESSAGE\_SEVERITY**](dxgi-info-queue-message-severity.md)<br/>                   | Values that specify debug message severity levels for an information queue.<br/>                                                                                            |
| [**DXGI\_MEMORY\_SEGMENT\_GROUP**](dxgi-memory-segment-group.md)<br/>                                  | Specifies the memory segment group to use.<br/>                                                                                                                             |
| [**DXGI\_MODE\_ROTATION**](https://msdn.microsoft.com/library/windows/desktop/bb173065)<br/>                                        | Flags that indicate how the back buffers should be rotated to fit the physical rotation of a monitor.<br/>                                                                  |
| [**DXGI\_MODE\_SCALING**](https://msdn.microsoft.com/library/windows/desktop/bb173066)<br/>                                          | Flags indicating how an image is stretched to fit a given monitor's resolution.<br/>                                                                                        |
| [**DXGI\_MODE\_SCANLINE\_ORDER**](https://msdn.microsoft.com/library/windows/desktop/bb173067)<br/>                           | Flags indicating the method the raster uses to create an image on a surface.<br/>                                                                                           |
| [**DXGI\_MULTIPLANE\_OVERLAY\_YCbCr\_FLAGS**](dxgi-multiplane-overlay-ycbcr-flags.md)<br/>             | Options for swap-chain color space.<br/>                                                                                                                                    |
| [**DXGI\_OFFER\_RESOURCE\_FLAGS**](dxgi-offer-resource-flags.md)<br/>                                  | Specifies flags for the [**OfferResources1**](idxgidevice4-offerresources1.md) method.<br/>                                                                                |
| [**DXGI\_OFFER\_RESOURCE\_PRIORITY**](-dxgi-offer-resource-priority.md)<br/>                           | Identifies the importance of a resource’s content when you call the [**IDXGIDevice2::OfferResources**](idxgidevice2-offerresources.md) method to offer the resource. <br/> |
| [**DXGI\_OUTDUPL\_POINTER\_SHAPE\_TYPE**](dxgi-outdupl-pointer-shape-type.md)<br/>                     | Identifies the type of pointer shape.<br/>                                                                                                                                  |
| [**DXGI\_OVERLAY\_COLOR\_SPACE\_SUPPORT\_FLAG**](dxgi-overlay-color-space-support-flag.md)<br/>        | Specifies support for overlay color space.<br/>                                                                                                                             |
| [**DXGI\_OVERLAY\_SUPPORT\_FLAG**](dxgi-overlay-support-flag.md)<br/>                                  | Specifies overlay support to check for in a call to [**IDXGIOutput3::CheckOverlaySupport**](idxgioutput3-checkoverlaysupport.md).<br/>                                     |
| [**DXGI\_RECLAIM\_RESOURCE\_RESULTS**](dxgi-reclaim-resource-results.md)<br/>                          | Specifies result flags for the [**ReclaimResources1**](idxgidevice4-reclaimresources1.md) method.<br/>                                                                     |
| [**DXGI\_RESIDENCY**](https://msdn.microsoft.com/library/windows/desktop/bb173070)<br/>                                                 | Flags indicating the memory location of a resource.<br/>                                                                                                                    |
| [**DXGI\_SCALING**](dxgi-scaling.md)<br/>                                                              | Identifies resize behavior when the back-buffer size does not match the size of the target output.<br/>                                                                     |
| [**DXGI\_SWAP\_CHAIN\_COLOR\_SPACE\_SUPPORT\_FLAG**](dxgi-swap-chain-color-space-support-flag.md)<br/> | Specifies color space support for the swap chain.<br/>                                                                                                                      |
| [**DXGI\_SWAP\_CHAIN\_FLAG**](https://msdn.microsoft.com/library/windows/desktop/bb173076)<br/>                                   | Options for swap-chain behavior.<br/>                                                                                                                                       |
| [**DXGI\_SWAP\_EFFECT**](dxgi-swap-effect.md)<br/>                                                     | Options for handling pixels in a display surface after calling [**IDXGISwapChain1::Present1**](idxgiswapchain1-present1.md). <br/>                                         |



 

## Related topics

<dl> <dt>

[DXGI Reference](d3d10-graphics-reference-dxgi.md)
</dt> </dl>

 

 




