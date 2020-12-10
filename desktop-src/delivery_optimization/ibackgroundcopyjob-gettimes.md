---
title: IBackgroundCopyJob GetTimes method (Deliveryoptimization.h)
description: Retrieves job-related time stamps, such as the time that the job was created or last modified.
ms.assetid: 9002FB8D-08CB-4878-980F-15FE0DC952A6
keywords:
- GetTimes method
- GetTimes method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, GetTimes method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.GetTimes
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::GetTimes method

Retrieves job-related time stamps, such as the time that the job was created or last modified.

## Syntax


```C++
HRESULT GetTimes(
  [out] BG_JOB_TIMES *pTimes
);
```



## Parameters

<dl> <dt>

*pTimes* \[out\]
</dt> <dd>

Contains job-related time stamps. For available time stamps, see the [**BG_JOB_TIMES**](bg-job-times.md) structure.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                              | Description                                         |
|------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl> | Time stamps were successfully retrieved.<br/> |



 

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

[**BG_JOB_TIMES**](bg-job-times.md)
</dt> </dl>

 

 





