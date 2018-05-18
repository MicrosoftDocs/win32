---
title: IDatabase ChangeStreamLock method
description: Will change the access type for the specified stream.
ms.assetid: '22e38b76-72d0-49f5-9a92-c33aa428fef0'
keywords: ["ChangeStreamLock method Windows Mail (formerly Outlook Express)", "ChangeStreamLock method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , ChangeStreamLock method"]
topic_type:
- apiref
api_name:
- IDatabase.ChangeStreamLock
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::ChangeStreamLock method

\[**ChangeStreamLock** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Will change the access type for the specified stream.

## Syntax


```C++
HRESULT ChangeStreamLock(
  [in] IStream    *pStream,
  [in] ACCESSTYPE tyAccessNew
);
```



## Parameters

<dl> <dt>

*pStream* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

The stream to change the access type on.

</dd> <dt>

*tyAccessNew* \[in\]
</dt> <dd>

Type: **[**ACCESSTYPE**](oe-accesstype.md)**

The new access type to request.

</dd> </dl>

## Return value

Type: **HRESULT**

Use the SUCCEEDED macro to determine whether the operation succeeded.



| Return code                                                                                         | Description                                             |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>**DB\_E\_LOCKEDFORREAD**</dt> </dl> | Read access is held by more than one reader.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





