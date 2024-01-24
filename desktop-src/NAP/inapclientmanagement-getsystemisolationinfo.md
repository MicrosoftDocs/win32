---
title: INapClientManagement GetSystemIsolationInfo method (NapManagement.h)
description: Retrieves information about the isolation state of the NapClient.
ms.assetid: e1f69e66-71ca-402e-9c94-8af159d00b21
keywords:
- GetSystemIsolationInfo method NAP
- GetSystemIsolationInfo method NAP , INapClientManagement interface
- INapClientManagement interface NAP , GetSystemIsolationInfo method
topic_type:
- apiref
api_name:
- INapClientManagement.GetSystemIsolationInfo
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapClientManagement::GetSystemIsolationInfo method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **GetSystemIsolationInfo** method retrieves information about the isolation state of the NapClient.

## Syntax


```C++
HRESULT GetSystemIsolationInfo(
  [out] IsolationInfo **isolationInfo,
  [out] BOOL          *unknownConnections
) const;
```



## Parameters

<dl> <dt>

*isolationInfo* \[out\]
</dt> <dd>

A pointer to a pointer to an [**IsolationInfo**](/windows/win32/api/naptypes/ns-naptypes-isolationinfo) structure that contains isolation state information.

</dd> <dt>

*unknownConnections* \[out\]
</dt> <dd>

A pointer to a flag that indicates whether any of the connections are in an unknown state. If any of them are, the flag is set to **TRUE**; otherwise the flag is set to **FALSE**.

</dd> </dl>

## Return value

The method returns an HRESULT status code including but not limited to one of the following.



| Return code                                                                                         | Description                                                        |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                | Operation successful.<br/>                                   |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>      | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>       | System resource limit, could not perform the operation.<br/> |
| <dl> <dt>**RPC\_E\_DISCONNECTED**</dt> </dl> | The NapAgent is not running.<br/>                            |



 

## Remarks

The isolation information that is retrieved does not reflect unknown states.

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

 

 





