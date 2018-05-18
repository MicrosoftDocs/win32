---
title: DRendezvousSessionEvents OnContextData event
description: Invoked when context data has come from the RendezvousApplication object.
ms.assetid: 'e6d9b128-4222-42b1-976a-d4cff51d65fb'
keywords: ["OnContextData event Remote Assistance", "OnContextData event Remote Assistance , DRendezvousSessionEvents interface", "DRendezvousSessionEvents interface Remote Assistance , OnContextData event"]
topic_type:
- apiref
api_name:
- DRendezvousSessionEvents.OnContextData
api_location:
- RendezvousSession.tlb
api_type:
- COM
---

# DRendezvousSessionEvents::OnContextData event

Invoked when context data has come from the [**RendezvousApplication**](remoteassist-rendezvousapplication.md) object.

## Syntax


```C++
void OnContextData(
  [in] BSTR bstrData
);
```



## Parameters

<dl> <dt>

*bstrData* \[in\]
</dt> <dd>

The context data sent by the [**RendezvousApplication**](remoteassist-rendezvousapplication.md) object.

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



 

 





