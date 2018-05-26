---
title: GetRecoveryPointData method of the MSFT\_ReplicationCapabilities class
description: Returns, for a given ReplicationType, recovery point data.
ms.assetid: F14F4AFE-F554-4DFA-8E45-2B953676E357
keywords:
- GetRecoveryPointData method Windows Storage Management API
- GetRecoveryPointData method Windows Storage Management API , MSFT_ReplicationCapabilities class
- MSFT_ReplicationCapabilities class Windows Storage Management API , GetRecoveryPointData method
topic_type:
- apiref
api_name:
- MSFT_ReplicationCapabilities.GetRecoveryPointData
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetRecoveryPointData method of the MSFT\_ReplicationCapabilities class

Returns, for a given *ReplicationType*, recovery point data.

## Syntax


```mof
UInt32 GetRecoveryPointData(
  [in]  UInt16 ReplicationType,
  [in]  UInt16 DefaultRecoveryPoint,
  [out] UInt16 RecoveryPointValues[],
  [out] UInt16 RecoveryPointIndicator,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

A value representing the replication type. This must be in the enumeration [**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md).SupportedReplicationTypes.

</dd> <dt>

*DefaultRecoveryPoint* \[in\]
</dt> <dd>

Default recovery point value.

</dd> <dt>

*RecoveryPointValues* \[out\]
</dt> <dd></dd> <dt>

*RecoveryPointIndicator* \[out\]
</dt> <dd>

Indicates the semantics of the supported values.

<dl> <dt>

<span id="Range"></span><span id="range"></span><span id="RANGE"></span>**Range** (1)
</dt> <dt>

<span id="Discrete"></span><span id="discrete"></span><span id="DISCRETE"></span>**Discrete** (2)
</dt> </dl> </dd> <dt>

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

**In Use** (6)
</dt> <dt>

**Property Is Not Supported** (7)
</dt> <dt>

**DMTF Reserved** (..)
</dt> <dt>

**Vendor Specific** (0x8000..)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md)
</dt> </dl>

 

 





