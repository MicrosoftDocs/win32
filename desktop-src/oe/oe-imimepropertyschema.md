---
title: IMimePropertySchema interface
description: Do not use. Manipulates MimeOLE's global property schema.
ms.assetid: 3a1674ed-b6dd-4092-a76a-f8b5c1eaf0f0
keywords:
- IMimePropertySchema interface Windows Mail (formerly Outlook Express)
- IMimePropertySchema interface Windows Mail (formerly Outlook Express) , described
topic_type:
- apiref
api_name:
- IMimePropertySchema
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

# IMimePropertySchema interface

Do not use. Manipulates MimeOLE's global property schema.

## Members

The **IMimePropertySchema** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Remarks

The MimeOLE property schema is used to manage a collection of properties and attributes for each property. MimeOLE internally uses this property schema for various types operations and to determine how certain properties should be handled. MimeOLE has a default property schema that contains the majority of the properties that a client uses.

When MimeOLE loads a message, if it encounters properties that do not exist in the property schema, they are added with default attributes.

Using this interface, a client can also add new properties to the schema and change attributes for existing properties.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





