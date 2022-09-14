---
title: INapServerCallback OnComplete method (NapSystemHealthValidator.h)
description: Used by SHVs to signal asynchronous request completion.
ms.assetid: 959ee4ac-7c29-4013-a174-24abc6a580c7
keywords:
- OnComplete method NAP
- OnComplete method NAP , INapServerCallback interface
- INapServerCallback interface NAP , OnComplete method
topic_type:
- apiref
api_name:
- INapServerCallback.OnComplete
api_location:
- qshvhost.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapServerCallback::OnComplete method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapServerCallback::OnComplete** method is used by SHVs to signal asynchronous request completion.

## Syntax


```C++
HRESULT OnComplete(
  [in] INapSystemHealthValidationRequest *request,
  [in] HRESULT                           errorCode
);
```



## Parameters

<dl> <dt>

*request* \[in\]
</dt> <dd>

A pointer to an [**INapSystemHealthValidationRequest**](inapsystemhealthvalidationrequest.md) object that represents a validation request.

</dd> <dt>

*errorCode* \[in\]
</dt> <dd>

A [**NAP error code**](nap-error-constants.md) that indicates the reason why the validation could not be performed.

> [!Note]  
> Typically, the return value of the [**INapSystemHealthValidationRequest::SetSoHResponse**](inapsystemhealthvalidationrequest-setsohresponse-method.md) method is passed to this parameter. However, if **SetSoHResponse** could not be called due to a reprocessing failure, the value returned by the failed command is passed.

 

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

Validators must return S\_OK if the [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) validation could be completed, regardless of whether the **SoHRequest** passed the health check.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                    |
| Header<br/>                   | <dl> <dt>NapSystemHealthValidator.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthValidator.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qshvhost.dll</dt> </dl>                 |



## See also

<dl> <dt>


</dt> <dt>

[**INapServerCallback**](inapservercallback.md)
</dt> <dt>

[**INapSystemHealthValidationRequest**](inapsystemhealthvalidationrequest.md)
</dt> </dl>

 

 





