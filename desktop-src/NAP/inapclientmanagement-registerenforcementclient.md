---
title: INapClientManagement RegisterEnforcementClient method (NapManagement.h)
description: Registers an enforcement client with the NAP system.
ms.assetid: 26ea45ea-a366-4162-91dc-06bcd0261c56
keywords:
- RegisterEnforcementClient method NAP
- RegisterEnforcementClient method NAP , INapClientManagement interface
- INapClientManagement interface NAP , RegisterEnforcementClient method
topic_type:
- apiref
api_name:
- INapClientManagement.RegisterEnforcementClient
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapClientManagement::RegisterEnforcementClient method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **RegisterEnforcementClient** method registers an enforcement client with the NAP system.

## Syntax


```C++
HRESULT RegisterEnforcementClient(
  [in] const NapComponentRegistrationInfo *enforcer
);
```



## Parameters

<dl> <dt>

*enforcer* \[in\]
</dt> <dd>

A pointer to a [**NapComponentRegistrationInfo**](/windows/win32/api/naptypes/ns-naptypes-napcomponentregistrationinfo) data structure that contains the registration information that is associated with the enforcement client.

</dd> </dl>

## Return value

The method returns an HRESULT status code including but not limited to one of the following.



| Return code                                                                                            | Description                                                                       |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | Operation successful.<br/>                                                  |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>         | Permissions error, access denied.<br/>                                      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>          | System resource limit, could not perform the operation.<br/>                |
| <dl> <dt>**NAP\_E\_CONFLICTING\_ID**</dt> </dl> | An enforcement agent using the given identifier is already registered.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>NapManagement.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapManagement.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qagent.dll</dt> </dl>        |



## See also

<dl> <dt>

[**INapClientManagement**](inapclientmanagement.md)
</dt> </dl>

 

 





