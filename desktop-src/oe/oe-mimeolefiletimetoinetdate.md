---
title: MimeOleFileTimeToInetDate function
description: Do not use. Creates an internet date from a specified file time. Output is in RFC822 format \ 0034;ddd, dd mmm yyyy hh mm ss +/- hhmm\\0 \ 0034;, such as \ 0034;Tue, 21 Jan 1997 18 25 40 GMT \ 0034;.
ms.assetid: 'aa8fb686-2686-4362-84f1-f7e5d28a9e4a'
keywords: ["MimeOleFileTimeToInetDate function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleFileTimeToInetDate
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleFileTimeToInetDate function

Do not use. Creates an internet date from a specified file time. Output is in RFC822 format: "ddd, dd mmm yyyy hh:mm:ss +/- hhmm\\0", such as "Tue, 21 Jan 1997 18:25:40 GMT".

## Syntax


```C++
HRESULT MimeOleFileTimeToInetDate(
  _In_    LPFILETIME pft,
  _Inout_ LPSTR      pszDate,
  _In_    ULONG      cchMax
);
```



## Parameters

<dl> <dt>

*pft* \[in\]
</dt> <dd>

Type: **LPFILETIME**

Specifies a [FILETIME](http://msdn.microsoft.com/library/com/htm/cms_a2z_3vdx.asp) structure.

</dd> <dt>

*pszDate* \[in, out\]
</dt> <dd>

Type: **LPSTR**

Specifies a **null**-terminated string to receive the Internet date.

</dd> <dt>

*cchMax* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the buffer size of *pszDate*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                | Description                                           |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Indicates success. <br/>                        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | Indicates *pszDate* or *pft* is **NULL**. <br/> |
| <dl> <dt>**MIME\_E\_BUFFER\_TOO\_SMALL**</dt> </dl> | Indicates buffer too small. <br/>               |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





