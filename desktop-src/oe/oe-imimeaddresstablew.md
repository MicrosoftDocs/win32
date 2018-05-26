---
title: IMimeAddressTableW interface
description: Do not use.
ms.assetid: 47f163d2-f770-4a2a-bb56-77d77f1e819a
keywords:
- IMimeAddressTableW interface Windows Mail (formerly Outlook Express)
- IMimeAddressTableW interface Windows Mail (formerly Outlook Express) , described
topic_type:
- apiref
api_name:
- IMimeAddressTableW
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

# IMimeAddressTableW interface

Do not use. Manipulates a collection of message recipients, such as addresses. The address table is used to manipulate the address-type properties on an [**IMimePropertySet**](oe-imimepropertyset.md) object. Addresses are stored as part of the [RFC 822](http://www.ietf.org/rfc/rfc822.txt) or [RFC 1521](http://www.ietf.org/rfc/rfc1521.txt) message header. The methods of **IMimeAddressTableW** support Unicode.

## Members

The **IMimeAddressTableW** interface inherits from [**IMimeAddressTable**](oe-imimeaddresstable.md) but does not have additional members.

## Remarks

There are multiple ways in which a client can obtain an **IMimeAddressTableW** object:

-   By calling [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) (**IMimeAddressTableW** does not support aggregation), for example:

    `CoCreateInstance(CLSID_IMimeAddressTableW, NULL, CLSCTX_INPROC_SERVER, IID_IMimeAddressTableW, (LPVOID *)&pAddressTableW);`

-   By using an [**IMimePropertySet**](oe-imimepropertyset.md) object, for example:

    `IMimePropertySet::BindToObject(IID_IMimeAddressTableW, (LPVOID *)&pAddressTableW);`

-   By using an [**IMimeBodyW**](oe-imimebodyw.md) object, for example:

    `IMimeBodyW::BindToObject(&pAddressTableW);`

-   By using an [**IMimeMessage**](oe-imimemessage.md) object, for example:

    `IMimeMessage::GetAddressTable(hBody, IID_IMimeAddressTableW, (LPVOID *)&pAddressTableW);`

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





