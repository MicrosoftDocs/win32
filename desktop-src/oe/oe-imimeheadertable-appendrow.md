---
title: IMimeHeaderTable AppendRow method
description: Appends a new row to the header table.
ms.assetid: e7f4e98c-929a-48bf-b8d2-455ac006eb94
keywords:
- AppendRow method Windows Mail (formerly Outlook Express)
- AppendRow method Windows Mail (formerly Outlook Express) , IMimeHeaderTable interface
- IMimeHeaderTable interface Windows Mail (formerly Outlook Express) , AppendRow method
topic_type:
- apiref
api_name:
- IMimeHeaderTable.AppendRow
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

# IMimeHeaderTable::AppendRow method

Appends a new row to the header table.

## Syntax


```C++
HRESULT AppendRow(
  [in]  LPCSTR       pszHeader,
  [in]  DWORD        dwFlags,
  [in]  LPCSTR       pszData,
  [in]  ULONG        cchData,
  [out] LPHHEADERROW phRow
);
```



## Parameters

<dl> <dt>

*pszHeader* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the name of the header to append when **HTF\_NAMEINDATA** is not specified in *dwFlags*.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask that indicates that the subject is located in the header data.



| Value                                                                                                                                                            | Meaning                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="HTF_NAMEINDATA"></span><span id="htf_nameindata"></span><dl> <dt>**HTF\_NAMEINDATA**</dt> </dl> | Indicates that the name of the header is contained in the header data. For example, "*Subject*: This is the subject data." The name in the data is "*Subject*:".<br/> |



 

</dd> <dt>

*pszData* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies a **LPCSTR** that contains the header data.

</dd> <dt>

*cchData* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that indicates the number of characters in *pszData*.

</dd> <dt>

*phRow* \[out\]
</dt> <dd>

Type: **LPHHEADERROW**

Receives the handle of the new row.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                                                                                                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszData* is **NULL** and *cchData* is not zero. Also may indicate that *pszHeader* is **NULL** and **HTF\_NAMEINDATA** is not specified in *dwFlags*. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>                                                                                                                  |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





