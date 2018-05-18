---
title: MOUNTDEV\_UNIQUE\_ID structure
description: The MOUNTDEV\_UNIQUE\_ID structure contains a unique volume ID that a mount manager client provides to the mount manager in response to an IOCTL\_MOUNTDEV\_QUERY\_UNIQUE\_ID request.
ms.assetid: 'cc6cbda8-4056-41e7-98f9-927a99e66081'
keywords: ["MOUNTDEV_UNIQUE_ID structure Storage Devices", "PMOUNTDEV_UNIQUE_ID structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MOUNTDEV_UNIQUE_ID
api_location:
- mountdev.h
api_type:
- HeaderDef
---

# MOUNTDEV\_UNIQUE\_ID structure

The MOUNTDEV\_UNIQUE\_ID structure contains a unique volume ID that a mount manager client provides to the mount manager in response to an [**IOCTL\_MOUNTDEV\_QUERY\_UNIQUE\_ID**](ioctl-mountdev-query-unique-id.md) request.

## Syntax


```C++
typedef struct _MOUNTDEV_UNIQUE_ID {
  USHORT UniqueIdLength;
  UCHAR  UniqueId[1];
} MOUNTDEV_UNIQUE_ID, *PMOUNTDEV_UNIQUE_ID;
```



## Members

<dl> <dt>

**UniqueIdLength**
</dt> <dd>

Contains the length of the unique volume ID.

</dd> <dt>

**UniqueId**
</dt> <dd>

Contains the unique volume ID as an array of bytes.

</dd> </dl>

## Remarks

For a discussion of unique volume IDs and how the mount manager uses them, see [Supporting Mount Manager Requests in a Storage Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff567603).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountdev.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_MOUNTDEV\_UNIQUE\_ID\_CHANGE\_NOTIFY**](https://msdn.microsoft.com/library/windows/hardware/ff560443)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MOUNTDEV_UNIQUE_ID%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






