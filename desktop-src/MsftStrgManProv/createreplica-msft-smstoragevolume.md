---
title: CreateReplica method of the MSFT\_SMStorageVolume class
description: Creates a replication relationship between virtual disks.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '36905908-2e50-44cb-ac74-b4e4864dfcbc'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateReplica method", "CreateReplica method, MSFT_SMStorageVolume class", "MSFT_SMStorageVolume class, CreateReplica method"]
topic_type:
- apiref
api_name:
- MSFT_SMStorageVolume.CreateReplica
api_location:
- StorageService.dll
api_type:
- COM
---

# CreateReplica method of the MSFT\_SMStorageVolume class

Creates a replication relationship between virtual disks.

## Syntax


```mof
UInt32 CreateReplica(
  [in]            string                     ElementName,
  [in]            uint16                     SyncType,
  [in]            uint16                     Mode,
  [in]            MSFT_SMReplicaPeer     REF TargetStorageSystem,
  [in, out]       MSFT_SMStorageVolume   REF TargetStorageVolume,
  [in]            MSFT_SMPool            REF TargetStoragePool,
  [in]            UInt32                     RecoveryPointObjective,
  [in, optional]  MSFT_SMReplicationSettings ReplicationSettings,
  [out]           MSFT_SMReplicaPeer     REF TargetReplicaPeer,
  [in, optional]  String                     username,
  [in, optional]  String                     password,
  [out]           MSFT_SMJob             REF Job,
  [out, optional] MSFT_SMExtendedStatus      ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

The user friendly name for the replica relationship. The systems can use a default name if this value is set to **NULL**.

</dd> <dt>

*SyncType* \[in\]
</dt> <dd>

Indicates the type of copy to make.

The possible values are:

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>0–5</dd> <dt>

<span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span>

**Mirror** (6)


</dt> <dd></dd> <dt>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>

**Snapshot** (7)


</dt> <dd></dd> <dt>

<span id="Clone"></span><span id="clone"></span><span id="CLONE"></span>

**Clone** (8)


</dt> <dd></dd> <dt>

<span id="TokenizedClone"></span><span id="tokenizedclone"></span><span id="TOKENIZEDCLONE"></span>

**TokenizedClone** (9)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>10–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*Mode* \[in\]
</dt> <dd>

The setting to use to update target elements. If this value is **NULL**, the system will specify this setting.

The possible values are:

<dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>**Synchronous** (2)


</dt> <dd>

Update target elements synchronously.

</dd> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>**Asynchronous** (3)


</dt> <dd>

Update target elements asynchronously.

</dd> <dt>

<span id="Adaptive"></span><span id="adaptive"></span><span id="ADAPTIVE"></span>

<span id="Adaptive"></span><span id="adaptive"></span><span id="ADAPTIVE"></span>**Adaptive** (4)


</dt> <dd>

Dynamically switch between synchronous and asynchronous modes.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific**


</dt> <dd></dd> </dl> </dd> <dt>

*TargetStorageSystem* \[in\]
</dt> <dd>

A [**MSFT\_SMReplicaPeer**](msft-smreplicapeer.md) object that specifies the replica target system to use when the replication relationship is created.

</dd> <dt>

*TargetStorageVolume* \[in, out\]
</dt> <dd>

A [**MSFT\_SMStorageVolume**](msft-smstoragevolume.md) object that specifies the volume to create for the replica relationship. If this parameter is specified, the *TargetStoragePool* parameter will be ignored.

</dd> <dt>

*TargetStoragePool* \[in\]
</dt> <dd>

The [**MSFT\_SMPool**](msft-smpool.md) object that specifies the storage pool to create for the replica relationship. This volume is ignored if the *TargetStorageVolume* parameter is specified.

</dd> <dt>

*RecoveryPointObjective* \[in\]
</dt> <dd>

Indicates the maximum interval in which data from copy operations might be lost. For synchronous copy operations, this interval is "0". For asynchronous copy operations, this parameter represents the interval since the most recent transmission of data to the target element.

</dd> <dt>

*ReplicationSettings* \[in, optional\]
</dt> <dd>

The replication settings.

</dd> <dt>

*TargetReplicaPeer* \[out\]
</dt> <dd>

When this method returns, this parameter contains a reference to the [**MSFT\_SMReplicaPeer**](msft-smreplicapeer.md) object that specifies the replica peer for the target volume of the replica relationship.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

The username to use to authenticate the SMI-S provider. If this parameter is not set, the storage service will attempt to retrieve the credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

The password to use to authenticate the SMI-S provider. If this parameter is not set, the storage service will attempt to retrieve the credentials from the configuration provider.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the [**MSFT\_SMJob**](msft-smjob.md) object that specifies a reference to a job if this method returns "Method Parameters Checked - Job Started". If this operation performs synchronously, this parameter is set to **NULL**.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

A [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object that specifies detailed status information about the result of this operation.

</dd> </dl>

## Return value

The possible return values are:

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

**Object Not Found** (8)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| Header<br/>                   | <dl> <dt>Adojet.h</dt> </dl>           |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageVolume**](msft-smstoragevolume.md)
</dt> </dl>

 

 





