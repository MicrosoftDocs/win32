---
title: IMimeAddressTable interface
description: Do not use.
ms.assetid: cd4da9ed-9637-4381-868a-e30dfb9613be
keywords:
- IMimeAddressTable interface Windows Mail (formerly Outlook Express)
- IMimeAddressTable interface Windows Mail (formerly Outlook Express) , described
topic_type:
- apiref
api_name:
- IMimeAddressTable
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

# IMimeAddressTable interface

Do not use. Manipulates a collection of message recipients (for example, addresses). The address table is used to manipulate the address-type properties on an [**IMimePropertySet**](oe-imimepropertyset.md) object. Addresses are stored as part of the [RFC 822](http://www.ietf.org/rfc/rfc822.txt) or [RFC 1521](http://www.ietf.org/rfc/rfc1521.txt) message header.

## Members

The **IMimeAddressTable** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Remarks

There are multiple ways in which a client can obtain an **IMimeAddressTable** object:

-   By calling [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) (**IMimeAddressTable** does not support aggregation), for example:

    `CoCreateInstance(CLSID_IMimeAddressTable, NULL, CLSCTX_INPROC_SERVER, IID_IMimeAddressTable, (LPVOID *)&pAddressTable);`

-   By using an [**IMimePropertySet**](oe-imimepropertyset.md) object, for example:

    `IMimePropertySet::BindToObject(IID_IMimeAddressTable, (LPVOID *)&pAddressTable);`

-   By using an [**IMimeBody**](oe-imimebody.md) object, for example:

    `IMimeBody::BindToObject(&pAddressTable);`

-   By using an [**IMimeMessage**](oe-imimemessage.md) object, for example:

    `IMimeMessage::GetAddressTable(hBody, IID_IMimeAddressTable, (LPVOID *)&pAddressTable);`

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





