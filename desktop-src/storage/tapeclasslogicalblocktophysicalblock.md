---
title: TapeClassLogicalBlockToPhysicalBlock routine
description: The TapeClassLogicalBlockToPhysicalBlock routine translates a pseudological block address to a physical block address. This routine is for SCSI-1 devices.
ms.assetid: 4ad11a15-ba72-4921-a00a-6d3bfb443b51
keywords:
- TapeClassLogicalBlockToPhysicalBlock routine Storage Devices
topic_type:
- apiref
api_name:
- TapeClassLogicalBlockToPhysicalBlock
api_location:
- Tape.lib
- Tape.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TapeClassLogicalBlockToPhysicalBlock routine

The **TapeClassLogicalBlockToPhysicalBlock** routine translates a pseudological block address to a physical block address. This routine is for SCSI-1 devices.

## Syntax


```C++
TAPE_PHYS_POSITION TapeClassLogicalBlockToPhysicalBlock(
  _In_ UCHAR   DensityCode,
  _In_ ULONG   LogicalBlockAddress,
  _In_ ULONG   BlockLength,
  _In_ BOOLEAN FromBOT
);
```



## Parameters

<dl> <dt>

*DensityCode* \[in\]
</dt> <dd>

Specifies the tape media density code. This routine supports tapes with the following density codes: QIC\_24, QIC\_120, QIC\_150, QIC\_525, QIC\_1000, QIC\_2GB, QIC\_1350, and QIC\_2100.

</dd> <dt>

*LogicalBlockAddress* \[in\]
</dt> <dd>

Specifies a pseudological block address.

</dd> <dt>

*BlockLength* \[in\]
</dt> <dd>

Specifies the logical block size, in bytes.

</dd> <dt>

*FromBOT* \[in\]
</dt> <dd>

**TRUE** indicates that the physical block calculation should start at the beginning of the tape and account for the physical device header. **FALSE** indicates that the tape has two partitions, that the block address is on the directory partition, and therefore no physical device header needs to be factored into the calculation.

</dd> </dl>

## Return value

**TapeClassLogicalBlockToPhysicalBlock** returns a structure containing the physical block address:

typedef struct \_TAPE\_PHYS\_POSITION {

ULONG SeekBlockAddress;

ULONG SpaceBlockCount;

} TAPE\_PHYS\_POSITION, PTAPE\_PHYS\_POSITION;

## Remarks

A tape miniclass driver calls **TapeClassLogicalBlockToPhysicalBlock** to translate a logical block address from an application to a physical block address for a tape device. **TapeClassLogicalBlockToPhysicalBlock** is not necessary for SCSI-2 or later drivers because devices that comply with SCSI-2 or later standards support logical block addressing.

To position a tape to the physical block address returned by this routine, a tape miniclass driver issues two SCSI commands: a LOCATE command to position the tape to the **SeekBlockAddress**, and then a SPACE command to advance the tape **SpaceBlockCount**. The **SpaceBlockCount** value is necessary if the pseudological blocks on the tape are smaller than the physical blocks; in that case, the logical block boundary might not align with a physical block boundary.

If a tape miniclass driver calls this routine with an unsupported tape density code, **TapeClassLogicalBlockToPhysicalBlock** does not perform any translation. It returns the logical block address in **SeekBlockAddress** and returns zero in **SpaceBlockCount**.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Tape.lib</dt> </dl>                        |



## See also

<dl> <dt>

[**TapeClassPhysicalBlockToLogicalBlock**](tapeclassphysicalblocktologicalblock.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TapeClassLogicalBlockToPhysicalBlock%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






