---
title: MimeOleGetDefaultCharset function
description: Do not use. Returns the default charset.
ms.assetid: 8d0f09b1-2031-451e-b35c-bbcf74bd5a46
keywords:
- MimeOleGetDefaultCharset function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetDefaultCharset
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

# MimeOleGetDefaultCharset function

Do not use. Returns the default charset.

## Syntax


```C++
HRESULT MimeOleGetDefaultCharset(
  _Out_ LPHCHARSET phCharset
);
```



## Parameters

<dl> <dt>

*phCharset* \[out\]
</dt> <dd>

Type: **LPHCHARSET**

Receives the handle of the default character set.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                  |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that *phCharset* has not yet been set. <br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *phCharset* is **NULL**. <br/>          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





