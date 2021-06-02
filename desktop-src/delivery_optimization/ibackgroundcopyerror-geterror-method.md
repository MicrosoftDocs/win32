---
title: IBackgroundCopyError GetError method (Deliveryoptimization.h)
description: Retrieves the error code and identify the context in which the error occurred.
ms.assetid: C87897CD-9648-4CEF-B963-68EE35356929
keywords:
- GetError method
- GetError method, IBackgroundCopyError interface
- IBackgroundCopyError interface, GetError method
topic_type:
- apiref
api_name:
- IBackgroundCopyError.GetError
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyError::GetError method

Retrieves the error code and identify the context in which the error occurred.

## Syntax


```C++
HRESULT GetError(
  [out] BG_ERROR_CONTEXT *pContext,
  [out] HRESULT          *pErrorCode
);
```



## Parameters

<dl> <dt>

*pContext* \[out\]
</dt> <dd>

Context in which the error occurred. For a list of context values, see the [**BG_ERROR_CONTEXT**](bg-error-context.md) enumeration.

</dd> <dt>

*pErrorCode* \[out\]
</dt> <dd>

Error code of the error that occurred.

</dd> </dl>

## Return value

This method returns **S_OK** on success or one of the standard COM HRESULT values on error.

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

[**IBackgroundCopyError::GetFile**](ibackgroundcopyerror-getfile-method.md)
</dt> </dl>

 

 





