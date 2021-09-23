---
title: IBackgroundCopyCallback JobTransferred method (Deliveryoptimization.h)
description: Delivery Optimization calls your implementation of the JobTransferred method when all of the files in the job have been successfully transferred.
ms.assetid: D3088279-2D26-4707-9BA2-19D2758EA1CC
keywords:
- JobTransferred method
- JobTransferred method, IBackgroundCopyCallback interface
- IBackgroundCopyCallback interface, JobTransferred method
topic_type:
- apiref
api_name:
- IBackgroundCopyCallback.JobTransferred
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyCallback::JobTransferred method

Delivery Optimization calls your implementation of the **JobTransferred** method when all of the files in the job have been successfully transferred.

## Syntax


```C++
HRESULT JobTransferred(
  [in] IBackgroundCopyJob *pJob
);
```



## Parameters

<dl> <dt>

*pJob* \[in\]
</dt> <dd>

Contains job-related information, such as the time the job completed, the number of bytes transferred, and the number of files transferred. Do not release *pJob*; Delivery Optimization releases the interface when the method returns.

</dd> </dl>

## Return value

This method should return S_OK.

## Remarks

Typically, your implementation should call the [**IBackgroundCopyJob::Complete**](ibackgroundcopyjob-complete.md) method to acknowledge that Delivery Optimization successfully transferred the files. Download files and the reply file are not available on the client until you call the **Complete** method.

If you do not call the [**Complete**](ibackgroundcopyjob-complete.md) method or the [**IBackgroundCopyJob::Cancel**](ibackgroundcopyjob-cancel.md) method Delivery Optimization cancels the job after 30 days and deletes the incomplete files.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyCallback is defined as 97EA99C7-0186-4AD4-8DF9-C5B4E0ED6B22<br/>          |



## See also

<dl> <dt>

[**IBackgroundCopyCallback**](ibackgroundcopycallback.md)
</dt> <dt>

[**IBackgroundCopyJob**](ibackgroundcopyjob-.md)
</dt> <dt>

[**IBackgroundCopyJob::Complete**](ibackgroundcopyjob-complete.md)
</dt> <dt>

[**IBackgroundCopyJob::Cancel**](ibackgroundcopyjob-cancel.md)
</dt> </dl>

 

 





