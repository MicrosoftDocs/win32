---
title: IDatabase CopyStream method
description: Copies a stream to the specified database and stream.
ms.assetid: dd7b8bf6-811c-49a5-92fa-01e6fa88568f
keywords:
- CopyStream method Windows Mail (formerly Outlook Express)
- CopyStream method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , CopyStream method
topic_type:
- apiref
api_name:
- IDatabase.CopyStream
api_location:
- Directdb.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDatabase::CopyStream method

\[**CopyStream** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Copies a stream to the specified database and stream.

## Syntax


```C++
HRESULT CopyStream(
  [in]  IDatabase     iDest,
  [in]  FILEADDRESS   faStream,
  [out] LPFILEADDRESS pfaNew
);
```



## Parameters

<dl> <dt>

*iDest* \[in\]
</dt> <dd>

Type: **[**IDatabase**](oe-idatabase.md)**

Specifies the database to copy the stream to.

</dd> <dt>

*faStream* \[in\]
</dt> <dd>

Type: **FILEADDRESS**

Identifies the stream to be copied from the database.

</dd> <dt>

*pfaNew* \[out\]
</dt> <dd>

Type: **LPFILEADDRESS**

On success, contains the stream identifier for the new stream in the database specified by pDest.

</dd> </dl>

## Return value

Type: **HRESULT**

Use the SUCCEEDED macro to determine whether the operation succeeded.



| Return code                                                                                          | Description                                                  |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                 | The index successfully deleted.<br/>                   |
| <dl> <dt>**D\_E\_STREAMTABLEFULL**</dt> </dl> | Indicates that too many streams are already open.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





