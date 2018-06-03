---
title: IMimeEditTag SetDest method
description: Sets the destination.
ms.assetid: 0920cedb-49c0-4f2a-8925-cb1c55d5e854
keywords:
- SetDest method Windows Mail (formerly Outlook Express)
- SetDest method Windows Mail (formerly Outlook Express) , IMimeEditTag interface
- IMimeEditTag interface Windows Mail (formerly Outlook Express) , SetDest method
topic_type:
- apiref
api_name:
- IMimeEditTag.SetDest
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

# IMimeEditTag::SetDest method

\[**IMimeEditTag::SetDest** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sets the destination.

## Syntax


```C++
HRESULT SetDest(
  [in] BSTR bstr
);
```



## Parameters

<dl> <dt>

*bstr* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the destination.

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



 

 





