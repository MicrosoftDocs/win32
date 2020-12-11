---
title: INapSystemHealthAgentBinding2 GetSystemIsolationInfoEx method (NapSystemHealthAgent.h)
description: Is called by SHAs to determine the system isolation state and extended isolation state.
ms.assetid: 237e5539-889c-457d-8db0-bf3379f28b85
keywords:
- GetSystemIsolationInfoEx method NAP
- GetSystemIsolationInfoEx method NAP , INapSystemHealthAgentBinding2 interface
- INapSystemHealthAgentBinding2 interface NAP , GetSystemIsolationInfoEx method
topic_type:
- apiref
api_name:
- INapSystemHealthAgentBinding2.GetSystemIsolationInfoEx
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentBinding2::GetSystemIsolationInfoEx method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentBinding2::GetSystemIsolationInfoEx** method is called by SHAs to determine the system isolation state and extended isolation state.

> [!Note]  
> Use [**INapSystemHealthAgentBinding::GetSystemIsolationInfo**](inapsystemhealthagentbinding-getsystemisolationinfo-method.md) in order to only determine the isolation state of the system.

 

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

A pointer to a pointer to an [**IsolationInfoEx**](/windows/win32/api/naptypes/ns-naptypes-isolationinfoex) structure that contains the extended isolation state of the system for known connections. *isolationInfo* indicates if the system is in a state of restricted access, probation, or unrestricted access, as well as [**ExtendedIsolationState**](/windows/win32/api/naptypes/ne-naptypes-extendedisolationstate) information.

</dd> <dt>

*unknownConnections* \[out\]
</dt> <dd>

A pointer to a **BOOL** that is **TRUE** if any connections are in an unknown state and **FALSE** otherwise.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                             | Description                                                                                                                    |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                   | Operation succeeded.<br/>                                                                                                |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl>         | Permissions error, access denied.<br/>                                                                                   |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>          | System resource limit, could not perform the operation.<br/>                                                             |
| <dl> <dt>**NAP\_E\_NOT\_INITIALIZED**</dt> </dl> | The SHA has not been previously initialized.<br/>                                                                        |
| <dl> <dt>**RPC\_E\_DISCONNECTED**</dt> </dl>     | The NapAgent has been stopped. This object will recover automatically and rebind to the NapAgent, once it restarts.<br/> |



 

## Remarks

The SHA must free the [**IsolationInfoEx**](/windows/win32/api/naptypes/ns-naptypes-isolationinfoex) structure by calling [**FreeIsolationInfoEx**](freeisolationinfoex.md).

The SHA must call [**Initialize**](inapsystemhealthagentbinding-initialize-method.md) before calling this method or any other method of the [**INapSystemHealthAgentBinding2**](inapsystemhealthagentbinding2.md) interface.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>NapSystemHealthAgent.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthAgent.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qagent.dll</dt> </dl>               |



## See also

<dl> <dt>

[**INapSystemHealthAgentBinding2**](inapsystemhealthagentbinding2.md)
</dt> </dl>

 

 





