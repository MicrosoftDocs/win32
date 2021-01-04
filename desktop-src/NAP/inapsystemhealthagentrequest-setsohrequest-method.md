---
title: INapSystemHealthAgentRequest SetSoHRequest method (NapSystemHealthAgent.h)
description: Is used by health agents to write their SoH request resulting from the call to INapSystemHealthAgentCallback GetSoHRequest.
ms.assetid: 76471cf2-e5df-4e07-b872-ccac0fd45998
keywords:
- SetSoHRequest method NAP
- SetSoHRequest method NAP , INapSystemHealthAgentRequest interface
- INapSystemHealthAgentRequest interface NAP , SetSoHRequest method
topic_type:
- apiref
api_name:
- INapSystemHealthAgentRequest.SetSoHRequest
api_location:
- qagentrt.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentRequest::SetSoHRequest method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentRequest::SetSoHRequest** method is used by health agents to write their SoH request resulting from the call to [**INapSystemHealthAgentCallback::GetSoHRequest**](inapsystemhealthagentcallback-getsohrequest-method.md).

## Syntax


```C++
HRESULT SetSoHRequest(
  [in] const SoHRequest *sohRequest,
  [in]       BOOL       cacheSohForLaterUse
);
```



## Parameters

<dl> <dt>

*sohRequest* \[in\]
</dt> <dd>

A pointer to a [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) packet.

</dd> <dt>

*cacheSohForLaterUse* \[in\]
</dt> <dd>

A **BOOL** that is **TRUE** if the NapAgent should cache the [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) and **FALSE** otherwise.

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
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>NapSystemHealthAgent.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthAgent.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qagentrt.dll</dt> </dl>             |



## See also

<dl> <dt>

[**INapSystemHealthAgentRequest**](inapsystemhealthagentrequest.md)
</dt> </dl>

 

 





