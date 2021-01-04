---
title: INapSystemHealthAgentCallback interface (NapSystemHealthAgent.h)
description: Are declared by the system and implemented by the SHA writer so the NapAgent can communicate with the SHA.
ms.assetid: f299e796-c81d-4a22-b9c8-f80990098044
keywords:
- INapSystemHealthAgentCallback interface NAP
- INapSystemHealthAgentCallback interface NAP , described
topic_type:
- apiref
api_name:
- INapSystemHealthAgentCallback
api_location:
- NapSystemHealthAgent.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentCallback interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentCallback** interface provides callback methods that are declared by the system and implemented by the SHA writer so the NapAgent can communicate with the SHA.

## Members

The **INapSystemHealthAgentCallback** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **INapSystemHealthAgentCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapSystemHealthAgentCallback** interface has these methods.



| Method                                                                                                                                           | Description                                                                                                          |
|:-------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**INapSystemHealthAgentCallback::CompareSoHRequests**](inapsystemhealthagentcallback-comparesohrequests-method.md)                             | Used by the SHA to compare the SoHs.<br/>                                                                      |
| [**INapSystemHealthAgentCallback::GetFixupInfo**](inapsystemhealthagentcallback-getfixupinfo-method.md)                                         | Called by the NapAgent to determine the state of the SHA.<br/>                                                 |
| [**INapSystemHealthAgentCallback::GetSoHRequest**](inapsystemhealthagentcallback-getsohrequest-method.md)                                       | Called by the NapAgent to query the SHA's SoH request.<br/>                                                    |
| [**INapSystemHealthAgentCallback::NotifyOrphanedSoHRequest**](inapsystemhealthagentcallback-notifyorphanedsohrequest-method.md)                 | Called if an SoH request was queried from the SHA, but the response never came back.<br/>                      |
| [**INapSystemHealthAgentCallback::NotifySystemIsolationStateChange**](inapsystemhealthagentcallback-notifysystemisolationstatechange-method.md) | Called by the NapAgent to indicate that the system isolation state or the probation end-time has changed.<br/> |
| [**INapSystemHealthAgentCallback::ProcessSoHResponse**](inapsystemhealthagentcallback-processsohresponse-method.md)                             | Called when the NapAgent receives an SoH response destined for this health agent.<br/>                         |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>NapSystemHealthAgent.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthAgent.idl</dt> </dl> |



## See also

<dl> <dt>

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

