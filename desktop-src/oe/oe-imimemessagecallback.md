---
title: IMimeMessageCallback interface
description: This interface is implemented by the client and allows it to modify the way MimeOLE renders a message by inserting streams between message parts.
ms.assetid: 1193ee40-04c8-49b9-8efb-4689541e8385
keywords:
- IMimeMessageCallback interface Windows Mail (formerly Outlook Express)
- IMimeMessageCallback interface Windows Mail (formerly Outlook Express) , described
topic_type:
- apiref
api_name:
- IMimeMessageCallback
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMimeMessageCallback interface

\[**IMimeMessageCallback** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This interface is implemented by the client and allows it to modify the way MimeOLE renders a message by inserting streams between message parts. A client passes a pointer to its implementation of this interface when calling [**CreateWebPage**](oe-imimemessage-createwebpage.md).

## Members

The **IMimeMessageCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





