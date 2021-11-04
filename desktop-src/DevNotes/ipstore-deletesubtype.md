---
description: Deletes a specified subtype from within the specified type.
ms.assetid: 1c44a609-80af-4e28-b1b5-2b4faea143bd
title: IPStore::DeleteSubtype method (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPStore.DeleteSubtype
api_type: 
- COM
api_location: 
- Pstorec.dll
---

# IPStore::DeleteSubtype method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

Deletes a specified subtype from within the specified type.

## Syntax


```C++
HRESULT DeleteSubtype(
  [in]       PST_KEY Key,
  [in] const GUID    *pType,
  [in] const GUID    *pSubtype,
  [in]       DWORD   dwFlags
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

Specifies whether the type is local to the computer or associated only with the creating user.



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

*dwFlags* \[in\]
</dt> <dd>

Reserved: must be set to zero.

</dd> </dl>

## Return value

The return value is an **HRESULT** value. A value of **PST\_E\_OK** indicates the function was successful.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



## See also

<dl> <dt>

[**IPStore**](ipstore.md)
</dt> </dl>

 

 
