---
title: STORAGE\_ACCESS\_ALIGNMENT\_DESCRIPTOR structure
description: The STORAGE\_ACCESS\_ALIGNMENT\_DESCRIPTOR structure is used in conjunction with the IOCTL\_STORAGE\_QUERY\_PROPERTY request to retrieve the storage access alignment descriptor data for a device.
ms.assetid: '988122bf-d7de-44a3-a059-c984bf636cd0'
keywords: ["STORAGE_ACCESS_ALIGNMENT_DESCRIPTOR structure Storage Devices", "PSTORAGE_ACCESS_ALIGNMENT_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_ACCESS_ALIGNMENT_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_ACCESS\_ALIGNMENT\_DESCRIPTOR structure

The STORAGE\_ACCESS\_ALIGNMENT\_DESCRIPTOR structure is used in conjunction with the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request to retrieve the storage access alignment descriptor data for a device.

## Syntax


```C++
typedef struct _STORAGE_ACCESS_ALIGNMENT_DESCRIPTOR {
  ULONG Version;
  ULONG Size;
  ULONG BytesPerCacheLine;
  ULONG BytesOffsetForCacheAlignment;
  ULONG BytesPerLogicalSector;
  ULONG BytesPerPhysicalSector;
  ULONG BytesOffsetForSectorAlignment;
} STORAGE_ACCESS_ALIGNMENT_DESCRIPTOR, *PSTORAGE_ACCESS_ALIGNMENT_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Contains the size of the structure STORAGE\_ACCESS\_ALIGNMENT\_DESCRIPTOR. The value of this member will change as members are added to the structure.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the total size of the descriptor, in bytes.

</dd> <dt>

**BytesPerCacheLine**
</dt> <dd>

The number of bytes in a cache line of the device.

</dd> <dt>

**BytesOffsetForCacheAlignment**
</dt> <dd>

The address offset necessary for proper cache access alignment, in bytes.

</dd> <dt>

**BytesPerLogicalSector**
</dt> <dd>

The number of bytes in a logical sector of the device.

</dd> <dt>

**BytesPerPhysicalSector**
</dt> <dd>

The number of bytes in a physical sector of the device.

</dd> <dt>

**BytesOffsetForSectorAlignment**
</dt> <dd>

The logical sector offset within the first physical sector where the first logical sector is placed, in bytes.

Example: Offset = 3 Logical sectors


```
+- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|LBA      |X|X|X|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|
|- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
|Physical |               |                  |
|Sector   |      0        |        1         |         2
+- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```



In this example, BytesOffsetForSectorAlignment = 3 \* size\_of\_logical\_sector.

</dd> </dl>

## Remarks

Storage class drivers issue a device-control request with the I/O control code [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to retrieve this structure, which contains access alignment information for data transfer operations. The structure can be retrieved either from the device object for the bus or from an FDO, which forwards the request to the underlying bus.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_ACCESS_ALIGNMENT_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






