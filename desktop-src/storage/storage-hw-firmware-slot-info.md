---
title: STORAGE\_HW\_FIRMWARE\_SLOT\_INFO structure
description: This structure contains information about a slot on a device.
ms.assetid: D5DF9785-83E0-4137-8E5F-357F94721CAD
keywords:
- STORAGE_HW_FIRMWARE_SLOT_INFO structure Storage Devices
- PSTORAGE_HW_FIRMWARE_SLOT_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_HW_FIRMWARE_SLOT_INFO
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_HW\_FIRMWARE\_SLOT\_INFO structure

This structure contains information about a slot on a device.

## Syntax


```C++
typedef struct _STORAGE_HW_FIRMWARE_SLOT_INFO {
  ULONG Version;
  ULONG Size;
  UCHAR SlotNumber;
  UCHAR ReadOnly  :1;
  UCHAR Reserved0  :7;
  UCHAR Reserved1[6];
  UCHAR Revision[STORAGE_HW_FIRMWARE_REVISION_LENGTH];
} STORAGE_HW_FIRMWARE_SLOT_INFO, *PSTORAGE_HW_FIRMWARE_SLOT_INFO;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. This should be set to sizeof(STORAGE\_HW\_FIRMWARE\_SLOT\_INFO)

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure.

</dd> <dt>

**SlotNumber**
</dt> <dd>

The slot number of this slot.

</dd> <dt>

**ReadOnly**
</dt> <dd>

Indicates whether this slot is read-only or not.

</dd> <dt>

**Reserved0**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Revision**
</dt> <dd>

The revision of the firmware on this slot.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                                      |
| Server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_HW_FIRMWARE_SLOT_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





