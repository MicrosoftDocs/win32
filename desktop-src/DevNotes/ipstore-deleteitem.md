---
description: Deletes the specified item from the protected storage.
ms.assetid: 1d071245-a563-4fba-9300-c47ca9a9d625
title: IPStore::DeleteItem method (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPStore.DeleteItem
api_type: 
- COM
api_location: 
- Pstorec.dll
---

# IPStore::DeleteItem method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

Deletes the specified item from the protected storage.

## Syntax


```C++
HRESULT DeleteItem(
  [in]       PST_KEY         Key,
  [in] const GUID            *pItemType,
  [in] const GUID            *pItemSubType,
  [in]       LPCWSTR         szItemName,
  [in]       PPST_PROMPTINFO pPromptInfo,
  [in]       DWORD           dwFlags
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

A pointer to a **GUID** that identifies the data type of the item to delete.

</dd> <dt>

*pItemSubType* \[in\]
</dt> <dd>

A **GUID** that indicates the item subtype to delete.

</dd> <dt>

*szItemName* \[in\]
</dt> <dd>

A string that contains the name of the item to delete.

</dd> <dt>

*pPromptInfo* \[in\]
</dt> <dd>

A pointer to a [**PST\_PROMPTINFO**](pst-promptinfo.md) structure.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Specifies user interface and security behaviors for the delete operation.



| Value                                                                                                                                                                                                                                             | Meaning                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <span id="PST_NO_UI_MIGRATION"></span><span id="pst_no_ui_migration"></span><dl> <dt>**PST\_NO\_UI\_MIGRATION**</dt> <dt>0x00000010</dt> </dl> | Do not show user interface unless a custom password is required.<br/> |



 

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

 

 
