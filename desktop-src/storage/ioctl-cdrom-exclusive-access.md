---
title: IOCTL\_CDROM\_EXCLUSIVE\_ACCESS control code
description: The IOCTL\_CDROM\_EXCLUSIVE\_ACCESS request instructs the CD-ROM class driver to Report the access state of a CD-ROM device.
ms.assetid: 449936d8-9257-4044-a38f-e68d8e8d5c68
keywords:
- IOCTL_CDROM_EXCLUSIVE_ACCESS control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_CDROM_EXCLUSIVE_ACCESS
api_location:
- Ntddcdrm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_CDROM\_EXCLUSIVE\_ACCESS control code

The IOCTL\_CDROM\_EXCLUSIVE\_ACCESS request instructs the CD-ROM class driver to:

-   Report the access state of a CD-ROM device.

-   Lock a CD-ROM device for exclusive access.

-   Unlock a CD-ROM device for exclusive access.

A valid FileObject handle must exist in order for this IOCTL to succeed. The FileObject handle protects the system from unexpected application termination or accidental acquisition of an exclusive access lock without subsequent release of the exclusive access lock. A valid FileObject handle is necessary because when an application closes, the CD-ROM class driver will receive CLEANUP and CLOSE I/O Request Packets (IRPs), which it can use to automatically release an exclusive access lock obtained by that handle. This simple method protects against the majority of accidental releases of exclusive access. Any methods used to avoid this functionality may reduce the safety and effectiveness of the exclusive access locking method.

## Input Buffer

Depending on the operation that the caller requests, the caller must provide one of the following structures as input at **Irp-&gt;AssociatedIrp.SystemBuffer**:

-   [**CDROM\_EXCLUSIVE\_ACCESS**](cdrom-exclusive-access.md) (to report the access state of a CD-ROM device)

-   [**CDROM\_EXCLUSIVE\_LOCK**](cdrom-exclusive-lock.md) (to lock a CD-ROM device for exclusive access)

-   [**CDROM\_EXCLUSIVE\_ACCESS**](cdrom-exclusive-access.md) (to unlock a CD-ROM device that the application locked for exclusive access)

## Input Buffer Length

The **Parameters.DeviceIoControl.InputBufferLength** member in the [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure indicates the size, in bytes, of the user-allocated input buffer.

## Output Buffer

If the caller requests the exclusive access state of the CD-ROM device (**RequestType** = **ExclusiveAccessQueryState**), the CD-ROM class driver returns a [**CDROM\_EXCLUSIVE\_LOCK\_STATE**](cdrom-exclusive-lock-state.md)-type structure in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** whose **LockState** member indicates the access state of the device.

## Output Buffer Length

The **Parameters.DeviceIoControl.OutputBufferLength** member in the I/O stack location (IO\_STACK\_LOCATION) indicates the size, in bytes, of the output buffer.

## Status block

The **Information** field is set to the number of bytes that are returned. The **Status** field is set to STATUS\_SUCCESS if the request succeeds.

If the request fails, the **Status** field might be set to one of the following error messages:

<dl> <dt>

<span id="STATUS_INFO_LENGTH_MISMATCH__Windows_error_code__ERROR_BAD_LENGTH__"></span><span id="status_info_length_mismatch__windows_error_code__error_bad_length__"></span><span id="STATUS_INFO_LENGTH_MISMATCH__WINDOWS_ERROR_CODE__ERROR_BAD_LENGTH__"></span>STATUS\_INFO\_LENGTH\_MISMATCH (Windows error code: ERROR\_BAD\_LENGTH) 
</dt> <dd>

The input buffer was too small.

</dd> <dt>

<span id="STATUS_BUFFER_TOO_SMALL__Windows_error_code__ERROR_INSUFFICIENT_BUFFER__"></span><span id="status_buffer_too_small__windows_error_code__error_insufficient_buffer__"></span><span id="STATUS_BUFFER_TOO_SMALL__WINDOWS_ERROR_CODE__ERROR_INSUFFICIENT_BUFFER__"></span>STATUS\_BUFFER\_TOO\_SMALL (Windows error code: ERROR\_INSUFFICIENT\_BUFFER) 
</dt> <dd>

The output buffer was too small for a **ExclusiveAccessQueryState** request.

</dd> <dt>

<span id="STATUS_INVALID_PARAMETER__Windows_error_code__ERROR_INVALID_PARAMETER__"></span><span id="status_invalid_parameter__windows_error_code__error_invalid_parameter__"></span><span id="STATUS_INVALID_PARAMETER__WINDOWS_ERROR_CODE__ERROR_INVALID_PARAMETER__"></span>STATUS\_INVALID\_PARAMETER (Windows error code: ERROR\_INVALID\_PARAMETER) 
</dt> <dd>

The CD-ROM class driver returns this status code when one of the following two errors occurs:

-   The **RequestType** that was specified is not a valid member of [**EXCLUSIVE\_ACCESS\_REQUEST\_TYPE**](exclusive-access-request-type.md).

-   The caller name string in the **CallerName** member of [**CDROM\_EXCLUSIVE\_LOCK**](cdrom-exclusive-lock.md) violates the naming convention. **CallerName** must be a **NULL**-terminated string that contains the following characters: alphanumerics (A - Z, a - z, 0 - 9), spaces, periods, commas, colons (:), semi-colons (;), hyphens (-), and underscores (\_). The length of the string must be less than CDROM\_EXCLUSIVE\_CALLER\_LENGTH bytes, including the **NULL** at the end of the string.

</dd> <dt>

<span id="STATUS_INVALID_DEVICE_REQUEST__Windows_error_code__ERROR_INVALID_FUNCTION__"></span><span id="status_invalid_device_request__windows_error_code__error_invalid_function__"></span><span id="STATUS_INVALID_DEVICE_REQUEST__WINDOWS_ERROR_CODE__ERROR_INVALID_FUNCTION__"></span>STATUS\_INVALID\_DEVICE\_REQUEST (Windows error code: ERROR\_INVALID\_FUNCTION) 
</dt> <dd>

The CD-ROM class driver returns this status code when one of the following two errors occurs:

-   The caller made the request at an IRQL level other than PASSIVE\_LEVEL.

-   The caller sent a request with **RequestType** = **ExclusiveAccessUnlockDevice** to unlock a device that is not in exclusive mode.

</dd> <dt>

<span id="STATUS_INVALID_HANDLE__Windows_error_code__ERROR_INVALID_HANDLE__"></span><span id="status_invalid_handle__windows_error_code__error_invalid_handle__"></span><span id="STATUS_INVALID_HANDLE__WINDOWS_ERROR_CODE__ERROR_INVALID_HANDLE__"></span>STATUS\_INVALID\_HANDLE (Windows error code: ERROR\_INVALID\_HANDLE) 
</dt> <dd>

The CD-ROM class driver returns this status code when one of the following two errors occurs:

-   The file object that is required to keep track of the request was not available. The CD-ROM class driver did not receive a request to create a file object from this caller.

-   The caller sent a request with **RequestType** = **ExclusiveAccessUnlockDevice** to unlock a device, even though the caller does not have exclusive access to the device.

</dd> <dt>

<span id="STATUS_INVALID_DEVICE_STATE__Windows_error_code__ERROR_BAD_COMMAND__"></span><span id="status_invalid_device_state__windows_error_code__error_bad_command__"></span><span id="STATUS_INVALID_DEVICE_STATE__WINDOWS_ERROR_CODE__ERROR_BAD_COMMAND__"></span>STATUS\_INVALID\_DEVICE\_STATE (Windows error code: ERROR\_BAD\_COMMAND) 
</dt> <dd>

The caller attempted to lock a device while the file system driver was mounted on this device, without specifying that the class driver should suspend the check for a mounted file system driver. To suspend the check for a mounted file system driver, the caller must set the **Flags** member of [**CDROM\_EXCLUSIVE\_ACCESS**](cdrom-exclusive-access.md) to 1.

</dd> <dt>

<span id="STATUS_ACCESS_DENIED__Windows_error_code__ERROR_ACCESS_DENIED__"></span><span id="status_access_denied__windows_error_code__error_access_denied__"></span><span id="STATUS_ACCESS_DENIED__WINDOWS_ERROR_CODE__ERROR_ACCESS_DENIED__"></span>STATUS\_ACCESS\_DENIED (Windows error code: ERROR\_ACCESS\_DENIED) 
</dt> <dd>

The device is already locked for exclusive access.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**CDROM\_EXCLUSIVE\_ACCESS**](cdrom-exclusive-access.md)
</dt> <dt>

[**CDROM\_EXCLUSIVE\_LOCK**](cdrom-exclusive-lock.md)
</dt> <dt>

[**CDROM\_EXCLUSIVE\_LOCK\_STATE**](cdrom-exclusive-lock-state.md)
</dt> <dt>

[**EXCLUSIVE\_ACCESS\_REQUEST\_TYPE**](exclusive-access-request-type.md)
</dt> <dt>

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CDROM_EXCLUSIVE_ACCESS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






