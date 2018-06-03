---
title: IHashTable Next method
description: Fetches table entries.
ms.assetid: 73127ec3-71db-420d-b3db-1a2b0713be5b
keywords:
- Next method Windows Mail (formerly Outlook Express)
- Next method Windows Mail (formerly Outlook Express) , IHashTable interface
- IHashTable interface Windows Mail (formerly Outlook Express) , Next method
topic_type:
- apiref
api_name:
- IHashTable.Next
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IHashTable::Next method

\[**IHashTable::Next** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Fetches table entries.

## Syntax


```C++
HRESULT Next(
  [in]      ULONG    cFetch,
  [in, out] LPVOID** **prgpv,
  [out]     ULONG*   *pcFetched
);
```



## Parameters

<dl> <dt>

*cFetch* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the desired number of entries.

</dd> <dt>

*prgpv* \[in, out\]
</dt> <dd>

Type: **LPVOID\*\*\*\***

Specifies an array of table entries.

</dd> <dt>

*pcFetched* \[out\]
</dt> <dd>

Type: **ULONG\*\***

Specifies the number of entries returned.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                              |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method retrieved the number of entries specified by *cFetch*. <br/>            |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | The method retrieved fewer than the number of entries specified by *cFetch*. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | No entries were retrieved.<br/>                                                    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | An attempt to allocate memory failed.<br/>                                         |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





