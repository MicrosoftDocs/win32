---
title: IHashTable Replace method
description: On success, replaces a specified table entry.
ms.assetid: 7fba486a-bf36-4ea7-aa51-6ad76b54b246
keywords:
- Replace method Windows Mail (formerly Outlook Express)
- Replace method Windows Mail (formerly Outlook Express) , IHashTable interface
- IHashTable interface Windows Mail (formerly Outlook Express) , Replace method
topic_type:
- apiref
api_name:
- IHashTable.Replace
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IHashTable::Replace method

\[**IHashTable::Replace** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

On success, replaces a specified table entry.

## Syntax


```C++
HRESULT Replace(
  [in] LPCSTR psz,
  [in] LPVOID pv
);
```



## Parameters

<dl> <dt>

*psz* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies table entry to be replaced.

</dd> <dt>

*pv* \[in\]
</dt> <dd>

Type: **LPVOID**

Specifies the replacing entry.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The entry is replaced. <br/>                              |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





