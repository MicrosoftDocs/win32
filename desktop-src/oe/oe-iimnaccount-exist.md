---
title: IImnAccount Exist method
description: Determines whether the account was opened and initialized from a previously saved account.
ms.assetid: cb5ab629-959e-431e-ae6f-dd8850aefd35
keywords:
- Exist method Windows Mail (formerly Outlook Express)
- Exist method Windows Mail (formerly Outlook Express) , IImnAccount interface
- IImnAccount interface Windows Mail (formerly Outlook Express) , Exist method
topic_type:
- apiref
api_name:
- IImnAccount.Exist
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

# IImnAccount::Exist method

\[**IImnAccount::Exist** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Determines whether the account was opened and initialized from a previously saved account.

## Syntax


```C++
HRESULT Exist();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                                     |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that the account was opened from the registry.<br/>             |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that the account is a new account that has not been saved.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





