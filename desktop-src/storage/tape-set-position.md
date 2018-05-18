---
title: TAPE\_SET\_POSITION structure
description: The TAPE\_SET\_POSITION structure is used in conjunction with the IOCTL\_TAPE\_SET\_POSITION request to move the current position on the tape to the specified partition and offset.
ms.assetid: '93918e09-2742-47ca-94a5-043af2a3a338'
keywords: ["TAPE_SET_POSITION structure Storage Devices", "PTAPE_SET_POSITION structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- TAPE_SET_POSITION
api_location:
- ntddtape.h
api_type:
- HeaderDef
---

# TAPE\_SET\_POSITION structure

The TAPE\_SET\_POSITION structure is used in conjunction with the [**IOCTL\_TAPE\_SET\_POSITION**](ioctl-tape-set-position.md) request to move the current position on the tape to the specified partition and offset.

## Syntax


```C++
typedef struct _TAPE_SET_POSITION {
  ULONG         Method;
  ULONG         Partition;
  LARGE_INTEGER Offset;
  BOOLEAN       Immediate;
} TAPE_SET_POSITION, *PTAPE_SET_POSITION;
```



## Members

<dl> <dt>

**Method**
</dt> <dd>

Indicates the type of positioning to perform. This member must have one of the following values:

<dl> <dt>

<span id="TAPE_REWIND"></span><span id="tape_rewind"></span>TAPE\_REWIND
</dt> <dd>

Positions the tape at the beginning of the partition indicated in **Partition** if the media is partitioned, and to the beginning of the media if the media is not partitioned. If the media is not partitioned, **Partition** must be set to zero. The **Offset** member is ignored.

</dd> <dt>

<span id="TAPE_ABSOLUTE_BLOCK"></span><span id="tape_absolute_block"></span>TAPE\_ABSOLUTE\_BLOCK
</dt> <dd>

Positions the tape at the absolute block address located at the offset from the beginning specified by **Offset**. The value in the **Partition** member is ignored.

</dd> <dt>

<span id="TAPE_LOGICAL_BLOCK"></span><span id="tape_logical_block"></span>TAPE\_LOGICAL\_BLOCK
</dt> <dd>

Positions the tape to the logical block address specified by **Offset**, relative to the beginning of the partition indicated in **Partition**. If the media is not partitioned, **Partition** must be set to zero.

</dd> <dt>

<span id="TAPE_PSEUDO_LOGICAL_BLOCK"></span><span id="tape_pseudo_logical_block"></span>TAPE\_PSEUDO\_LOGICAL\_BLOCK
</dt> <dd>

Positions the tape to the pseudological block address specified by **Offset**, relative to the beginning of the partition indicated in **Partition**. If the media is not partitioned, **Partition** must be to zero.

</dd> <dt>

<span id="TAPE_SPACE_END_OF_DATA"></span><span id="tape_space_end_of_data"></span>TAPE\_SPACE\_END\_OF\_DATA
</dt> <dd>

Positions the tape at the end of the partition indicated in **Partition**, or if the media is not partitioned, at the end of the tape. The **Offset** member is ignored.

</dd> <dt>

<span id="TAPE_SPACE_RELATIVE_BLOCKS"></span><span id="tape_space_relative_blocks"></span>TAPE\_SPACE\_RELATIVE\_BLOCKS
</dt> <dd>

Starting from the current position, positions the tape immediately after the number of blocks specified by **Offset**. The **Partition** member is ignored.

</dd> <dt>

<span id="TAPE_SPACE_FILEMARKS"></span><span id="tape_space_filemarks"></span>TAPE\_SPACE\_FILEMARKS
</dt> <dd>

Starting from the current position, positions the tape immediately after the number of filemarks specified by **Offset**. The **Partition** member is ignored.

</dd> <dt>

<span id="TAPE_SPACE_SEQUENTIAL_FMKS"></span><span id="tape_space_sequential_fmks"></span>TAPE\_SPACE\_SEQUENTIAL\_FMKS
</dt> <dd>

Starting from the current position, positions the tape immediately after the next occurrence, if any, of the number of consecutive filemarks specified by **Offset**. The **Partition** member is ignored.

</dd> <dt>

<span id="TAPE_SPACE_SETMARKS"></span><span id="tape_space_setmarks"></span>TAPE\_SPACE\_SETMARKS
</dt> <dd>

Starting from the current position, positions the tape immediately after the number of setmarks specified by **Offset**. The **Partition** member is ignored.

</dd> <dt>

<span id="TAPE_SPACE_SEQUENTIAL_SMKS"></span><span id="tape_space_sequential_smks"></span>TAPE\_SPACE\_SEQUENTIAL\_SMKS
</dt> <dd>

Starting from the current position, positions the tape immediately after the next occurrence, if any, of the number of consecutive setmarks specified by **Offset**. The **Partition** member is ignored.

</dd> </dl> </dd> <dt>

**Partition**
</dt> <dd>

Indicates the partition in which to set the tape's position. This member must have one of the following values:

<dl> <dt>

NOT\_PARTITIONED (or zero)
</dt> <dt>

DATA\_PARTITION
</dt> <dt>

DIRECTORY\_PARTITION
</dt> </dl>

If the media is not partitioned, this member is zero.

</dd> <dt>

**Offset**
</dt> <dd>

Specifies an offset whose type depends on the value in **Method**. If the specified method positions the tape to a block address, **Offset** specifies the byte offset into the specified partition. If the specified method is to skip blocks, filemarks, or setmarks, **Offset** specifies the number to skip. If **Offset** is zero, the tape is positioned at the beginning of the partition.

</dd> <dt>

**Immediate**
</dt> <dd>

When set to **TRUE**, indicates that the target device should return status immediately. When set to **FALSE**, indicates that the device should return status after the operation is complete.

</dd> </dl>

## Remarks

Note that a drive or a tape may not support all **Method** values.

Partitions are numbered logically from 1 to N. However, a partition number does not imply a physical position on the tape. For example, partition number one might not be at the beginning of the media.

When the offset specifies a number of blocks, filemarks, or setmarks to position over, a positive value N in the offset causes forward positioning over N blocks, filemarks, or setmarks, halting on the end-of-partition or end-of-tape side of the block, filemark, or setmark. A zero value in the offset causes no change of position. A negative value N in the offset causes reverse positioning, toward the beginning of the partition or the tape media, over N blocks, filemarks, or setmarks, halting on the beginning-of-partition side of a block, filemark, or setmark.

## Requirements



|                   |                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_TAPE\_SET\_POSITION**](ioctl-tape-set-position.md)
</dt> <dt>

[**TapeMiniSetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff567954)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_SET_POSITION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






