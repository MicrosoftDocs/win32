---
title: IBackgroundCopyJob Resume method (Deliveryoptimization.h)
description: Activates a new job or restarts a job that has been suspended.
ms.assetid: B745BDA6-36B9-41FD-9737-61D14150A9E4
keywords:
- Resume method
- Resume method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, Resume method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.Resume
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::Resume method

Activates a new job or restarts a job that has been suspended.

## Syntax


```C++
HRESULT Resume();
```



## Parameters

This method has no parameters.

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                                          | Description                                                                                          |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl>             | Job was successfully restarted.<br/>                                                           |
| <dl> <dt>**DO_E_EMPTY**</dt> </dl>          | There are no files to transfer.<br/>                                                           |
| <dl> <dt>**DO_E_INVALID_STATE**</dt> </dl> | The state of the job cannot be BG_JOB_STATE_CANCELLED or BG_JOB_STATE_ACKNOWLEDGED.<br/> |



 

## Remarks

When you create a job, the job is initially suspended. Calling **Resume** moves the job to the Transferring state. Note that the job must contain one or more files before calling this method.

If a job that is in the BG_JOB_STATE_TRANSIENT_ERROR or BG_JOB_STATE_ERROR state, call the **Resume** method to restart the job after you fix the error.

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

[**IBackgroundCopyJob::Suspend**](ibackgroundcopyjob-suspend.md)
</dt> </dl>

 

 





