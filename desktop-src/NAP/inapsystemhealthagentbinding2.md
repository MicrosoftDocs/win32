---
title: INapSystemHealthAgentBinding2 interface (NapSystemHealthAgent.h)
description: The SHAs use to communicate with the NapAgent. | INapSystemHealthAgentBinding2 interface (NapSystemHealthAgent.h)
ms.assetid: 2b087d79-a738-42d6-a8f2-4698ab844446
keywords:
- INapSystemHealthAgentBinding2 interface NAP
- INapSystemHealthAgentBinding2 interface NAP , described
topic_type:
- apiref
api_name:
- INapSystemHealthAgentBinding2
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentBinding2 interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentBinding2** provides methods that the SHAs use to communicate with the NapAgent.

> [!Note]  
> This interface inherits all the methods of [**INapSystemHealthAgentBinding**](inapsystemhealthagentbinding.md) and should be used instead.

 

## Members

The **INapSystemHealthAgentBinding2** interface inherits from [**INapSystemHealthAgentBinding**](inapsystemhealthagentbinding.md). **INapSystemHealthAgentBinding2** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapSystemHealthAgentBinding2** interface has these methods.



| Method                                                                                                                    | Description                                                                                     |
|:--------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**INapSystemHealthAgentBinding2::GetSystemIsolationInfoEx**](inapsystemhealthagentbinding2-getsystemisolationinfoex.md) | Called by SHAs to determine the system isolation state and extended isolation state.<br/> |



 

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

[**INapSystemHealthAgentBinding**](inapsystemhealthagentbinding.md)
</dt> <dt>

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

 





