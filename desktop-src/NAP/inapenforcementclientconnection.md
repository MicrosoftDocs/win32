---
title: INapEnforcementClientConnection interface (NapEnforcementClient.h)
description: Allow for client connection management. | INapEnforcementClientConnection interface (NapEnforcementClient.h)
ms.assetid: 96b94995-24b8-47ed-880e-6182d1bfe925
keywords:
- INapEnforcementClientConnection interface NAP
- INapEnforcementClientConnection interface NAP , described
topic_type:
- apiref
api_name:
- INapEnforcementClientConnection
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientConnection interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientConnection** provides methods that allow for client connection management.

> [!Note]  
> [**INapEnforcementClientConnection2**](inapenforcementclientconnection2.md) inherits all the methods of this interface and should be used instead.

 

## Members

The **INapEnforcementClientConnection** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **INapEnforcementClientConnection** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapEnforcementClientConnection** interface has these methods.



| Method                                                                                                                           | Description                                                                                                                               |
|:---------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| [**INapEnforcementClientConnection::GetConnectionId**](inapenforcementclientconnection-getconnectionid-method.md)               | Gets the connection ID of the client.<br/>                                                                                          |
| [**INapEnforcementClientConnection::GetCorrelationId**](inapenforcementclientconnection-getcorrelationid-method.md)             | Gets the ID used to correlate SoH-requests and SoH-responses.<br/>                                                                  |
| [**INapEnforcementClientConnection::GetEnforcerPrivateData**](inapenforcementclientconnection-getenforcerprivatedata-method.md) | Used by the enforcer to get private data.<br/>                                                                                      |
| [**INapEnforcementClientConnection::GetFlags**](inapenforcementclientconnection-getflags-method.md)                             | Gets the value of the flag that differentiates first-time responses from responses due to SoHRequests cached by the enforcers.<br/> |
| [**INapEnforcementClientConnection::GetIsolationInfo**](inapenforcementclientconnection-getisolationinfo-method.md)             | Used get the isolation information of the client.<br/>                                                                              |
| [**INapEnforcementClientConnection::GetMaxSize**](inapenforcementclientconnection-getmaxsize-method.md)                         | Gets the maximum size of the SoH packet for this client.<br/>                                                                       |
| [**INapEnforcementClientConnection::GetPrivateData**](inapenforcementclientconnection-getprivatedata-method.md)                 | Used by the NapAgent to get private data.<br/>                                                                                      |
| [**INapEnforcementClientConnection::GetSoHRequest**](inapenforcementclientconnection-getsohrequest-method.md)                   | Gets the SoH Request.<br/>                                                                                                          |
| [**INapEnforcementClientConnection::GetSoHResponse**](inapenforcementclientconnection-getsohresponse-method.md)                 | Gets the SoH-Response received by the enforcement client.<br/>                                                                      |
| [**INapEnforcementClientConnection::GetStringCorrelationId**](inapenforcementclientconnection-getstringcorrelationid-method.md) | Gets the string version of the CorrelationId. Used primarily for logging purposes.<br/>                                             |
| [**INapEnforcementClientConnection::Initialize**](inapenforcementclientconnection-initialize-method.md)                         | Initializes the connection.<br/>                                                                                                    |
| [**INapEnforcementClientConnection::SetConnectionId**](inapenforcementclientconnection-setconnectionid-method.md)               | Sets the connection ID of the client.<br/>                                                                                          |
| [**INapEnforcementClientConnection::SetCorrelationId**](inapenforcementclientconnection-setcorrelationid-method.md)             | Sets the ID used to correlate SoH-requests and SoH-responses.<br/>                                                                  |
| [**INapEnforcementClientConnection::SetEnforcerPrivateData**](inapenforcementclientconnection-setenforcerprivatedata-method.md) | Used by the enforcer to set private data.<br/>                                                                                      |
| [**INapEnforcementClientConnection::SetFlags**](inapenforcementclientconnection-setflags-method.md)                             | Sets the flag that differentiates first-time responses from responses due to SoHRequests cached by enforcers.<br/>                  |
| [**INapEnforcementClientConnection::SetIsolationInfo**](inapenforcementclientconnection-setisolationinfo-method.md)             | Used by the NapAgent to set the isolation information of the client.<br/>                                                           |
| [**INapEnforcementClientConnection::SetMaxSize**](inapenforcementclientconnection-setmaxsize-method.md)                         | Sets the maximum size of the SoH packet for this client.<br/>                                                                       |
| [**INapEnforcementClientConnection::SetPrivateData**](inapenforcementclientconnection-setprivatedata-method.md)                 | Used by the NapAgent to set private data.<br/>                                                                                      |
| [**INapEnforcementClientConnection::SetSoHRequest**](inapenforcementclientconnection-setsohrequest-method.md)                   | Sets the SoH Request.<br/>                                                                                                          |
| [**INapEnforcementClientConnection::SetSoHResponse**](inapenforcementclientconnection-setsohresponse-method.md)                 | Sets the SoH-Response and is used by the enforcement client on receiving a packet.<br/>                                             |



 

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

 

