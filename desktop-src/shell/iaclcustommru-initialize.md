---
description: Loads a list of strings into the most recently used (MRU) list from the registry.
title: IACLCustomMRU::Initialize method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IACLCustomMRU.Initialize
api_type: 
- COM
api_location: 
ms.assetid: 358921b0-46c4-4428-b0b5-57a44fc3247b

---

# IACLCustomMRU::Initialize method

Loads a list of strings into the most recently used (MRU) list from the registry.

## Syntax


```C++
HRESULT Initialize(
  [in] LPCWSTR pwszMRURegKey,
  [in] DWORD   dwMax
);
```



## Parameters

<dl> <dt>

*pwszMRURegKey* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to a buffer containing the registry key holding the strings for the MRU list.

</dd> <dt>

*dwMax* \[in\]
</dt> <dd>

Type: **DWORD**

The maximum number of entries that can be taken from *pwszMRURegKey*.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



 

 




