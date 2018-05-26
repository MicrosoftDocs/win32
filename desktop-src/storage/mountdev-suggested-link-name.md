---
title: MOUNTDEV\_SUGGESTED\_LINK\_NAME structure
description: Mount manager clients that are able to keep track of their drive letters use this structure to request that the mount manager assign them a particular link name.
ms.assetid: 5c6e3337-8071-486a-826a-ade722eb8449
keywords:
- MOUNTDEV_SUGGESTED_LINK_NAME structure Storage Devices
- PMOUNTDEV_SUGGESTED_LINK_NAME structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MOUNTDEV_SUGGESTED_LINK_NAME
api_location:
- mountdev.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MOUNTDEV\_SUGGESTED\_LINK\_NAME structure

Mount manager clients that are able to keep track of their drive letters use this structure to request that the mount manager assign them a particular link name.

## Syntax


```C++
typedef struct _MOUNTDEV_SUGGESTED_LINK_NAME {
  BOOLEAN UseOnlyIfThereAreNoOtherLinks;
  USHORT  NameLength;
  WCHAR   Name[1];
} MOUNTDEV_SUGGESTED_LINK_NAME, *PMOUNTDEV_SUGGESTED_LINK_NAME;
```



## Members

<dl> <dt>

**UseOnlyIfThereAreNoOtherLinks**
</dt> <dd>

Indicates that the mount manager should use the suggested link name only if there are no other persistent links assigned to the client.

</dd> <dt>

**NameLength**
</dt> <dd>

Contains the length of the suggested name.

</dd> <dt>

**Name**
</dt> <dd>

Contains a variable-sized array of wide characters that holds the name of the suggested link in wide characters. Drive letter names must include the full path of the symbolic link in object namespace and must have the traditional Microsoft MS-DOS syntax. For instance, drive letter "D" must be represented in this manner: "\\DosDevices\\D:". The alternative symbolic link path of "\\??\\D:" may not be used, nor may abbreviations of the symbolic link such as "D:".

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountdev.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_MOUNTDEV\_QUERY\_SUGGESTED\_LINK\_NAME**](ioctl-mountdev-query-suggested-link-name.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MOUNTDEV_SUGGESTED_LINK_NAME%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






