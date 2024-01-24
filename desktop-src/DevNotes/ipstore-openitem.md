---
description: Opens an item for multiple accesses.
ms.assetid: b0602abd-dbda-40d0-befa-348c1179fa4f
title: IPStore::OpenItem method (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPStore.OpenItem
api_type: 
- COM
api_location: 
- Pstorec.dll
---

# IPStore::OpenItem method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

Opens an item for multiple accesses.

## Syntax


```C++
HRESULT OpenItem(
  [in]       PST_KEY        Key,
  [in] const PSGUID         *pItemType,
  [in] const GUID           *pItemSubtype,
  [in]       LPCWSTR        *szItemName,
  [in]       PST_ACCESSMODE ModeFlags,
  [in]       PPST_PROMPTIFO pProomptInfo,
  [in]       DWORD          dwFlags
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

*pItemType* \[in\]
</dt> <dd>

A pointer to a GUID that identifies the data type of the item to open.

</dd> <dt>

*pItemSubtype* \[in\]
</dt> <dd>

A pointer to a GUID that indicates the item subtype to open.

</dd> <dt>

*szItemName* \[in\]
</dt> <dd>

A string that contains the name of the item to open.

</dd> <dt>

*ModeFlags* \[in\]
</dt> <dd>

Describes the access modes to which a specified set of access clauses pertains. For more information, see [**PStore Types**](pstore-types.md).



| Value                                                                                                                                                                                                         | Meaning                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| <span id="PST_READ"></span><span id="pst_read"></span><dl> <dt>**PST\_READ**</dt> <dt>0x0001</dt> </dl>    | Read access mode.<br/>  |
| <span id="PST_WRITE"></span><span id="pst_write"></span><dl> <dt>**PST\_WRITE**</dt> <dt>0x0002</dt> </dl> | Write access mode.<br/> |



 

</dd> <dt>

*pProomptInfo* \[in\]
</dt> <dd>

A pointer to a [**PST\_PROMPTINFO**](pst-promptinfo.md) structure.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved: must be set to zero.

</dd> </dl>

## Return value

The return value is an **HRESULT** value. A value of **PST\_E\_OK** indicates the function was successful.

## Remarks

Using **OpenItem** to open an item in the protected storage database requires that it eventually be closed using [**IPStore::CloseItem**](ipstore-closeitem.md) to prevent a memory leak.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



## See also

<dl> <dt>

[**IPStore**](ipstore.md)
</dt> <dt>

[**PST\_PROMPTINFO**](pst-promptinfo.md)
</dt> </dl>

 

 
