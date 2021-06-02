---
title: INapServerManagement RegisterSystemHealthValidator method (NapServerManagement.h)
description: Registers an SHV.
ms.assetid: 23f147d5-3c4e-48ca-940a-c4350ad6ecb3
keywords:
- RegisterSystemHealthValidator method NAP
- RegisterSystemHealthValidator method NAP , INapServerManagement interface
- INapServerManagement interface NAP , RegisterSystemHealthValidator method
topic_type:
- apiref
api_name:
- INapServerManagement.RegisterSystemHealthValidator
api_location:
- qsvrmgmt.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapServerManagement::RegisterSystemHealthValidator method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapServerManagement::RegisterSystemHealthValidator** method registers an SHV.

## Syntax


```C++
HRESULT RegisterSystemHealthValidator(
  [in] const NapComponentRegistrationInfo *validator,
  [in] const CLSID                        *validatorClsid
);
```



## Parameters

<dl> <dt>

*validator* \[in\]
</dt> <dd>

A pointer to a [**NapComponentRegistrationInfo**](/windows/win32/api/naptypes/ns-naptypes-napcomponentregistrationinfo) structure that contains the SHV registration information.

</dd> <dt>

*validatorClsid* \[in\]
</dt> <dd>

A pointer to the CLSID of the COM class that implements the [**INapSystemHealthValidator**](inapsystemhealthvalidator.md) interface.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                            | Description                                                        |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                  | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl>        | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>         | System resource limit, could not perform the operation.<br/> |
| <dl> <dt>**NAP\_E\_CONFLICTING\_ID**</dt> </dl> | SHV id is already registered.<br/>                           |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                               |
| Header<br/>                   | <dl> <dt>NapServerManagement.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapServerManagement.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qsvrmgmt.dll</dt> </dl>            |



## See also

<dl> <dt>

[**INapServerManagement**](inapservermanagement.md)
</dt> </dl>

 

 





