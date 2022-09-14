---
title: INapEnforcementClientCallback GetConnections method (NapEnforcementClient.h)
description: Is called by the NapAgent and implemented by the enforcement client to return a set of connections.
ms.assetid: 8f697217-5799-48e4-9f0b-715f516e48d9
keywords:
- GetConnections method NAP
- GetConnections method NAP , INapEnforcementClientCallback interface
- INapEnforcementClientCallback interface NAP , GetConnections method
topic_type:
- apiref
api_name:
- INapEnforcementClientCallback.GetConnections
api_location:
- NapEnforcementClient.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientCallback::GetConnections method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientCallback::GetConnections** callback method is called by the NapAgent and implemented by the enforcement client to return a set of connections.

## Syntax


```C++
HRESULT GetConnections(
  [out] Connections **connections
);
```



## Parameters

<dl> <dt>

*connections* \[out\]
</dt> <dd>

A pointer to the current set of maintained [**Connections**](connections-struct.md).

</dd> </dl>

## Return value

This callback method must return one the following error codes.



| Return code                                                                                                | Description                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Return this value if the operation succeeded.<br/>                                                                                                                                                              |
| <dl> <dt>**RPC\_S\_SERVER\_UNAVAILABLE**</dt> </dl> | Returning this value causes the enforcer to be removed from the bound-SHA list, and the corresponding NapAgent cache entry to be flushed. The failing SHA can then re-initialize itself with the NapAgent.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>NapEnforcementClient.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapEnforcementClient.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapEnforcementClientCallback**](inapenforcementclientcallback.md)
</dt> </dl>

 

 





