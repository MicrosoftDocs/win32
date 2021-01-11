---
description: Valid partition types used by disk drivers.
ms.assetid: b2e15b93-a02b-4d6f-b242-b5ec9a30c97b
title: Disk Partition Types (WinIoCtl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Disk Partition Types

The following table identifies the valid partition types that are used by disk drivers.



| Constant/value                                                                                                                                                                                                                                      | Description                                                                                                                                                |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PARTITION_ENTRY_UNUSED"></span><span id="partition_entry_unused"></span><dl> <dt>**PARTITION\_ENTRY\_UNUSED**</dt> <dt>0x00</dt> </dl> | An unused entry partition.<br/>                                                                                                                      |
| <span id="PARTITION_EXTENDED"></span><span id="partition_extended"></span><dl> <dt>**PARTITION\_EXTENDED**</dt> <dt>0x05</dt> </dl>              | An extended partition.<br/>                                                                                                                          |
| <span id="PARTITION_FAT_12"></span><span id="partition_fat_12"></span><dl> <dt>**PARTITION\_FAT\_12**</dt> <dt>0x01</dt> </dl>                   | A FAT12 file system partition.<br/>                                                                                                                  |
| <span id="PARTITION_FAT_16"></span><span id="partition_fat_16"></span><dl> <dt>**PARTITION\_FAT\_16**</dt> <dt>0x04</dt> </dl>                   | A FAT16 file system partition.<br/>                                                                                                                  |
| <span id="PARTITION_FAT32"></span><span id="partition_fat32"></span><dl> <dt>**PARTITION\_FAT32**</dt> <dt>0x0B</dt> </dl>                       | A FAT32 file system partition.<br/>                                                                                                                  |
| <span id="PARTITION_IFS"></span><span id="partition_ifs"></span><dl> <dt>**PARTITION\_IFS**</dt> <dt>0x07</dt> </dl>                             | An IFS partition.<br/>                                                                                                                               |
| <span id="PARTITION_LDM"></span><span id="partition_ldm"></span><dl> <dt>**PARTITION\_LDM**</dt> <dt>0x42</dt> </dl>                             | A logical disk manager (LDM) partition.<br/>                                                                                                         |
| <span id="PARTITION_NTFT"></span><span id="partition_ntft"></span><dl> <dt>**PARTITION\_NTFT**</dt> <dt>0x80</dt> </dl>                          | An NTFT partition.<br/>                                                                                                                              |
| <span id="VALID_NTFT"></span><span id="valid_ntft"></span><dl> <dt>**VALID\_NTFT**</dt> <dt>0xC0</dt> </dl>                                      | A valid NTFT partition.<br/> The high bit of a partition type code indicates that a partition is part of an NTFT mirror or striped array.<br/> |



## Remarks

There are several macros that can help you detect the partition type: **IsContainerPartition**, **IsFTPartition**, and **IsRecognizedPartition**. For more information, see WinIoCtl.h.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>WinIoCtl.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**PARTITION\_INFORMATION\_EX**](/windows/desktop/api/WinIoCtl/ns-winioctl-partition_information_ex)
</dt> <dt>

[**PARTITION\_INFORMATION\_MBR**](/windows/desktop/api/WinIoCtl/ns-winioctl-partition_information_mbr)
</dt> <dt>

[**SET\_PARTITION\_INFORMATION**](/windows/desktop/api/WinIoCtl/ns-winioctl-set_partition_information)
</dt> </dl>

 

 




