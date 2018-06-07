---
title: Winioctl.h
description: This section contains reference topics for the Winioctl.h header.
ms.assetid: 28DAE998-CADC-46F7-BB20-E5B8B7C47E3F
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Winioctl.h

This section contains reference topics for the Winioctl.h header.

## In this section



| Topic                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOCTL\_CDROM\_ENABLE\_STREAMING Control Code**](ioctl-cdrom-enable-streaming.md)<br/>          | Enables or disables CDROM streaming mode on a per-handle basis for raw read and write requests. <br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function and specify the [**IOCTL\_CDROM\_ENABLE\_STREAMING**](ioctl-cdrom-enable-streaming.md) I/O control request as the *dwIoControlCode* parameter.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**IOCTL\_CDROM\_GET\_PERFORMANCE Control Code**](ioctl-cdrom-get-performance.md)<br/>            | Retrieves the supported speeds from the device. The [**IOCTL\_CDROM\_GET\_PERFORMANCE**](ioctl-cdrom-get-performance.md) I/O control request is a wrapper over the MMC command, GET PERFORMANCE.<br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with [**IOCTL\_CDROM\_GET\_PERFORMANCE**](ioctl-cdrom-get-performance.md) as the *dwIoControlCode* parameter.<br/>                                                                                                                                                                                                                                                                                                                                                             |
| [**IOCTL\_CDROM\_SEND\_OPC\_INFORMATION Control Code**](ioctl-cdrom-send-opc-information.md)<br/> | The [**IOCTL\_CDROM\_SEND\_OPC\_INFORMATION**](ioctl-cdrom-send-opc-information.md) control code can be used in file systems and other implementations that want to perform the Optimum Power Calibration (OPC) procedure in advance, so that the first streaming write does not have to wait for the procedure to finish. The optical drive performs the OPC procedure to determine the optimum power of the laser during write. The procedure is necessary to ensure quality, but it wears out the media and should not be performed too often.<br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with [**IOCTL\_CDROM\_SEND\_OPC\_INFORMATION**](ioctl-cdrom-send-opc-information.md) as the *dwIoControlCode* parameter.<br/> |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Winioctl.h%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





