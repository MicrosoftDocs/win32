---
title: IBackgroundCopyJob GetError method
description: Retrieves the error interface after an error occurs.
ms.assetid: 66891557-C118-4C66-AEFC-D8FD70976B9A
keywords:
- GetError method
- GetError method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, GetError method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.GetError
api_location:
- dosvc.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IBackgroundCopyJob::GetError method

Retrieves the error interface after an error occurs.

Delivery Optimization (DO) generates an error object when the state of the job is BG\_JOB\_STATE\_ERROR or BG\_JOB\_STATE\_TRANSIENT\_ERROR. The service does not create an error object when a call to an **IBackgroundCopyXXXX** interface method fails. The error object is available until DO begins transferring data (the state of the job changes to BG\_JOB\_STATE\_TRANSFERRING) for the job or until your application exits.

## Syntax


```C++
HRESULT GetError(
  [out] IBackgroundCopyError **ppError
);
```



## Parameters

<dl> <dt>

*ppError* \[out\]
</dt> <dd>

Error interface that provides the error code, a description of the error, and the context in which the error occurred. This parameter also identifies the file being transferred at the time the error occurred. Release *ppError* when done.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                                                           | Description                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>****S\_OK****</dt> </dl>                              | Successfully generated the error object.<br/>                                                                                                                                                       |
| <dl> <dt>**DO\_E\_ERROR\_INFORMATION\_UNAVAILABLE**</dt> </dl> | The error interface is available only after an error occurs (BG\_JOB\_STATE\_ERROR or BG\_JOB\_STATE\_TRANSIENT\_ERROR) and before DO begins transferring data (BG\_JOB\_STATE\_TRANSFERRING).<br/> |



 

## Remarks

The job is placed in an error state on fatal errors. Use one of the following options to determine if the job is in error:

-   To poll for the state of the job, call the [**IBackgroundCopyJob::GetState**](ibackgroundcopyjob-getstate.md) method. The job is in error if the state is BG\_JOB\_STATE\_ERROR.
-   To receive notification when an error occurs, implement the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface (specifically, the [**JobError**](https://www.bing.com/search?q=**JobError**) method). Then, call the [**IBackgroundCopyJob::SetNotifyInterface**](ibackgroundcopyjob-setnotifyinterface.md) method to register the callback and the [**IBackgroundCopyJob::SetNotifyFlags**](ibackgroundcopyjob-setnotifyflags.md) method to set the BG\_NOTIFY\_JOB\_ERROR flag.

The [**IBackgroundCopyError**](ibackgroundcopyerror.md) interface contains information that you use to determine the cause of the error and if the transfer process can proceed. After you determine the cause of the error, perform one of the following options:

-   To cancel the job, call the [**IBackgroundCopyJob::Cancel**](ibackgroundcopyjob-cancel.md) method.
-   To save those files that transferred successfully before the error occurred, call the [**IBackgroundCopyJob::Complete**](ibackgroundcopyjob-complete.md) method.
-   To finish processing the job, fix the problem, and then call the [**IBackgroundCopyJob::Resume**](ibackgroundcopyjob-resume.md) method.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID\_IBackgroundCopyJob is defined as 37668D37-507E-4160-9316-26306D150B12<br/>               |



## See also

<dl> <dt>

[**IBackgroundCopyJob**](ibackgroundcopyjob-.md)
</dt> <dt>

[**IBackgroundCopyCallback::JobError**](ibackgroundcopycallback-joberror-method.md)
</dt> <dt>

[**IBackgroundCopyError**](ibackgroundcopyerror.md)
</dt> <dt>

[**IBackgroundCopyJob::GetState**](ibackgroundcopyjob-getstate.md)
</dt> </dl>

 

 





