---
title: IBackgroundCopyJob SetNoProgressTimeout method (Deliveryoptimization.h)
description: Sets the length of time that Delivery Optimization tries to transfer the file after a transient error condition occurs. If there is progress, the timer is reset.
ms.assetid: DC86F74F-8429-4D78-B425-CAF19867B05E
keywords:
- SetNoProgressTimeout method
- SetNoProgressTimeout method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, SetNoProgressTimeout method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.SetNoProgressTimeout
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::SetNoProgressTimeout method

Sets the length of time that Delivery Optimization tries to transfer the file after a transient error condition occurs. If there is progress, the timer is reset.

## Syntax


```C++
HRESULT SetNoProgressTimeout(
  [in] ULONG RetryPeriod
);
```



## Parameters

<dl> <dt>

*RetryPeriod* \[in\]
</dt> <dd>

Length of time, in seconds, that Delivery Optimization tries to transfer the file after there has been no progress made. The default retry period for high priority job is 3600 seconds (1 hour) and for low priority job is 86400 seconds (24 hours).

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                                          | Description                                                                                          |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl>             | Retry period successfully set.<br/>                                                            |
| <dl> <dt>**DO_E_INVALID_STATE**</dt> </dl> | The state of the job cannot be BG_JOB_STATE_CANCELLED or BG_JOB_STATE_ACKNOWLEDGED.<br/> |



 

## Remarks

If Delivery Optimization does not make progress during the retry period, it moves the state of the job from BG_JOB_STATE_TRANSIENT_ERROR to BG_JOB_STATE_ERROR. If you request error notification, Delivery Optimization then calls your [**JobError**](https://www.bing.com/search?q=**JobError**) callback.

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

[**IBackgroundCopyJob::GetNoProgressTimeout**](ibackgroundcopyjob-getnoprogresstimeout.md)
</dt> </dl>

 

 





