---
title: IBackgroundCopyError GetFile method (Deliveryoptimization.h)
description: Retrieves an interface pointer to the file object associated with the error.
ms.assetid: 7E1DB3EE-0690-4D0E-BA98-70F5FBDCF12F
keywords:
- GetFile method
- GetFile method, IBackgroundCopyError interface
- IBackgroundCopyError interface, GetFile method
topic_type:
- apiref
api_name:
- IBackgroundCopyError.GetFile
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyError::GetFile method

Retrieves an interface pointer to the file object associated with the error.

## Syntax


```C++
HRESULT GetFile(
  [out] IBackgroundCopyFile **ppFile
);
```



## Parameters

<dl> <dt>

*ppFile* \[out\]
</dt> <dd>

An [**IBackgroundCopyFile**](ibackgroundcopyfile.md) interface pointer whose methods you use to determine the local and remote file names associated with the error. The *ppFile* parameter is set to **NULL** if the error is not associated with the local or remote file. When done, release *ppFile*.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values.



| Return code                                                                                                | Description                                                                                                    |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl>                   | Successfully retrieved an interface pointer to the file object.<br/>                                     |
| <dl> <dt>**DO_E_FILE_NOT_AVAILABLE**</dt> </dl> | The error is not associated with a local or remote file. The *ppFile* parameter is set to **NULL**.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyError is defined as 19C613A0-FCB8-4F28-81AE-897C3D078F81<br/>             |



## See also

<dl> <dt>

[**IBackgroundCopyError**](ibackgroundcopyerror.md)
</dt> <dt>

[**IBackgroundCopyError::GetError**](ibackgroundcopyerror-geterror-method.md)
</dt> </dl>

 

 





