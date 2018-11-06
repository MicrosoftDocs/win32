---
Description: Adds an entry to the most recently used (MRU) list.
title: IACLCustomMRU::AddMRUString method
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IACLCustomMRU.AddMRUString
api_type: 
- COM
api_location: 
---

# IACLCustomMRU::AddMRUString method

Adds an entry to the most recently used (MRU) list.

## Syntax


```C++
HRESULT AddMRUString(
  [in] LPCWSTR pwszEntry
);
```



## Parameters

<dl> <dt>

*pwszEntry* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to a buffer containing the new entry.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



 

 




