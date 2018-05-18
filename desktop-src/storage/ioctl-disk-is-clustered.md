---
title: IOCTL\_DISK\_IS\_CLUSTERED control code
description: Allows a driver or application to determine if a disk is clustered.
ms.assetid: '46b72c16-2656-4ceb-a786-5fb24818b2a7'
keywords: ["IOCTL_DISK_IS_CLUSTERED control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_DISK_IS_CLUSTERED
api_location:
- Ntdddisk.h
api_type:
- HeaderDef
---

# IOCTL\_DISK\_IS\_CLUSTERED control code

Allows a driver or application to determine if a disk is clustered.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a Boolean value, with **TRUE** indicating that the disk is clustered.

## Output Buffer Length

Length of a Boolean.

## Status block

**Irp-&gt;IoStatus.Status** is set to STATUS\_SUCCESS if the request is successful. Otherwise, **Status** to the appropriate error condition as a [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) code.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DISK_IS_CLUSTERED%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





