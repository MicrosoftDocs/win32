---
title: IMimeEnumMessageParts interface
description: Do not use. Enumerates the partial messages contained inside of an IMimeMessageParts object.
ms.assetid: 546f0628-3b85-4e90-ac5a-0390145f6a46
keywords:
- IMimeEnumMessageParts interface Windows Mail (formerly Outlook Express)
- IMimeEnumMessageParts interface Windows Mail (formerly Outlook Express) , described
topic_type:
- apiref
api_name:
- IMimeEnumMessageParts
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

# IMimeEnumMessageParts interface

Do not use. Enumerates the partial messages contained inside of an [**IMimeMessageParts**](oe-imimemessageparts.md) object.

## Members

The **IMimeEnumMessageParts** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Remarks

A client can obtain an [**IMimeMessageParts**](oe-imimemessageparts.md) object by calling [**EnumParts**](oe-imimemessageparts-enumparts.md). This interface adheres to the definition of a standard OLE enumerator interface.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





