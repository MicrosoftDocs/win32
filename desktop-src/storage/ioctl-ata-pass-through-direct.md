---
title: IOCTL\_ATA\_PASS\_THROUGH\_DIRECT control code
description: Allows an application to send almost any ATA command to a target device, with the following restrictions If a class driver for the target type of device exists, the application must send the request to the class driver.
ms.assetid: 705918c7-c4ea-4495-b87f-2904f7d45ac0
keywords:
- IOCTL_ATA_PASS_THROUGH_DIRECT control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_ATA_PASS_THROUGH_DIRECT
api_location:
- Ntddscsi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_ATA\_PASS\_THROUGH\_DIRECT control code

Allows an application to send almost any ATA command to a target device, with the following restrictions:

-   If a class driver for the target type of device exists, the application must send the request to the class driver. Thus, an application can send this request directly to the system port driver for a target logical unit only if there is no class driver for the device.

-   The application *must* use this request rather than [**IOCTL\_ATA\_PASS\_THROUGH**](ioctl-ata-pass-through.md) if the embedded ATA command might require the underlying miniport driver to access memory directly.

If the ATA command requests a data transfer operation, the caller must set up a cache-aligned buffer from which, or into which, the driver can transfer data directly. The IOCTL\_ATA\_PASS\_THROUGH\_DIRECT request is typically used for transferring large amounts of data (more than 16 KB).

## Input Buffer

**Parameters.DeviceIoControl.InputBufferLength** indicates the size in bytes of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. The value of **InputBufferLength** is fixed and does not depend on the amount of data transferred. It is equal to **sizeof**(ATA\_PASS\_THROUGH\_DIRECT). If the size of the buffer is less than **sizeof**(ATA\_PASS\_THROUGH\_DIRECT), the port driver fails the I/O request and returns an error.

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains an [**ATA\_PASS\_THROUGH\_DIRECT**](ata-pass-through-direct.md) structure that includes a set of task file input registers that indicate the sort of command to be performed. The caller must initialize all the members of this structure except for **PathId**, **TargetId**, and **Lun**, which the port driver fills in. For a data-out command, the **DataBuffer** member of **ATA\_PASS\_THROUGH\_DIRECT** must point to a cache-aligned buffer containing the data to be written.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** indicates the size in bytes of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. The value of **InputBufferLength** is fixed and does not depend on the amount of data transferred. It is equal to **sizeof**(ATA\_PASS\_THROUGH\_DIRECT). If the size of the buffer is less than **sizeof**(ATA\_PASS\_THROUGH\_DIRECT), the port driver fails the I/O request and returns an error.

## Output Buffer

The port driver formats the return data using an [**ATA\_PASS\_THROUGH\_DIRECT**](ata-pass-through-direct.md) structure that it stores in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

The port driver stores the transferred data in the cache-aligned buffer pointed to by the **DataBuffer** member of [**ATA\_PASS\_THROUGH\_DIRECT**](ata-pass-through-direct.md).

The port driver fills the **CurrentTaskFile** member of [**ATA\_PASS\_THROUGH\_DIRECT**](ata-pass-through-direct.md) with the values present in the device's output registers at the completion of the ATA command. The application is responsible for interpreting the contents of the output registers to determine what errors, if any, were returned by the device.

## Output Buffer Length

The port driver updates the **DataTransferLength** member of the [**ATA\_PASS\_THROUGH\_DIRECT**](ata-pass-through-direct.md) structure to indicate the amount of data that was transferred from the device.

## Status block

The **Information** member is set to the number of bytes returned in the output buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. The **Status** member is set to STATUS\_SUCCESS or possibly to STATUS\_BUFFER\_TOO\_SMALL or STATUS\_INVALID\_PARAMETER if the input **Length** value in [**ATA\_PASS\_THROUGH\_DIRECT**](ata-pass-through-direct.md) is improperly set.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows Server 2003.<br/>                                                    |
| Header<br/>  | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ATA\_PASS\_THROUGH\_DIRECT**](ata-pass-through-direct.md)
</dt> <dt>

[**IOCTL\_ATA\_PASS\_THROUGH**](ioctl-ata-pass-through.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_ATA_PASS_THROUGH_DIRECT%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






