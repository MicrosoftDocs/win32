---
title: IBackgroundCopyJob SetPriority method
description: Specifies the priority level of your job. The priority level determines when your job is processed relative to other jobs in the transfer queue.
ms.assetid: DC943093-CA1D-4840-B7AC-29710764D4E5
keywords:
- SetPriority method
- SetPriority method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, SetPriority method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.SetPriority
api_location:
- dosvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IBackgroundCopyJob::SetPriority method

Specifies the priority level of your job. The priority level determines when your job is processed relative to other jobs in the transfer queue.

## Syntax


```C++
HRESULT SetPriority(
  [in] BG_JOB_PRIORITY Priority
);
```



## Parameters

<dl> <dt>

*Priority* \[in\]
</dt> <dd>

Specifies the priority level of your job relative to other jobs in the transfer queue. The default is BG\_JOB\_PRIORITY\_NORMAL. For a list of priority levels, see the [**BG\_JOB\_PRIORITY**](bg-job-priority-.md) enumeration.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                              | Description                                   |
|------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>****S\_OK****</dt> </dl> | Job priority was successfully set.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID\_IBackgroundCopyJob is defined as 37668D37-507E-4160-9316-26306D150B12<br/>               |



## See also

<dl> <dt>

[**IBackgroundCopyJob**](ibackgroundcopyjob-.md)
</dt> <dt>

[**BG\_JOB\_PRIORITY**](bg-job-priority-.md)
</dt> <dt>

[**IBackgroundCopyJob::GetPriority**](ibackgroundcopyjob-getpriority.md)
</dt> </dl>

 

 





