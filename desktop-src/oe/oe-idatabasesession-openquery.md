---
title: IDatabaseSession OpenQuery method
description: This function is not supported.
ms.assetid: dd41f939-30b6-45ef-ae3d-bac3a1d2914e
keywords:
- OpenQuery method Windows Mail (formerly Outlook Express)
- OpenQuery method Windows Mail (formerly Outlook Express) , IDatabaseSession interface
- IDatabaseSession interface Windows Mail (formerly Outlook Express) , OpenQuery method
topic_type:
- apiref
api_name:
- IDatabaseSession.OpenQuery
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

# IDatabaseSession::OpenQuery method

This function is not supported.

## Syntax


```C++
HRESULT OpenQuery(
  [in] IDatabase *pDatabase,
  [in] LPCSTR    pszQuery,
  [in] LPVOID    pReserved
);
```



## Parameters

<dl> <dt>

*pDatabase* \[in\]
</dt> <dd>

Type: **[**IDatabase**](oe-idatabase.md)\***

The database to query.

</dd> <dt>

*pszQuery* \[in\]
</dt> <dd>

Type: **LPCSTR**

The query string.

</dd> <dt>

*pReserved* \[in\]
</dt> <dd>

Type: **LPVOID**

Reserved data.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                               | Description                                 |
|-------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The function is not implemented.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





