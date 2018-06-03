---
title: IMimeHeaderTable SetRowData method
description: Sets or changes the data for a row in the header table.
ms.assetid: 6064cc70-78fb-4ed0-867c-f71b1df4ef57
keywords:
- SetRowData method Windows Mail (formerly Outlook Express)
- SetRowData method Windows Mail (formerly Outlook Express) , IMimeHeaderTable interface
- IMimeHeaderTable interface Windows Mail (formerly Outlook Express) , SetRowData method
topic_type:
- apiref
api_name:
- IMimeHeaderTable.SetRowData
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

# IMimeHeaderTable::SetRowData method

Sets or changes the data for a row in the header table.

## Syntax


```C++
HRESULT SetRowData(
  [in] HHEADERROW hRow,
  [in] DWORD      dwFlags,
  [in] LPCSTR     pszData,
  [in] ULONG      cchData
);
```



## Parameters

<dl> <dt>

*hRow* \[in\]
</dt> <dd>

Type: **HHEADERROW**

Specifies the handle of the row to set data for.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask that indicates that the name of the header is contained in *pszData*.



| Value                                                                                                                                                            | Meaning                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="HTF_NAMEINDATA"></span><span id="htf_nameindata"></span><dl> <dt>**HTF\_NAMEINDATA**</dt> </dl> | Indicates that the name of the header is contained in the header data. For example, "*Subject*: This is the subject data." The name in the data is "*Subject*:".<br/> |



 

</dd> <dt>

*pszData* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the data to set for this row.

</dd> <dt>

*cchData* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the number of characters in *pszData*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                                                                                                                                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *pszData* is **NULL** and *cchData* is not zero. Also may indicate that *pszData* is **NULL** and **HTF\_NAMEINDATA** is not specified in *dwFlags*. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Indicates that an attempt to allocate memory failed. <br/>                                                                                                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that an unknown error has occurred.<br/>                                                                                                                        |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hRow* is an invalid handle.<br/>                                                                                                                          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





