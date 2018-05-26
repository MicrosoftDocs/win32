---
title: IMimeWebDocument interface
description: This interface is implemented by the client and is used to provide a data source for Web-related documents.
ms.assetid: ebbb1c27-b4d6-44c2-8bae-676058efe889
keywords:
- IMimeWebDocument interface Windows Mail (formerly Outlook Express)
- IMimeWebDocument interface Windows Mail (formerly Outlook Express) , described
topic_type:
- apiref
api_name:
- IMimeWebDocument
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

# IMimeWebDocument interface

\[**IMimeWebDocument** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

This interface is implemented by the client and is used to provide a data source for Web-related documents. A client can use this interface to attach Web documents to a message object by calling [**AttachObject**](oe-imimemessage-attachobject.md). This interface can also be used when calling [**SetData**](oe-imimebody-setdata.md).

## Members

The **IMimeWebDocument** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





