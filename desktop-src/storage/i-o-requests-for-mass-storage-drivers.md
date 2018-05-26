---
title: I/O requests for mass storage drivers
description: This section describes the basic set of I/O requests that are sent to drivers of storage devices and to intermediate drivers that are layered above them.
ms.assetid: 31562bc0-1bcc-4218-b82d-7f60f5a453bd
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# I/O requests for mass storage drivers

This section describes the basic set of I/O requests that are sent to drivers of storage devices and to intermediate drivers that are layered above them. It describes the system-defined I/O control codes that must be handled by all storage devices and those that must be handled by a particular type of device.

Most I/O control codes listed in this section can be issued from either a kernel-mode driver or a user-mode application. When the I/O control code is issued from a kernel-mode driver, the caller provides an I/O Request Packet (IRP) that contains an IO\_STATUS\_BLOCK data structure. This data structure is used to return error information to the caller. When the I/O control code is issued from a user-mode application with the DeviceIocontrol routine, the caller can obtain error information by calling the GetLastError routine.

## 

This section contains the following information:

-   [Blocking Direct Write Operations to Volumes and Disks](blocking-direct-write-operations-to-volumes-and-disks.md)

-   [Storage I/O Requests](storage-i-o-requests.md)

-   [General Storage I/O Control Codes](general-storage-i-o-control-codes.md)

-   [Disk I/O Control Codes](disk-i-o-control-codes.md)

-   [CD-ROM I/O Control Codes](cd-rom-i-o-control-codes.md)

-   [DVD I/O Control Codes](dvd-i-o-control-codes.md)

-   [IDE I/O Control Codes](ide-i-o-control-codes.md)

-   [Tape I/O Control Codes](tape-i-o-control-codes.md)

-   [Changer I/O Control Codes](changer-i-o-control-codes.md)

-   [SCSI Port I/O Control Codes](scsi-port-i-o-control-codes.md)

-   [MPIO I/O Control Codes](mpio-i-o-control-codes.md)

-   [Mount Manager I/O Control Codes](mount-manager-i-o-control-codes.md)

-   [Volume Manager I/O Control Codes](volume-manager-i-o-control-codes.md)

-   [NV Cache Manager I/O Control Codes](nv-cache-manager-i-o-control-codes.md)

-   [Virtual Miniport I/O Control Codes](virtual-miniport-i-o-control-codes.md)

-   [Storage Silo Driver I/O Control Codes](storage-silo-driver-i-o-control-codes.md)

## Related topics

<dl> <dt>

[Storage driver design guide](http://go.microsoft.com/fwlink/p/?LinkId=798409)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20I/O%20requests%20for%20mass%20storage%20drivers%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





