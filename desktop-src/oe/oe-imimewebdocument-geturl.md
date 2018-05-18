---
title: IMimeWebDocument GetURL method
description: Called by MimeOLE to get a URL for the Web document.
ms.assetid: '878cd230-1193-4123-bbba-9b55f9d0a274'
keywords: ["GetURL method Windows Mail (formerly Outlook Express)", "GetURL method Windows Mail (formerly Outlook Express) , IMimeWebDocument interface", "IMimeWebDocument interface Windows Mail (formerly Outlook Express) , GetURL method"]
topic_type:
- apiref
api_name:
- IMimeWebDocument.GetURL
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeWebDocument::GetURL method

\[**IMimeWebDocument::GetURL** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Called by MimeOLE to get a URL for the Web document. The client should return the URL associated with the Web document.

## Syntax


```C++
HRESULT GetURL(
  [out] LPSTR *ppszURL
);
```



## Parameters

<dl> <dt>

*ppszURL* \[out\]
</dt> <dd>

Type: **LPSTR\***

On success, contains a pointer to the URL for the Web document. The caller is responsible for freeing this pointer.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                            | Description                                                      |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Indicates success. <br/>                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Indicates that there is no URL for the Web document. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





