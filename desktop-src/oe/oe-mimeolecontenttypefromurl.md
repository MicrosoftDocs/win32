---
title: MimeOleContentTypeFromUrl function
description: Do not use. Returns the Content-Type for the specified URL.
ms.assetid: e7c7dcc9-e91b-4bbf-864e-ad3c9c5229ee
keywords:
- MimeOleContentTypeFromUrl function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleContentTypeFromUrl
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MimeOleContentTypeFromUrl function

Do not use. Returns the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) for the specified URL.

## Syntax


```C++
HRESULT MimeOleContentTypeFromUrl(
  _In_  LPCSTR pszBase,
  _In_  LPCSTR pszUrl,
  _Out_ LPSTR  *ppszCntType
);
```



## Parameters

<dl> <dt>

*pszBase* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the base URL.

</dd> <dt>

*pszUrl* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the relative URL.

</dd> <dt>

*ppszCntType* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to an **LPSTR** that contains the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp). Note: **LPSTR** needs to have been valid prior to call and user is responsible for freeing what is pointed to by this parameter.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                 |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that a pointer parameter is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





