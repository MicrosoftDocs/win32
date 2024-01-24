---
title: INapSystemHealthAgentCallback NotifyOrphanedSoHRequest method (NapSystemHealthAgent.h)
description: Is called if an SoHRequest was queried from the SHA, but the response never came back.
ms.assetid: 9e6fac6c-fb23-4725-ae0f-28ef8a6c4ea6
keywords:
- NotifyOrphanedSoHRequest method NAP
- NotifyOrphanedSoHRequest method NAP , INapSystemHealthAgentCallback interface
- INapSystemHealthAgentCallback interface NAP , NotifyOrphanedSoHRequest method
topic_type:
- apiref
api_name:
- INapSystemHealthAgentCallback.NotifyOrphanedSoHRequest
api_location:
- NapSystemHealthAgent.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentCallback::NotifyOrphanedSoHRequest method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentCallback::NotifyOrphanedSoHRequest** method is called if an [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) was queried from the SHA, but the response never came back.

## Syntax


```C++
HRESULT NotifyOrphanedSoHRequest(
  [in] const CorrelationId *correlationId
);
```



## Parameters

<dl> <dt>

*correlationId* \[in\]
</dt> <dd>

A pointer to the unique [**CorrelationId**](/windows/win32/api/naptypes/ns-naptypes-correlationid) structure that identifies the orphaned [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh).

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                          | Description                   |
|--------------------------------------------------------------------------------------|-------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Indicates success.<br/> |



 

## Remarks

This callback method is declared by the NAP system and is to be implemented by the SHA writer.

This method can be called by the system in the following cases:

-   A [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) could not be sent on the wire.
-   A [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) was sent on the wire, but no **SoHResponse** came back, i.e. the enforcer timed out or there was no corresponding SHV on the server-side.
-   The connection went down or an enforcer went offline.

This is only a best effort notification, so SHAs must not rely on this information to clean up state. There are several situations in which an SHA will not be notified:

-   If an enforcer misbehaves, i.e. it does not notify the SHA when the connection state is down.
-   If an enforcer crashes.
-   In error conditions, i.e. the NapAgent is out of memory.

SHAs may get some spurious notifications when they first bind to the NapAgent, for instance, if an SoH exchange is in progress when the SHA bound, and then it times out.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>NapSystemHealthAgent.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthAgent.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapSystemHealthAgentCallback**](inapsystemhealthagentcallback.md)
</dt> </dl>

 

 





