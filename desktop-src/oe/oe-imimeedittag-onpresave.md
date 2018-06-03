---
title: IMimeEditTag OnPreSave method
description: Called by the packer before the document is persisted.
ms.assetid: 60d484f7-5192-4ed9-9069-a32b13c3028b
keywords:
- OnPreSave method Windows Mail (formerly Outlook Express)
- OnPreSave method Windows Mail (formerly Outlook Express) , IMimeEditTag interface
- IMimeEditTag interface Windows Mail (formerly Outlook Express) , OnPreSave method
topic_type:
- apiref
api_name:
- IMimeEditTag.OnPreSave
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

# IMimeEditTag::OnPreSave method

\[**IMimeEditTag::OnPreSave** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Called by the packer before the document is persisted. The tag removes any temporary state and changes its data parameters to point to the destination, if set.

## Syntax


```C++
HRESULT OnPreSave();
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



 

 





