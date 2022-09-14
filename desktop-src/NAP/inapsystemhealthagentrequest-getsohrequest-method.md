---
title: INapSystemHealthAgentRequest GetSoHRequest method (NapSystemHealthAgent.h)
description: Can be used by SHAs get SoHs previously cached by the NapAgent.
ms.assetid: 187a4513-79db-45cb-8d64-6a92a2d3b004
keywords:
- GetSoHRequest method NAP
- GetSoHRequest method NAP , INapSystemHealthAgentRequest interface
- INapSystemHealthAgentRequest interface NAP , GetSoHRequest method
topic_type:
- apiref
api_name:
- INapSystemHealthAgentRequest.GetSoHRequest
api_location:
- qagentrt.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentRequest::GetSoHRequest method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentRequest::GetSoHRequest** method can be used by SHAs get SoHs previously cached by the NapAgent.

## Syntax


```C++
HRESULT GetSoHRequest(
  [out] SoHRequest **sohRequest
);
```



## Parameters

<dl> <dt>

*sohRequest* \[out\]
</dt> <dd>

A pointer to a pointer to a [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh).

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                            | Description                                                            |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                  | Operation succeeded.<br/>                                        |
| <dl> <dt>**NAP\_E\_NO\_CACHED\_SOH**</dt> </dl> | The SoH is not found; NapAgent does not have a cached copy.<br/> |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl>        | Permissions error, access denied.<br/>                           |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>         | System resource limit, could not perform the operation.<br/>     |



 

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

 

 





