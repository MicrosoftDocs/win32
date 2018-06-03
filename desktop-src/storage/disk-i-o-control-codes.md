---
title: Disk I/O Control Codes
description: Disk I/O Control Codes
ms.assetid: 754f1f14-dbfa-4d86-93f1-fe53efd96bd0
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Disk I/O Control Codes

## 

The following summarizes the public I/O control codes that disk-type drivers support. However, each device driver is required to handle only those I/O control codes that its particular device(s) support.

For example, only a floppy driver would handle IOCTL\_STORAGE\_GET\_MEDIA\_TYPES requests; it would not handle IOCTL\_DISK\_GET/SET\_PARTITION\_INFO or IOCTL\_GET/SET\_DRIVE\_LAYOUT requests. As another example, a filter driver like the system-supplied diskperf driver that monitors disk performance statistics would handle IOCTL\_DISK\_PERFORMANCE requests from a corresponding (user-mode) application; it would simply pass down other IOCTL\_DISK\_*XXX* requests to the underlying disk device driver.

All public I/O control codes for drivers of disk-type devices use buffered I/O. Consequently, the input or output data buffer for these requests is at **Irp-&gt;AssociatedIrp.SystemBuffer**.

Class drivers for storage devices handle additional public I/O control codes, along with those described in this section. For more information about requirements for storage class drivers, see [General Storage I/O Control Codes](general-storage-i-o-control-codes.md).

The IOCTL\_INTERNAL\_DISK\_*XXXXX* codes can be used for communication between two kernel-mode drivers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Disk%20I/O%20Control%20Codes%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




