---
title: IBackgroundCopyJob GetNotifyFlags method (Deliveryoptimization.h)
description: Retrieves the event notification flags for the job.
ms.assetid: 95ADC97F-63DC-4EB6-B85C-7BCC79238C12
keywords:
- GetNotifyFlags method
- GetNotifyFlags method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, GetNotifyFlags method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.GetNotifyFlags
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::GetNotifyFlags method

Retrieves the event notification flags for the job.

## Syntax


```C++
HRESULT GetNotifyFlags(
  [out] ULONG *pNotifyFlags
);
```



## Parameters

<dl> <dt>

*pNotifyFlags* \[out\]
</dt> <dd>

Identifies the events that your application receives. The following table lists the event notification flag values.



| Value                                                                                                                                                                                                  | Meaning                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <span id="BG_NOTIFY_JOB_TRANSFERRED"></span><span id="bg_notify_job_transferred"></span><dl> <dt>**BG_NOTIFY_JOB_TRANSFERRED**</dt> </dl>    | All of the files in the job have been transferred.<br/>                  |
| <span id="BG_NOTIFY_JOB_ERROR"></span><span id="bg_notify_job_error"></span><dl> <dt>**BG_NOTIFY_JOB_ERROR**</dt> </dl>                      | An error has occurred.<br/>                                              |
| <span id="BG_NOTIFY_DISABLE"></span><span id="bg_notify_disable"></span><dl> <dt>**BG_NOTIFY_DISABLE**</dt> </dl>                             | Event notification is disabled. If set, DO ignores the other flags.<br/> |
| <span id="BG_NOTIFY_JOB_MODIFICATION"></span><span id="bg_notify_job_modification"></span><dl> <dt>**BG_NOTIFY_JOB_MODIFICATION**</dt> </dl> | The job has been modified.<br/>                                          |



 

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                              | Description                                                |
|------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl> | Event notify flags were successfully retrieved.<br/> |



 

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

[**IBackgroundCopyCallback**](ibackgroundcopycallback.md)
</dt> <dt>

[**IBackgroundCopyJob::GetNotifyInterface**](ibackgroundcopyjob-getnotifyinterface.md)
</dt> <dt>

[**IBackgroundCopyJob::SetNotifyFlags**](ibackgroundcopyjob-setnotifyflags.md)
</dt> </dl>

 

 





