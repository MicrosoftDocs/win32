---
title: IHashTable Insert method
description: Inserts a table entry or replaces the data of an existing entry.
ms.assetid: '97a0bbc8-79a3-41a0-bfdc-99827d565a0b'
keywords: ["Insert method Windows Mail (formerly Outlook Express)", "Insert method Windows Mail (formerly Outlook Express) , IHashTable interface", "IHashTable interface Windows Mail (formerly Outlook Express) , Insert method"]
topic_type:
- apiref
api_name:
- IHashTable.Insert
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IHashTable::Insert method

\[**IHashTable::Insert** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Inserts a table entry or replaces the data of an existing entry.

## Syntax


```C++
HRESULT Insert(
  [in] LPCSTR psz,
  [in] LPVOID pv,
  [in] DWORD  dwFlags
);
```



## Parameters

<dl> <dt>

*psz* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the table entry to insert.

</dd> <dt>

*pv* \[in\]
</dt> <dd>

Type: **LPVOID**

Specifies the entry data.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask of HF\_xxx flags.



| Value                                                                                                                                                                                                                                   | Meaning                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="HF_NO_DUPLICATES"></span><span id="hf_no_duplicates"></span><dl> <dt>**HF\_NO\_DUPLICATES**</dt> <dt>0x00000001</dt> </dl> | If duplicate entry exists, replaces old data with new data.<br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                            | Description                                         |
|----------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Data of an existing entry was replaced. <br/> |
| <dl> <dt>**NOERROR**</dt> </dl> | New entry was inserted into table. <br/>      |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





