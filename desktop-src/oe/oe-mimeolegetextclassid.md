---
title: MimeOleGetExtClassId function
description: Do not use. On success, returns the class ID for a given file name extension string.
ms.assetid: 9c6115eb-97f5-44c2-9b5b-3138ca22fa35
keywords:
- MimeOleGetExtClassId function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetExtClassId
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

# MimeOleGetExtClassId function

Do not use. On success, returns the class ID for a given file name extension string.

## Syntax


```C++
HRESULT MimeOleGetExtClassId(
  _In_  LPCSTR  pszExtension,
  _Out_ LPCLSID pclsid
);
```



## Parameters

<dl> <dt>

*pszExtension* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies a file name extension as a string.

</dd> <dt>

*pclsid* \[out\]
</dt> <dd>

Type: **LPCLSID**

Returns a class ID pointer. NOTE: user is responsible for freeing pointer.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                                       |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success. <br/>                                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that pointer argument is **NULL**. <br/>                          |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that file name extension is not recognized in the registry. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates data not returned. <br/>                                          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





