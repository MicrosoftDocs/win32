---
title: INapClientManagement UnregisterEnforcementClient method (NapManagement.h)
description: Unregisters an enforcement client with the NAP system.
ms.assetid: 549683de-7f2c-4da6-9616-862e0e99d21f
keywords:
- UnregisterEnforcementClient method NAP
- UnregisterEnforcementClient method NAP , INapClientManagement interface
- INapClientManagement interface NAP , UnregisterEnforcementClient method
topic_type:
- apiref
api_name:
- INapClientManagement.UnregisterEnforcementClient
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapClientManagement::UnregisterEnforcementClient method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **UnregisterEnforcementClient** method unregisters an enforcement client with the NAP system.

## Syntax


```C++
HRESULT UnregisterEnforcementClient(
  [in] EnforcementEntityId id
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

An [**EnforcementEntityId**](nap-datatypes.md) value that identifies the enforcement client to unregister.

</dd> </dl>

## Return value

The method returns an HRESULT status code including but not limited to one of the following.



| Return code                                                                                         | Description                                                                    |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                | Operation successful.<br/>                                               |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>      | Permissions error, access denied.<br/>                                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>       | System resource limit, could not perform the operation.<br/>             |
| <dl> <dt>**NAP\_E\_STILL\_BOUND**</dt> </dl> | The enforcement client could not be unregistered and remains bound.<br/> |



 

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

 

 





