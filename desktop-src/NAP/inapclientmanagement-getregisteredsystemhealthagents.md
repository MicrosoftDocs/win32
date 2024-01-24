---
title: INapClientManagement GetRegisteredSystemHealthAgents method (NapManagement.h)
description: Retrieves information about the registered SHAs.
ms.assetid: c38d2d23-62d4-49f0-81a3-52394866f0c4
keywords:
- GetRegisteredSystemHealthAgents method NAP
- GetRegisteredSystemHealthAgents method NAP , INapClientManagement interface
- INapClientManagement interface NAP , GetRegisteredSystemHealthAgents method
topic_type:
- apiref
api_name:
- INapClientManagement.GetRegisteredSystemHealthAgents
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapClientManagement::GetRegisteredSystemHealthAgents method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **GetRegisteredSystemHealthAgents** method retrieves information about the registered SHAs.

## Syntax


```C++
HRESULT GetRegisteredSystemHealthAgents(
  [out] SystemHealthEntityCount      *count,
  [out] NapComponentRegistrationInfo **agents
) const;
```



## Parameters

<dl> <dt>

*count* \[out\]
</dt> <dd>

A pointer to a [**SystemHealthEntityCount**](nap-datatypes.md) that describes the number of registered SHAs.

</dd> <dt>

*agents* \[out\]
</dt> <dd>

A pointer to an array of [**NapComponentRegistrationInfo**](/windows/win32/api/naptypes/ns-naptypes-napcomponentregistrationinfo) structures that describe the registered SHAs.

</dd> </dl>

## Return value

The method returns an HRESULT status code including but not limited to one of the following.



| Return code                                                                                         | Description                                                        |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                | Operation successful.<br/>                                   |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>      | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>       | System resource limit, could not perform the operation.<br/> |
| <dl> <dt>**RPC\_E\_DISCONNECTED**</dt> </dl> | The NapAgent is not running.<br/>                            |



 

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

 

 





