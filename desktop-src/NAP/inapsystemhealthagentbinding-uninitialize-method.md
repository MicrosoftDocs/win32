---
title: INapSystemHealthAgentBinding Uninitialize method (NapSystemHealthAgent.h)
description: Causes the NapAgent to release all its references to system health agent COM pointers.
ms.assetid: 8b9fabc9-7453-41fe-a1e7-2ec5fa275a3a
keywords:
- Uninitialize method NAP
- Uninitialize method NAP , INapSystemHealthAgentBinding interface
- INapSystemHealthAgentBinding interface NAP , Uninitialize method
topic_type:
- apiref
api_name:
- INapSystemHealthAgentBinding.Uninitialize
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentBinding::Uninitialize method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentBinding::Uninitialize** method causes the NapAgent to release all its references to system health agent COM pointers.

## Syntax


```C++
HRESULT Uninitialize();
```



## Parameters

This method has no parameters.

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                             | Description                                                                                                                    |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                   | Operation succeeded.<br/>                                                                                                |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl>         | Permissions error, access denied.<br/>                                                                                   |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>          | System resource limit, could not perform the operation.<br/>                                                             |
| <dl> <dt>**NAP\_E\_NOT\_INITIALIZED**</dt> </dl> | The SHA has not been previously initialized.<br/>                                                                        |
| <dl> <dt>**RPC\_E\_DISCONNECTED**</dt> </dl>     | The NapAgent has been stopped. This object will recover automatically and rebind to the NapAgent, once it restarts.<br/> |



 

## Remarks

The NapAgent blocks execution of this method call until all existing calls on the Binding and Callback interfaces complete.

The SHA must call [**Initialize**](inapsystemhealthagentbinding-initialize-method.md) before calling this method or any other method of the [**INapSystemHealthAgentBinding2**](inapsystemhealthagentbinding2.md) interface.

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

 

 





