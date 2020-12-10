---
title: IBackgroundCopyJob EnumFiles method (Deliveryoptimization.h)
description: Retrieves an IEnumBackgroundCopyFiles interface pointer that you use to enumerate the files in a job.
ms.assetid: 94FA5D7B-08C1-497E-9813-571D35AE3BCF
keywords:
- EnumFiles method
- EnumFiles method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, EnumFiles method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.EnumFiles
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::EnumFiles method

Retrieves an [**IEnumBackgroundCopyFiles**](ienumbackgroundcopyfiles-.md) interface pointer that you use to enumerate the files in a job.

## Syntax


```C++
HRESULT EnumFiles(
  [out] IEnumBackgroundCopyFiles **ppEnumFiles
);
```



## Parameters

<dl> <dt>

*ppEnumFiles* \[out\]
</dt> <dd>

[**IEnumBackgroundCopyFiles**](ienumbackgroundcopyfiles-.md) interface pointer that you use to enumerate the files in the job. Release *ppEnumFiles* when done.

</dd> </dl>

## Return value

This method returns **S_OK** on success or one of the standard COM **HRESULT** values on error.

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

[**IEnumBackgroundCopyFiles**](ienumbackgroundcopyfiles-.md)
</dt> </dl>

 

 





