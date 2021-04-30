---
title: INapSystemHealthAgentCallback GetFixupInfo method (NapSystemHealthAgent.h)
description: Is called by the NapAgent to determine the state of the system health agent, while it is processing a SoHResponse.
ms.assetid: cf919b56-3d40-4c49-9c91-25c20ae5ccda
keywords:
- GetFixupInfo method NAP
- GetFixupInfo method NAP , INapSystemHealthAgentCallback interface
- INapSystemHealthAgentCallback interface NAP , GetFixupInfo method
topic_type:
- apiref
api_name:
- INapSystemHealthAgentCallback.GetFixupInfo
api_location:
- NapSystemHealthAgent.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentCallback::GetFixupInfo method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentCallback::GetFixupInfo** method is called by the NapAgent to determine the state of the system health agent, while it is processing a [**SoHResponse**](/windows/win32/api/naptypes/ns-naptypes-soh).

## Syntax


```C++
HRESULT GetFixupInfo(
  [out] FixupInfo **info
);
```



## Parameters

<dl> <dt>

*info* \[out\]
</dt> <dd>

A pointer to a pointer to a [**FixupInfo**](/windows/win32/api/naptypes/ns-naptypes-fixupinfo) structure that contains the fix-up status of the agent.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                          | Description                   |
|--------------------------------------------------------------------------------------|-------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Indicates success.<br/> |



 

## Remarks

This callback method is declared by the NAP system and is to be implemented by the SHA writer.

The system health agent must return **S\_OK** immediately without blocking.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>NapSystemHealthAgent.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthAgent.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapSystemHealthAgentCallback**](inapsystemhealthagentcallback.md)
</dt> </dl>

 

 





