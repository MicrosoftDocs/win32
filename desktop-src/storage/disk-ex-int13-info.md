---
title: DISK\_EX\_INT13\_INFO structure
description: The DISK\_EX\_INT13\_INFO structure is used by the BIOS to report disk detection data for a partition with an extended INT13 format.
ms.assetid: '82e3a1e9-275a-489a-9e6e-d76007a1abb9'
keywords: ["DISK_EX_INT13_INFO structure Storage Devices", "PDISK_EX_INT13_INFO structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DISK_EX_INT13_INFO
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# DISK\_EX\_INT13\_INFO structure

The DISK\_EX\_INT13\_INFO structure is used by the BIOS to report disk detection data for a partition with an extended INT13 format.

## Syntax


```C++
typedef struct _DISK_EX_INT13_INFO {
  USHORT  ExBufferSize;
  USHORT  ExFlags;
  ULONG   ExCylinders;
  ULONG   ExHeads;
  ULONG   ExSectorsPerTrack;
  ULONG64 ExSectorsPerDrive;
  USHORT  ExSectorSize;
  USHORT  ExReserved;
} DISK_EX_INT13_INFO, *PDISK_EX_INT13_INFO;
```



## Members

<dl> <dt>

**ExBufferSize**
</dt> <dd>

Indicates the size of the buffer that the caller provides to the BIOS in which to return the requested drive data. **ExBufferSize** must be 26 or greater. If **ExBufferSize** is less than 26, the BIOS returns an error . If **ExBufferSize** is between 30 and 66, the BIOS sets it to exactly 30 on exit. If **ExBufferSize** is 66 or greater, the BIOS sets it to exactly 66 on exit.

</dd> <dt>

**ExFlags**
</dt> <dd>

Provides information about the drive. The following table describes the significance of each bit, where bit 0 is the least significant bit and bit 15 the most significant bit. A value of one in the indicated bit means that the feature described in the "Meaning" column is available. A value of zero in the indicated bit means that the feature is not available with this drive.



| Bit number       | Meaning                                                                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 <br/>    | DMA boundary errors are handled transparently. <br/>                                                                                                        |
| 1 <br/>    | The geometry supplied in bytes 8-12 is valid. <br/>                                                                                                         |
| 2 <br/>    | Device is removable. <br/>                                                                                                                                  |
| 3 <br/>    | Device supports write with verify. <br/>                                                                                                                    |
| 4 <br/>    | Device has change line support (bit 2 must be set). <br/>                                                                                                   |
| 5 <br/>    | Device is lockable (bit 2 must be set). <br/>                                                                                                               |
| 6 <br/>    | Device geometry is set to maximum, no media is present (bit 2 must be set). This bit is turned off when media is present in a removable media device. <br/> |
| 7-15 <br/> | Reserved, must be 0. <br/>                                                                                                                                  |



 

</dd> <dt>

**ExCylinders**
</dt> <dd>

Indicates the number of *physical* cylinders. This is one greater than the maximum cylinder number.

</dd> <dt>

**ExHeads**
</dt> <dd>

Indicates the number of *physical* heads. This is one greater than the maximum head number.

</dd> <dt>

**ExSectorsPerTrack**
</dt> <dd>

Indicates the number of *physical* sectors per track. This number is the same as the maximum sector number.

</dd> <dt>

**ExSectorsPerDrive**
</dt> <dd>

Indicates the total count of sectors on the disk. This is one greater than the maximum logical block address.

</dd> <dt>

**ExSectorSize**
</dt> <dd>

Indicates the sector size in bytes.

</dd> <dt>

**ExReserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_DETECTION\_INFO**](disk-detection-info.md)
</dt> <dt>

[**DISK\_INT13\_INFO**](disk-int13-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_EX_INT13_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






