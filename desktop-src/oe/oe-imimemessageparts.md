---
title: IMimeMessageParts interface
description: Do not use. Manages a partial message collection.
ms.assetid: '479e54e8-2cde-4b23-8a34-1fca4148873c'
keywords: ["IMimeMessageParts interface Windows Mail (formerly Outlook Express)", "IMimeMessageParts interface Windows Mail (formerly Outlook Express) , described"]
topic_type:
- apiref
api_name:
- IMimeMessageParts
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessageParts interface

Do not use. Manages a partial message collection.

## Members

The **IMimeMessageParts** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Remarks

Because of message size limitations on the Internet, it may be necessary to split a large message into smaller parts before transmitting it using a particular protocol. Likewise, a client may receive a group of partial messages from another client that need to be combined to produce the original message. This interface allows a client to perform both types of operations.

To split a message into smaller parts, a client calls [**SplitMessage**](oe-imimemessage-splitmessage.md), which creates an **IMimeMessageParts** object. The client then calls [**EnumParts**](oe-imimemessageparts-enumparts.md) to obtain an [**IMimeEnumMessageParts**](oe-imimeenummessageparts.md) object that can be used to enumerate and save the partial messages.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





