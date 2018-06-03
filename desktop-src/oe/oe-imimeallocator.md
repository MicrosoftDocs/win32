---
title: IMimeAllocator interface
description: Do not use. Provides utilities that allow a client to free resources associated with MimeOLE object types.
ms.assetid: 15c62a29-02ed-4000-af96-8b3d785787f9
keywords:
- IMimeAllocator interface Windows Mail (formerly Outlook Express)
- IMimeAllocator interface Windows Mail (formerly Outlook Express) , described
topic_type:
- apiref
api_name:
- IMimeAllocator
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

# IMimeAllocator interface

Do not use. Provides utilities that allow a client to free resources associated with MimeOLE object types.

## Members

The **IMimeAllocator** interface inherits from **IMalloc** but does not have additional members.

## Remarks

**IMimeAllocator** does not support aggregation.

The following provides an example of how a client can create an **IMimeAllocator** object.

`CoCreateInstance(CLSID_IMimeAllocator, NULL, CLSCTX_INPROC_SERVER, IID_IMimeAllocator, (LPVOID *)&pAllocator);`

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





