---
title: INapClientManagement UnregisterSystemHealthAgent method (NapManagement.h)
description: Unregisters an SHA with the NAP system.
ms.assetid: c3ad6f2a-c39a-4590-8487-24c802433845
keywords:
- UnregisterSystemHealthAgent method NAP
- UnregisterSystemHealthAgent method NAP , INapClientManagement interface
- INapClientManagement interface NAP , UnregisterSystemHealthAgent method
topic_type:
- apiref
api_name:
- INapClientManagement.UnregisterSystemHealthAgent
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapClientManagement::UnregisterSystemHealthAgent method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **UnregisterSystemHealthAgent** method unregisters an SHA with the NAP system.

## Syntax


```C++
HRESULT UnregisterSystemHealthAgent(
  [in] SystemHealthEntityId id
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

A [**SystemHealthEntityId**](nap-datatypes.md) that identifies the System Health Agent to be unregistered.

</dd> </dl>

## Return value

The method returns an HRESULT status code including but not limited to one of the following.



| Return code                                                                                         | Description                                                        |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                | Operation successful.<br/>                                   |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>      | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>       | System resource limit, could not perform the operation.<br/> |
| <dl> <dt>**NAP\_E\_STILL\_BOUND**</dt> </dl> | The SHA remains bound and could not be unregistered.<br/>    |



 

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

 

 





