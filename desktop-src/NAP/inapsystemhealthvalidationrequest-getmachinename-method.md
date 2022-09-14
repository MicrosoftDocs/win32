---
title: INapSystemHealthValidationRequest GetMachineName method (NapSystemHealthValidator.h)
description: Is used by System Health Validators (SHVs) to retrieve the machine name of the NAP client. The SHV then logs this information.
ms.assetid: 2ea6a65d-1579-4a05-b5bc-aebf6421e46a
keywords:
- GetMachineName method NAP
- GetMachineName method NAP , INapSystemHealthValidationRequest interface
- INapSystemHealthValidationRequest interface NAP , GetMachineName method
topic_type:
- apiref
api_name:
- INapSystemHealthValidationRequest.GetMachineName
api_location:
- qshvhost.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthValidationRequest::GetMachineName method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthValidationRequest::GetMachineName** method is used by System Health Validators (SHVs) to retrieve the machine name of the NAP client. The SHV then logs this information.

## Syntax


```C++
HRESULT GetMachineName(
  [out] CountedString **machineName
);
```



## Parameters

<dl> <dt>

*machineName* \[out\]
</dt> <dd>

A pointer to a pointer to a [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) structure that contains the machine name of the NAP client.

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

 

 





