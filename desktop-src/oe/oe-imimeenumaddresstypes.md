---
title: IMimeEnumAddressTypes interface
description: Do not use. Enumerates the items in an IMimeAddressTable object.
ms.assetid: e3bb3f07-a2ed-4177-a3b3-cf1d702110f7
keywords:
- IMimeEnumAddressTypes interface Windows Mail (formerly Outlook Express)
- IMimeEnumAddressTypes interface Windows Mail (formerly Outlook Express) , described
topic_type:
- apiref
api_name:
- IMimeEnumAddressTypes
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

# IMimeEnumAddressTypes interface

Do not use. Enumerates the items in an [**IMimeAddressTable**](oe-imimeaddresstable.md) object.

## Members

The **IMimeEnumAddressTypes** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Remarks

This interface allows a client to enumerate a specified set of address types for a message. A client can obtain an **IMimeEnumAddressTypes** object by calling [**EnumTypes**](oe-imimeaddresstable-enumtypes.md) or by calling [**EnumAddressTypes**](oe-imimemessage-enumaddresstypes.md). This interface adheres to the definition of a standard OLE enumerator interface.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





