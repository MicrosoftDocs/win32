---
Description: 'This section contains reference topics for the Tvout.h header.'
ms.assetid: 'B8D412B8-1F4F-4827-97DC-3FFAA52F1CA8'
title: 'Tvout.h'
---

# Tvout.h

This section contains reference topics for the Tvout.h header.

## In this section



| Topic                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**VIDEOPARAMETERS**](videoparameters.md)<br/> | The video miniport driver receives a pointer to a VIDEOPARAMETERS structure in the **InputBuffer** member of a [**VIDEO\_REQUEST\_PACKET**](video-request-packet.md) when the IOCTL request is [**IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS**](ioctl-video-handle-videoparameters.md). Depending on the **dwCommand** member of the VIDEOPARAMETERS structure, the miniport driver should get or set the television connector and copy protection capabilities of the device.<br/> |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdisplay\display%5D:%20Tvout.h%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




