---
title: I/O Control Codes Sent by the Mount Manager
description: I/O Control Codes Sent by the Mount Manager
ms.assetid: 7bc798c6-ed14-4721-994e-5df9112ed882
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# I/O Control Codes Sent by the Mount Manager

## 

The mount manager publishes an interface that client drivers, such as class drivers, must support -to receive persistent symbolic link names from the mount manager. the mount manager client drivers register to receive the IOCTLs listed in this section from the mount manager by calling **IoRegisterDeviceInterface** with the MOUNTDEV\_MOUNTED\_DEVICE\_GUID GUID defined in *Mountmgr.h*. Any driver that subscribes to this interface must support some subset of these IOCTLs. To determine whether a specific IOCTL is required, check the **Operation** section of the IOCTL.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20I/O%20Control%20Codes%20Sent%20by%20the%20Mount%20Manager%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




