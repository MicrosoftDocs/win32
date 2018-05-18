---
title: MSFT\_StorageNodeToDisk class
description: Association between MSFT\_StorageNode and MSFT\_Disk.
ms.assetid: 'B892198B-F423-4F6A-8A43-99917D98B78F'
keywords: ["MSFT_StorageNodeToDisk class Windows Storage Management API", "MSFT_StorageNodeToDisk class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageNodeToDisk
- MSFT_StorageNodeToDisk.DiskNumber
- MSFT_StorageNodeToDisk.OperationalStatus
- MSFT_StorageNodeToDisk.HealthStatus
- MSFT_StorageNodeToDisk.IsOffline
- MSFT_StorageNodeToDisk.OfflineReason
- MSFT_StorageNodeToDisk.IsReadOnly
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageNodeToDisk class

Association between [**MSFT\_StorageNode**](msft-storagenode.md) and [**MSFT\_Disk**](msft-disk.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageNodeToDisk
{
  UInt32  DiskNumber;
  UInt16  OperationalStatus;
  UInt16  HealthStatus;
  Boolean IsOffline;
  UInt16  OfflineReason;
  Boolean IsReadOnly;
};
```

## Members

The **MSFT\_StorageNodeToDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNodeToDisk** class has these properties.

<dl> <dt>

**DiskNumber**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The operating system's number for the disk. Disk 0 is typically the boot device. Disk numbers may not necessarily remain the same across reboots.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Denotes the health status of the disk.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>**Healthy** (1)
</dt> <dt>

<span id="Failing"></span><span id="failing"></span><span id="FAILING"></span>**Failing** (4)
</dt> <dt>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>**Failed** (8)
</dt> </dl>

</dd> <dt>

**IsOffline**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the disk is offline.

</dd> <dt>

**IsReadOnly**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the disk is read only.

</dd> <dt>

**OfflineReason**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If *IsOffline* is **TRUE**, this property denotes the specific reason for the disk being offline.



| Value                                                                                                                                                                                                                                                                                                           | Meaning                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <span id="Policy"></span><span id="policy"></span><span id="POLICY"></span><dl> <dt>**Policy**</dt> <dt>1</dt> </dl>                                                                                         | The user requested the disk to be offline.<br/>                       |
| <span id="Redundant_Path"></span><span id="redundant_path"></span><span id="REDUNDANT_PATH"></span><dl> <dt>**Redundant Path**</dt> <dt>2</dt> </dl>                                                         | The disk is used for multi-path I/O.<br/>                             |
| <span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span><dl> <dt>**Snapshot**</dt> <dt>3</dt> </dl>                                                                                 | The disk is a snapshot disk.<br/>                                     |
| <span id="Collision"></span><span id="collision"></span><span id="COLLISION"></span><dl> <dt>**Collision**</dt> <dt>4</dt> </dl>                                                                             | There was a signature or identifier collision with another disk.<br/> |
| <span id="Resource_Exhaustion"></span><span id="resource_exhaustion"></span><span id="RESOURCE_EXHAUSTION"></span><dl> <dt>**Resource Exhaustion**</dt> <dt>5</dt> </dl>                                     | There were insufficient resources to bring the disk online.<br/>      |
| <span id="Critical_Write_Failures"></span><span id="critical_write_failures"></span><span id="CRITICAL_WRITE_FAILURES"></span><dl> <dt>**Critical Write Failures**</dt> <dt>6</dt> </dl>                     | There were critical write failures on the disk.<br/>                  |
| <span id="Data_Integrity_Scan_Required"></span><span id="data_integrity_scan_required"></span><span id="DATA_INTEGRITY_SCAN_REQUIRED"></span><dl> <dt>**Data Integrity Scan Required**</dt> <dt>7</dt> </dl> | A data integrity scan is required.<br/>                               |



 

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Denotes the operational status of the disk:

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Online"></span><span id="online"></span><span id="ONLINE"></span>**Online** (1)
</dt> <dt>

<span id="Not_Ready"></span><span id="not_ready"></span><span id="NOT_READY"></span>**Not Ready** (2)
</dt> <dt>

<span id="No_Media"></span><span id="no_media"></span><span id="NO_MEDIA"></span>**No Media** (3)
</dt> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>**Offline** (4)
</dt> <dt>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>**Failed** (5)
</dt> <dt>

<span id="Missing"></span><span id="missing"></span><span id="MISSING"></span>**Missing** (6)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Disk**](msft-disk.md)
</dt> <dt>

[**MSFT\_StorageNode**](msft-storagenode.md)
</dt> </dl>

 

 





