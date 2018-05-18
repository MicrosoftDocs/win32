---
title: General Storage I/O Control Codes
description: General Storage I/O Control Codes
ms.assetid: '24b54cc9-f56c-4d32-927c-0f774bc534d4'
---

# General Storage I/O Control Codes

## 

Storage devices of different kinds often require the same services. Rather than duplicate the IOCTL requests that provide these services for each device type, this section defines a set of standard services and accompanying device control codes that are frequently required by storage devices. The I/O control codes defined here have the form IOCTL\_STORAGE\_*XXX* and they replace the IOCTL\_*DeviceType*\_*XXX* control codes, where *DeviceType* was DISK, TAPE, or CDROM. For example, IOCTL\_STORAGE\_RESERVE replaces IOCTL\_DISK\_RESERVE, IOCTL\_TAPE\_RESERVE, and IOCTL\_CDROM\_RESERVE. The IOCTL\_STORAGE\_*XXX* control codes have identical values for function code, transfer method, and required access as the previous disk, tape, and CD-ROM codes. The only difference is the device type.

The storage class driver initiates some of these requests, but usually it is an application that does so. Storage class drivers must handle some or all of these requests, depending on the type of storage device. Where no storage class driver exists, the application might make the request directly to the port driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20General%20Storage%20I/O%20Control%20Codes%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




