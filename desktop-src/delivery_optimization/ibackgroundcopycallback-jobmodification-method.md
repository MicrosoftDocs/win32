---
title: IBackgroundCopyCallback JobModification method (Deliveryoptimization.h)
description: Delivery Optimization calls your implementation of the JobModification method when the job has been modified.
ms.assetid: 4AC2575F-57FB-45E6-B29C-12DF615237F3
keywords:
- JobModification method
- JobModification method, IBackgroundCopyCallback interface
- IBackgroundCopyCallback interface, JobModification method
topic_type:
- apiref
api_name:
- IBackgroundCopyCallback.JobModification
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyCallback::JobModification method

Delivery Optimization calls your implementation of the [**JobModification**](https://www.bing.com/search?q=**JobModification**) method when the job has been modified. The service generates this event when bytes are transferred, files have been added to the job, properties have been modified, or the state of the job has changed.

## Syntax


```C++
HRESULT JobModification(
  [in] IBackgroundCopyJob *pJob,
  [in] DWORD              dwReserved
);
```



## Parameters

<dl> <dt>

*pJob* \[in\]
</dt> <dd>

Contains the methods for accessing property, progress, and state information of the job. Do not release *pJob*; Delivery Optimization releases the interface when the [**JobModification**](https://www.bing.com/search?q=**JobModification**) method returns.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Return value

This method should return S_OK.

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
</dt> </dl>

 

 





