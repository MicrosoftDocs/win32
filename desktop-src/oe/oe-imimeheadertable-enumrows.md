---
title: IMimeHeaderTable EnumRows method
description: Creates an enumerator object for enumerating the rows in the header table object.
ms.assetid: 6e668410-5d67-4c66-8ec3-8c85b2107875
keywords:
- EnumRows method Windows Mail (formerly Outlook Express)
- EnumRows method Windows Mail (formerly Outlook Express) , IMimeHeaderTable interface
- IMimeHeaderTable interface Windows Mail (formerly Outlook Express) , EnumRows method
topic_type:
- apiref
api_name:
- IMimeHeaderTable.EnumRows
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

# IMimeHeaderTable::EnumRows method

Creates an enumerator object for enumerating the rows in the header table object.

## Syntax


```C++
HRESULT EnumRows(
  [in]  LPCSTR              pszHeader,
  [in]  DWORD               dwFlags,
  [out] IMimeEnumHeaderRows **ppEnum
);
```



## Parameters

<dl> <dt>

*pszHeader* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a string to compare header names against. Only rows whose header names match this value are enumerated. All rows are enumerated when this parameter is **NULL**.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask that indicates the type of data to return.



| Value                                                                                                                                                                           | Meaning                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <span id="HTF_ENUMHANDLESONLY"></span><span id="htf_enumhandlesonly"></span><dl> <dt>**HTF\_ENUMHANDLESONLY**</dt> </dl> | Indicates that only rows handles (no data) should be returned in the enumeration.<br/> |



 

</dd> <dt>

*ppEnum* \[out\]
</dt> <dd>

Type: **[**IMimeEnumHeaderRows**](oe-imimeenumheaderrows.md)\*\***

Receives the address of a pointer to a [**IMimeEnumHeaderRows**](oe-imimeenumheaderrows.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppEnum* is **NULL**. <br/>                 |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/> |



 

## Remarks

Rows are enumerated in the order in which they would appear in a saved header.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





