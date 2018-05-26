---
title: IMimeEditTag OnPostSave method
description: Called after the packer has saved the document.
ms.assetid: df506119-b956-400d-82fb-ae579738b972
keywords:
- OnPostSave method Windows Mail (formerly Outlook Express)
- OnPostSave method Windows Mail (formerly Outlook Express) , IMimeEditTag interface
- IMimeEditTag interface Windows Mail (formerly Outlook Express) , OnPostSave method
topic_type:
- apiref
api_name:
- IMimeEditTag.OnPostSave
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

# IMimeEditTag::OnPostSave method

\[**IMimeEditTag::OnPostSave** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Called after the packer has saved the document. The tag restores its temporary state and reverts back to the original source URL.

## Syntax


```C++
HRESULT OnPostSave();
```



## Parameters

This method has no parameters.

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



 

 





