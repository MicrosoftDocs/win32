---
title: Storage I/O Requests
description: Storage I/O Requests
ms.assetid: '86d23bec-f70c-4ad3-bd0d-85259e83b3c6'
---

# Storage I/O Requests

## 

The list that follows contains the major IRPs that storage drivers must handle. The list provides a brief description of each major IRP. For more information about these IRPs, see [IRP Major Function Codes](https://msdn.microsoft.com/library/windows/hardware/ff550710).

-   IRP\_MJ\_CLOSE
    -   **Drivers Required to Handle this IRP** - All mass storage drivers must handle this request. For more information, see [**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff550720).
    -   **General Description** - Returns STATUS\_SUCCESS to indicate that the driver has completed the request.
    -   **When Called** - The handle to the file object that represents that the target device object was released.

<!-- -->

-   IRP\_MJ\_CREATE
    -   **Drivers Required to Handle this IRP** - All mass storage drivers must handle this request. For more information, see [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729).
    -   **General Description** - Returns STATUS\_SUCCESS to indicate that the device or partition exists. For a disk or CD-ROM device, this request opens the device as the target of I/O requests from the caller.
    -   **When Called** - A higher-level driver tries to connect or attach one of its device objects to the target device object, or a user-mode process has tried to open a file that is stored on the physical device. This causes a file system to perform a mount operation.

<!-- -->

-   IRP\_MJ\_DEVICE\_CONTROL
    -   **Drivers Required to Handle this IRP** - All mass storage drivers must handle this request. For more information, see [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744).
    -   **General Description** - Determined by the I/O control code set at **Parameters.DeviceIoControl.IoControlCode** in the driver's I/O stack location of the IRP. An **IoControlCode** value of [**IOCTL\_SCSI\_PASS\_THROUGH**](ioctl-scsi-pass-through.md) together with a **MinorFunction** value of IRP\_MN\_SCSI\_CLASS indicates that the pass-through IOCTL request was processed by a storage class driver before it was forwarded to the port driver. For more information about SCSI pass-through requests, see [Handling SCSI Pass-Through Requests](https://msdn.microsoft.com/library/windows/hardware/ff556006).
    -   **When Called** - A Win32 application has called [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216), or a higher-level driver has set up such a request.
-   IRP\_MJ\_FLUSH\_BUFFERS
    -   **Drivers Required to Handle this IRP** - Drivers of devices with internal caches for data and drivers that maintain internal buffers for data must handle this request. For more information, see [**IRP\_MJ\_FLUSH\_BUFFERS**](https://msdn.microsoft.com/library/windows/hardware/ff550760).
    -   **General Description** - Transfers any data that was cached in the device or in the driver's internal buffer(s) to system memory or out to the device. If the device or driver supports caching or buffering data, the driver must handle this request.
    -   **When Called** - A file system or DTP application makes this request to ensure data integrity.
-   IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL
    -   **Drivers Required to Handle this IRP** - This IRP is equivalent to IRP\_MJ\_SCSI. Only the port driver must handle this IRP. For more information, see [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766)
    -   **General Description** - Sends queue control commands to the port driver.
    -   **When Called** - A storage class driver or an application can use this driver to issue queue control commands to the port driver.
-   IRP\_MJ\_PNP
    -   **Drivers Required to Handle this IRP** - Storage drivers that support Plug and Play (PnP) must handle this request. For more information, see [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772).
    -   **General Description** - Determined by the minor function code that is set in the I/O stack location of the IRP.
    -   **When Called** - The PnP manager sends this request to initiate a PnP operation, such as starting or stopping a device.
-   IRP\_MJ\_POWER
    -   **Drivers Required to Handle this IRP** - Storage drivers that support power management must handle this request. For more information, see [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784).
-   IRP\_MJ\_READ
    -   **Drivers Required to Handle this IRP** - Disk, CD-ROM, DVD, and tape drivers must handle this request. For more information, see [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794).
    -   **General Description** - Transfers data from the device to system memory.
    -   **When Called** - A user-mode application that has a handle for an opened file or a handle for the opened file object that represents that the device has requested data. This request can also be issued by a higher-level driver.
-   IRP\_MJ\_SCSI
    -   **Drivers Required to Handle this IRP** - Port drivers must handle this request.
    -   **General Description** - Storage class drivers, or possibly applications, can use this request to send queue control commands to the port driver.
    -   **When Called** - The storage class driver calls this routine to lock or unlock the port driver's request queue or to issue a request to change to the power state of a device.
-   IRP\_MJ\_SHUTDOWN
    -   **Drivers Required to Handle this IRP** - Disk and tape drivers must handle this request. For more information, see [**IRP\_MJ\_SHUTDOWN**](https://msdn.microsoft.com/library/windows/hardware/ff550807).
    -   **General Description** - Transfers any data that is cached in the device or in the driver's internal buffer(s) to system memory or out to the device before the system is shut down. If the device or driver supports caching or buffering data, the driver must handle this request. The **Status** field of the I/O Status Block is set to STATUS\_SUCCESS when the data was transferred.
    -   **When Called** - The user has decided to shut down the system.
-   IRP\_MJ\_SYSTEM\_CONTROL
    -   **Drivers Required to Handle this IRP** - All storage drivers must support this request. For more information, see [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813).
-   IRP\_MJ\_WRITE
    -   **Drivers Required to Handle this IRP** - Disk and tape drivers must handle this request. For more information, see [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819).
    -   **General Description** - Transfers data from system memory to the underlying device. The **Information** field of the I/O Status Block is set to the number of bytes that are transferred, whatever the **Status** field's value. Possible values are any of those returned for read requests, STATUS\_MEDIA\_WRITE\_PROTECTED returned by drivers of removable-media devices, and STATUS\_NOT\_SUPPORTED returns by the system for drivers that have no *DispatchWrite* routine.
    -   **Input** - Drivers of disk and tape devices generally use direct I/O, so the lowest-level driver transfers data by using DMA or PIO from the buffer described by the MDL at **Irp-&gt;MdlAddress**.
    -   **When Called** - A user-mode application that has a handle for an opened file or a handle for the opened file object that represents that the device has requested data be written to the device. This request can also be issued by a higher-level driver.

Errors returned by these IRPs vary according to the device, the minor IRP number, and for device control IRPs, the IOCTL value. The following list identifies some common errors:

<dl> Device Errors


```
STATUS_INVALID_DEVICE_REQUEST
STATUS_NO_SUCH_DEVICE
STATUS_IO_TIMEOUT
STATUS_DEVICE_NOT_CONNECTED 
STATUS_IO_DEVICE_ERROR 
STATUS_DEVICE_NOT_READY 
STATUS_DEVICE_BUSY 
```



  
Sector/Data Errors


```
STATUS_DEVICE_DATA_ERROR
STATUS_CRC_ERROR 
```



  
and, by drivers of removable-media devices:


```
STATUS_NO_MEDIA_IN_DEVICE
STATUS_VERIFY_REQUIRED
```



  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Storage%20I/O%20Requests%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




