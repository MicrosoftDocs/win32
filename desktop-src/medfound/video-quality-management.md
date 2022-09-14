---
description: Video Quality Management
ms.assetid: 3617adf2-ed7b-4788-abce-58bc22a14511
title: Video Quality Management
ms.topic: article
ms.date: 05/31/2018
---

# Video Quality Management

This topic describes some improvements to the video pipeline in Windows 7, both for Microsoft Media Foundation and Microsoft DirectShow.

In a perfect world, video would never glitch, regardless of the video resolution or the CPU/GPU load. In reality, of course, the video pipeline must be able to cope with finite hardware resources, and it must adaptively tailor playback to the system environment. The goals for video quality management are to:

-   Reduce glitching (dropped or late frames).
-   Reduce memory usage, especially in the GPU.
-   Reduce power consumption, especially in laptops running on battery power.
-   Get the best image quality possible, given resource constraints.
-   Keep video synchronized with audio.

Some of these goals are contrary, particularly on low-end systems. Generally there is a trade-off between speed and quality. Glitching is more objectionable than moderate reductions in visual quality. The relative importance of power consumption varies with the environment; in a laptop running on battery power, it is very important.

In Windows 7, the enhanced video renderer (EVR) has better support for video quality management. Both the Media Foundation pipeline and the DirectShow pipeline have been updated to take advantage of these capabilities. A two-pronged approach is used:

-   Before playback starts, the pipeline can perform static optimizations, based on the user's power management settings and information about the hardware.
-   After playback starts, the pipeline can apply dynamic optimizations, based on run-time performance.

## Quality Management in Media Foundation

To enable static optimizations, set the [MF\_TOPOLOGY\_STATIC\_PLAYBACK\_OPTIMIZATIONS](mf-topology-static-playback-optimizations.md) attribute on the partial topology before resolving the topology. The topology loader queries this attribute in its [**IMFTopoLoader::Load**](/windows/desktop/api/mfidl/nf-mfidl-imftopoloader-load) method.

If you enable static optimizations, you should set two other attributes on the topology:



| Attribute                                                                                                                                      | Description                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <span id="MF_TOPOLOGY_PLAYBACK_MAX_DIMS"></span><span id="mf_topology_playback_max_dims"></span>MF\_TOPOLOGY\_PLAYBACK\_MAX\_DIMS<br/>   | Specifies the maximum size of the video playback window.<br/> |
| <span id="MF_TOPOLOGY_PLAYBACK_FRAMERATE"></span><span id="mf_topology_playback_framerate"></span>MF\_TOPOLOGY\_PLAYBACK\_FRAMERATE<br/> | Specifies the monitor refresh rate.<br/>                      |



 

These two attributes help the pipeline calculate the most effective setting for quality management.

Dynamic optimizations are performed by the quality manager. You do not need to do anything to enable the quality manager; it is automatically enabled. The quality manager existed in Windows Vista; in Windows 7, the EVR can respond better to messages from the quality manager.

## Quality Management in DirectShow

DirectShow supports static and dynamic optimizations for DVD playback. To enable these optimizations in a DVD playback application, set the following flags in the *dwFlags* parameter of the **IDvdGraphBuilder::RenderDvdVideoVolume** method:



| Flag                  | Description                    |
|-----------------------|--------------------------------|
| AM\_DVD\_ADAPT\_GRAPH | Enables static optimizations.  |
| AM\_DVD\_EVR\_QOS     | Enables dynamic optimizations. |



 

Other DirectShow applications can enable dynamic optimizations by calling the [**IEVRFilterConfigEx::SetConfigPrefs**](/windows/desktop/api/evr/nf-evr-ievrfilterconfigex-setconfigprefs) method directly on the EVR filter. Specify the **EVRFilterConfigPrefs\_EnableQoS** flag.

> [!Note]  
> Static optimizations in DirectShow are limited to DVD playback.

 

## Quality Management in the EVR

The EVR supports some new configuration flags for quality management. If you enable the quality management optimizations described previously, you do not have to set these flags directly. However, they are documented for applications that want more granular control over the EVR.

Set the following flags on the EVR mixer by calling the [**IMFVideoMixerControl2::SetMixingPrefs**](/windows/desktop/api/evr/nf-evr-imfvideomixercontrol2-setmixingprefs) method:




| Flags | Description | 
|-------|-------------|
| <ul><li><strong>MFVideoMixPrefs_ForceHalfInterlace</strong></li><li><strong>MFVideoMixPrefs_AllowDropToHalfInterlace</strong></li></ul> | Skip the second field of every interlaced frame. | 
| <ul><li><strong>MFVideoMixPrefs_AllowDropToBob</strong></li><li><strong>MFVideoMixPrefs_ForceBob</strong></li></ul> | Use bob deinterlacing, even if the driver supports a higher-quality deinterlace mode. | 




 

Set the following flags on the EVR presenter by calling the [**IMFVideoDisplayControl::SetRenderingPrefs**](/windows/desktop/api/evr/nf-evr-imfvideodisplaycontrol-setrenderingprefs) method:




| Flags | Description | 
|-------|-------------|
| <ul><li><strong>MFVideoRenderPrefs_ForceOutputThrottling</strong></li><li><strong>MFVideoRenderPrefs_AllowOutputThrottling</strong></li></ul> | Throttle output to match GPU bandwidth. | 
| <ul><li><strong>MFVideoRenderPrefs_ForceBatching</strong></li><li><strong>MFVideoRenderPrefs_AllowBatching</strong></li></ul> | Batch Direct3D Present calls. This optimization enables the system to enter into idle states more frequently, which can reduce power consumption. | 
| <ul><li>MFVideoRenderPrefs_ForceScaling</li><li>MFVideoRenderPrefs_AllowScaling</li></ul> | Perform video mixing using a rectangle smaller than the output rectangle. Scale the result to the correct output size. | 




 

In addition, the EVR media sink supports configuration attributes that correspond to each of these flags:

-   [EVRConfig\_AllowBatching](evrconfig-allowbatching.md)
-   [EVRConfig\_AllowDropToBob](evrconfig-allowdroptobob.md)
-   [EVRConfig\_AllowDropToHalfInterlace](evrconfig-allowdroptohalfinterlace.md)
-   [EVRConfig\_AllowScaling](evrconfig-allowscaling.md)
-   [EVRConfig\_AllowDropToThrottle](evrconfig-allowdroptothrottle.md)
-   [EVRConfig\_ForceBatching](evrconfig-forcebatching.md)
-   [EVRConfig\_ForceBob](evrconfig-forcebob.md)
-   [EVRConfig\_ForceHalfInterlace](evrconfig-forcehalfinterlace.md)
-   [EVRConfig\_ForceScaling](evrconfig-forcescaling.md)
-   [EVRConfig\_ForceThrottle](evrconfig-forcethrottle.md)

Before playback starts, you can set these attributes directly on the EVR media sink, as an alternative to calling the [**IMFVideoMixerControl2**](/windows/desktop/api/evr/nn-evr-imfvideomixercontrol2) and [**IMFVideoDisplayControl**](/windows/desktop/api/evr/nn-evr-imfvideodisplaycontrol) methods. To set these attributes, query the EVR media sink for [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes).

## Related topics

<dl> <dt>

[Media Session](media-session.md)
</dt> </dl>

 

 




