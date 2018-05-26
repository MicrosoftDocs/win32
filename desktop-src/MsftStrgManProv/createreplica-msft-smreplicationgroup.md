---
title: CreateReplica method of the MSFT\_SMReplicationGroup class
description: Creates a replica relationship between replication groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dca55d0a-d69f-4b39-85f2-10e531a350d9
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateReplica method
- CreateReplica method, MSFT_SMReplicationGroup class
- MSFT_SMReplicationGroup class, CreateReplica method
topic_type:
- apiref
api_name:
- MSFT_SMReplicationGroup.CreateReplica
api_location:
- StorageService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateReplica method of the MSFT\_SMReplicationGroup class

Creates a replica relationship between replication groups.

## Syntax


```mof
UInt32 CreateReplica(
  [in]            string                      RelationshipName,
  [in]            uint16                      SyncType,
  [in]            uint16                      Mode,
  [in]            MSFT_SMReplicaPeer      REF TargetStorageSystem,
  [in, optional]  MSFT_SMReplicationGroup REF TargetGroupObject,
  [in]            MSFT_SMPool             REF TargetStoragePool,
  [in, optional]  MSFT_SMReplicationSettings  ReplicationSettings,
  [in]            UInt32                      RecoveryPointObjective,
  [out]           MSFT_SMReplicaPeer      REF TargetReplicaPeer,
  [in, optional]  String                      username,
  [in, optional]  String                      password,
  [out]           MSFT_SMJob              REF Job,
  [out, optional] MSFT_SMExtendedStatus       ExtendedStatus
);
```



## Parameters

<dl> <dt>

*RelationshipName* \[in\]
</dt> <dd>

The name of the new replica relationship.

</dd> <dt>

*SyncType* \[in\]
</dt> <dd>

Indicates the type of copy to make.

The possible values are:

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>0 5</dd> <dt>

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


</dt> <dd>10 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 ...</dd> </dl> </dd> <dt>

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

Indicates the replica target system to use when setting up a relationship of storage objects within the system.

</dd> <dt>

*TargetGroupObject* \[in, optional\]
</dt> <dd>

A [**MSFT\_SMReplicationGroup**](msft-smreplicationgroup.md) object that specifies the target replication group to create.

</dd> <dt>

*TargetStoragePool* \[in\]
</dt> <dd>

An array that contains [**MSFT\_SMPool**](msft-smpool.md) objects that contain storage objects of the target replication group.

> [!Note]  
> If this parameter is specified, *TargetStoragePool* parameter must be set to **NULL**.

 

</dd> <dt>

*ReplicationSettings* \[in, optional\]
</dt> <dd>

A [**MSFT\_SMReplicationSettings**](msft-smreplicationsettings.md) object that contains settings to apply to the replication relationship.

</dd> <dt>

*RecoveryPointObjective* \[in\]
</dt> <dd>

Indicates the maximum interval in which data from copy operations might be lost. For synchronous copy operations, this interval is "0". For asynchronous copy operations, this parameter represents the interval since the most recent transmission of data to the target element.

</dd> <dt>

*TargetReplicaPeer* \[out\]
</dt> <dd>

A [**MSFT\_SMReplicaPeer**](msft-smreplicapeer.md) object that specifies the association between the source replication group and the instance of the replication target.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

The username used to authenticate the SMI-S provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

The password used to authenticate the SMI-S provider.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If this operation is asynchronous, when this method returns, this parameter contains a reference to the object that represents the job; otherwise this parameter is set to **NULL**.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

When this method returns, this parameter contains a [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object that contains detailed status information about the results of this operation.

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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| Header<br/>                   | <dl> <dt>Adojet.h</dt> </dl>           |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMReplicationGroup**](msft-smreplicationgroup.md)
</dt> </dl>

 

 





