---
title: IMimeHeaderTable FindNextRow method
description: Continues to iterate through the rows in the header table.
ms.assetid: 3c7f6c4d-ec9b-481f-87b2-8d26ab2ed68d
keywords:
- FindNextRow method Windows Mail (formerly Outlook Express)
- FindNextRow method Windows Mail (formerly Outlook Express) , IMimeHeaderTable interface
- IMimeHeaderTable interface Windows Mail (formerly Outlook Express) , FindNextRow method
topic_type:
- apiref
api_name:
- IMimeHeaderTable.FindNextRow
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

# IMimeHeaderTable::FindNextRow method

Continues to iterate through the rows in the header table.

## Syntax


```C++
HRESULT FindNextRow(
  [in]  LPFINDHEADER pFindHeader,
  [out] LPHHEADERROW phRow
);
```



## Parameters

<dl> <dt>

*pFindHeader* \[in\]
</dt> <dd>

Type: **LPFINDHEADER**

Specifies a pointer to a [**FINDHEADER**](oe-findheader.md) structure.

</dd> <dt>

*phRow* \[out\]
</dt> <dd>

Type: **LPHHEADERROW**

Receives the handle of the header row.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                                   |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success.<br/>                                                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pFindHeader* or *phRow* is **NULL**. <br/>              |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that *phRow* is invalid because there are no more rows. <br/> |



 

## Remarks

A client must call [**IMimeHeaderTable::FindFirstRow**](oe-imimeheadertable-findfirstrow.md) before calling this method.

If *pFindHeader*-&gt;**pszHeader** is **NULL**, all the rows in the header table are iterated. Otherwise, only the headers whose names match *pFindHeader*-&gt;**pszHeader** are enumerated.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





