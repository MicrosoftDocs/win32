---
title: IMimeHeaderTable GetRowInfo method
description: Gets information about a row in the header table.
ms.assetid: ddc5e867-077a-4fde-a18d-b564527c1e9b
keywords:
- GetRowInfo method Windows Mail (formerly Outlook Express)
- GetRowInfo method Windows Mail (formerly Outlook Express) , IMimeHeaderTable interface
- IMimeHeaderTable interface Windows Mail (formerly Outlook Express) , GetRowInfo method
topic_type:
- apiref
api_name:
- IMimeHeaderTable.GetRowInfo
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

# IMimeHeaderTable::GetRowInfo method

Gets information about a row in the header table.

## Syntax


```C++
HRESULT GetRowInfo(
  [in]      HHEADERROW      hRow,
  [in, out] LPHEADERROWINFO pInfo
);
```



## Parameters

<dl> <dt>

*hRow* \[in\]
</dt> <dd>

Type: **HHEADERROW**

Specifies the handle of the row to get information for.

</dd> <dt>

*pInfo* \[in, out\]
</dt> <dd>

Type: **LPHEADERROWINFO**

Receives a pointer to a [**HEADERROWINFO**](oe-headerrowinfo.md) structure that contains the information about the row.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                             |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *pInfo* is **NULL**. <br/>         |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hRow* is an invalid handle. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





