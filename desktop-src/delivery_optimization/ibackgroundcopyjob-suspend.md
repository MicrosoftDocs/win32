---
title: IBackgroundCopyJob Suspend method (Deliveryoptimization.h)
description: Suspends a job. New jobs, jobs that are in error, and jobs that have finished transferring files are automatically suspended.
ms.assetid: 23EED354-A3AC-4865-8C06-ADA097851F96
keywords:
- Suspend method
- Suspend method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, Suspend method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.Suspend
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::Suspend method

Suspends a job. New jobs, jobs that are in error, and jobs that have finished transferring files are automatically suspended.

## Syntax


```C++
HRESULT Suspend();
```



## Parameters

This method has no parameters.

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                                          | Description                                                                                          |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl>             | Successfully suspended the job.<br/>                                                           |
| <dl> <dt>**DO_E_INVALID_STATE**</dt> </dl> | The state of the job cannot be BG_JOB_STATE_CANCELLED or BG_JOB_STATE_ACKNOWLEDGED.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyJob is defined as 37668D37-507E-4160-9316-26306D150B12<br/>               |



## See also

<dl> <dt>

[**IBackgroundCopyJob**](ibackgroundcopyjob-.md)
</dt> <dt>

[**IBackgroundCopyJob::Cancel**](ibackgroundcopyjob-cancel.md)
</dt> <dt>

[**IBackgroundCopyJob::Resume**](ibackgroundcopyjob-resume.md)
</dt> </dl>

 

 





