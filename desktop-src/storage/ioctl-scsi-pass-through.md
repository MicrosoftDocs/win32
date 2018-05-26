---
title: IOCTL\_SCSI\_PASS\_THROUGH control code
description: Allows an application to send almost any SCSI command to a target device, with the following restrictions Multitarget commands, such as COPY, are not allowed.Bidirectional data transfer operations are not supported.If a class driver for the target type of device exists, the request must be sent to that class driver. Thus, an application can send this request directly to the system port driver for a target logical unit (LU) only if there is no class driver for the type of device that is connected to that LU. The system port driver does not check to determine if a device has been claimed by a class driver before it processes a pass-through request. Therefore, if an application bypasses a class driver that has claimed a device and sends a pass-through request for that device directly to the port driver, a conflict for control of the device can occur between the class driver and the application. If a pass-through request is sent to an adapter device object and if it originates from user mode and targets an LU that is claimed by a class driver, Storport fails the request with STATUS\_INVALID\_DEVICE\_REQUEST. If the request is sent to an LU device object, originates in kernel mode, or targets an unclaimed LU, it is passed to the miniport driver.This request cannot be used if the CDB might require the underlying miniport driver to access memory directly. If the callers CDB might require direct access to memory, use IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT instead. Applications must not attempt to send a pass-through request asynchronously. All pass-through requests must be synchronous. Applications do not require administrative privileges to send a pass-through request to a device, but they must have read/write access to the device. The calling application creates the SCSI command descriptor block, which can include a request for request-sense data if a CHECK CONDITION occurs. IOCTL\_SCSI\_PASS\_THROUGH is a buffered device control request. To bypass buffering in system memory, callers should use IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT. When handling an IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT request, the system locks down the buffer in user memory and the device accesses this memory directly. This request is typically used for transferring small amounts of data ( 16K).Applications can send this request by means of an IRP\_MJ\_DEVICE\_CONTROL request.Storage class drivers set the minor IRP number to IRP\_MN\_SCSI\_CLASS to indicate that the request has been processed by a storage class driver.
ms.assetid: c7c4a98a-51c3-46c8-856e-053291b412b3
keywords:
- IOCTL_SCSI_PASS_THROUGH control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_SCSI_PASS_THROUGH
api_location:
- Ntddscsi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_SCSI\_PASS\_THROUGH control code

Allows an application to send almost any SCSI command to a target device, with the following restrictions:

-   Multitarget commands, such as COPY, are not allowed.

-   Bidirectional data transfer operations are not supported.

-   If a class driver for the target type of device exists, the request must be sent to that class driver. Thus, an application can send this request directly to the system port driver for a target logical unit (LU) only if there is no class driver for the type of device that is connected to that LU. The system port driver does not check to determine if a device has been claimed by a class driver before it processes a pass-through request. Therefore, if an application bypasses a class driver that has claimed a device and sends a pass-through request for that device directly to the port driver, a conflict for control of the device can occur between the class driver and the application. If a pass-through request is sent to an adapter device object and if it originates from user mode and targets an LU that is claimed by a class driver, Storport fails the request with STATUS\_INVALID\_DEVICE\_REQUEST. If the request is sent to an LU device object, originates in kernel mode, or targets an unclaimed LU, it is passed to the miniport driver.

-   This request cannot be used if the CDB might require the underlying miniport driver to access memory directly. If the caller's CDB might require direct access to memory, use [**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](ioctl-scsi-pass-through-direct.md) instead.

-   Applications must not attempt to send a pass-through request asynchronously. All pass-through requests must be synchronous.

-   Applications do not require administrative privileges to send a pass-through request to a device, but they must have read/write access to the device.

The calling application creates the SCSI command descriptor block, which can include a request for request-sense data if a CHECK CONDITION occurs.

**IOCTL\_SCSI\_PASS\_THROUGH** is a buffered device control request. To bypass buffering in system memory, callers should use [**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](ioctl-scsi-pass-through-direct.md). When handling an **IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT** request, the system locks down the buffer in user memory and the device accesses this memory directly.

This request is typically used for transferring small amounts of data (&lt;16K).

Applications can send this request by means of an [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) request.

Storage class drivers set the minor IRP number to IRP\_MN\_SCSI\_CLASS to indicate that the request has been processed by a storage class driver.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Input Buffer

This structure includes a SCSI CDB, which must be initialized by the caller except for the path, target ID, and logical unit number (LUN), which are filled in by the port driver. For a data-out command, the data to be transferred is included in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** at **DataBufferOffset** in the **SCSI\_PASS\_THROUGH** structure. However, the caller must allocate additional storage, immediately following **SCSI\_PASS\_THROUGH**, if the caller asks for request-sense data.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** indicates the size, in bytes, of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**, which must be at least (*sense data size* + **sizeof**(SCSI\_PASS\_THROUGH)). The size of the [**SCSI\_PASS\_THROUGH**](scsi-pass-through.md) structure varies, depending on its **DataTransferLength** specification.

## Output Buffer

The port driver returns any request-sense data and any data transferred from the device to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

The **SenseInfoLength** and **DataTransferLength** in the [**SCSI\_PASS\_THROUGH**](scsi-pass-through.md) structure are updated to indicate the amount of data transferred.

## Status block

The **Information** field is set to the number of bytes returned in the output buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_BUFFER\_TOO\_SMALL or STATUS\_INVALID\_PARAMETER if the input **Length** value in [**SCSI\_PASS\_THROUGH**](scsi-pass-through.md) is improperly set.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SCSI\_PASS\_THROUGH**](scsi-pass-through.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_SCSI_PASS_THROUGH%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






