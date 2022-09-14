---
title: INapSystemHealthAgentBinding FlushCache method (NapSystemHealthAgent.h)
description: Is called by an SHA to flush its SoH cache.
ms.assetid: a771ce03-1922-4e2d-9490-7ee9f693857c
keywords:
- FlushCache method NAP
- FlushCache method NAP , INapSystemHealthAgentBinding interface
- INapSystemHealthAgentBinding interface NAP , FlushCache method
topic_type:
- apiref
api_name:
- INapSystemHealthAgentBinding.FlushCache
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentBinding::FlushCache method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentBinding::FlushCache** method is called by an SHA to flush its SoH cache.

## Syntax


```C++
HRESULT FlushCache();
```



## Parameters

This method has no parameters.

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                         | Description                                                                                                                    |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>               | Operation succeeded.<br/>                                                                                                |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl>     | Permissions error, access denied.<br/>                                                                                   |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>      | System resource limit, could not perform the operation.<br/>                                                             |
| <dl> <dt>**RPC\_E\_DISCONNECTED**</dt> </dl> | The NapAgent has been stopped. This object will recover automatically and rebind to the NapAgent, once it restarts.<br/> |



 

## Remarks

The NapAgent maintains a cache of recent SoHs provided by different SHAs. This cache is useful to optimize boot-time performance, when SHAs may or may not be bound to the system.

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

 

 





