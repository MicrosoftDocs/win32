---
title: IImnAccount Delete method
description: Deletes the account from the registry.
ms.assetid: b5357374-da50-4613-959b-cc8e1400f0ec
keywords:
- Delete method Windows Mail (formerly Outlook Express)
- Delete method Windows Mail (formerly Outlook Express) , IImnAccount interface
- IImnAccount interface Windows Mail (formerly Outlook Express) , Delete method
topic_type:
- apiref
api_name:
- IImnAccount.Delete
api_location:
- Msoeacct.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IImnAccount::Delete method

\[**IImnAccount::Delete** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes the account from the registry.

## Syntax


```C++
HRESULT Delete();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                          | Description                                                      |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                 | Indicates success. <br/>                                   |
| <dl> <dt>**E\_RegOpenKeyFailed**</dt> </dl>   | Indicates that the registry could not be opened. <br/>     |
| <dl> <dt>**E\_RegDeleteKeyFailed**</dt> </dl> | Indicates that the account to delete does not exist. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





