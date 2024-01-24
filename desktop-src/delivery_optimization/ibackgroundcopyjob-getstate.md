---
title: IBackgroundCopyJob GetState method (Deliveryoptimization.h)
description: Retrieves the state of the job.
ms.assetid: 975AF0FB-37AE-4CE8-9EC1-35A972E422D8
keywords:
- GetState method
- GetState method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, GetState method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.GetState
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::GetState method

Retrieves the state of the job.

## Syntax


```C++
HRESULT GetState(
  [out] BG_JOB_STATE *pJobState
);
```



## Parameters

<dl> <dt>

*pJobState* \[out\]
</dt> <dd>

The state of the job. For example, the state reflects whether the job is in error, transferring data, or suspended. For a list of job states, see the [**BG_JOB_STATE**](bg-job-state-.md) enumeration.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                              | Description                                                 |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl> | The state of the job was successfully retrieved.<br/> |



 

## Remarks

If you want to know when a job is in error or has transferred all the files in the job, you can use this method to poll for the state of the job or you can register to receive notification when events occur. For details on registering to receive event notification, see the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface.

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

[**BG_JOB_STATE**](bg-job-state-.md)
</dt> <dt>

[**IBackgroundCopyCallback**](ibackgroundcopycallback.md)
</dt> </dl>

 

 





