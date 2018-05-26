---
title: DEVICE\_DATA\_SET\_LB\_PROVISIONING\_STATE structure
description: The DEVICE\_DATA\_SET\_LB\_PROVISIONING\_STATE structure is returned by an IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES request when requesting logical block provisioning information for a data set range.
ms.assetid: 99FBD363-0999-4AEE-A222-69C0FB71D248
keywords:
- DEVICE_DATA_SET_LB_PROVISIONING_STATE structure Storage Devices
- PDEVICE_DATA_SET_LB_PROVISIONING_STATE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DEVICE_DATA_SET_LB_PROVISIONING_STATE
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

# DEVICE\_DATA\_SET\_LB\_PROVISIONING\_STATE structure

The **DEVICE\_DATA\_SET\_LB\_PROVISIONING\_STATE** structure is returned by an [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) request when requesting logical block provisioning information for a data set range.

## Syntax


```C++
typedef struct _DEVICE_DATA_SET_LB_PROVISIONING_STATE {
  ULONG     Size;
  ULONG     Version;
  ULONGLONG SlabSizeInBytes;
  ULONG     SlabOffsetDeltaInBytes;
  ULONG     SlabAllocationBitMapBitCount;
  ULONG     SlabAllocationBitMapLength;
  ULONG     SlabAllocationBitMap[ANYSIZE_ARRAY];
} DEVICE_DATA_SET_LB_PROVISIONING_STATE, *PDEVICE_DATA_SET_LB_PROVISIONING_STATE;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The size of this structure, including the slab allocation bitmap, in bytes.

</dd> <dt>

**Version**
</dt> <dd>

The version of this structure.

</dd> <dt>

**SlabSizeInBytes**
</dt> <dd>

The size, in bytes, of a slab.

</dd> <dt>

**SlabOffsetDeltaInBytes**
</dt> <dd>

The difference, in bytes, from the offset specified in the data set range to the starting slab position.

</dd> <dt>

**SlabAllocationBitMapBitCount**
</dt> <dd>

The number of bits in the allocation bitmap mapping slabs for the data set range.

</dd> <dt>

**SlabAllocationBitMapLength**
</dt> <dd>

The number of **ULONG** array values containing the slab allocation bitmap.

</dd> <dt>

**SlabAllocationBitMap**
</dt> <dd>

A bitmap of slab allocations.

</dd> </dl>

## Remarks

Provisioning state information is returned when the **Action** member of [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) is set to **DeviceDsmAction\_Allocation**. The caller should include only one data set range in the system buffer at **DataSetRangesOffset**.

On return, the system buffer contains a [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES\_OUPUT**](device-manage-data-set-attributes-output.md) structure followed by the **DEVICE\_DATA\_SET\_LB\_PROVISIONING\_STATE** structure. The **DEVICE\_DATA\_SET\_LB\_PROVISIONING\_STATE** structure begins at an offset from the beginning of the system buffer specified by **OutputBlockOffset** in **DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES\_OUPUT**.

Each bit in the allocation bitmap represents a slab mapping within the data set range requested. The bits correspond directly to the slabs in the data set range. This means that bit 0 in the bitmap marks the first slab in the range. A slab is mapped if the bit value = 1 and unmapped if the bit value = 0.

Space for **SlabAllocationBitMap** should be allocated based on the number of possible slabs in the requested data set range. The **SlabAllocationBitMapLength** of the bitmap returned is (*number of slabs* / 32) + ((*number of slabs* MOD 32) &gt; 0 ? 1 : 0).

Slab size is determined by the **OptimalUnmapGranularity** member of [**DEVICE\_LB\_PROVISIONING\_DESCRIPTOR**](device-lb-provisioning-descriptor.md) returned from an [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request. The length of the data set range provided should be a multiple of **OptimalUnmapGranularity**. When the range length is not a multiple of **OptimalUnmapGranularity**, it is reduced to be a multiple.

If the starting offset in the data set range is not aligned on a slab boundary, a multiple of **OptimalUnmapGranularity**, the offset will be adjusted to the next boundary. The difference between the requested offset and the adjusted offset is returned in **SlabOffsetDeltaInBytes**.

If the slab allocation total returned in **SlabAllocationBitMapBitCount** is not as expected because of data set range alignment or length adjustments, an additional request may be submitted with a data set range modified according to the values in both **SlabAllocationBitMapBitCount** and **SlabOffsetDeltaInBytes**. The new range will properly select the slabs left out of the bitmap returned by the previous request.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                              |
| Header<br/>  | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff552520)
</dt> <dt>

[**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md)
</dt> <dt>

[**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md)
</dt> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DEVICE_DATA_SET_LB_PROVISIONING_STATE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






