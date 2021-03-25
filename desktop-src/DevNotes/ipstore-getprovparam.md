---
description: Intended to set the specified parameter information.
ms.assetid: e1a5766f-a303-47f1-a4bb-33f4253a5464
title: IPStore::GetProvParam method (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPStore.GetProvParam
api_type: 
- COM
api_location: 
- Pstorec.dll
---

# IPStore::GetProvParam method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

\[This method is not implemented.\]

Intended to set the specified parameter information. Note, however, that it is not implemented and will always fail.

## Syntax


```C++
HRESULT GetProvParam(
  [in]  DWORD dwParam,
  [out] DWORD *pcbData,
  [out] BYTE  **ppbData,
  [in]  DWORD dwFlags
);
```



## Parameters

<dl> <dt>

*dwParam* \[in\]
</dt> <dd>

Reserved.

</dd> <dt>

*pcbData* \[out\]
</dt> <dd>

Reserved.

</dd> <dt>

*ppbData* \[out\]
</dt> <dd>

Reserved.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved.

</dd> </dl>

## Return value

Calls to this method will always fail.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



## See also

<dl> <dt>

[**IPStore**](ipstore.md)
</dt> </dl>

 

 
