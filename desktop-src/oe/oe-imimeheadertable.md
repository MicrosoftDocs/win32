---
title: IMimeHeaderTable interface
description: Do not use. Manipulates the rows in a message header or a body header.
ms.assetid: 0c2b9731-02e0-462c-9b33-08dee4b4eb7c
keywords:
- IMimeHeaderTable interface Windows Mail (formerly Outlook Express)
- IMimeHeaderTable interface Windows Mail (formerly Outlook Express) , described
topic_type:
- apiref
api_name:
- IMimeHeaderTable
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

# IMimeHeaderTable interface

Do not use. Manipulates the rows in a message header or a body header.

## Members

The **IMimeHeaderTable** interface inherits from [**IPersistStream**](https://msdn.microsoft.com/library/windows/desktop/ms690091) but does not have additional members.

## Remarks

**IMimeHeaderTable** allows the client to treat each line in a header as a row where each row consists of a header name and header data.

A header can sometimes contain the same row multiple times. For example, most messages have multiple "Received" headers. This interface is the best way of managing duplicate rows in a header.

A client uses the [**IMimePropertySet**](oe-imimepropertyset.md) interface as the primary way to manipulate a message header. **IMimeHeaderTable** gives the client more low-level control over the rows in a header than **IMimePropertySet**.

There are multiple ways in which a client can obtain an **IMimeHeaderTable** object:

-   By calling [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) (**IMimeHeaderTable** does not support aggregation), for example:

    `CoCreateInstance(CLSID_IMimeHeaderTable, NULL, CLSCTX_INPROC_SERVER, IID_IMimeHeaderTable, (LPVOID*)&pHeaderTable);`

-   By using an [**IMimePropertySet**](oe-imimepropertyset.md) object, for example:

    `IMimePropertySet::BindToObject(hBody, IID_IMimeHeaderTable, (LPVOID*)&pHeaderTable);`

-   By using an [**IMimeBody**](oe-imimebody.md) object, for example:

    `IMimeBody::BindToObject(IID_IMimeHeaderTable, (LPVOID*)&pHeaderTable);`

-   By using an [**IMimeAddressTable**](oe-imimeaddresstable.md) object, for example:

    `IMimeAddressTable::BindToObject(IID_IMimeHeaderTable, (LPVOID*)&pHeaderTable);`

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





