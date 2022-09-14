---
title: INapEnforcementClientBinding interface (NapEnforcementClient.h)
description: Enforcement clients use to communicate with the NapAgent.
ms.assetid: 73c5c9ad-f213-4d34-9262-996acb570a55
keywords:
- INapEnforcementClientBinding interface NAP
- INapEnforcementClientBinding interface NAP , described
topic_type:
- apiref
api_name:
- INapEnforcementClientBinding
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientBinding interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientBinding** provides methods that enforcement clients use to communicate with the NapAgent.

## Members

The **INapEnforcementClientBinding** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **INapEnforcementClientBinding** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapEnforcementClientBinding** interface has these methods.



| Method                                                                                                                           | Description                                                                                                                                                                                                           |
|:---------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**INapEnforcementClientBinding::CreateConnection**](inapenforcementclientbinding-createconnection-method.md)                   | Used by enforcers to create connection objects.<br/>                                                                                                                                                            |
| [**INapEnforcementClientBinding::GetSoHRequest**](inapenforcementclientbinding-getsohrequest-method.md)                         | Used by the enforcement client when it needs an SoH-request for a particular connection.<br/>                                                                                                                   |
| [**INapEnforcementClientBinding::Initialize**](inapenforcementclientbinding-initialize-method.md)                               | Starts up the NapAgent service. The enforcement client must call this method before calling any other method of this interface.<br/>                                                                            |
| [**INapEnforcementClientBinding::NotifyConnectionStateDown**](inapenforcementclientbinding-notifyconnectionstatedown-method.md) | Used to inform the NapAgent that a connection to an enforcement client has gone down.<br/>                                                                                                                      |
| [**INapEnforcementClientBinding::NotifySoHChangeFailure**](inapenforcementclientbinding-notifysohchangefailure-method.md)       | Used by the enforcement client to inform the NapAgent that it could not process a previous [**INapEnforcementClientCallback::NotifySoHChange**](inapenforcementclientcallback-notifysohchange-method.md).<br/> |
| [**INapEnforcementClientBinding::ProcessSoHResponse**](inapenforcementclientbinding-processsohresponse-method.md)               | Used by enforcement clients whenever they get an SoH-Response data blob from the enforcement server.<br/>                                                                                                       |
| [**INapEnforcementClientBinding::Uninitialize**](inapenforcementclientbinding-uninitialize-method.md)                           | Concludes the NapAgent service for this client connection.<br/>                                                                                                                                                 |



 

## Remarks

All the APIs in this interface will return RPC\_E\_DISCONNECTED if the NapAgent is stopped. This object will recover automatically and rebind to the NapAgent, once it restarts.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>NapEnforcementClient.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapEnforcementClient.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qagent.dll</dt> </dl>               |



## See also

<dl> <dt>

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

