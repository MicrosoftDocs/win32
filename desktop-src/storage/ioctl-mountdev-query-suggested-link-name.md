---
title: IOCTL\_MOUNTDEV\_QUERY\_SUGGESTED\_LINK\_NAME control code
description: Support for this IOCTL by the mount manager clients is optional.
ms.assetid: 4afd8c7a-b7b4-4a02-a270-d4e29f5329f9
keywords:
- IOCTL_MOUNTDEV_QUERY_SUGGESTED_LINK_NAME control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_MOUNTDEV_QUERY_SUGGESTED_LINK_NAME
api_location:
- Mountdev.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_MOUNTDEV\_QUERY\_SUGGESTED\_LINK\_NAME control code

Support for this IOCTL by the mount manager clients is optional. Some mount manager clients are able to keep track of their drive letters across reboots of the system without the help of the mount manager. Such clients can send a suggested drive letter name to the mount manager in response to this IOCTL. The mount manager uses the suggested name if the mount manager's database does not already contain a persistent drive letter name for the client's volume. Otherwise, it ignores the suggestion and uses the drive letter name in its persistent name database.

Drive letter names must include the full path of the symbolic link in object namespace and must have the traditional MS-DOS syntax. For instance, drive letter "D" must be represented in this manner: "\\DosDevices\\D:". The alternative symbolic link path of "\\??\\D:" may not be used, nor may abbreviations of the symbolic link such as "D:".

## Output Buffer

The client driver must place a variable-length structure of type [**MOUNTDEV\_SUGGESTED\_LINK\_NAME**](mountdev-suggested-link-name.md), defined in *moundev.h*, at the beginning of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. Starting at the address of the structure member *Name*, the client driver must insert the suggested persistent name.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer, which must be greater than or equal to **sizeof**(MOUNTDEV\_SUGGESTED\_LINK\_NAME).

## Status block

If the operation is successful, the **Information** field is set to the total number of bytes returned and the **Status** field is set to STATUS\_SUCCESS.

If **OutputBufferLength** is less than **sizeof**(MOUNTDEV\_SUGGESTED\_LINK\_NAME), the **Status** field is set to STATUS\_INVALID\_PARAMETER.

If **OutputBufferLength** is less than the total length of output data, the **Status** field is set to STATUS\_BUFFER\_OVERFLOW and the **Information** field is set to **sizeof**(MOUNTDEV\_SUGGESTED\_LINK\_NAME).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountdev.h (include Mountdev.h)</dt> </dl> |



## See also

<dl> <dt>

[**MOUNTDEV\_SUGGESTED\_LINK\_NAME**](mountdev-suggested-link-name.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MOUNTDEV_QUERY_SUGGESTED_LINK_NAME%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






