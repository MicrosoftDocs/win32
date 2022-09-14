---
title: INapSystemHealthAgentRequest GetStringCorrelationId method (NapSystemHealthAgent.h)
description: Is used by system health agents to log the correlation ID.
ms.assetid: 5d6f2392-2ada-474a-b150-31e0583c2ea7
keywords:
- GetStringCorrelationId method NAP
- GetStringCorrelationId method NAP , INapSystemHealthAgentRequest interface
- INapSystemHealthAgentRequest interface NAP , GetStringCorrelationId method
topic_type:
- apiref
api_name:
- INapSystemHealthAgentRequest.GetStringCorrelationId
api_location:
- qagentrt.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentRequest::GetStringCorrelationId method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentRequest::GetStringCorrelationId** method is used by system health agents to log the correlation ID.

## Syntax


```C++
HRESULT GetStringCorrelationId(
  [out] StringCorrelationId **correlationId
);
```



## Parameters

<dl> <dt>

*correlationId* \[out\]
</dt> <dd>

A pointer to a pointer to a unique [**CorrelationId**](/windows/win32/api/naptypes/ns-naptypes-correlationid) for this SoH exchange.

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

 

 





