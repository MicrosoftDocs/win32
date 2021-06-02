---
title: INapSystemHealthValidationRequest SetSoHResponse method (NapSystemHealthValidator.h)
description: Allows System Health Validators (SHVs) to set the SoHResponse to be sent to its System Health Agent (SHA) counterpart on the client-side.
ms.assetid: 250b90ac-ce8f-4771-9d20-84c491adfb2c
keywords:
- SetSoHResponse method NAP
- SetSoHResponse method NAP , INapSystemHealthValidationRequest interface
- INapSystemHealthValidationRequest interface NAP , SetSoHResponse method
topic_type:
- apiref
api_name:
- INapSystemHealthValidationRequest.SetSoHResponse
api_location:
- qshvhost.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthValidationRequest::SetSoHResponse method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthValidationRequest::SetSoHResponse** method allows System Health Validators (SHVs) to set the [**SoHResponse**](/windows/win32/api/naptypes/ns-naptypes-soh) to be sent to its System Health Agent (SHA) counterpart on the client-side.

## Syntax


```C++
HRESULT SetSoHResponse(
  [in] const SoHResponse *sohResponse
);
```



## Parameters

<dl> <dt>

*sohResponse* \[in\]
</dt> <dd>

A pointer to a [**SoHResponse**](/windows/win32/api/naptypes/ns-naptypes-soh) structure.

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

 

 





