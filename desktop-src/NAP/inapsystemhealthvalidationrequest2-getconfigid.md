---
title: INapSystemHealthValidationRequest2 GetConfigID method (NapSystemHealthValidator.h)
description: Used by the System Health Validators (SHVs) to retrieve the configuration ID in a validation request.
ms.assetid: 6d5564e4-8386-444b-a859-f0c855e4ee30
keywords:
- GetConfigID method NAP
- GetConfigID method NAP , INapSystemHealthValidationRequest2 interface
- INapSystemHealthValidationRequest2 interface NAP , GetConfigID method
topic_type:
- apiref
api_name:
- INapSystemHealthValidationRequest2.GetConfigID
api_location:
- qshvhost.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthValidationRequest2::GetConfigID method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthValidationRequest2::GetConfigId** method is used by the System Health Validators (SHVs) to retrieve the configuration ID in a validation request.

## Syntax


```C++
HRESULT GetConfigID(
  [out] UINT32 *configID
) const;
```



## Parameters

<dl> <dt>

*configID* \[out\]
</dt> <dd>

On return, a pointer to UINT32 that contains a configuration ID of the SHV.

</dd> </dl>

## Return value

Returns one of the following error codes based on the result of this operation.



| Return code                                                                                  | Description                                     |
|----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Operation successful.<br/>                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The configID parameter was **NULL**.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>NapSystemHealthValidator.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthValidator.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qshvhost.dll</dt> </dl>                 |



## See also

<dl> <dt>

[**INapSystemHealthValidationRequest2**](inapsystemhealthvalidationrequest2.md)
</dt> </dl>

 

 





