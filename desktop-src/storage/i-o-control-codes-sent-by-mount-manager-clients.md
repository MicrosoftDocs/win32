---
title: I/O Control Codes Sent by Mount Manager Clients
description: I/O Control Codes Sent by Mount Manager Clients
ms.assetid: 1a75fa4d-c04b-419b-ada9-7634d9adf370
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# I/O Control Codes Sent by Mount Manager Clients

## 

The mount manager publishes an interface that allows the mount manager's clients to set, query, and delete persistent names for volumes. To access this interface, clients can obtain a pointer to the mount manager's device object using the object name MOUNTMGR\_DEVICE\_NAME, defined in *Mountmgr.h*. For instance:


```
    // Obtain a pointer to the mount manager device object &amp;
    // use it to send any of the I/O Control codes in this 
    // section to the mount manager.
    RtlInitUnicodeString(&amp;name, MOUNTMGR_DEVICE_NAME);
    status = IoGetDeviceObjectPointer(&amp;name,
                FILE_READ_ATTRIBUTES, 
                &amp;fileObject, &amp;deviceObject);
    irp = IoBuildDeviceIoControlRequest(
            IOCTL_MOUNTMGR_CREATE_POINT,
            deviceObject, createPoint, createPointSize, 
            NULL, 0, FALSE, &amp;event, &amp;ioStatus);
    status = IoCallDriver(deviceObject, irp);
```



The call sequence in this pseudocode sample has been simplified for the sake of brevity. For a more complete pseudocode example, see [**IOCTL\_MOUNTMGR\_CREATE\_POINT**](ioctl-mountmgr-create-point.md).

The following material describes the I/O control codes that the mount manager clients can send to the mount manager.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20I/O%20Control%20Codes%20Sent%20by%20Mount%20Manager%20Clients%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




