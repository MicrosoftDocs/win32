---
title: DRIVE\_LAYOUT\_INFORMATION\_GPT structure
description: The DRIVE\_LAYOUT\_INFORMATION\_GPT structure reports the drive signature for a GUID Partition Table partition.
ms.assetid: 'd99180e0-d989-470c-b330-23372938ab25'
keywords: ["DRIVE_LAYOUT_INFORMATION_GPT structure Storage Devices", "PDRIVE_LAYOUT_INFORMATION_GPT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DRIVE_LAYOUT_INFORMATION_GPT
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# DRIVE\_LAYOUT\_INFORMATION\_GPT structure

The DRIVE\_LAYOUT\_INFORMATION\_GPT structure reports the drive signature for a GUID Partition Table partition.

## Syntax


```C++
typedef struct _DRIVE_LAYOUT_INFORMATION_GPT {
  GUID          DiskId;
  LARGE_INTEGER StartingUsableOffset;
  LARGE_INTEGER UsableLength;
  ULONG         MaxPartitionCount;
} DRIVE_LAYOUT_INFORMATION_GPT, *PDRIVE_LAYOUT_INFORMATION_GPT;
```



## Members

<dl> <dt>

**DiskId**
</dt> <dd>

Contains a GUID that uniquely identifies the drive. The GUID data type is described on the [Using GUIDs in Drivers](https://msdn.microsoft.com/library/windows/hardware/ff565392) reference page.

</dd> <dt>

**StartingUsableOffset**
</dt> <dd>

Contains an offset in bytes to the location immediately following the primary partition table. This offset begins the region on the drive where partitions reside, but partition one is not necessarily located precisely at this offset.

</dd> <dt>

**UsableLength**
</dt> <dd>

Indicates the total usable space in bytes available on the drive.

</dd> <dt>

**MaxPartitionCount**
</dt> <dd>

Indicates the maximum number of partitions allowed on the drive.

</dd> </dl>

## Remarks

This structure contains the drive layout information that is specific to a drive with a GUID Partition Table partition. It is encapsulated within the [**DRIVE\_LAYOUT\_INFORMATION\_EX**](drive-layout-information-ex.md) structure. For further information see Intel's *Extensible Firmware Interface* specification.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DRIVE_LAYOUT_INFORMATION_GPT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






