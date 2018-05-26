---
Description: The IOCTL\_USBPRINT\_GET\_LPT\_STATUS request allows upper-layer software (such as a language monitor), to request and obtain the printer status byte from a USB printer.
ms.assetid: 706e62f9-1be6-43bd-812a-dbb459877909
title: IOCTL\_USBPRINT\_GET\_LPT\_STATUS control code
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_USBPRINT\_GET\_LPT\_STATUS control code

The **IOCTL\_USBPRINT\_GET\_LPT\_STATUS** request allows upper-layer software (such as a language monitor), to request and obtain the printer status byte from a USB printer.

## Input Buffer

Not used in this operation; set this parameter to **NULL**. A pointer to a UCHAR input buffer.

## Input Buffer Length

Not used in this operation; set this parameter to 0. The size of the input buffer, in bytes.

## Output Buffer

A pointer to the output buffer, which consists of UCHAR data. On success this buffer holds the following: a two-byte prefix that specifies the size, in bytes, of the device's IEEE 1284 device ID; the device ID; and a null terminator. An IEEE 1284 device ID can be up to 64 KB in size. On failure, if **GetLastError** returns the error code **ERROR\_FILE\_NOT\_FOUND**, this buffer contains the value **BATTERY\_TAG\_INVALID**.

## Output Buffer Length

The size of the output buffer, in bytes.

## Status block

**Irp-&gt;IoStatus.Status** is set to **STATUS\_SUCCESS** if the request is successful. Otherwise, **Status** to the appropriate error condition as a [NTSTATUS](kernel.ntstatus_values) code.

## Remarks

To retrieve a handle to the device, you must call the **CreateFile** function with either the name of a device or the name of the driver associated with a device. To specify a device name, use the following format:

\\\\.\\DeviceName

**DeviceIoControl** can accept a handle to a specific device. For example, to open a handle to the logical drive A: with **CreateFile**, specify \\\\.\\a:. Alternatively, you can use the names \\\\.\\PhysicalDrive0, \\\\.\\PhysicalDrive1, and so on, to open handles to the physical drives on a system.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Usbprint.h</dt> </dl> |



## See also

<dl> <dt>

[Creating IOCTL Requests in Drivers](kernel.creating_ioctl_requests_in_drivers)
</dt> <dt>

[**WdfIoTargetSendInternalIoctlOthersSynchronously**](wdf.wdfiotargetsendinternalioctlotherssynchronously)
</dt> <dt>

[**WdfIoTargetSendInternalIoctlSynchronously**](wdf.wdfiotargetsendinternalioctlsynchronously)
</dt> <dt>

[**WdfIoTargetSendIoctlSynchronously**](wdf.wdfiotargetsendioctlsynchronously)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IOCTL_USBPRINT_GET_LPT_STATUS%20control%20code%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





