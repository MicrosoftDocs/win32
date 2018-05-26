---
title: IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_OUT control code
description: The generic storage class driver (classpnp.sys) exposes an I/O control (IOCTL) interface for issuing Persistent Reserve Out commands.
ms.assetid: a9863ac9-46e2-4888-879e-7d56e9260142
keywords:
- IOCTL_STORAGE_PERSISTENT_RESERVE_OUT control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_PERSISTENT_RESERVE_OUT
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_OUT control code

The generic storage class driver (*classpnp.sys*) exposes an I/O control (IOCTL) interface for issuing Persistent Reserve Out commands. The behavior of the storage device when a Persistent Reserve Out command is received is described in the [SCSI Primary Commands - 2 (SPC-2)](http://go.microsoft.com/fwlink/p/?linkid=153142) specification. The IOCTL interface requires the caller to have read/write access to the physical device for Persistent Reserve Out commands. User-mode applications, services, and kernel-mode drivers can use this IOCTL to control persistent reservations. If called from a driver, this IOCTL must be called from a thread running at IRQL &lt; DISPATCH\_LEVEL. This IOCTL is defined with FILE\_READ\_ACCESS and FILE\_WRITE\_ACCESS, requiring a device handle to have both read and write permissions to issue the Persistent Reserve Out command.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**PERSISTENT\_RESERVE\_COMMAND**](persistent-reserve-command.md) structure. You must allocate the buffer from nonpaged pool and must align it correctly for the target device and adapter.

PR\_OUT.ServiceAction can be one of the following:

-   RESERVATION\_ACTION\_REGISTER

-   RESERVATION\_ACTION\_RESERVE

-   RESERVATION\_ACTION\_RELEASE

-   RESERVATION\_ACTION\_CLEAR

-   RESERVATION\_ACTION\_PREEMPT

-   RESERVATION\_ACTION\_PREEMPT\_ABORT

-   RESERVATION\_ACTION\_REGISTER\_IGNORE\_EXISTING

PR\_OUT.Scope can be one of the following:

-   RESERVATION\_SCOPE\_LU

-   RESERVATION\_SCOPE\_ELEMENT

PR\_OUT.Type can be one of the following:

-   RESERVATION\_TYPE\_WRITE\_EXCLUSIVE

-   RESERVATION\_TYPE\_EXCLUSIVE

-   RESERVATION\_TYPE\_WRITE\_EXCLUSIVE\_REGISTRANTS

-   RESERVATION\_TYPE\_EXCLUSIVE\_REGISTRANTS

PR\_OUT.ParameterList is used to hold the [**PRO\_PARAMETER\_LIST**](pro-parameter-list.md) structure. This structure is required and must be contiguous with the rest of the [**PERSISTENT\_RESERVE\_COMMAND**](persistent-reserve-command.md) structure.

## Input Buffer Length

The length of a [**PERSISTENT\_RESERVE\_COMMAND**](persistent-reserve-command.md) structure.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero.

The **Status** field is set to one of the following:

<dl> <dt>

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS
</dt> <dd>

The operation was successful.

</dd> <dt>

<span id="STATUS_INVALID_PARAMETER__ERROR_INVALID_PARAMETER_"></span><span id="status_invalid_parameter__error_invalid_parameter_"></span>STATUS\_INVALID\_PARAMETER (ERROR\_INVALID\_PARAMETER)
</dt> <dd>

The input buffer structure is incorrectly sized or populated.

</dd> <dt>

<span id="STATUS_INVALID_DEVICE_REQUEST__ERROR_INVALID_FUNCTION_"></span><span id="status_invalid_device_request__error_invalid_function_"></span>STATUS\_INVALID\_DEVICE\_REQUEST (ERROR\_INVALID\_FUNCTION)
</dt> <dd>

The I/O control code (IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_OUT) is not supported by the storage drivers.

</dd> <dt>

<span id="STATUS_DEVICE_BUSY__ERROR_BUSY_"></span><span id="status_device_busy__error_busy_"></span>STATUS\_DEVICE\_BUSY (ERROR\_BUSY)
</dt> <dd>

The command failed because of a Reservation Conflict (for more information, see the [SCSI Primary Commands - 2 (SPC-2)](http://go.microsoft.com/fwlink/p/?linkid=153142) specification).

</dd> <dt>

<span id="STATUS_IO_DEVICE_ERROR__ERROR_IO_DEVICE_"></span><span id="status_io_device_error__error_io_device_"></span>STATUS\_IO\_DEVICE\_ERROR (ERROR\_IO\_DEVICE)
</dt> <dd>

The device does not support the Persistent Reserve Out command.

</dd> <dt>

<span id="STATUS_INVALID_USER_BUFFER__ERROR_INVALID_USER_BUFFER_"></span><span id="status_invalid_user_buffer__error_invalid_user_buffer_"></span>STATUS\_INVALID\_USER\_BUFFER (ERROR\_INVALID\_USER\_BUFFER)
</dt> <dd>

The input buffer is not aligned correctly for the device or adapter. This status could only be returned when a driver sends an IOCTL to the storage stack. This status will not be returned when a user-mode application sends the IOCTL through the DeviceIoControl API as the I/O Manager automatically aligns the buffers.

</dd> <dt>

<span id="STATUS_INFO_LENGTH_MISMATCH"></span><span id="status_info_length_mismatch"></span>STATUS\_INFO\_LENGTH\_MISMATCH
</dt> <dd>

The input buffer length for the IOCTL is less than sizeof(PERSISTENT\_RESERVE\_COMMAND) or the size that is specified in the [**PERSISTENT\_RESERVE\_COMMAND**](persistent-reserve-command.md) data structure is less than sizeof(PERSISTENT\_RESERVE\_COMMAND).

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_PERSISTENT_RESERVE_OUT%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





