---
title: FILTER\_EXTENSION structure
description: The crash dump driver passes a pointer to a FILTER\_EXTENSION structure when the filter driver callback routines are called.
ms.assetid: '1113e917-3273-4ba7-8702-fe90a22fb024'
keywords: ["FILTER_EXTENSION structure Storage Devices", "PFILTER_EXTENSION structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- FILTER_EXTENSION
api_location:
- ntdddump.h
api_type:
- HeaderDef
---

# FILTER\_EXTENSION structure

The crash dump driver passes a pointer to a FILTER\_EXTENSION structure when the filter driver callback routines are called.

## Syntax


```C++
typedef struct _FILTER_EXTENSION {
  FILTER_DUMP_TYPE    DumpType;
  PDEVICE_OBJECT      DeviceObject;
  DISK_GEOMETRY       Geometry;
  LARGE_INTEGER       DiskSize;
  DISK_PARTITION_INFO PartitionInfo;
  PVOID               DumpData;
} FILTER_EXTENSION, *PFILTER_EXTENSION;
```



## Members

<dl> <dt>

**DumpType**
</dt> <dd>

This parameter indicates the type of dump that this instance of the filter driver is loaded on.

</dd> <dt>

**DeviceObject**
</dt> <dd>

A pointer to the device object of the dump volume. This pointer points to the top of the dump volume stack.

</dd> <dt>

**Geometry**
</dt> <dd>

The disk geometry of the dump device in [**DISK\_GEOMETRY**](disk-geometry.md) format.

</dd> <dt>

**DiskSize**
</dt> <dd>

Size of the disk.

</dd> <dt>

**PartitionInfo**
</dt> <dd>

The partition information in [**DISK\_PARTITION\_INFO**](disk-partition-info.md) format.

</dd> <dt>

**DumpData**
</dt> <dd>

A pointer to the context data that is provided by the filter driver in [**FILTER\_INITIALIZATION\_DATA**](filter-initialization-data.md).

</dd> </dl>

## Remarks

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows Vista and Windows Server 2008.<br/>                                  |
| Header<br/>  | <dl> <dt>Ntdddump.h (include Ntdddump.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_GEOMETRY**](disk-geometry.md)
</dt> <dt>

[**DISK\_PARTITION\_INFO**](disk-partition-info.md)
</dt> <dt>

[**FILTER\_INITIALIZATION\_DATA**](filter-initialization-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FILTER_EXTENSION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






