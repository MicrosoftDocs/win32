---
title: IDatabase SetSize method
description: Sets the size of the database.
ms.assetid: '9b8fed0b-3184-4b4d-a2d2-33793aeb6c9a'
keywords: ["SetSize method Windows Mail (formerly Outlook Express)", "SetSize method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , SetSize method"]
topic_type:
- apiref
api_name:
- IDatabase.SetSize
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::SetSize method

\[**SetSize** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sets the size of the database. Will have no effect if cbSize is less than the size of the database currently.

## Syntax


```C++
HRESULT SetSize(
  [in] DWORD cbSize
);
```



## Parameters

<dl> <dt>

*cbSize* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the new size of the database.

</dd> </dl>

## Return value

Type: **HRESULT**

Use the SUCCEEDED macro to determine whether the operation succeeded.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





