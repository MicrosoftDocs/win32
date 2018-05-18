---
title: DRIVE\_LAYOUT\_INFORMATION\_MBR structure
description: The DRIVE\_LAYOUT\_INFORMATION\_MBR structure reports the drive signature for a Master Boot Record partition.
ms.assetid: '41df2847-7cfa-4746-82bd-d0b8b482a0d4'
keywords: ["DRIVE_LAYOUT_INFORMATION_MBR structure Storage Devices", "PDRIVE_LAYOUT_INFORMATION_MBR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DRIVE_LAYOUT_INFORMATION_MBR
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# DRIVE\_LAYOUT\_INFORMATION\_MBR structure

The DRIVE\_LAYOUT\_INFORMATION\_MBR structure reports the drive signature for a Master Boot Record partition.

## Syntax


```C++
typedef struct _DRIVE_LAYOUT_INFORMATION_MBR {
  ULONG Signature;
} DRIVE_LAYOUT_INFORMATION_MBR, *PDRIVE_LAYOUT_INFORMATION_MBR;
```



## Members

<dl> <dt>

**Signature**
</dt> <dd>

Specifies the disk signature value, which uniquely identifies the disk.

</dd> </dl>

## Remarks

This structure contains the drive layout information that is specific to a drive with a Master Boot Record partition. It is contained within the [**DRIVE\_LAYOUT\_INFORMATION\_EX**](drive-layout-information-ex.md) structure.

## Requirements



|                   |                                                                                                         |
|-------------------|---------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntddk.h)</dt> </dl> |



## See also

<dl> <dt>

[**DRIVE\_LAYOUT\_INFORMATION\_EX**](drive-layout-information-ex.md)
</dt> <dt>

[**IoReadPartitionTable**](ioreadpartitiontable.md)
</dt> <dt>

[**IoWritePartitionTable**](iowritepartitiontable.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DRIVE_LAYOUT_INFORMATION_MBR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






