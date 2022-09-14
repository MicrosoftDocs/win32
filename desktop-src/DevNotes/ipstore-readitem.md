---
description: Reads the specified data item from protected storage.
ms.assetid: e565a0ea-5d8e-4706-a176-2305a95f0d67
title: IPStore::ReadItem method (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPStore.ReadItem
api_type: 
- COM
api_location: 
- Pstorec.dll
---

# IPStore::ReadItem method

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

Reads the specified data item from protected storage.

## Syntax


```C++
HRESULT ReadItem(
  [in]       PST_KEY        Key,
  [in] const PSGUID         *pItemType,
  [in] const GUID           *pItemSubtype,
  [in]       LPCWSTR        *szItemName,
  [in]       DWORD          cbData,
  [in]       BYTE_RPC_FAR   *pbData,
  [in]       PPST_PROMPTIFO pPromptInfo,
  [in]       DWORD          dwFlags
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

A pointer to a GUID that identifies the data type of the item to read.

</dd> <dt>

*pItemSubtype* \[in\]
</dt> <dd>

A pointer to a GUID that identifies the data subtype of the item to read.

</dd> <dt>

*szItemName* \[in\]
</dt> <dd>

A pointer to a string that contains the name assigned to the stored data item.

</dd> <dt>

*cbData* \[in\]
</dt> <dd>

A **DWORD** that indicates the size of the buffer that contains the stored data item.

</dd> <dt>

*pbData* \[in\]
</dt> <dd>

A pointer to a buffer that contains the stored data item.

</dd> <dt>

*pPromptInfo* \[in\]
</dt> <dd>

A pointer to a [**PST\_PROMPTINFO**](pst-promptinfo.md) structure.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Specifies user interface and security behaviors for the read operation.

The flag values can be combined with a logical OR.



| Value                                                                                                                                                                                                                                                              | Meaning                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PST_UNRESTRICTED_ITEMDATA"></span><span id="pst_unrestricted_itemdata"></span><dl> <dt>**PST\_UNRESTRICTED\_ITEMDATA**</dt> <dt>0x00000004</dt> </dl> | Specifies that the data stream is nonsecure. By default, item calls are secure.<br/>                                                                                                                                             |
| <span id="PST_PROMPT_QUERY"></span><span id="pst_prompt_query"></span><dl> <dt>**PST\_PROMPT\_QUERY**</dt> <dt>0x00000008</dt> </dl>                            | Specifies that the confirmation be returned upon success. If the user interface is enabled, a success of **PST\_E\_OK** is returned. If the user interface is not enabled, a value of **PST\_E\_ITEM\_EXISTS** is returned.<br/> |
| <span id="PST_NO_UI_MIGRATION"></span><span id="pst_no_ui_migration"></span><dl> <dt>**PST\_NO\_UI\_MIGRATION**</dt> <dt>0x00000010</dt> </dl>                  | Do not show user interface unless a custom password is required.<br/>                                                                                                                                                            |



 

</dd> </dl>

## Return value

The return value is an **HRESULT** value. A value of **PST\_E\_OK** indicates the function was successful.

## Remarks

If **ReadItem** completes successfully, the application is responsible for freeing the returned data buffer using the [**CoTaskMemFree**](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemfree) function.

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

 

 
