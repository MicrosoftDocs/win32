---
title: IImnAccountManager interface
description: This object allows a client to create, open, delete, and enumerate accounts.
ms.assetid: 9ec2ff2d-a08b-4bdc-8e5c-00bf298212d0
keywords:
- IImnAccountManager interface Windows Mail (formerly Outlook Express)
- IImnAccountManager interface Windows Mail (formerly Outlook Express) , described
topic_type:
- apiref
api_name:
- IImnAccountManager
api_location:
- Msoeacct.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IImnAccountManager interface

\[**IImnAccountManager** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [New Handling for Account Data](oe-account-entry.md).\]

This object allows a client to create, open, delete, and enumerate accounts.

## Members

The **IImnAccountManager** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Remarks

This is the top-level interface; it provides access to the other interfaces.

A client can obtain an **IImnAccountManager** object by calling the following function.


```C++
CoCreateInstance(CLSID_ImnAccountManager, NULL, CLSCTX_INPROC_SERVER, 
                IID_IImnAccountManager, (LPVOID *)&amp;pAccountManager);
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





