---
title: DISK\_INT13\_INFO structure
description: The DISK\_INT13\_INFO structure is used by the BIOS to report disk detection data for a partition with an INT13 format.
ms.assetid: '8a9c335a-1c5f-4379-83bb-21391ae46a3c'
keywords: ["DISK_INT13_INFO structure Storage Devices", "PDISK_INT13_INFO structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DISK_INT13_INFO
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# DISK\_INT13\_INFO structure

The DISK\_INT13\_INFO structure is used by the BIOS to report disk detection data for a partition with an INT13 format.

## Syntax


```C++
typedef struct _DISK_INT13_INFO {
  USHORT DriveSelect;
  ULONG  MaxCylinders;
  USHORT SectorsPerTrack;
  USHORT MaxHeads;
  USHORT NumberDrives;
} DISK_INT13_INFO, *PDISK_INT13_INFO;
```



## Members

<dl> <dt>

**DriveSelect**
</dt> <dd>

Corresponds to the Device/Head register defined in the *AT Attachment (ATA)* specification. When zero, the fourth bit of this register indicates that drive zero is selected. When 1, it indicates that drive one is selected. The values of bits 0, 1, 2, 3, and 6 depend on the command in the command register. Bits 5 and 7 are no longer used. For more information about the values that the Device/Head register can hold, see the ATA specification.

</dd> <dt>

**MaxCylinders**
</dt> <dd>

Indicates the maximum number of cylinders on the disk.

</dd> <dt>

**SectorsPerTrack**
</dt> <dd>

Indicates the number of sectors per track.

</dd> <dt>

**MaxHeads**
</dt> <dd>

Indicates the maximum number of disk heads.

</dd> <dt>

**NumberDrives**
</dt> <dd>

Indicates the number of drives.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_DETECTION\_INFO**](disk-detection-info.md)
</dt> <dt>

[**DISK\_EX\_INT13\_INFO**](disk-ex-int13-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_INT13_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






