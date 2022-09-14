---
title: IBackgroundCopyManager CreateJob method (Deliveryoptimization.h)
description: Creates a job.
ms.assetid: BDE5BE4D-9AE9-463D-B900-850D255EAB58
keywords:
- CreateJob method
- CreateJob method, IBackgroundCopyManager interface
- IBackgroundCopyManager interface, CreateJob method
topic_type:
- apiref
api_name:
- IBackgroundCopyManager.CreateJob
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyManager::CreateJob method

Creates a job.

## Syntax


```C++
HRESULT CreateJob(
  [in]  LPCWSTR            pDisplayName,
  [in]  BG_JOB_TYPE        Type,
  [out] GUID               *pJobID,
  [out] IBackgroundCopyJob **ppJob
);
```



## Parameters

<dl> <dt>

*pDisplayName* \[in\]
</dt> <dd>

Null-terminated string that contains a display name for the job. Typically, the display name is used to identify the job in a user interface. Note that more than one job may have the same display name. Must not be **NULL**. The name is limited to 256 characters, not including the null terminator.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type of transfer job, such as BG_JOB_TYPE_DOWNLOAD. For a list of transfer types, see the [**BG_JOB_TYPE**](bg-job-type.md) enumeration.

</dd> <dt>

*pJobID* \[out\]
</dt> <dd>

Uniquely identifies your job in the queue. Use this identifier when you call the [**IBackgroundCopyManager::GetJob**](ibackgroundcopymanager-getjob.md) method to get a job from the queue.

</dd> <dt>

*ppJob* \[out\]
</dt> <dd>

An [**IBackgroundCopyJob**](ibackgroundcopyjob-.md) interface pointer that you use to modify the job's properties and specify the files to be transferred. To activate the job in the queue, call the [**IBackgroundCopyJob::Resume**](ibackgroundcopyjob-resume.md) method. Release *ppJob* when done.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                              | Description                                    |
|------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl> | Successfully generated the new job.<br/> |



 

## Remarks

Only the user who creates the job or a user with administrator privileges can [add files to the job](https://www.bing.com/search?q=add+files+to+the+job) and [change the job's properties](https://www.bing.com/search?q=change+the+job's+properties).

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

[**IBackgroundCopyJob::Resume**](ibackgroundcopyjob-resume.md)
</dt> </dl>
