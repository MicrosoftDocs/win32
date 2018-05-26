---
title: TapeClassPhysicalBlockToLogicalBlock routine
description: The TapeClassPhysicalBlockToLogicalBlock routine translates a physical block address to a pseudological block address. This routine is for SCSI-1 devices.
ms.assetid: fc95f5c8-2892-479d-ac25-32c07e9c7aab
keywords:
- TapeClassPhysicalBlockToLogicalBlock routine Storage Devices
topic_type:
- apiref
api_name:
- TapeClassPhysicalBlockToLogicalBlock
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

# TapeClassPhysicalBlockToLogicalBlock routine

The **TapeClassPhysicalBlockToLogicalBlock** routine translates a physical block address to a pseudological block address. This routine is for SCSI-1 devices.

## Syntax


```C++
ULONG TapeClassPhysicalBlockToLogicalBlock(
  _In_ UCHAR   DensityCode,
  _In_ ULONG   PhysicalBlockAddress,
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

*PhysicalBlockAddress* \[in\]
</dt> <dd>

Specifies the physical block address obtained by a SCSI READ POSITION command.

</dd> <dt>

*BlockLength* \[in\]
</dt> <dd>

Specifies the logical block size, in bytes.

</dd> <dt>

*FromBOT* \[in\]
</dt> <dd>

**TRUE** indicates that the logical block calculation should start at the beginning of the tape and account for the physical device header. **FALSE** indicates that the tape has two partitions, that the block address is on the directory partition, and therefore no physical device header needs to be factored into the calculation.

</dd> </dl>

## Return value

**TapeClassPhysicalBlockToLogicalBlock** returns the logical block address.

## Remarks

A tape miniclass driver calls **TapeClassPhysicalBlockToLogicalBlock** to translate a physical block address from a tape device to a logical block address for an application. **TapeClassPhysicalBlockToLogicalBlock** is not necessary for SCSI-2 or later drivers because devices that comply with SCSI-2 or later standards support logical block addressing.

If a tape miniclass driver calls this routine with an unsupported tape density code, **TapeClassPhysicalBlockToLogicalBlock** returns the physical block address in the return value, without performing any translation.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Tape.lib</dt> </dl>                        |



## See also

<dl> <dt>

[**TapeClassLogicalBlockToPhysicalBlock**](tapeclasslogicalblocktophysicalblock.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TapeClassPhysicalBlockToLogicalBlock%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






