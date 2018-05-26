---
title: MimeOleSetDefaultCharset function
description: Do not use. Sets default character set to the specified value (on success).
ms.assetid: 1027e939-19a0-41c1-b32f-35df31fe75c4
keywords:
- MimeOleSetDefaultCharset function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleSetDefaultCharset
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

# MimeOleSetDefaultCharset function

Do not use. Sets default character set to the specified value (on success).

## Syntax


```C++
HRESULT MimeOleSetDefaultCharset(
  _In_ HCHARSET hCharset
);
```



## Parameters

<dl> <dt>

*hCharset* \[in\]
</dt> <dd>

Type: **HCHARSET**

Specifies handle of character set to be made default.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                       |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                     |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hCharset* is invalid. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





