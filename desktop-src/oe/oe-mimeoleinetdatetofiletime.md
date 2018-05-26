---
title: MimeOleInetDateToFileTime function
description: Do not use. On success, creates a file time from a specified Internet date. Input is in RFC822 format \ 0034;ddd, dd mmm yyyy hh mm ss +/- hhmm\\0 \ 0034;, such as \ 0034;Tue, 21 Jan 1997 18 25 40 GMT \ 0034;. On failure, created file time defaults to current system time.
ms.assetid: 9afae9dd-6a38-43dd-a010-6eb5a9982021
keywords:
- MimeOleInetDateToFileTime function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleInetDateToFileTime
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MimeOleInetDateToFileTime function

Do not use. On success, creates a file time from a specified Internet date. Input is in RFC822 format: "ddd, dd mmm yyyy hh:mm:ss +/- hhmm\\0", such as "Tue, 21 Jan 1997 18:25:40 GMT". On failure, created file time defaults to current system time.

## Syntax


```C++
HRESULT MimeOleInetDateToFileTime(
  _In_  LPCSTR     pszDate,
  _Out_ LPFILETIME pft
);
```



## Parameters

<dl> <dt>

*pszDate* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies a **null**-terminated string containing the Internet date.

</dd> <dt>

*pft* \[out\]
</dt> <dd>

Type: **LPFILETIME**

Returns a [FILETIME](http://msdn.microsoft.com/library/com/htm/cms_a2z_3vdx.asp) structure containing the file time.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                           |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates *pszDate* or *pft* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





