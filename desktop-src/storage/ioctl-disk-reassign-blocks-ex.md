---
title: IOCTL\_DISK\_REASSIGN\_BLOCKS\_EX control code
description: Maps defective blocks to a new location on disk. This request instructs the device to reassign the bad block address to a good block from its spare-block pool.
ms.assetid: 885CC365-A730-4C1E-AD74-89D47DC17407
keywords:
- IOCTL_DISK_REASSIGN_BLOCKS_EX control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_DISK_REASSIGN_BLOCKS_EX
api_location:
- Ntdddisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_DISK\_REASSIGN\_BLOCKS\_EX control code

Maps defective blocks to a new location on disk. This request instructs the device to reassign the bad block address to a good block from its spare-block pool. A **IOCTL\_DISK\_REASSIGN\_BLOCKS\_EX** request allows for a larger number of blocks for assignment than the [**IOCTL\_DISK\_REASSIGN\_BLOCKS**](ioctl-disk-reassign-blocks.md) request.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the [**REASSIGN\_BLOCKS\_EX**](reassign-blocks-ex.md) values to be set. Note that this structure contains a variable-sized array of block numbers. It is the caller's responsibility to make sure that the array of block numbers is sorted in ascending order.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer, which must be &gt;= **sizeof**(REASSIGN\_BLOCKS\_EX).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field can be set to STATUS\_SUCCESS, or possibly to STATUS\_INFO\_LENGTH\_MISMATCH, STATUS\_INSUFFICIENT\_RESOURCES, or STATUS\_BUFFER\_TOO\_SMALL.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                              |
| Header<br/>  | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**REASSIGN\_BLOCKS\_EX**](reassign-blocks-ex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_REASSIGN_BLOCKS_EX%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






