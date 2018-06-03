---
title: IImnEnumAccounts Reset method
description: Resets the current position back to the beginning of the enumerator.
ms.assetid: d7b3a9f0-10af-449d-b743-9e9fed03ce22
keywords:
- Reset method Windows Mail (formerly Outlook Express)
- Reset method Windows Mail (formerly Outlook Express) , IImnEnumAccounts interface
- IImnEnumAccounts interface Windows Mail (formerly Outlook Express) , Reset method
topic_type:
- apiref
api_name:
- IImnEnumAccounts.Reset
api_location:
- Msoeacct.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IImnEnumAccounts::Reset method

\[**IImnEnumAccounts::Reset** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Resets the current position back to the beginning of the enumerator.

## Syntax


```C++
HRESULT Reset();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





