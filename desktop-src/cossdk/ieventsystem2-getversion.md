---
description: Retrieves the version number of the event system.
ms.assetid: 6355f1b3-e1e7-435f-9795-d92464e004ae
title: IEventSystem2::GetVersion method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEventSystem2.GetVersion
api_type: 
- COM
api_location: 
---

# IEventSystem2::GetVersion method

Retrieves the version number of the event system.

## Syntax


```C++
HRESULT GetVersion(
  [out] int *pnVersion
);
```



## Parameters

<dl> <dt>

*pnVersion* \[out\]
</dt> <dd>

The version number of the event system.

</dd> </dl>

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

 

 




