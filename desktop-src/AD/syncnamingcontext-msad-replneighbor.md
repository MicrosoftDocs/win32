---
title: SyncNamingContext method of the MSAD_ReplNeighbor class
description: Calls the DsReplicaSync function that synchronizes a destination naming context with one of its sources.
ms.assetid: 005053c4-8d9c-42f6-bae6-3ecdedd5ac2b
ms.tgt_platform: multiple
keywords:
- SyncNamingContext method Active Directory
- SyncNamingContext method Active Directory , MSAD_ReplNeighbor class
- MSAD_ReplNeighbor class Active Directory , SyncNamingContext method
topic_type:
- apiref
api_name:
- MSAD_ReplNeighbor.SyncNamingContext
api_location:
- replprov.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SyncNamingContext method of the MSAD\_ReplNeighbor class

Calls the [**DsReplicaSync**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicasynca) function that synchronizes a destination naming context with one of its sources.

## Syntax


```mof
void SyncNamingContext(
  [in] uint32 Options
);
```



## Parameters

<dl> <dt>

*Options* \[in\]
</dt> <dd>

Additional data that determines how the method processes the request. This parameter can be a combination of the following values.

<dt>

<span id="DS_REPSYNC_ADD_REFERENCE"></span><span id="ds_repsync_add_reference"></span>

<span id="DS_REPSYNC_ADD_REFERENCE"></span><span id="ds_repsync_add_reference"></span>**DS\_REPSYNC\_ADD\_REFERENCE**


</dt> <dd>

Causes the source directory system agent (DSA) to verify that the local DSA is present in the source replicates-to list. If the local DSA is not present, it is added. This ensures that the source sends change notifications.

</dd> <dt>

<span id="DS_REPSYNC_ALL_SOURCES"></span><span id="ds_repsync_all_sources"></span>

<span id="DS_REPSYNC_ALL_SOURCES"></span><span id="ds_repsync_all_sources"></span>**DS\_REPSYNC\_ALL\_SOURCES**


</dt> <dd>

This value is not supported.

**Windows Server 2008 R2, Windows Server 2008 and Windows Server 2003:** Synchronizes from all sources.

</dd> <dt>

<span id="DS_REPSYNC_ASYNCHRONOUS_OPERATION"></span><span id="ds_repsync_asynchronous_operation"></span>

<span id="DS_REPSYNC_ASYNCHRONOUS_OPERATION"></span><span id="ds_repsync_asynchronous_operation"></span>**DS\_REPSYNC\_ASYNCHRONOUS\_OPERATION**


</dt> <dd>

Performs this operation asynchronously.

**Windows Server 2008 R2, Windows Server 2008 and Windows Server 2003:** Required when using **DS\_REPSYNC\_ALL\_SOURCES**.

</dd> <dt>

<span id="DS_REPSYNC_FORCE"></span><span id="ds_repsync_force"></span>

<span id="DS_REPSYNC_FORCE"></span><span id="ds_repsync_force"></span>**DS\_REPSYNC\_FORCE**


</dt> <dd>

Synchronizes even if the link is currently disabled.

</dd> <dt>

<span id="DS_REPSYNC_FULL"></span><span id="ds_repsync_full"></span>

<span id="DS_REPSYNC_FULL"></span><span id="ds_repsync_full"></span>**DS\_REPSYNC\_FULL**


</dt> <dd>

Synchronizes starting from the first Update Sequence Number (USN).

</dd> <dt>

<span id="DS_REPSYNC_INTERSITE_MESSAGING"></span><span id="ds_repsync_intersite_messaging"></span>

<span id="DS_REPSYNC_INTERSITE_MESSAGING"></span><span id="ds_repsync_intersite_messaging"></span>**DS\_REPSYNC\_INTERSITE\_MESSAGING**


</dt> <dd>

Synchronizes using an ISM.

</dd> <dt>

<span id="DS_REPSYNC_NO_DISCARD"></span><span id="ds_repsync_no_discard"></span>

<span id="DS_REPSYNC_NO_DISCARD"></span><span id="ds_repsync_no_discard"></span>**DS\_REPSYNC\_NO\_DISCARD**


</dt> <dd>

Does not discard this synchronization request, even if a similar synchronization is pending.

</dd> <dt>

<span id="DS_REPSYNC_PERIODIC"></span><span id="ds_repsync_periodic"></span>

<span id="DS_REPSYNC_PERIODIC"></span><span id="ds_repsync_periodic"></span>**DS\_REPSYNC\_PERIODIC**


</dt> <dd>

Indicates that this operation is a periodic synchronization request that is scheduled by the administrator.

</dd> <dt>

<span id="DS_REPSYNC_URGENT"></span><span id="ds_repsync_urgent"></span>

<span id="DS_REPSYNC_URGENT"></span><span id="ds_repsync_urgent"></span>**DS\_REPSYNC\_URGENT**


</dt> <dd>

Indicates that this operation is a notification of an update that is marked as urgent.

</dd> <dt>

<span id="DS_REPSYNC_WRITEABLE"></span><span id="ds_repsync_writeable"></span>

<span id="DS_REPSYNC_WRITEABLE"></span><span id="ds_repsync_writeable"></span>**DS\_REPSYNC\_WRITEABLE**


</dt> <dd>

Indicates that this replica is writable. If this flag is not set, the replica is read-only.

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftActiveDirectory<br/>                                               |
| MOF<br/>                      | <dl> <dt>Replprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Replprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSAD\_ReplNeighbor**](msad-replneighbor.md)
</dt> </dl>

 

 





