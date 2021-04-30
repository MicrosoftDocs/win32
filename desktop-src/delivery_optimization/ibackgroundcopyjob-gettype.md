---
title: IBackgroundCopyJob GetType method (Deliveryoptimization.h)
description: Retrieves the type of transfer being performed, such as a file download or upload.
ms.assetid: F543A601-9385-4A73-A4E2-DE61433E84D3
keywords:
- GetType method
- GetType method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, GetType method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.GetType
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::GetType method

Retrieves the type of transfer being performed, such as a file download or upload.

## Syntax


```C++
HRESULT GetType(
  [out] BG_JOB_TYPE *pJobType
);
```



## Parameters

<dl> <dt>

*pJobType* \[out\]
</dt> <dd>

Type of transfer being performed. For a list of transfer types, see the [**BG_JOB_TYPE**](bg-job-type.md) enumeration.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                              | Description                                          |
|------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl> | Transfer type was successfully retrieved.<br/> |



 

## Remarks

Specify the type of transfer when you create the job.

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

[**BG_JOB_TYPE**](bg-job-type.md)
</dt> <dt>

[**IBackgroundCopyManager::CreateJob**](ibackgroundcopymanager-createjob.md)
</dt> </dl>

 

 





