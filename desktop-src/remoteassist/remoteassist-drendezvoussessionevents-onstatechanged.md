---
title: DRendezvousSessionEvents OnStateChanged event
description: Invoked when the session state has changed from the previous state.
ms.assetid: 'f3c27aff-81c2-49ad-a9b3-144d1f3e1980'
keywords: ["OnStateChanged event Remote Assistance", "OnStateChanged event Remote Assistance , DRendezvousSessionEvents interface", "DRendezvousSessionEvents interface Remote Assistance , OnStateChanged event"]
topic_type:
- apiref
api_name:
- DRendezvousSessionEvents.OnStateChanged
api_location:
- RendezvousSession.tlb
api_type:
- COM
---

# DRendezvousSessionEvents::OnStateChanged event

Invoked when the session state has changed from the previous state.

## Syntax


```C++
void OnStateChanged(
  [in] RENDEZVOUS_SESSION_STATE prevState
);
```



## Parameters

<dl> <dt>

*prevState* \[in\]
</dt> <dd>

Specifies the previous state of the session.

</dd> </dl>

## Return value

This event does not return a value.

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                             |
| Header<br/>                   | <dl> <dt>RendezvousSession.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>RendezvousSession.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>RendezvousSession.tlb</dt> </dl> |



 

 





