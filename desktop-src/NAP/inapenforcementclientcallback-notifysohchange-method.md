---
title: INapEnforcementClientCallback NotifySoHChange method (NapEnforcementClient.h)
description: Is used by the NapAgent to inform the enforcement client of SoH changes.
ms.assetid: da8b9238-6371-4a6a-a9e7-ab791391ffc2
keywords:
- NotifySoHChange method NAP
- NotifySoHChange method NAP , INapEnforcementClientCallback interface
- INapEnforcementClientCallback interface NAP , NotifySoHChange method
topic_type:
- apiref
api_name:
- INapEnforcementClientCallback.NotifySoHChange
api_location:
- NapEnforcementClient.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientCallback::NotifySoHChange method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientCallback::NotifySoHChange** callback method is used by the NapAgent to inform the enforcement client of SoH changes.

## Syntax


```C++
HRESULT NotifySoHChange();
```



## Parameters

This method has no parameters.

## Return value

This callback method must return one the following error codes.



| Return code                                                                                                | Description                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Return this value if the operation succeeded.<br/>                                                                                                                                                              |
| <dl> <dt>**RPC\_S\_SERVER\_UNAVAILABLE**</dt> </dl> | Returning this value causes the enforcer to be removed from the bound-SHA list, and the corresponding NapAgent cache entry to be flushed. The failing SHA can then re-initialize itself with the NapAgent.<br/> |



 

## Remarks

The completion of system fix-up is a system health change event. That means you must call **NotifySoHChange** when a [**INapSystemHealthAgentCallback::GetFixupInfo**](inapsystemhealthagentcallback-getfixupinfo-method.md) notification indicates that the client is fixed. When a client is fixed, the **state** member of the [**FixupInfo**](/windows/win32/api/naptypes/ns-naptypes-fixupinfo) structure returned by **GetFixupInfo** has a value of **fixupStateSuccess**.

After being called by the NapAgent via this callback, the enforcement agent must then call [**INapEnforcementClientBinding::GetSoHRequest**](inapenforcementclientbinding-getsohrequest-method.md) to retrieve the new request. This call can be made on the same thread as **INapEnforcementClientCallback::NotifySoHChange**.

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

 

 





