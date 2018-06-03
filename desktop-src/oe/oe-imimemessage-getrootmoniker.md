---
title: IMimeMessage GetRootMoniker method
description: GetRootMoniker is reserved.
ms.assetid: 61feb0ef-ee35-4191-b7ac-5e39bdf72406
keywords:
- GetRootMoniker method Windows Mail (formerly Outlook Express)
- GetRootMoniker method Windows Mail (formerly Outlook Express) , IMimeMessage interface
- IMimeMessage interface Windows Mail (formerly Outlook Express) , GetRootMoniker method
topic_type:
- apiref
api_name:
- IMimeMessage.GetRootMoniker
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

# IMimeMessage::GetRootMoniker method

\[**GetRootMoniker** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

**GetRootMoniker** is reserved.

## Syntax


```C++
HRESULT GetRootMoniker(
  [out] IMoniker **ppMoniker
);
```



## Parameters

<dl> <dt>

*ppMoniker* \[out\]
</dt> <dd>

Type: **[IMoniker](http://msdn.microsoft.com/library/com/htm/cmi_m_8otu.asp)\*\***

Not used.

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



 

 





