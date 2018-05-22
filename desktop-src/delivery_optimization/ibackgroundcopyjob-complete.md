---
title: IBackgroundCopyJob Complete method
description: Ends the job and saves the transferred files on the client.
ms.assetid: 'A3706DBA-C44E-4F7A-A787-62FB436706FC'
keywords: ["Complete method", "Complete method, IBackgroundCopyJob interface", "IBackgroundCopyJob interface, Complete method"]
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.Complete
api_location:
- dosvc.dll
api_type:
- COM
---

# IBackgroundCopyJob::Complete method

Ends the job and saves the transferred files on the client.

## Syntax


```C++
HRESULT Complete();
```



## Parameters

This method has no parameters.

## Return value

This method returns the following **HRESULT** values. The method can also return errors related to renaming the temporary copies of the transferred files to their given names.



| Return code                                                                                          | Description                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>****S\_OK****</dt> </dl>             | All files transferred successfully.<br/>                                                                                                                                                         |
| <dl> <dt>**DO\_E\_INVALID\_STATE**</dt> </dl> | For downloads, the state of the job cannot be BG\_JOB\_STATE\_CANCELLED or BG\_JOB\_STATE\_ACKNOWLEDGED. <br/> For uploads, the state of the job must be BG\_JOB\_STATE\_TRANSFERRED.<br/> |



 

## Remarks

All of the files have been successfully transferred if the job's state is **BG\_JOB\_STATE\_TRANSFERRED**. To check the state of the job, call the [**IBackgroundCopyJob::GetState**](ibackgroundcopyjob-getstate.md) method. You can also implement the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface to receive notification when all of the files have been transferred to the client.

DO retains jobs that are less than 30 days only. All older jobs will be removed. DO does not support the [JobInactivityTimeout](delivery_optimization-group_policies) Group Policy.

For download jobs, you can call the **Complete** method at anytime during the transfer process; however, only files that were successfully transferred to the client before calling this method are saved. For example, if you call the **Complete** method while DO is processing the third of five files, only the first two files are saved. To determine which files have been transferred, call the [**IBackgroundCopyFile::GetProgress**](ibackgroundcopyfile-getprogress-method.md) method and compare the **BytesTransferred** member to the **BytesTotal** member of the [**BG\_FILE\_PROGRESS**](bg-file-progress.md) structure.

For upload jobs, you can call the **Complete** method only when the job's state is **BG\_JOB\_STATE\_TRANSFERRED**.

The owner of the file is the user who made the call. For example, if an administrator completes someone else's job, the administrator—not the owner of the job—owns the file.

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

[**IBackgroundCopyJob::Cancel**](ibackgroundcopyjob-cancel.md)
</dt> <dt>

[**IBackgroundCopyJob::GetState**](ibackgroundcopyjob-getstate.md)
</dt> </dl>

 

 





