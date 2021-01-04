---
title: IBackgroundCopyJob GetNotifyInterface method (Deliveryoptimization.h)
description: Retrieves the interface pointer to your implementation of the IBackgroundCopyCallback interface.
ms.assetid: 1AA50C03-AC84-4AA9-8EC3-3FBA865C70C0
keywords:
- GetNotifyInterface method
- GetNotifyInterface method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, GetNotifyInterface method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.GetNotifyInterface
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::GetNotifyInterface method

Retrieves the interface pointer to your implementation of the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface.

## Syntax


```C++
HRESULT GetNotifyInterface(
  [out] IUnknown **ppNotifyInterface
);
```



## Parameters

<dl> <dt>

*ppNotifyInterface* \[out\]
</dt> <dd>

Interface pointer to your implementation of the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface. When done, release *ppNotifyInterface*.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                              | Description                                                           |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl> | Notification interface pointer was successfully retrieved.<br/> |



 

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

[**IBackgroundCopyJob::GetNotifyFlags**](ibackgroundcopyjob-getnotifyflags.md)
</dt> <dt>

[**IBackgroundCopyJob::SetNotifyInterface**](ibackgroundcopyjob-setnotifyinterface.md)
</dt> </dl>

 

 





