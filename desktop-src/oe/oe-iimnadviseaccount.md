---
title: IImnAdviseAccount interface
description: When a method in the account manager is called that deletes, modifies or changes a default account, notifications are generated.
ms.assetid: b5b9d742-5ad7-4d65-a69a-820e4ee86ee4
keywords:
- IImnAdviseAccount interface Windows Mail (formerly Outlook Express)
- IImnAdviseAccount interface Windows Mail (formerly Outlook Express) , described
topic_type:
- apiref
api_name:
- IImnAdviseAccount
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

# IImnAdviseAccount interface

\[**IImnAdviseAccount** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [New Handling for Account Data](oe-account-entry.md).\]

When a method in the account manager is called that deletes, modifies or changes a default account, notifications are generated. A client can hook all notifications by implementing the simple **IImnAdviseAccount** interface.

## Members

The **IImnAdviseAccount** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





