---
title: IBackgroundCopyJob GetNoProgressTimeout method (Deliveryoptimization.h)
description: Retrieves the length of time that the service tries to transfer the file after a transient error condition occurs. If there is progress, the timer is reset.
ms.assetid: 3C31A15B-62EF-4807-8EC3-78BAEA3E23AE
keywords:
- GetNoProgressTimeout method
- GetNoProgressTimeout method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, GetNoProgressTimeout method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.GetNoProgressTimeout
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::GetNoProgressTimeout method

Retrieves the length of time that the service tries to transfer the file after a transient error condition occurs. If there is progress, the timer is reset.

## Syntax


```C++
HRESULT GetNoProgressTimeout(
  [in] ULONG *pRetryPeriod
);
```



## Parameters

<dl> <dt>

*pRetryPeriod* \[in\]
</dt> <dd>

Length of time, in seconds, that the service tries to transfer the file after a transient error occurs.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                              | Description                                     |
|------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl> | Time-out was successfully retrieved.<br/> |



 

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

[**IBackgroundCopyJob::SetNoProgressTimeout**](ibackgroundcopyjob-setnoprogresstimeout.md)
</dt> </dl>

 

 





