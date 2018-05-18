---
Description: 'This section contains reference topics for the Dxmini.h header.'
ms.assetid: '263FD822-C2B6-4C78-8F03-586AAE43325A'
title: 'Dxmini.h'
---

# Dxmini.h

This section contains reference topics for the Dxmini.h header.

## In this section



| Topic                                                                           | Description                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DDBOBNEXTFIELDINFO**](ddbobnextfieldinfo.md)<br/>                     | The DDBOBNEXTFIELDINFO structure contains the bob information for the surface. <br/>                                                                                                                                                                                            |
| [**DDFLIPOVERLAYINFO**](ddflipoverlayinfo.md)<br/>                       | The DDFLIPOVERLAYINFO structure contains the flip information for the surface. <br/>                                                                                                                                                                                            |
| [**DDFLIPVIDEOPORTINFO**](ddflipvideoportinfo.md)<br/>                   | The DDFLIPVIDEOPORTINFO structure contains the [video port extensions (VPE)](wdkgloss.v#wdkgloss-video-port-extensions--vpe-) object and surface information. <br/>                                                                        |
| [**DDGETCURRENTAUTOFLIPININFO**](ddgetcurrentautoflipininfo.md)<br/>     | The DDGETCURRENTAUTOFLIPININFO structure contains the [video port extensions (VPE)](wdkgloss.v#wdkgloss-video-port-extensions--vpe-) object information. <br/>                                                                             |
| [**DDGETCURRENTAUTOFLIPOUTINFO**](ddgetcurrentautoflipoutinfo.md)<br/>   | The DDGETCURRENTAUTOFLIPOUTINFO structure provides the surface information. <br/>                                                                                                                                                                                               |
| [**DDGETIRQINFO**](ddgetirqinfo.md)<br/>                                 | The DDGETIRQINFO structure contains interrupt information for the video miniport driver. <br/>                                                                                                                                                                                  |
| [**DDGETPOLARITYININFO**](ddgetpolarityininfo.md)<br/>                   | The DDGETPOLARITYININFO structure contains the [video port extensions (VPE)](wdkgloss.v#wdkgloss-video-port-extensions--vpe-) object information. <br/>                                                                                    |
| [**DDGETPOLARITYOUTINFO**](ddgetpolarityoutinfo.md)<br/>                 | The DDGETPOLARITYOUTINFO structure contains the polarity information of the [video port extensions (VPE)](wdkgloss.v#wdkgloss-video-port-extensions--vpe-) object. <br/>                                                                   |
| [**DDGETPREVIOUSAUTOFLIPININFO**](ddgetpreviousautoflipininfo.md)<br/>   | The DDGETPREVIOUSAUTOFLIPININFO structure provides the [video port extensions (VPE)](wdkgloss.v#wdkgloss-video-port-extensions--vpe-) object information. <br/>                                                                            |
| [**DDGETPREVIOUSAUTOFLIPOUTINFO**](ddgetpreviousautoflipoutinfo.md)<br/> | The DDGETPREVIOUSAUTOFLIPOUTINFO structure provides the surface data. <br/>                                                                                                                                                                                                     |
| [**DDGETTRANSFERSTATUSOUTINFO**](ddgettransferstatusoutinfo.md)<br/>     | The DDGETTRANSFERSTATUSOUTINFO structure contains the transfer status information. <br/>                                                                                                                                                                                        |
| [**DDLOCKININFO**](ddlockininfo.md)<br/>                                 | The DDLOCKININFO structure contains the surface information. <br/>                                                                                                                                                                                                              |
| [**DDLOCKOUTINFO**](ddlockoutinfo.md)<br/>                               | The DDLOCKOUTINFO structure contains the surface information output from the [*DxLock*](dxlock.md) function. <br/>                                                                                                                                                             |
| [**DDSETSTATEININFO**](ddsetstateininfo.md)<br/>                         | The DDSETSTATEININFO structure contains the surface and [video port extensions (VPE)](wdkgloss.v#wdkgloss-video-port-extensions--vpe-) object information. <br/>                                                                           |
| [**DDSETSTATEOUTINFO**](ddsetstateoutinfo.md)<br/>                       | The DDSETSTATEOUTINFO structure contains the state information for the [video port extensions (VPE)](wdkgloss.v#wdkgloss-video-port-extensions--vpe-) object. <br/>                                                                        |
| [**DDSKIPNEXTFIELDINFO**](ddskipnextfieldinfo.md)<br/>                   | The DDSKIPNEXTFIELDINFO structure contains the skip information for the [video port extensions (VPE)](wdkgloss.v#wdkgloss-video-port-extensions--vpe-) object. <br/>                                                                       |
| [**DDSURFACEDATA**](ddsurfacedata.md)<br/>                               | The DDSURFACEDATA structure is used by DirectDraw to represent a surface to the kernel-mode miniport driver. <br/>                                                                                                                                                              |
| [**DDTRANSFERININFO**](ddtransferininfo.md)<br/>                         | The DDTRANSFERININFO structure contains the transfer information for the surface <br/>                                                                                                                                                                                          |
| [**DDTRANSFEROUTINFO**](ddtransferoutinfo.md)<br/>                       | The DDTRANSFEROUTINFO structure returns the polarity of the field being captured.<br/>                                                                                                                                                                                          |
| [**DDVIDEOPORTDATA**](ddvideoportdata.md)<br/>                           | The DDVIDEOPORTDATA structure is used by DirectDraw to represent a [video port extensions (VPE)](wdkgloss.v#wdkgloss-video-port-extensions--vpe-) object to the kernel-mode video miniport driver. <br/>                                   |
| [**DX\_IRQDATA**](dx-irqdata.md)<br/>                                    | The DX\_IRQDATA structure contains the IRQ information supplied by the driver.<br/>                                                                                                                                                                                             |
| [**DXAPI\_INTERFACE**](dxapi-interface.md)<br/>                          | The DXAPI\_INTERFACE structure contains the interface callback functions that a [video miniport driver](display.video_miniport_drivers_in_the_windows_2000_display_driver_model) implements to support [Kernel-Mode Video Transport](display.kernel_mode_video_transport).<br/> |
| [*PDX\_IRQCALLBACK*](irqcallback.md)<br/>                                | The **IRQCallback** function performs operations related to the IRQ that occurred. <br/>                                                                                                                                                                                        |
| [DxApi Functions](dxapi-functions.md)<br/>                               |                                                                                                                                                                                                                                                                                       |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdisplay\display%5D:%20Dxmini.h%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




