---
title: IBackgroundCopyJob Cancel method
description: Deletes the job from the transfer queue and removes related temporary files from the client (downloads) and server (uploads).
ms.assetid: 'DC502DC2-1335-476F-A1B8-FDB6BA595FF1'
keywords: ["Cancel method", "Cancel method, IBackgroundCopyJob interface", "IBackgroundCopyJob interface, Cancel method"]
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.Cancel
api_location:
- dosvc.dll
api_type:
- COM
---

# IBackgroundCopyJob::Cancel method

Deletes the job from the transfer queue and removes related temporary files from the client (downloads) and server (uploads).

## Syntax


```C++
HRESULT Cancel();
```



## Parameters

This method has no parameters.

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                                          | Description                                                                                              |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| <dl> <dt>****S\_OK****</dt> </dl>             | Job was successfully canceled.<br/>                                                                |
| <dl> <dt>**DO\_E\_INVALID\_STATE**</dt> </dl> | Cannot cancel a job whose state is BG\_JOB\_STATE\_CANCELLED or BG\_JOB\_STATE\_ACKNOWLEDGED.<br/> |



 

## Remarks

You can cancel a job at any time; however, the job cannot be recovered after it is canceled.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
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

[**IBackgroundCopyJob::Complete**](ibackgroundcopyjob-complete.md)
</dt> <dt>

[**IBackgroundCopyJob::Resume**](ibackgroundcopyjob-resume.md)
</dt> <dt>

[**IBackgroundCopyJob::Suspend**](ibackgroundcopyjob-suspend.md)
</dt> </dl>

 

 





