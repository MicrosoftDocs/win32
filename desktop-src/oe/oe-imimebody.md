---
title: IMimeBody interface
description: Do not use. Manipulates the header and contents of a message body.
ms.assetid: d21434f2-c65e-4640-bb60-8dce4568d363
keywords:
- IMimeBody interface Windows Mail (formerly Outlook Express)
- IMimeBody interface Windows Mail (formerly Outlook Express) , described
topic_type:
- apiref
api_name:
- IMimeBody
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IMimeBody interface

Do not use. Manipulates the header and contents of a message body.

## Members

The **IMimeBody** interface inherits from [**IMimePropertySet**](oe-imimepropertyset.md) but does not have additional members.

## Remarks

There are multiple ways in which a client can obtain an **IMimeBody** object:

-   By calling [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) (**IMimeBody** supports aggregation), for example:

    `CoCreateInstance(CLSID_IMimeBody, NULL, CLSCTX_INPROC_SERVER, IID_IMimeBody, (LPVOID *)&pBody);`

-   By using an [**IMimeMessage**](oe-imimemessage.md) or [**IMimeMessageTree**](oe-imimemessagetree.md) object, for example:

    `IMimeMessage::BindToObject(hBody, IID_IMimeBody, (LPVOID *)&pBody);`

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





