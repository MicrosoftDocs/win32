---
title: IMimeEditTag IsValidMimeType method
description: Called by the packer to validate a mime-type.
ms.assetid: b671aa37-cbf9-4df3-9dac-4474782a1bd1
keywords:
- IsValidMimeType method Windows Mail (formerly Outlook Express)
- IsValidMimeType method Windows Mail (formerly Outlook Express) , IMimeEditTag interface
- IMimeEditTag interface Windows Mail (formerly Outlook Express) , IsValidMimeType method
topic_type:
- apiref
api_name:
- IMimeEditTag.IsValidMimeType
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

# IMimeEditTag::IsValidMimeType method

\[**IMimeEditTag::IsValidMimeType** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Called by the packer to validate a mime-type.

## Syntax


```C++
HRESULT IsValidMimeType(
  [in] LPWSTR pszTypeW
);
```



## Parameters

<dl> <dt>

*pszTypeW* \[in\]
</dt> <dd>

Type: **LPWSTR**

Specifies a mime type.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





