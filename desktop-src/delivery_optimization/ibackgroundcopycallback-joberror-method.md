---
title: IBackgroundCopyCallback JobError method
description: Delivery Optimization (DO) calls your implementation of the JobError method when the state of the job changes to BG\_JOB\_STATE\_ERROR.
ms.assetid: 121712A5-98EB-4B2F-A004-A3BDF9C1332B
keywords:
- JobError method
- JobError method, IBackgroundCopyCallback interface
- IBackgroundCopyCallback interface, JobError method
topic_type:
- apiref
api_name:
- IBackgroundCopyCallback.JobError
api_location:
- dosvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IBackgroundCopyCallback::JobError method

Delivery Optimization (DO) calls your implementation of the [**JobError**](delivery_optimization-ibackgroundcopycallback_joberror) method when the state of the job changes to BG\_JOB\_STATE\_ERROR.

## Syntax


```C++
HRESULT JobError(
  [in] IBackgroundCopyJob   *pJob,
  [in] IBackgroundCopyError *pError
);
```



## Parameters

<dl> <dt>

*pJob* \[in\]
</dt> <dd>

Contains job-related information, such as the number of bytes and files transferred before the error occurred. It also contains the methods to resume and cancel the job. Do not release *pJob*; DO releases the interface when the [**JobError**](delivery_optimization-ibackgroundcopycallback_joberror) method returns.

</dd> <dt>

*pError* \[in\]
</dt> <dd>

Contains error information, such as the file being processed at the time the fatal error occurred and a description of the error. Do not release *pError*; DO releases the interface when the [**JobError**](delivery_optimization-ibackgroundcopycallback_joberror) method returns.

</dd> </dl>

## Return value

This method should return **S\_OK**; otherwise, DO continues to call this method until **S\_OK** is returned. For performance reasons, you should limit the number of times you return a value other than **S\_OK** to a few times. As an alternative to returning an error code, consider always returning **S\_OK** and handling the error internally. The interval at which this method is called is arbitrary.

## Remarks

After you determine the cause of the error, perform one of the following options:

-   To cancel the job, call the [**IBackgroundCopyJob::Cancel**](ibackgroundcopyjob-cancel.md) method.
-   To accept the portion of the job that transferred successfully before the error occurred, call the [**IBackgroundCopyJob::Complete**](ibackgroundcopyjob-complete.md) method. This option does not apply to upload jobs; you cannot complete a portion of an upload job.
-   To finish processing the job, fix the problem, and then call the [**IBackgroundCopyJob::Resume**](ibackgroundcopyjob-resume.md) method.

Transient errors do not generate calls to the [**JobError**](delivery_optimization-ibackgroundcopycallback_joberror) method.

DO returns BG\_ERROR\_CONTEXT\_REMOTE\_FILE if the job hit a HTTP 403 error, BG\_ERROR\_CONTEXT\_NONE otherwise.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID\_IBackgroundCopyCallback is defined as 97EA99C7-0186-4AD4-8DF9-C5B4E0ED6B22<br/>          |



## See also

<dl> <dt>

[**IBackgroundCopyCallback**](ibackgroundcopycallback.md)
</dt> <dt>

[**IBackgroundCopyError**](ibackgroundcopyerror.md)
</dt> <dt>

[**IBackgroundCopyJob**](ibackgroundcopyjob-.md)
</dt> <dt>

[**IBackgroundCopyJob::Cancel**](ibackgroundcopyjob-cancel.md)
</dt> <dt>

[**IBackgroundCopyJob::Resume**](ibackgroundcopyjob-resume.md)
</dt> </dl>

 

 





