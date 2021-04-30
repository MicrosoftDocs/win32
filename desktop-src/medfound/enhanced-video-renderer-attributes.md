---
description: EVR Attributes
ms.assetid: 33f9bb09-625f-4bbb-a884-70c6bba3700b
title: EVR Attributes
ms.topic: article
ms.date: 05/31/2018
---

# EVR Attributes

The following attributes can be used to configure the Enhanced Video Renderer (EVR).



| Attribute                                                                                                         | Description                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [EVRConfig\_AllowBatching](evrconfig-allowbatching.md)                                                           | Allows the EVR to batch calls to the Microsoft Direct3D **IDirect3DDevice9::Present** method.                            |
| [EVRConfig\_AllowDropToBob](evrconfig-allowdroptobob.md)                                                         | Allows the EVR to improve performance by using bob deinterlacing.                                                        |
| [EVRConfig\_AllowDropToHalfInterlace](evrconfig-allowdroptohalfinterlace.md)                                     | Allows the EVR to improve performance by skipping the second field of every interlaced frame.                            |
| [EVRConfig\_AllowDropToThrottle](evrconfig-allowdroptothrottle.md)                                               | Allows the EVR to limit its output to match GPU bandwidth.                                                               |
| [EVRConfig\_AllowScaling](evrconfig-allowscaling.md)                                                             | Allows the EVR to mix the video within a rectangle that is smaller than the output rectangle, and then scale the result. |
| [EVRConfig\_ForceBatching](evrconfig-forcebatching.md)                                                           | Forces the EVR to batch calls to the **IDirect3D9Device::Present** method.                                               |
| [EVRConfig\_ForceBob](evrconfig-forcebob.md)                                                                     | Forces the EVR to use bob deinterlacing.                                                                                 |
| [EVRConfig\_ForceHalfInterlace](evrconfig-forcehalfinterlace.md)                                                 | Forces the EVR to skip the second field of every interlaced frame.                                                       |
| [EVRConfig\_ForceScaling](evrconfig-forcescaling.md)                                                             | Forces the EVR to mix the video within a rectangle that is smaller than the output rectangle, and then scale the result. |
| [EVRConfig\_ForceThrottle](evrconfig-forcethrottle.md)                                                           | Forces the EVR to limit its output to match GPU bandwidth.                                                               |
| [**MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_ACTIVATE**](mf-activate-custom-video-mixer-activate-attribute.md)         | Specifies an activation object that creates a custom video mixer for the enhanced video renderer (EVR).                  |
| [**MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_CLSID**](mf-activate-custom-video-mixer-clsid-attribute.md)               | CLSID of a custom video mixer for the EVR.                                                                               |
| [**MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_FLAGS**](mf-activate-custom-video-mixer-flags-attribute.md)               | Specifies how to create a custom mixer for the EVR.                                                                      |
| [**MF\_ACTIVATE\_CUSTOM\_VIDEO\_PRESENTER\_ACTIVATE**](mf-activate-custom-video-presenter-activate-attribute.md) | Specifies an activation object that creates a custom video presenter for the EVR.                                        |
| [**MF\_ACTIVATE\_CUSTOM\_VIDEO\_PRESENTER\_CLSID**](mf-activate-custom-video-presenter-clsid-attribute.md)       | CLSID of a custom video presenter for the EVR.                                                                           |
| [**MF\_ACTIVATE\_CUSTOM\_VIDEO\_PRESENTER\_FLAGS**](mf-activate-custom-video-presenter-flags-attribute.md)       | Specifies how to create a custom presenter for the EVR.                                                                  |
| [**MF\_ACTIVATE\_VIDEO\_WINDOW**](mf-activate-video-window-attribute.md)                                         | Handle to the video clipping window.                                                                                     |
| [**MF\_SA\_REQUIRED\_SAMPLE\_COUNT**](mf-sa-required-sample-count-attribute.md)                                  | Indicates the number of uncompressed buffers that the EVR media sink requires for deinterlacing.                         |
| [**VIDEO\_ZOOM\_RECT**](video-zoom-rect-attribute.md)                                                            | Specifies the zoom rectangle for the EVR mixer.                                                                          |



 

## Related topics

<dl> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> </dl>

 

 



