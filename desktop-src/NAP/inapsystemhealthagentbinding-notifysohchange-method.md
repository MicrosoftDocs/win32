---
title: INapSystemHealthAgentBinding NotifySoHChange method (NapSystemHealthAgent.h)
description: Is used by SHAs when their SoH changes.
ms.assetid: 3a653282-03b0-49d5-833f-966497f46faa
keywords:
- NotifySoHChange method NAP
- NotifySoHChange method NAP , INapSystemHealthAgentBinding interface
- INapSystemHealthAgentBinding interface NAP , NotifySoHChange method
topic_type:
- apiref
api_name:
- INapSystemHealthAgentBinding.NotifySoHChange
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentBinding::NotifySoHChange method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentBinding::NotifySoHChange** method is used by SHAs when their SoH changes.

## Syntax


```C++
HRESULT NotifySoHChange();
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

SHAs must not call this API speculatively since it results in an SoH exchange on the wire. Calls to this API should only be made when necessary.

The NapAgent does not hold this thread to process the SoH change. Instead, it returns immediately and processes the change asynchronously.

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

 

 





