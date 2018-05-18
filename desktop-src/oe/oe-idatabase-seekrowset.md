---
title: IDatabase SeekRowset method
description: Moves the current position within the rowset.
ms.assetid: 'c7791e59-4849-4674-9e11-c36fd4eac745'
keywords: ["SeekRowset method Windows Mail (formerly Outlook Express)", "SeekRowset method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , SeekRowset method"]
topic_type:
- apiref
api_name:
- IDatabase.SeekRowset
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::SeekRowset method

\[**SeekRowset** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Moves the current position within the rowset.

## Syntax


```C++
HRESULT SeekRowset(
  [in]  HROWSET        hRowset,
  [in]  SEEKROWSETTYPE tySeek,
  [in]  LONG           cRows,
  [out] LPROWORDINAL   piRowNew
);
```



## Parameters

<dl> <dt>

*hRowset* \[in\]
</dt> <dd>

Type: **HROWSET**

Specifies the Rowset that will be used.

</dd> <dt>

*tySeek* \[in\]
</dt> <dd>

Type: **[**SEEKROWSETTYPE**](oe-seekrowsettype.md)**

Specifies how the current position will be moved.

</dd> <dt>

*cRows* \[in\]
</dt> <dd>

Type: **LONG**

Specifies how far to move the current position in the rowset. If SEEK\_ROWSET\_BEGIN or SEEK\_ROWSET\_END is specified, cRows will specify an offset from the beginning or the end of the rows in the set.

</dd> <dt>

*piRowNew* \[out\]
</dt> <dd>

Type: **LPROWORDINAL**

Optional. Will return the current position of the rowset. Counting starts at 1.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following codes. Use the SUCCEEDED macro to determine whether the operation succeeded.



| Return code                                                                                     | Description                                              |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**SUCCEEDED**</dt> </dl>        | The operation succeeded.<br/>                      |
| <dl> <dt>**DB\_E\_NORECORDS**</dt> </dl> | Indicates there are no records in the Rowset.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





