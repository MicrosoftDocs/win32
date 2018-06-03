---
title: IMimeHeaderTable CountRows method
description: Counts the number of rows whose header name matches the specified string.
ms.assetid: a19179a5-7f0a-4044-b058-d165ca721ed9
keywords:
- CountRows method Windows Mail (formerly Outlook Express)
- CountRows method Windows Mail (formerly Outlook Express) , IMimeHeaderTable interface
- IMimeHeaderTable interface Windows Mail (formerly Outlook Express) , CountRows method
topic_type:
- apiref
api_name:
- IMimeHeaderTable.CountRows
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

# IMimeHeaderTable::CountRows method

Counts the number of rows whose header name matches the specified string.

## Syntax


```C++
HRESULT CountRows(
  [in]  LPCSTR pszHeader,
  [out] ULONG  *pcRows
);
```



## Parameters

<dl> <dt>

*pszHeader* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies a **LPCSTR** that contains the string to compare against the header name.

</dd> <dt>

*pcRows* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the number of rows.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pcRows* is **NULL**. <br/> |



 

## Remarks

This method counts the total number of rows in the header table when *pszHeader* is **NULL**.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





