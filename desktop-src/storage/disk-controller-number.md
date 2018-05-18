---
title: DISK\_CONTROLLER\_NUMBER structure
description: DISK\_CONTROLLER\_NUMBER is used with IOCTL\_DISK\_CONTROLLER\_NUMBER to retrieve the controller number and disk number of an IDE disk.
ms.assetid: '5dc9f04b-8d7c-4ac7-9518-8836d56d5eed'
keywords: ["DISK_CONTROLLER_NUMBER structure Storage Devices", "PDISK_CONTROLLER_NUMBER structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DISK_CONTROLLER_NUMBER
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# DISK\_CONTROLLER\_NUMBER structure

DISK\_CONTROLLER\_NUMBER is used with IOCTL\_DISK\_CONTROLLER\_NUMBER to retrieve the controller number and disk number of an IDE disk.

## Syntax


```C++
typedef struct _DISK_CONTROLLER_NUMBER {
  ULONG ControllerNumber;
  ULONG DiskNumber;
} DISK_CONTROLLER_NUMBER, *PDISK_CONTROLLER_NUMBER;
```



## Members

<dl> <dt>

**ControllerNumber**
</dt> <dd>

Contains the number of the IDE controller for the disk.

</dd> <dt>

**DiskNumber**
</dt> <dd>

Contains the number of the disk.

</dd> </dl>

## Remarks

After DISK\_CONTROLLER\_NUMBER receives the controller number and the disk number, these values can be used to determine whether the disk is attached to the primary or to the secondary IDE controller.

## Requirements



|                   |                                                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h, Ntddk.h, or Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DISK\_CONTROLLER\_NUMBER**](ioctl-disk-controller-number.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_CONTROLLER_NUMBER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






