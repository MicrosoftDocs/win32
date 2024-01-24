---
title: IBackgroundCopyFile2 SetRemoteName method (Deliveryoptimization.h)
description: Changes the remote name to a new URL in a download job.
ms.assetid: 344D4193-C96E-4B94-AA53-F9307FEB2565
keywords:
- SetRemoteName method
- SetRemoteName method, IBackgroundCopyFile2 interface
- IBackgroundCopyFile2 interface, SetRemoteName method
topic_type:
- apiref
api_name:
- IBackgroundCopyFile2.SetRemoteName
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyFile2::SetRemoteName method

Changes the remote name to a new URL in a download job.

## Syntax


```C++
HRESULT SetRemoteName(
  [in] LPCWSTR RemoteName
);
```



## Parameters

<dl> <dt>

*RemoteName* \[in\]
</dt> <dd>

Null-terminated string that contains the name of the file on the server. For information on specifying the remote name, see the **RemoteName** member.

</dd> </dl>

## Return value

This method returns the following return values, as well as others.



| Return code                                                                                  | Description                                                                                                           |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl>     | Success<br/>                                                                                                    |
| <dl> <dt>**E_INVALIDARG**</dt> </dl> | The new remote name is an invalid URL or the new URL is too long (the URL cannot exceed 2,200 characters).<br/> |



 

## Remarks

Typically, you call this method if you want to change the URL used to transfer the file or if you want to change the file name or path.

This method does not serialize when it returns. To serialize the change, [**suspend**](ibackgroundcopyjob-suspend.md) the job, call this method (if changing multiple files in the job, use a loop), and [**resume**](ibackgroundcopyjob-resume.md) the job. Calling the **IBackgroundCopyJob::Resume** method serializes the change.

If the time stamp or file size of the new remote name is different from the previous remote name or the new server does not support checkpoint resume (for HTTP remote names), Delivery Optimization restarts the download. Otherwise, the transfer resumes from the same position on the new server. Delivery Optimization does not restart already transferred files.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyFile2 is defined as 83e81b93-0873-474d-8a8c-f2018b1a939c<br/>             |



## See also

<dl> <dt>

[**IBackgroundCopyFile2**](ibackgroundcopyfile2.md)
</dt> </dl>

 

 





