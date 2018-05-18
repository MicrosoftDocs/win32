---
title: IMimePropertySet interface
description: Do not use. Manages an Internet message header or body header. This interface allows a client to manipulate a header as a collection of properties.
ms.assetid: '69b98775-58a2-4ea6-b592-89c0bb5d1385'
keywords: ["IMimePropertySet interface Windows Mail (formerly Outlook Express)", "IMimePropertySet interface Windows Mail (formerly Outlook Express) , described"]
topic_type:
- apiref
api_name:
- IMimePropertySet
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimePropertySet interface

Do not use. Manages an Internet message header or body header. This interface allows a client to manipulate a header as a collection of properties.

## Members

The **IMimePropertySet** interface inherits from [**IPersistStreamInit**](https://msdn.microsoft.com/library/windows/desktop/ms682273) but does not have additional members.

## Remarks

**IMimePropertySet** supports the [**IPersistStreamInit**](https://msdn.microsoft.com/library/windows/desktop/ms682273) interface. This means that **IMimePropertySet** supports persistence. The persistence format is an Internet message header as defined in [RFC 822](http://www.ietf.org/rfc/rfc822.txt) and [RFC 1521](http://www.ietf.org/rfc/rfc1521.txt).

There are multiple ways in which a client can obtain an **IMimePropertySet** object:

-   By calling [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) (**IMimePropertySet** does not support aggregation), for example:

    `CoCreateInstance(CLSID_IMimePropertySet, NULL, CLSCTX_INPROC_SERVER, IID_IMimePropertySet, (LPVOID*)&pPropertySet);`

-   By using an [**IMimeMessage**](oe-imimemessage.md) or [**IMimeMessageTree**](oe-imimemessagetree.md) object, for example:

    `IMimeMessage::BindToObject(hBody, IID_IMimePropertySet, (LPVOID*)&pPropertySet);`

-   By using an [**IMimeBody**](oe-imimebody.md) object, for example:

    `IMimeBody::BindToObject(IID_ IMimePropertySet, (LPVOID*)&pPropertySet);`

-   By using an [**IMimeAddressTable**](oe-imimeaddresstable.md) object, for example:

    `IMimeAddressTable::BindToObject(IID_IMimePropertySet, (LPVOID*)&pPropertySet);`

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





