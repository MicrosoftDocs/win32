---
title: IDatabase QueryRowset method
description: Retrieves the values for a number of rows from the rowset.
ms.assetid: '184d4d57-0b17-4674-81bf-d01c74c25401'
keywords: ["QueryRowset method Windows Mail (formerly Outlook Express)", "QueryRowset method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , QueryRowset method"]
topic_type:
- apiref
api_name:
- IDatabase.QueryRowset
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::QueryRowset method

\[**QueryRowset** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the values for a number of rows from the rowset.

## Syntax


```C++
HRESULT QueryRowset(
  [in]      HROWSET hRowset,
  [in, out] LPVOID  prgpRecord,
  [out]     LPDWORD pcObtained
);
```



## Parameters

<dl> <dt>

*hRowset* \[in\]
</dt> <dd>

Type: **HROWSET**

Specifies the Rowset that will be used.

</dd> <dt>

*prgpRecord* \[in, out\]
</dt> <dd>

Type: **LPVOID**

Specifies a caller-allocated buffer large enough to contain the desired number of records.

</dd> <dt>

*pcObtained* \[out\]
</dt> <dd>

Type: **LPDWORD**

Specifies the number of records that were returned.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following codes. Use the SUCCEEDED macro to determine whether the operation succeeded.



| Return code                                                                             | Description                                    |
|-----------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | The operation succeeded.<br/>            |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates 0 records were retrieved.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





