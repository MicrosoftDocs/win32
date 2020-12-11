---
title: INapSystemHealthAgentCallback ProcessSoHResponse method (NapSystemHealthAgent.h)
description: Is called when the NapAgent receives an SoHResponse destined for this health agent.
ms.assetid: 860b1012-7df8-456f-8f21-eb0e1abd2b3b
keywords:
- ProcessSoHResponse method NAP
- ProcessSoHResponse method NAP , INapSystemHealthAgentCallback interface
- INapSystemHealthAgentCallback interface NAP , ProcessSoHResponse method
topic_type:
- apiref
api_name:
- INapSystemHealthAgentCallback.ProcessSoHResponse
api_location:
- NapSystemHealthAgent.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentCallback::ProcessSoHResponse method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentCallback::ProcessSoHResponse** method is called when the NapAgent receives an [**SoHResponse**](/windows/win32/api/naptypes/ns-naptypes-soh) destined for this health agent.

## Syntax


```C++
HRESULT ProcessSoHResponse(
  [in] INapSystemHealthAgentRequest *request
);
```



## Parameters

<dl> <dt>

*request* \[in\]
</dt> <dd>

A COM pointer to a [**INapSystemHealthAgentRequest**](inapsystemhealthagentrequest.md) object that identifies the request object.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                            | Description                                                                              |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | Indicates success.<br/>                                                            |
| <dl> <dt>**NAP\_E\_INVALID\_PACKET**</dt> </dl> | Returned by this implementation if the response is not in the correct format.<br/> |



 

## Remarks

This callback method is declared by the NAP system and is to be implemented by the SHA writer.

When the NapAgent receives an [**SoHResponse**](/windows/win32/api/naptypes/ns-naptypes-soh) destined for this health agent, it invokes this method. The health agent must query the SoHResponse from the request object. It must not hold references to the request object once this call has completed.

The **INapSystemHealthAgentCallback::ProcessSoHResponse** method must not block. If any fix-up processing is required, any implementation of **ProcessSoHResponse** must start a new thread to perform fix-up processing. The NapAgent must call [**INapSystemHealthAgentCallBack::GetFixupInfo**](inapsystemhealthagentcallback-getfixupinfo-method.md) to determine the fix-up status of the SHA.

This method must return **NAP\_E\_INVALID\_PACKET** if the response is not in the correct format.

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

 

 





