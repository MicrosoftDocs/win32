---
title: DRendezvousSessionEvents OnSendError event
description: Invoked when the SendContextData method has failed on the remote end of the connection.
ms.assetid: c7c8025d-5d5a-4f0f-b7ed-a3a3cf8b755e
keywords:
- OnSendError event Remote Assistance
- OnSendError event Remote Assistance , DRendezvousSessionEvents interface
- DRendezvousSessionEvents interface Remote Assistance , OnSendError event
topic_type:
- apiref
api_name:
- DRendezvousSessionEvents.OnSendError
api_location:
- RendezvousSession.tlb
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DRendezvousSessionEvents::OnSendError event

Invoked when the [**SendContextData**](/windows/previous-versions/RendezvousSession/nf-rendezvoussession-irendezvoussession-sendcontextdata?branch=master) method has failed on the remote end of the connection.

## Syntax


```C++
void OnSendError(
  [in] LONG lReturnCode
);
```



## Parameters

<dl> <dt>

*lReturnCode* \[in\]
</dt> <dd>

**HRESULT** representing the error code.

</dd> </dl>

## Return value

This event does not return a value.

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                             |
| Header<br/>                   | <dl> <dt>RendezvousSession.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>RendezvousSession.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>RendezvousSession.tlb</dt> </dl> |



 

 





