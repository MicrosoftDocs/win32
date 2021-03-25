---
description: Retrieves information associated with a subtype.
ms.assetid: 3daf5f37-9e7f-4ce1-bd35-d7e3c2ef5c28
title: IPStore::GetSubtypeInfo method (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPStore.GetSubtypeInfo
api_type: 
- COM
api_location: 
- Pstorec.dll
---

# IPStore::GetSubtypeInfo method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

Retrieves information associated with a subtype.

## Syntax


```C++
HRESULT GetSubtypeInfo(
  [in]       PST_KEY       Key,
  [in] const GUID          *pType,
  [in] const GUID          *pSubtype,
  [in]       PPST_TYPEINFO **ppInfo,
  [in]       DWORD         dwFlags
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

The provider storage area.



| Value                                                                                                                                                                                                                                                   | Meaning                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <span id="PST_KEY_CURRENT_USER"></span><span id="pst_key_current_user"></span><dl> <dt>**PST\_KEY\_CURRENT\_USER**</dt> <dt>0x00000000</dt> </dl>    | The storage is maintained in the current user section of the registry.<br/>  |
| <span id="PST_KEY_LOCAL_MACHINE"></span><span id="pst_key_local_machine"></span><dl> <dt>**PST\_KEY\_LOCAL\_MACHINE**</dt> <dt>0x00000001</dt> </dl> | The storage is maintained in the local machine section of the registry.<br/> |



 

</dd> <dt>

*pType* \[in\]
</dt> <dd>

A pointer to a GUID that identifies the data type of the storage.

</dd> <dt>

*pSubtype* \[in\]
</dt> <dd>

A pointer to a GUID that identifies the data subtype of the storage.

</dd> <dt>

*ppInfo* \[in\]
</dt> <dd>

A pointer to a [**PST\_TYPEINFO**](pst-typeinfo.md) structure.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved: must be set to zero.

</dd> </dl>

## Return value

The return value is an **HRESULT** value. A value of PST\_E\_OK indicates the function was successful.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



## See also

<dl> <dt>

[**IPStore**](ipstore.md)
</dt> <dt>

[**PST\_TYPEINFO**](pst-typeinfo.md)
</dt> </dl>

 

 
