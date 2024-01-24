---
title: IBackgroundCopyManager GetJob method (Deliveryoptimization.h)
description: Retrieves a specified job from the transfer queue. Typically, your application persists the job identifier, so you can later retrieve the job from the queue.
ms.assetid: ED551A6B-66C7-47E9-93DA-E231BD637522
keywords:
- GetJob method
- GetJob method, IBackgroundCopyManager interface
- IBackgroundCopyManager interface, GetJob method
topic_type:
- apiref
api_name:
- IBackgroundCopyManager.GetJob
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyManager::GetJob method

Retrieves a specified job from the transfer queue. Typically, your application persists the job identifier, so you can later retrieve the job from the queue.

## Syntax


```C++
HRESULT GetJob(
  [in]  REFGUID            JobID,
  [out] IBackgroundCopyJob **ppJob
);
```



## Parameters

<dl> <dt>

*JobID* \[in\]
</dt> <dd>

Identifies the job to retrieve from the transfer queue. The [**CreateJob**](ibackgroundcopymanager-createjob.md) method returns the job identifier.

</dd> <dt>

*ppJob* \[out\]
</dt> <dd>

An [**IBackgroundCopyJob**](ibackgroundcopyjob-.md) interface pointer to the job specified by *JobID*. When done, release *ppJob*.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                                      | Description                                                        |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl>         | Job was successfully retrieved from the transfer queue.<br/> |
| <dl> <dt>**DO_E_NOT_FOUND**</dt> </dl> | The job was not found in the queue.<br/>                     |
| <dl> <dt>**E_ACCESSDENIED**</dt> </dl>   | User does not have permission to retrieve the job.<br/>      |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyManager is defined as 5CE34C0D-0DC9-4C1F-897C-DAA1B78CEE7C<br/>           |



## See also

<dl> <dt>

[**IBackgroundCopyManager**](ibackgroundcopymanager.md)
</dt> <dt>

[**IBackgroundCopyJob**](ibackgroundcopyjob-.md)
</dt> <dt>

[**IBackgroundCopyJob::GetId**](ibackgroundcopyjob-getid.md)
</dt> <dt>

[**IBackgroundCopyManager::CreateJob**](ibackgroundcopymanager-createjob.md)
</dt> </dl>

 

 





