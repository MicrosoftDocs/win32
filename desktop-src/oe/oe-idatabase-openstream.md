---
title: IDatabase OpenStream method
description: Opens a stream for access.
ms.assetid: 'a527bff4-d8a3-4bdc-8d96-db3fa2bc4176'
keywords: ["OpenStream method Windows Mail (formerly Outlook Express)", "OpenStream method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , OpenStream method"]
topic_type:
- apiref
api_name:
- IDatabase.OpenStream
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::OpenStream method

\[**OpenStream** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Opens a stream for access.

## Syntax


```C++
HRESULT OpenStream(
  [in]  ACCESSTYPE  tyAccess,
  [in]  FILEADDRESS faStream,
  [out] IStream     **ppStream
);
```



## Parameters

<dl> <dt>

*tyAccess* \[in\]
</dt> <dd>

Type: **[**ACCESSTYPE**](oe-accesstype.md)**

Specifies the access level being requested.

</dd> <dt>

*faStream* \[in\]
</dt> <dd>

Type: **FILEADDRESS**

Specifies the stream to open.

</dd> <dt>

*ppStream* \[out\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\*\***

On success, contains the stream identifier for the new stream in the database specified by faStream.

</dd> </dl>

## Return value

Type: **HRESULT**

Use the SUCCEEDED macro to determine whether the operation succeeded.



| Return code                                                                                           | Description                                                                    |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>**DB\_E\_LOCKEDFORREAD**</dt> </dl>   | Write access is requested and the stream is currently opened.<br/>       |
| <dl> <dt>**DB\_E\_LOCKEDFORWRITE**</dt> </dl>  | Write access is requested and the stream is already open for write.<br/> |
| <dl> <dt>**DB\_E\_STREAMTABLEFULL**</dt> </dl> | There are too many streams open.<br/>                                    |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





