---
title: ExecuteKCC method of the MSAD_DomainController class
description: Calls the DsReplicaConsistencyCheck function, which invokes the Knowledge Consistency Checker (KCC) to verify the replication topology.
ms.assetid: 958c9a15-cde2-4c74-bd4c-c2d53551cfb0
ms.tgt_platform: multiple
keywords:
- ExecuteKCC method Active Directory
- ExecuteKCC method Active Directory , MSAD_DomainController class
- MSAD_DomainController class Active Directory , ExecuteKCC method
topic_type:
- apiref
api_name:
- MSAD_DomainController.ExecuteKCC
api_location:
- replprov.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ExecuteKCC method of the MSAD\_DomainController class

Calls the [**DsReplicaConsistencyCheck**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicaconsistencycheck) function, which invokes the Knowledge Consistency Checker (KCC) to verify the replication topology.

## Syntax


```mof
void ExecuteKCC(
  [in] uint32 TaskID,
  [in] uint32 dwFlags
);
```



## Parameters

<dl> <dt>

*TaskID* \[in\]
</dt> <dd>

The task that the KCC should execute. **DS\_KCC\_TASKID\_UPDATE\_TOPOLOGY** is the only value that is currently supported.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

A set of flags that modify the behavior of the **ExecuteKCC** method. This parameter can be zero or a combination of one or more of the following values.

<dt>

<span id="DS_KCC_FLAG_ASYNC_OP"></span><span id="ds_kcc_flag_async_op"></span>

<span id="DS_KCC_FLAG_ASYNC_OP"></span><span id="ds_kcc_flag_async_op"></span>**DS\_KCC\_FLAG\_ASYNC\_OP**


</dt> <dd>

The task is queued and then the function returns without waiting for the task to complete.

</dd> <dt>

<span id="DS_KCC_FLAG_DAMPED"></span><span id="ds_kcc_flag_damped"></span>

<span id="DS_KCC_FLAG_DAMPED"></span><span id="ds_kcc_flag_damped"></span>**DS\_KCC\_FLAG\_DAMPED**


</dt> <dd>

The task will not be added to the queue if another queued task will run soon.

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

[**MSAD\_DomainController**](msad-domaincontroller.md)
</dt> </dl>

 

 





