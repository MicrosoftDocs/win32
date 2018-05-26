---
title: MOUNTDEV\_NAME structure
description: The MOUNTDEV\_NAME structure holds the name of a device.
ms.assetid: 26f5e98d-0709-403a-abcf-776c117d4f38
keywords:
- MOUNTDEV_NAME structure Storage Devices
- PMOUNTDEV_NAME structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MOUNTDEV_NAME
api_location:
- mountmgr.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MOUNTDEV\_NAME structure

The MOUNTDEV\_NAME structure holds the name of a device.

## Syntax


```C++
typedef struct _MOUNTDEV_NAME {
  USHORT NameLength;
  WCHAR  Name[1];
} MOUNTDEV_NAME, *PMOUNTDEV_NAME;
```



## Members

<dl> <dt>

**NameLength**
</dt> <dd>

Contains the length of the name, in bytes.

</dd> <dt>

**Name**
</dt> <dd>

Contains a variable-sized array of wide characters that holds the name of the device mount point. The name may be a nonpersistent target name such as "\\Device\\HarddiskVolume1", a persistent symbolic link name such as a drive letter, "\\DosDevices\\D:", or a mount point such as "\\DosDevices\\E:\\FilesysD\\mnt".

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_MOUNTDEV\_QUERY\_DEVICE\_NAME**](ioctl-mountdev-query-device-name.md)
</dt> <dt>

[**IOCTL\_MOUNTDEV\_LINK\_CREATED**](ioctl-mountdev-link-created.md)
</dt> <dt>

[**IOCTL\_MOUNTDEV\_LINK\_DELETED**](ioctl-mountdev-link-deleted.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MOUNTDEV_NAME%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






