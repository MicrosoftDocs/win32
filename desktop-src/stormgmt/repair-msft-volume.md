---
title: Repair method of the MSFT\_Volume class
description: Repairs the volume.
ms.assetid: 'ee445db1-1afe-45ce-88f5-44fe8a13e002'
keywords: ["Repair method Windows Storage Management API", "Repair method Windows Storage Management API , MSFT_Volume class", "MSFT_Volume class Windows Storage Management API , Repair method"]
topic_type:
- apiref
api_name:
- MSFT_Volume.Repair
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# Repair method of the MSFT\_Volume class

Repairs the volume.

## Syntax


```mof
UInt32 Repair(
  [in]  Boolean             OfflineScanAndFix,
  [in]  Boolean             Scan,
  [in]  Boolean             SpotFix,
  [out] UInt32              Output,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*OfflineScanAndFix* \[in\]
</dt> <dd>

Set to TRUE to perform an offline scan and fix.

</dd> <dt>

*Scan* \[in\]
</dt> <dd>

Set to TRUE to scan the volume.

</dd> <dt>

*SpotFix* \[in\]
</dt> <dd>

Set to TRUE to perform spot fixes on the volume.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

The output of the repair operation.

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

Returns a reference to the storage job object used to track the long-running operation.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**This command is not supported on x86 running in x64 environment.** (7)
</dt> <dt>

**Access Denied** (40001)
</dt> <dt>

**An unexpected I/O error has occured** (40004)
</dt> <dt>

**The specified file system is not supported** (43001)
</dt> <dt>

**Cannot perform the requested operation when the drive is read only** (43006)
</dt> <dt>

**The repair failed** (43007)
</dt> <dt>

**The scan failed** (43008)
</dt> <dt>

**A snapshot error occured while scanning this drive. You can try again, but if this problem persists, run an offline scan and fix.** (43009)
</dt> <dt>

**A scan is already running on this drive. Chkdsk can not run more than one scan on a drive at a time.** (43010)
</dt> <dt>

**A snapshot error occured while scanning this drive. You can try again, but if this problem persists, run an offline scan and fix.** (43011)
</dt> <dt>

**A snapshot error occured while scanning this drive. Run an offline scan and fix.** (43012)
</dt> <dt>

**Cannot open drive for direct access** (43013)
</dt> <dt>

**Cannot determine the file system of the drive** (43014)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





