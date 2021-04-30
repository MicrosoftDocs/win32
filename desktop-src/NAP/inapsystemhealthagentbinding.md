---
title: INapSystemHealthAgentBinding interface (NapSystemHealthAgent.h)
description: The SHAs use to communicate with the NapAgent. | INapSystemHealthAgentBinding interface (NapSystemHealthAgent.h)
ms.assetid: 9366f61f-086a-4f44-900e-9ec3165a35ba
keywords:
- INapSystemHealthAgentBinding interface NAP
- INapSystemHealthAgentBinding interface NAP , described
topic_type:
- apiref
api_name:
- INapSystemHealthAgentBinding
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentBinding interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentBinding** provides methods that the SHAs use to communicate with the NapAgent.

> [!Note]  
> [**INapSystemHealthAgentBinding2**](inapsystemhealthagentbinding2.md) inherits all the methods of this interface and should be used instead.

 

## Members

The **INapSystemHealthAgentBinding** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **INapSystemHealthAgentBinding** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapSystemHealthAgentBinding** interface has these methods.



| Method                                                                                                                     | Description                                                                                        |
|:---------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**INapSystemHealthAgentBinding::FlushCache**](inapsystemhealthagentbinding-flushcache-method.md)                         | Called by an SHA to flush its SoH cache.<br/>                                                |
| [**INapSystemHealthAgentBinding::GetSystemIsolationInfo**](inapsystemhealthagentbinding-getsystemisolationinfo-method.md) | Called by SHAs to determine the system isolation state.<br/>                                 |
| [**INapSystemHealthAgentBinding::Initialize**](inapsystemhealthagentbinding-initialize-method.md)                         | Initializes the SHA and binds the SHA to the NapAgent service. <br/>                         |
| [**INapSystemHealthAgentBinding::NotifySoHChange**](inapsystemhealthagentbinding-notifysohchange-method.md)               | Called by SHAs when their SoH changes.<br/>                                                  |
| [**INapSystemHealthAgentBinding::Uninitialize**](inapsystemhealthagentbinding-uninitialize-method.md)                     | Called by SHAs to cause the NapAgent to release all its references to SHA COM pointers.<br/> |



 

## Remarks

All the APIs in this interface will return **RPC\_E\_DISCONNECTED** if the NapAgent is stopped. This object will recover automatically and rebind to the NapAgent, once it restarts.

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

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

