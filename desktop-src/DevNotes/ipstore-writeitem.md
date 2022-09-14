---
description: Writes a data item to protected storage.
ms.assetid: d940470c-b881-4e05-8e52-f804eac11e45
title: IPStore::WriteItem method (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPStore.WriteItem
api_type: 
- COM
api_location: 
- Pstorec.dll
---

# IPStore::WriteItem method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

Writes a data item to protected storage.

## Syntax


```C++
HRESULT WriteItem(
  [in]        PST_KEY        Key,
  [in]  const GUID           *pItemType,
  [in]  const GUID           *pItemSubtype,
  [in]        LPCWSTR        *szItemName,
  [out]       DWORD          *cbData,
  [out]       BYTE           ppbData,
  [in]        PPST_PROMPTIFO pProomptInfo,
  [in]        DWORD          dwDefaultConfirmationStyle,
  [in]        DWORD          dwFlags
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

*pItemType* \[in\]
</dt> <dd>

A pointer to a **GUID** that identifies the data type of the data item being written.

</dd> <dt>

*pItemSubtype* \[in\]
</dt> <dd>

A pointer to a **GUID** that identifies the data subtype of the data item being written.

</dd> <dt>

*szItemName* \[in\]
</dt> <dd>

A pointer to a string that contains the name assigned to the stored data item.

</dd> <dt>

*cbData* \[out\]
</dt> <dd>

A pointer to a **DWORD** that indicates the size of the buffer that contains the stored data item.

</dd> <dt>

*ppbData* \[out\]
</dt> <dd>

A pointer to a buffer that contains the data item being written.

</dd> <dt>

*pProomptInfo* \[in\]
</dt> <dd>

Pointer to a [**PST\_PROMPTINFO**](pst-promptinfo.md) structure.

</dd> <dt>

*dwDefaultConfirmationStyle* \[in\]
</dt> <dd>

The default confirmation style.



| Value                                                                                                                                                                                                                             | Meaning                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <span id="PST_CF_DEFAULT"></span><span id="pst_cf_default"></span><dl> <dt>**PST\_CF\_DEFAULT**</dt> <dt>0x00000000</dt> </dl> | Allows the user to choose the confirmation style. <br/> |
| <span id="PST_CF_NONE"></span><span id="pst_cf_none"></span><dl> <dt>**PST\_CF\_NONE**</dt> <dt>0x00000001</dt> </dl>          | Forces silent item creation. <br/>                      |



 

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

The user interface and security behaviors for the write operation.



| Value                                                                                                                                                                                                                                                              | Meaning                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| <span id="PST_NO_OVERWRITE"></span><span id="pst_no_overwrite"></span><dl> <dt>**PST\_NO\_OVERWRITE**</dt> <dt>0x00000002</dt> </dl>                            | Specifies that the item be created in protected storage. Overwriting of an existing item is disallowed.<br/> |
| <span id="PST_UNRESTRICTED_ITEMDATA"></span><span id="pst_unrestricted_itemdata"></span><dl> <dt>**PST\_UNRESTRICTED\_ITEMDATA**</dt> <dt>0x00000004</dt> </dl> | Specifies that the data stream is nonsecure. By default, item calls are secure.<br/>                         |



 

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
</dt> <dt>

[**PST\_PROMPTINFO**](pst-promptinfo.md)
</dt> </dl>

 

 
