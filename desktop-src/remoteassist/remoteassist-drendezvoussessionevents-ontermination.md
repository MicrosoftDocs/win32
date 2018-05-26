---
title: DRendezvousSessionEvents OnTermination event
description: Invoked when the session has ended.
ms.assetid: fdcebc01-41b2-476d-a1a7-bac39ed50677
keywords:
- OnTermination event Remote Assistance
- OnTermination event Remote Assistance , DRendezvousSessionEvents interface
- DRendezvousSessionEvents interface Remote Assistance , OnTermination event
topic_type:
- apiref
api_name:
- DRendezvousSessionEvents.OnTermination
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

# DRendezvousSessionEvents::OnTermination event

Invoked when the session has ended.

## Syntax


```C++
void OnTermination(
  [in] LONG lReturnCode,
  [in] BSTR bstrData
);
```



## Parameters

<dl> <dt>

*lReturnCode* \[in\]
</dt> <dd>

**HRESULT** representing the return code.

</dd> <dt>

*bstrData* \[in\]
</dt> <dd>

Any data sent as part of the OnTermination event.

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



 

 





