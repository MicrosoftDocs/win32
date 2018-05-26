---
title: IMimeEditTag SetSrc method
description: Sets the source attributes on a tag.
ms.assetid: 2da034d3-d3f5-4719-99b4-ef88337eb5d3
keywords:
- SetSrc method Windows Mail (formerly Outlook Express)
- SetSrc method Windows Mail (formerly Outlook Express) , IMimeEditTag interface
- IMimeEditTag interface Windows Mail (formerly Outlook Express) , SetSrc method
topic_type:
- apiref
api_name:
- IMimeEditTag.SetSrc
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

# IMimeEditTag::SetSrc method

\[**IMimeEditTag::SetSrc** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sets the source attributes on a tag. This is tag-specific and is where the data is coming from. Implementors should adjust the HTML source accordingly.

## Syntax


```C++
HRESULT SetSrc(
  [in] BSTR bstr
);
```



## Parameters

<dl> <dt>

*bstr* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the source.

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



 

 





