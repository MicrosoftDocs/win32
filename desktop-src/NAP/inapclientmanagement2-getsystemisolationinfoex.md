---
title: INapClientManagement2 GetSystemIsolationInfoEx method (NapManagement.h)
description: Retrieves information about the isolation state and extended isolation state of the NapClient.
ms.assetid: 614bcf19-873e-4043-98b2-dcb152bae3e2
keywords:
- GetSystemIsolationInfoEx method NAP
- GetSystemIsolationInfoEx method NAP , INapClientManagement2 interface
- INapClientManagement2 interface NAP , GetSystemIsolationInfoEx method
topic_type:
- apiref
api_name:
- INapClientManagement2.GetSystemIsolationInfoEx
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapClientManagement2::GetSystemIsolationInfoEx method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **GetSystemIsolationInfoEx** method retrieves information about the isolation state and extended isolation state of the NapClient.

## Syntax


```C++
HRESULT GetSystemIsolationInfoEx(
  [out] IsolationInfoEx **isolationInfo,
  [out] BOOL            *unknownConnections
) const;
```



## Parameters

<dl> <dt>

*isolationInfo* \[out\]
</dt> <dd>

A pointer to a pointer to an [**IsolationInfoEx**](/windows/win32/api/naptypes/ns-naptypes-isolationinfoex) structure that contains isolation state information.

</dd> <dt>

*unknownConnections* \[out\]
</dt> <dd>

A pointer to a BOOL that is **TRUE** if any of the connections are in an unknown state and **FALSE** otherwise.

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

The SHA must free the [**IsolationInfoEx**](/windows/win32/api/naptypes/ns-naptypes-isolationinfoex) structure by calling [**FreeIsolationInfoEx**](freeisolationinfoex.md).

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

[**INapClientManagement2**](inapclientmanagement2.md)
</dt> </dl>

 

 





