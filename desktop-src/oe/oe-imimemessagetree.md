---
title: IMimeMessageTree interface
description: Do not use. Parses and creates Internet messages. IMimeMessageTree treats a message as a tree of bodies where each body has a header and associated content. It gives a client the most flexible, low-level access to a message.
ms.assetid: c36de21c-8a83-4d75-acfd-cf1440c3901a
keywords:
- IMimeMessageTree interface Windows Mail (formerly Outlook Express)
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , described
topic_type:
- apiref
api_name:
- IMimeMessageTree
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

# IMimeMessageTree interface

Do not use. Parses and creates Internet messages. **IMimeMessageTree** treats a message as a tree of bodies where each body has a header and associated content. It gives a client the most flexible, low-level access to a message.

## Members

The **IMimeMessageTree** interface inherits from [**IPersistStreamInit**](https://msdn.microsoft.com/library/windows/desktop/ms682273) but does not have additional members.

## Remarks

The [**IMimeMessage**](oe-imimemessage.md) and [**IMimeMessageW**](oe-imimemessagew.md) interfaces give a client higher-level access and are easier to use.

The persistence format for **IMimeMessageTree** is an [RFC 822](http://www.ietf.org/rfc/rfc822.txt) or [RFC 1521](http://www.ietf.org/rfc/rfc1521.txt) (MIME) message. This interface supports multiple persistence interfaces.

-   [**IPersistStreamInit**](https://msdn.microsoft.com/library/windows/desktop/ms682273): Loads and saves a message to an [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034).
-   [**IPersistFile**](https://msdn.microsoft.com/library/windows/desktop/ms687223): Loads and saves a message to a file.
-   [**IPersistMoniker**](https://msdn.microsoft.com/library/ms775042): Loads a message from a moniker.
-   [**IDataObject**](https://msdn.microsoft.com/library/windows/desktop/ms688421): Creates the ability to put various formats of the message onto the Windows clipboard.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





