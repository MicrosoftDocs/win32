---
title: IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_IN control code
description: The generic storage class driver (classpnp.sys) exposes an I/O control (IOCTL) interface for issuing Persistent Reserve In commands.
ms.assetid: a5a3e98b-8f6b-412d-a2eb-a28b5664340d
keywords:
- IOCTL_STORAGE_PERSISTENT_RESERVE_IN control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_PERSISTENT_RESERVE_IN
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_IN control code

The generic storage class driver (*classpnp.sys*) exposes an I/O control (IOCTL) interface for issuing Persistent Reserve In commands. The behavior of the storage device when a Persistent Reserve In command is received is described in the [SCSI Primary Commands - 2 (SPC-2)](http://go.microsoft.com/fwlink/p/?linkid=153142) specification. The IOCTL interface requires the caller to have read access to the physical device for Persistent Reserve In commands. User-mode applications, services, and kernel-mode drivers can use this IOCTL to control persistent reservations. If called from a driver, this IOCTL must be called from a thread running at IRQL &lt; DISPATCH\_LEVEL. This IOCTL is defined with FILE\_READ\_ACCESS, requiring a device handle to have read permissions to issue the Persistent Reserve In command.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**PERSISTENT\_RESERVE\_COMMAND**](persistent-reserve-command.md) structure. You must allocate the buffer from nonpaged pool and must align it correctly for the target device and adapter.

PR\_IN.ServiceAction can be one of the following:

-   RESERVATION\_ACTION\_READ\_KEYS

-   RESERVATION\_ACTION\_READ\_RESERVATIONS

PR\_IN.Allocation length is the size (in bytes) of the buffer allocated for the returned parameter list.

## Input Buffer Length

The length of .

## Output Buffer

For PR\_IN.ServiceAction = RESERVATION\_ACTION\_READ\_KEYS, the output buffer contains a [**PRI\_REGISTRATION\_LIST**](pri-registration-list.md) structure and must be at least sizeof(PRI\_REGISTRATION\_LIST).

For PR\_IN.ServiceAction = RESERVATION\_ACTION\_READ\_RESERVATIONS, the output buffer contains a [**PRI\_RESERVATION\_LIST**](pri-reservation-list.md) structure and must be at least sizeof(PRI\_RESERVATION\_LIST).

If the allocated buffer is too small to return all the Persistent Reserve In data, success will be returned and the required size will be returned in the parameter list **AdditionalLength** field.

## Output Buffer Length

The length of .

## Status block

The **Information** field is set to the size of the output buffer. For ServiceAction = RESERVATION\_ACTION\_READ\_KEYS, the output buffer is a [**PRI\_REGISTRATION\_LIST**](pri-registration-list.md) structure. For ServiceAction = RESERVATION\_ACTION\_READ\_RESERVATIONS, the output buffer is a [**PRI\_RESERVATION\_LIST**](pri-reservation-list.md) structure.

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

The I/O control code (IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_IN) is not supported by the storage drivers.

</dd> <dt>

<span id="STATUS_BUFFER_OVERFLOW__ERROR_MORE_DATA_"></span><span id="status_buffer_overflow__error_more_data_"></span>STATUS\_BUFFER\_OVERFLOW (ERROR\_MORE\_DATA)
</dt> <dd>

The output buffer is too small to hold the Persistent Reserve In data. The output buffer's **AdditionalLength** field will contain the size of the data to be returned.

</dd> <dt>

<span id="STATUS_DEVICE_BUSY__ERROR_BUSY_"></span><span id="status_device_busy__error_busy_"></span>STATUS\_DEVICE\_BUSY (ERROR\_BUSY)
</dt> <dd>

The command failed because of a Reservation Conflict (for more information, see the [SCSI Primary Commands - 2 (SPC-2)](http://go.microsoft.com/fwlink/p/?linkid=153142) specification).

</dd> <dt>

<span id="STATUS_IO_DEVICE_ERROR__ERROR_IO_DEVICE_"></span><span id="status_io_device_error__error_io_device_"></span>STATUS\_IO\_DEVICE\_ERROR (ERROR\_IO\_DEVICE)
</dt> <dd>

The device does not support the Persistent Reserve In command.

</dd> <dt>

<span id="STATUS_INVALID_USER_BUFFER__ERROR_INVALID_USER_BUFFER_"></span><span id="status_invalid_user_buffer__error_invalid_user_buffer_"></span>STATUS\_INVALID\_USER\_BUFFER (ERROR\_INVALID\_USER\_BUFFER)
</dt> <dd>

The input or output buffer is not aligned correctly for the device or adapter. This status could only be returned when a driver sends an IOCTL to the storage stack. This status will not be returned when a user-mode application sends the IOCTL through the DeviceIoControl API as the I/O Manager automatically aligns the buffers.

</dd> <dt>

<span id="STATUS_INFO_LENGTH_MISMATCH"></span><span id="status_info_length_mismatch"></span>STATUS\_INFO\_LENGTH\_MISMATCH
</dt> <dd>

The input buffer length for the IOCTL is less than sizeof(PERSISTENT\_RESERVE\_COMMAND) or the size that is specified in the [**PERSISTENT\_RESERVE\_COMMAND**](persistent-reserve-command.md) data structure is less than sizeof(PERSISTENT\_RESERVE\_COMMAND).

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_PERSISTENT_RESERVE_IN%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





