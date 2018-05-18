---
title: IImnAccount SetAsDefault method
description: Makes the account the default for the server types that it supports.
ms.assetid: '9991ea0e-2eb7-4a60-a834-c0bf89e88c90'
keywords: ["SetAsDefault method Windows Mail (formerly Outlook Express)", "SetAsDefault method Windows Mail (formerly Outlook Express) , IImnAccount interface", "IImnAccount interface Windows Mail (formerly Outlook Express) , SetAsDefault method"]
topic_type:
- apiref
api_name:
- IImnAccount.SetAsDefault
api_location:
- Msoeacct.dll
api_type:
- COM
---

# IImnAccount::SetAsDefault method

\[**IImnAccount::SetAsDefault** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Makes the account the default for the server types that it supports.

## Syntax


```C++
HRESULT SetAsDefault();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                            | Description                                           |
|----------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Indicates success. <br/>                        |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Indicates that an account cannot be found.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





