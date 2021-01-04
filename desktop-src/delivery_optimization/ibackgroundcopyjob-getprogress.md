---
title: IBackgroundCopyJob GetProgress method (Deliveryoptimization.h)
description: Retrieves job-related progress information, such as the number of bytes and files transferred.
ms.assetid: E23C82E1-3805-4C5D-9F18-0DA17F7C473E
keywords:
- GetProgress method
- GetProgress method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, GetProgress method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.GetProgress
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::GetProgress method

Retrieves job-related progress information, such as the number of bytes and files transferred.

## Syntax


```C++
HRESULT GetProgress(
  [out] BG_JOB_PROGRESS *pProgress
);
```



## Parameters

<dl> <dt>

*pProgress* \[out\]
</dt> <dd>

Contains data that you can use to calculate the percentage of the job that is complete.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                              | Description                                                 |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl> | Progress information was successfully retrieved.<br/> |



 

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
</dt> </dl>

 

 





