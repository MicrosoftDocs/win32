---
title: IBackgroundCopyJob GetPriority method (Deliveryoptimization.h)
description: Retrieves the priority level for the job. The priority level determines when the job is processed relative to other jobs in the transfer queue.
ms.assetid: 2F778B35-8DBB-4540-88C2-A2E18EBB0D89
keywords:
- GetPriority method
- GetPriority method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, GetPriority method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.GetPriority
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::GetPriority method

Retrieves the priority level for the job. The priority level determines when the job is processed relative to other jobs in the transfer queue.

## Syntax


```C++
HRESULT GetPriority(
  [out] BG_JOB_PRIORITY *pPriority
);
```



## Parameters

<dl> <dt>

*pPriority* \[out\]
</dt> <dd>

Priority of the job relative to other jobs in the transfer queue.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                              | Description                                           |
|------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl> | Priority level was successfully retrieved.<br/> |



 

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

[**IBackgroundCopyJob::SetPriority**](ibackgroundcopyjob-setpriority.md)
</dt> </dl>

 

 





