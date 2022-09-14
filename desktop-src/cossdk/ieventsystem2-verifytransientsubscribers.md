---
description: Verifies the existence of all transient subscribers in the data store. By calling this method, you can ensure that all transient subscribers listed in the data store are active.
ms.assetid: fffdde33-e960-42ef-a089-8ea8a6f33d52
title: IEventSystem2::VerifyTransientSubscribers method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEventSystem2.VerifyTransientSubscribers
api_type: 
- COM
api_location: 
---

# IEventSystem2::VerifyTransientSubscribers method

Verifies the existence of all transient subscribers in the data store. By calling this method, you can ensure that all transient subscribers listed in the data store are active.

## Syntax


```C++
HRESULT VerifyTransientSubscribers();
```



## Parameters

This method has no parameters.

## Return value

This method can return the standard return values E\_INVALIDARG, E\_OUTOFMEMORY, E\_UNEXPECTED, E\_FAIL, and S\_OK.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**IEventSystem2**](ieventsystem2.md)
</dt> </dl>

 

 




