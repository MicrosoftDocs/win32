---
title: INapSystemHealthValidationRequest GetStringCorrelationId method (NapSystemHealthValidator.h)
description: Is used by System Health Validators (SHVs) which must log this information.
ms.assetid: c3e45857-463b-4048-a178-ec26a318b63b
keywords:
- GetStringCorrelationId method NAP
- GetStringCorrelationId method NAP , INapSystemHealthValidationRequest interface
- INapSystemHealthValidationRequest interface NAP , GetStringCorrelationId method
topic_type:
- apiref
api_name:
- INapSystemHealthValidationRequest.GetStringCorrelationId
api_location:
- qshvhost.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthValidationRequest::GetStringCorrelationId method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthValidationRequest::GetStringCorrelationId** method is used by System Health Validators (SHVs) which must log this information.

## Syntax


```C++
HRESULT GetStringCorrelationId(
  [out] StringCorrelationId **correlationId
);
```



## Parameters

<dl> <dt>

*correlationId* \[out\]
</dt> <dd>

A pointer to a pointer to a unique [**StringCorrelationId**](nap-type-constants.md) for the SoH exchange.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

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

[**INapSystemHealthValidationRequest**](inapsystemhealthvalidationrequest.md)
</dt> </dl>

 

 





