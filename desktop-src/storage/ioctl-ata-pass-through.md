---
title: IOCTL\_ATA\_PASS\_THROUGH control code
description: Allows an application to send almost any ATA command to a target device, with the following restrictions If a class driver for the target type of device exists, the application must send the request to the class driver.
ms.assetid: '350d9777-18d7-412a-ab60-1e17070a12af'
keywords: ["IOCTL_ATA_PASS_THROUGH control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_ATA_PASS_THROUGH
api_location:
- Ntddscsi.h
api_type:
- HeaderDef
---

# IOCTL\_ATA\_PASS\_THROUGH control code

Allows an application to send almost any ATA command to a target device, with the following restrictions:

-   If a class driver for the target type of device exists, the application must send the request to the class driver. Thus, an application can send this request directly to the system port driver for a target logical unit (LU) only if there is no class driver for the type of device connected to that LU. The system port driver does not check to determine if a device has been claimed by a class driver before processing a pass-through request. Therefore, if an application bypasses a class driver that has claimed a device and sends a pass-through request for that device directly to the port driver, a conflict for control of the device can occur between the class driver and the application.

-   This request cannot be used if the command requires the underlying driver to access memory directly. If the caller's command might require direct access to memory, use [**IOCTL\_ATA\_PASS\_THROUGH\_DIRECT**](ioctl-ata-pass-through-direct.md) instead.

-   Applications must not attempt to send a pass-through request asynchronously. All pass-through requests must be synchronous.

-   Applications do not require administrative privileges to send a pass-through request to a device, but they must have read/write access to the device.

The calling application provides the ATA task file register contents for the intended command in the [**ATA\_PASS\_THROUGH\_EX**](ata-pass-through-ex.md) structure. The system double buffers all data transfers. This request is typically used for transferring small amounts of data (less than 16 KB).

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** should contain an [**ATA\_PASS\_THROUGH\_EX**](ata-pass-through-ex.md) structure, which includes a set of task file input registers that indicate the sort of command to be performed and its parameters. The caller must initialize all the members of this structure except for **PathId**, **TargetId**, and **Lun**, which the port driver fills in. For a data-out command, the **DataBufferOffset** member of the structure must point to a cache-aligned buffer containing the data to be written.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** indicates the size in bytes of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. If the embedded ATA command is a write operation, the size of the input buffer should be the sum of **sizeof**([**ATA\_PASS\_THROUGH\_EX**](ata-pass-through-ex.md)) and the value in the **DataTransferLength** member of **ATA\_PASS\_THROUGH\_EX**. The following pseudocode example shows how to calculate the buffer size:


```
ULONG buffsize; // size of the buffer
ATA_PASS_THROUGH_EX hdr;
hdr.DataTransferLength = size in bytes of the data transfer
buffsize = sizeof (ATA_PASS_THROUGH_EX) + hdr.DataTransferLength
```



If the embedded ATA command is a read operation or a device control operation that does not involve data transfer, **InputBufferLength** should be equal to **sizeof** (ATA\_PASS\_THROUGH\_EX).

In either case, if **InputBufferLength** is less than **sizeof** (ATA\_PASS\_THROUGH\_EX), the port driver fails the I/O request and returns an error.

## Output Buffer

The port driver formats the return data using an [**ATA\_PASS\_THROUGH\_EX**](ata-pass-through-ex.md) structure and stores the data in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

The port driver fills the **CurrentTaskFile** member with the values that are present in the device's output registers at the completion of the embedded ATA command. If the command was a data transfer, the port driver stores the transferred data in a cache-aligned buffer that is located at an offset of **DataBufferOffset** bytes from the beginning of the structure. The application is responsible for interpreting the contents of the output registers to determine what errors, if any, were returned by the device.

## Output Buffer Length

The port driver updates the **DataTransferLength** member of [**ATA\_PASS\_THROUGH\_EX**](ata-pass-through-ex.md) to indicate the amount of data actually transferred from the device. If the embedded ATA command is a write operation or a device control operation that does not transfer data, **OutputBufferLength** is equal to **sizeof**(ATA\_PASS\_THROUGH\_EX). If the embedded ATA command is a read operation, **OutputBufferLength** is equal to **sizeof**(ATA\_PASS\_THROUGH\_EX) + **DataTransferLength**.

## Status block

The **Information** member is set to the number of bytes returned in the output buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. The **Status** member is set to STATUS\_SUCCESS or possibly to STATUS\_BUFFER\_TOO\_SMALL or STATUS\_INVALID\_PARAMETER if the input **Status** value in [**ATA\_PASS\_THROUGH\_EX**](ata-pass-through-ex.md) is improperly set.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows Server 2003.<br/>                                                    |
| Header<br/>  | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ATA\_PASS\_THROUGH\_EX**](ata-pass-through-ex.md)
</dt> <dt>

[**IOCTL\_ATA\_PASS\_THROUGH\_DIRECT**](ioctl-ata-pass-through-direct.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_ATA_PASS_THROUGH%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






