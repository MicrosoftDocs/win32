---
title: GetSupportedCopyStates method of the MSFT\_SMReplicationCapabilities class
description: Retrieves the supported copy states for the specified replication type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7d2e871e-3638-4fcb-8043-6692e341c89c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedCopyStates method
- GetSupportedCopyStates method, MSFT_SMReplicationCapabilities class
- MSFT_SMReplicationCapabilities class, GetSupportedCopyStates method
topic_type:
- apiref
api_name:
- MSFT_SMReplicationCapabilities.GetSupportedCopyStates
api_location:
- StorageService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSupportedCopyStates method of the MSFT\_SMReplicationCapabilities class

Retrieves the supported copy states for the specified replication type.

## Syntax


```mof
uint32 GetSupportedCopyStates(
  [in]            uint16                ReplicationType,
  [out]           uint16                SupportedCopyStates[],
  [in, optional]  String                username,
  [in, optional]  String                password,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

Indicates the replication type for which to retrieve copy states.

The possible values are:

<dt>

<span id="Synchronous_Mirror_Local"></span><span id="synchronous_mirror_local"></span><span id="SYNCHRONOUS_MIRROR_LOCAL"></span>

**Synchronous Mirror Local** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Mirror_Local"></span><span id="asynchronous_mirror_local"></span><span id="ASYNCHRONOUS_MIRROR_LOCAL"></span>

**Asynchronous Mirror Local** (3)


</dt> <dd></dd> <dt>

<span id="Synchronous_Mirror_Remote"></span><span id="synchronous_mirror_remote"></span><span id="SYNCHRONOUS_MIRROR_REMOTE"></span>

**Synchronous Mirror Remote** (4)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Mirror_Remote"></span><span id="asynchronous_mirror_remote"></span><span id="ASYNCHRONOUS_MIRROR_REMOTE"></span>

**Asynchronous Mirror Remote** (5)


</dt> <dd></dd> <dt>

<span id="Synchronous_Snapshot_Local"></span><span id="synchronous_snapshot_local"></span><span id="SYNCHRONOUS_SNAPSHOT_LOCAL"></span>

**Synchronous Snapshot Local** (6)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Snapshot_Local"></span><span id="asynchronous_snapshot_local"></span><span id="ASYNCHRONOUS_SNAPSHOT_LOCAL"></span>

**Asynchronous Snapshot Local** (7)


</dt> <dd></dd> <dt>

<span id="Synchronous_Snapshot_Remote"></span><span id="synchronous_snapshot_remote"></span><span id="SYNCHRONOUS_SNAPSHOT_REMOTE"></span>

**Synchronous Snapshot Remote** (8)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Snapshot_Remote"></span><span id="asynchronous_snapshot_remote"></span><span id="ASYNCHRONOUS_SNAPSHOT_REMOTE"></span>

**Asynchronous Snapshot Remote** (9)


</dt> <dd></dd> <dt>

<span id="Synchronous_Clone_Local"></span><span id="synchronous_clone_local"></span><span id="SYNCHRONOUS_CLONE_LOCAL"></span>

**Synchronous Clone Local** (10)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Clone_Local"></span><span id="asynchronous_clone_local"></span><span id="ASYNCHRONOUS_CLONE_LOCAL"></span>

**Asynchronous Clone Local** (11)


</dt> <dd></dd> <dt>

<span id="Synchronous_Clone_Remote"></span><span id="synchronous_clone_remote"></span><span id="SYNCHRONOUS_CLONE_REMOTE"></span>

**Synchronous Clone Remote** (12)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Clone_Remote"></span><span id="asynchronous_clone_remote"></span><span id="ASYNCHRONOUS_CLONE_REMOTE"></span>

**Asynchronous Clone Remote** (13)


</dt> <dd></dd> <dt>

<span id="Synchronous_TokenizedClone_Local"></span><span id="synchronous_tokenizedclone_local"></span><span id="SYNCHRONOUS_TOKENIZEDCLONE_LOCAL"></span>

**Synchronous TokenizedClone Local** (14)


</dt> <dd></dd> <dt>

<span id="Asynchronous_TokenizedClone_Local"></span><span id="asynchronous_tokenizedclone_local"></span><span id="ASYNCHRONOUS_TOKENIZEDCLONE_LOCAL"></span>

**Asynchronous TokenizedClone Local** (15)


</dt> <dd></dd> <dt>

<span id="Synchronous_TokenizedClone_Remote"></span><span id="synchronous_tokenizedclone_remote"></span><span id="SYNCHRONOUS_TOKENIZEDCLONE_REMOTE"></span>

**Synchronous TokenizedClone Remote** (16)


</dt> <dd></dd> <dt>

<span id="Asynchronous_TokenizedClone_Remote"></span><span id="asynchronous_tokenizedclone_remote"></span><span id="ASYNCHRONOUS_TOKENIZEDCLONE_REMOTE"></span>

**Asynchronous TokenizedClone Remote** (17)


</dt> <dd></dd> <dt>

<span id="Adaptive_Mirror_Local"></span><span id="adaptive_mirror_local"></span><span id="ADAPTIVE_MIRROR_LOCAL"></span>

**Adaptive Mirror Local** (18)


</dt> <dd></dd> <dt>

<span id="Adaptive_Mirror_Remote"></span><span id="adaptive_mirror_remote"></span><span id="ADAPTIVE_MIRROR_REMOTE"></span>

**Adaptive Mirror Remote** (19)


</dt> <dd></dd> <dt>

<span id="Adaptive_Snapshot_Local"></span><span id="adaptive_snapshot_local"></span><span id="ADAPTIVE_SNAPSHOT_LOCAL"></span>

**Adaptive Snapshot Local** (20)


</dt> <dd></dd> <dt>

<span id="Adaptive_Snapshot_Remote"></span><span id="adaptive_snapshot_remote"></span><span id="ADAPTIVE_SNAPSHOT_REMOTE"></span>

**Adaptive Snapshot Remote** (21)


</dt> <dd></dd> <dt>

<span id="Adaptive_Clone_Local"></span><span id="adaptive_clone_local"></span><span id="ADAPTIVE_CLONE_LOCAL"></span>

**Adaptive Clone Local** (22)


</dt> <dd></dd> <dt>

<span id="Adaptive_Clone_Remote"></span><span id="adaptive_clone_remote"></span><span id="ADAPTIVE_CLONE_REMOTE"></span>

**Adaptive Clone Remote** (23)


</dt> <dd></dd> <dt>

<span id="Adaptive_TokenizedClone_Local"></span><span id="adaptive_tokenizedclone_local"></span><span id="ADAPTIVE_TOKENIZEDCLONE_LOCAL"></span>

**Adaptive TokenizedClone Local** (24)


</dt> <dd></dd> <dt>

<span id="Adaptive_TokenizedClone_Remote"></span><span id="adaptive_tokenizedclone_remote"></span><span id="ADAPTIVE_TOKENIZEDCLONE_REMOTE"></span>

**Adaptive TokenizedClone Remote** (25)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>26 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific** (32768)


</dt> <dd></dd> </dl> </dd> <dt>

*SupportedCopyStates* \[out\]
</dt> <dd>

An array that contains indicators of the supported copy states for the replication type.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

The username used to authenticate the SMI-S provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

The password used to authenticate the SMI-S provider.

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

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMReplicationCapabilities**](msft-smreplicationcapabilities.md)
</dt> </dl>

 

 





