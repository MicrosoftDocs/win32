---
title: INapServerInfo GetRegisteredSystemHealthValidators method (NapServerManagement.h)
description: Retrieves a list of registered SHVs.
ms.assetid: 029c7d5c-b397-415c-a530-0096de1ef771
keywords:
- GetRegisteredSystemHealthValidators method NAP
- GetRegisteredSystemHealthValidators method NAP , INapServerInfo interface
- INapServerInfo interface NAP , GetRegisteredSystemHealthValidators method
topic_type:
- apiref
api_name:
- INapServerInfo.GetRegisteredSystemHealthValidators
api_location:
- qsvrmgmt.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapServerInfo::GetRegisteredSystemHealthValidators method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapServerInfo::GetRegisteredSystemHealthValidators** method retrieves a list of registered SHVs.

## Syntax


```C++
HRESULT GetRegisteredSystemHealthValidators(
  [out] SystemHealthEntityCount      *count,
  [out] NapComponentRegistrationInfo **validators,
  [out] CLSID                        **validatorClsids
);
```



## Parameters

<dl> <dt>

*count* \[out\]
</dt> <dd>

A pointer to a [**SystemHealthEntityCount**](nap-type-constants.md) that contains the number of registered SHVs.

</dd> <dt>

*validators* \[out\]
</dt> <dd>

A pointer to a pointer to a [**NapComponentRegistrationInfo**](/windows/win32/api/naptypes/ns-naptypes-napcomponentregistrationinfo) structure that contains the SHV registration information.

</dd> <dt>

*validatorClsids* \[out\]
</dt> <dd>

Pointer to an array of IDs for the registered SHVs.

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
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                               |
| Header<br/>                   | <dl> <dt>NapServerManagement.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapServerManagement.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qsvrmgmt.dll</dt> </dl>            |



## See also

<dl> <dt>

[**NapComponentRegistrationInfo**](/windows/win32/api/naptypes/ns-naptypes-napcomponentregistrationinfo)
</dt> <dt>

[**INapServerInfo**](inapserverinfo.md)
</dt> </dl>

 

 





