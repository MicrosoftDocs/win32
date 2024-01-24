---
title: INapSystemHealthAgentBinding Initialize method (NapSystemHealthAgent.h)
description: Initializes the system health agent (SHA) and binds the SHA to the NapAgent service.
ms.assetid: abbc942b-0217-4b07-bf43-fab55ca9c411
keywords:
- Initialize method NAP
- Initialize method NAP , INapSystemHealthAgentBinding interface
- INapSystemHealthAgentBinding interface NAP , Initialize method
topic_type:
- apiref
api_name:
- INapSystemHealthAgentBinding.Initialize
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentBinding::Initialize method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentBinding::Initialize** method initializes the system health agent (SHA) and binds the SHA to the NapAgent service. This method must be called before calling any other method on the [**INapSystemHealthAgentBinding2**](inapsystemhealthagentbinding2.md) interface.

## Syntax


```C++
HRESULT Initialize(
  [in] SystemHealthEntityId          id,
  [in] INapSystemHealthAgentCallback *callback
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

A unique [SystemHealthEntityId](nap-datatypes.md) that contains the ID of the SHA being bound to the NapAgent service.

</dd> <dt>

*callback* \[in\]
</dt> <dd>

A COM pointer to an [**INapSystemHealthAgentCallback**](inapsystemhealthagentcallback.md) interface used by the NapAgent to callback the health agent with a notify/process. The NapAgent holds a reference to the object associated with this interface until [**Uninitialize**](inapsystemhealthagentbinding-uninitialize-method.md) is called.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                                | Description                                                                                                                    |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                      | Operation succeeded.<br/>                                                                                                |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl>            | Permissions error, access denied.<br/>                                                                                   |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>             | System resource limit, could not perform the operation.<br/>                                                             |
| <dl> <dt>**ERROR\_ALREADY\_INITIALIZED**</dt> </dl> | If the SHA has initialized previously, this error is returned.<br/>                                                      |
| <dl> <dt>**NAP\_E\_NOT\_REGISTERED**</dt> </dl>     | If the SHA has not registered earlier, this error is returned.<br/>                                                      |
| <dl> <dt>**RPC\_E\_DISCONNECTED**</dt> </dl>        | The NapAgent has been stopped. This object will recover automatically and rebind to the NapAgent, once it restarts.<br/> |



 

## Remarks

The NapAgent does not trigger a SoH exchange as a result of initialization. A system health agent must call [**NotifySoHChange**](inapsystemhealthagentbinding-notifysohchange-method.md) to request an exchange of SoH packets after initializing with the NapAgent.

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
</dt> </dl>

 

 





