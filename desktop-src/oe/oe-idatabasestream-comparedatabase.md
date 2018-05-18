---
title: IDatabaseStream CompareDatabase method
description: Determines whether a stream belongs to the given database.
ms.assetid: '608a1237-58a3-4ac2-bec1-2619d621a31b'
keywords: ["CompareDatabase method Windows Mail (formerly Outlook Express)", "CompareDatabase method Windows Mail (formerly Outlook Express) , IDatabaseStream interface", "IDatabaseStream interface Windows Mail (formerly Outlook Express) , CompareDatabase method"]
topic_type:
- apiref
api_name:
- IDatabaseStream.CompareDatabase
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabaseStream::CompareDatabase method

Determines whether a stream belongs to the given database.

## Syntax


```C++
HRESULT CompareDatabase(
  [in] IDatabase *pDatabase
);
```



## Parameters

<dl> <dt>

*pDatabase* \[in\]
</dt> <dd>

Type: **[**IDatabase**](oe-idatabase.md)\***

Specifies the database to be compared to.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                                     |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that the stream belongs to the specified database.<br/>         |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that the stream does not belong to the specified database.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





