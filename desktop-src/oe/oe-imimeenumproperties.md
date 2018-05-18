---
title: IMimeEnumProperties interface
description: Do not use. Enumerates the items in an IMimePropertySet object.
ms.assetid: 'bd14671c-eca2-45e2-a776-0e57ef14f8e6'
keywords: ["IMimeEnumProperties interface Windows Mail (formerly Outlook Express)", "IMimeEnumProperties interface Windows Mail (formerly Outlook Express) , described"]
topic_type:
- apiref
api_name:
- IMimeEnumProperties
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeEnumProperties interface

Do not use. Enumerates the items in an [**IMimePropertySet**](oe-imimepropertyset.md) object.

## Members

The **IMimeEnumProperties** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Remarks

This interface allows a client to enumerate the properties in a message or a message body. A client can obtain an **IMimeEnumProperties** object by calling [**EnumProps**](oe-imimepropertyset-enumprops.md). This interface adheres to the definition of a standard OLE enumerator interface.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





