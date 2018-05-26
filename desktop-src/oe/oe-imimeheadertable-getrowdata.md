---
title: IMimeHeaderTable GetRowData method
description: Gets the data associated with a row in the header table.
ms.assetid: 36ddb7e3-0f27-4369-a672-6e582b0dd16a
keywords:
- GetRowData method Windows Mail (formerly Outlook Express)
- GetRowData method Windows Mail (formerly Outlook Express) , IMimeHeaderTable interface
- IMimeHeaderTable interface Windows Mail (formerly Outlook Express) , GetRowData method
topic_type:
- apiref
api_name:
- IMimeHeaderTable.GetRowData
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

# IMimeHeaderTable::GetRowData method

Gets the data associated with a row in the header table.

## Syntax


```C++
HRESULT GetRowData(
  [in]  HHEADERROW hRow,
  [in]  DWORD      dwFlags,
  [out] LPSTR      *ppszData,
  [out] ULONG      *pcchData
);
```



## Parameters

<dl> <dt>

*hRow* \[in\]
</dt> <dd>

Type: **HHEADERROW**

Specifies the handle of the row to get data for.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask that indicates that the name of the header is returned in the data.



| Value                                                                                                                                                            | Meaning                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="HTF_NAMEINDATA"></span><span id="htf_nameindata"></span><dl> <dt>**HTF\_NAMEINDATA**</dt> </dl> | Indicates that the name of the header is contained in the header data. For example, "*Subject*: This is the subject data." The name in the data is "*Subject*:".<br/> |



 

</dd> <dt>

*ppszData* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to an **LPSTR** that contains the header row data. The client is responsible for freeing this pointer by calling [IMalloc::Free](http://msdn.microsoft.com/library/com/htm/cmi_m_1smd.asp).

</dd> <dt>

*pcchData* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the number of characters stored in the string pointed to by *ppszData*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                      |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                                    |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hRow* is an invalid handle. <br/>          |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Indicates that an attempt to allocate memory failed. <br/> |



 

## Remarks

The data returned from this method is in an Internet codepage and may be wrapped according to [RFC 822](http://www.ietf.org/rfc/rfc822.txt). Using this method, the client can get an untouched header from the message.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





