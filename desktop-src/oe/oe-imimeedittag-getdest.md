---
title: IMimeEditTag GetDest method
description: Destination is set by the MHTML packager; it is where the tag will end up after being archived into the Mime-Message.
ms.assetid: fb41617a-d4ca-4e9a-bc0e-130f858fc596
keywords:
- GetDest method Windows Mail (formerly Outlook Express)
- GetDest method Windows Mail (formerly Outlook Express) , IMimeEditTag interface
- IMimeEditTag interface Windows Mail (formerly Outlook Express) , GetDest method
topic_type:
- apiref
api_name:
- IMimeEditTag.GetDest
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

# IMimeEditTag::GetDest method

\[**IMimeEditTag::GetDest** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Destination is set by the MHTML packager; it is where the tag will end up after being archived into the Mime-Message. It might be a CID: or the original URL location. Implementors should hold onto and return this member data.

## Syntax


```C++
HRESULT GetDest(
  [out] BSTR *pbstr
);
```



## Parameters

<dl> <dt>

*pbstr* \[out\]
</dt> <dd>

Type: **BSTR\***

Specifies pointer to destination.

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



 

 





