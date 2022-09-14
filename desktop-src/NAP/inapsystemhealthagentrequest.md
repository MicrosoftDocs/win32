---
title: INapSystemHealthAgentRequest interface (NapSystemHealthAgent.h)
description: SHAs use to communicate and coordinate processing with the NAP system.
ms.assetid: 424e0fb7-cce7-4b75-b474-fda0e053284e
keywords:
- INapSystemHealthAgentRequest interface NAP
- INapSystemHealthAgentRequest interface NAP , described
topic_type:
- apiref
api_name:
- INapSystemHealthAgentRequest
api_location:
- qagentrt.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentRequest interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentRequest** interface provides methods that SHAs use to communicate and coordinate processing with the NAP system.

## Members

The **INapSystemHealthAgentRequest** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **INapSystemHealthAgentRequest** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapSystemHealthAgentRequest** interface has these methods.



| Method                                                                                                                     | Description                                                                                      |
|:---------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [**INapSystemHealthAgentRequest::GetCacheSoHFlag**](inapsystemhealthagentrequest-getcachesohflag-method.md)               | Used only by the NapAgent.<br/>                                                            |
| [**INapSystemHealthAgentRequest::GetCorrelationId**](inapsystemhealthagentrequest-getcorrelationid-method.md)             | Used by system health agents to correlate SoHs and [**SoHResponse**](/windows/win32/api/naptypes/ns-naptypes-soh).<br/> |
| [**INapSystemHealthAgentRequest::GetSoHRequest**](inapsystemhealthagentrequest-getsohrequest-method.md)                   | Used by SHAs to get SoHs previously cached by the NapAgent.<br/>                           |
| [**INapSystemHealthAgentRequest::GetSoHResponse**](inapsystemhealthagentrequest-getsohresponse-method.md)                 | Used by the health agent to retrieve their [**SoHResponse**](/windows/win32/api/naptypes/ns-naptypes-soh).<br/>         |
| [**INapSystemHealthAgentRequest::GetStringCorrelationId**](inapsystemhealthagentrequest-getstringcorrelationid-method.md) | Used by system health agents to log the correlation ID.<br/>                               |
| [**INapSystemHealthAgentRequest::SetSoHRequest**](inapsystemhealthagentrequest-setsohrequest-method.md)                   | Used by health agents to write their SoH request.<br/>                                     |



 

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

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

