---
title: IMimeBodyW interface
description: Do not use. Manipulates the header and contents of a message body. The methods of IMimeBodyW support Unicode.
ms.assetid: 'e7fc2b55-7b49-432d-a4c3-415d3abf8a36'
keywords: ["IMimeBodyW interface Windows Mail (formerly Outlook Express)", "IMimeBodyW interface Windows Mail (formerly Outlook Express) , described"]
topic_type:
- apiref
api_name:
- IMimeBodyW
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeBodyW interface

Do not use. Manipulates the header and contents of a message body. The methods of **IMimeBodyW** support Unicode.

## Members

The **IMimeBodyW** interface inherits from [**IMimeBody**](oe-imimebody.md) but does not have additional members.

## Remarks

There are multiple ways in which a client can obtain an [**IMimeBody**](oe-imimebody.md) object:

-   By calling [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) (**IMimeBodyW** supports aggregation), for example:

    `CoCreateInstance(CLSID_IMimeBodyW, NULL, CLSCTX_INPROC_SERVER, IID_IMimeBodyW, (LPVOID*)&pBody);`

-   By using an [**IMimeMessage**](oe-imimemessage.md) or [**IMimeMessageTree**](oe-imimemessagetree.md) object, for example:

    `IMimeMessage::BindToObject(hBody, IID_IMimeBodyW, (LPVOID*)&pBody);`

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





