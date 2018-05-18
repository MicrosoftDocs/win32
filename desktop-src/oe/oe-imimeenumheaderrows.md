---
title: IMimeEnumHeaderRows interface
description: This interface is used to enumerate the headers in a message or a message body.
ms.assetid: '2f56385d-5f50-43e6-bce8-f9814d769ca8'
keywords: ["IMimeEnumHeaderRows interface Windows Mail (formerly Outlook Express)", "IMimeEnumHeaderRows interface Windows Mail (formerly Outlook Express) , described"]
topic_type:
- apiref
api_name:
- IMimeEnumHeaderRows
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeEnumHeaderRows interface

\[**IMimeEnumHeaderRows** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This interface is used to enumerate the headers in a message or a message body. A client can obtain an **IMimeEnumHeaderRows** by calling [**EnumRows**](oe-imimeheadertable-enumrows.md).

## Members

The **IMimeEnumHeaderRows** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Remarks

**IMimeEnumHeaderRows** adheres to the definition of a standard OLE enumerator interface.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





