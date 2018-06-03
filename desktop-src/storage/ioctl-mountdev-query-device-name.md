---
title: IOCTL\_MOUNTDEV\_QUERY\_DEVICE\_NAME control code
description: Support for this IOCTL by the mount manager clients is mandatory.
ms.assetid: 3df96552-d4f6-4d1c-bc07-3eff5f3eabfb
keywords:
- IOCTL_MOUNTDEV_QUERY_DEVICE_NAME control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_MOUNTDEV_QUERY_DEVICE_NAME
api_location:
- Mountmgr.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_MOUNTDEV\_QUERY\_DEVICE\_NAME control code

Support for this IOCTL by the mount manager clients is mandatory. Upon receiving this IOCTL a client driver must provide the (nonpersistent) device (or target) name for the volume. The mount manager uses the *device name* returned by the client as the target of a symbolic link. An example of a device name would be "\\Device\\HarddiskVolume1".

## Output Buffer

The mount manager client returns a variable-length structure of type [**MOUNTDEV\_NAME**](mountdev-name.md), defined in *Mountmgr.h*, at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. The device name must be inserted at the address pointed to by the *Name* member of this structure.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer, which must be greater than or equal to **sizeof**(MOUNTDEV\_NAME).

## Status block

The **Information** field is set to FIELD\_OFFSET([**MOUNTDEV\_NAME**](mountdev-name.md), Name) + output-&gt;NameLength, or alternatively, output-&gt;NameLength + sizeof(USHORT), where output points to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**

If the operation is successful, the mount manager client must set the **Information** field to the length of the **NULL**-terminated string containing the device name and the **Status** field to STATUS\_SUCCESS.

If the output buffer is too small to hold the device name, the mount manager client must set the **Information** field to **sizeof**(MOUNTDEV\_NAME) and the **Status** field to STATUS\_BUFFER\_OVERFLOW. In addition, the mount manager client fills in the NameLength member of the [**MOUNTDEV\_NAME**](mountdev-name.md) structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**MOUNTDEV\_NAME**](mountdev-name.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MOUNTDEV_QUERY_DEVICE_NAME%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






