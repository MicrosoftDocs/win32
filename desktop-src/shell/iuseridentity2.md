---
description: IUserIdentity2 is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: 85238574-f6bf-43d7-a41b-3ea086c45e07
title: IUserIdentity2 interface (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUserIdentity2
api_type: 
- COM
api_location: 
- Msident.dll
---

# IUserIdentity2 interface

\[**IUserIdentity2** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Exposes methods that provide naming, password, and ordinal control for a specific user identity.

## Members

The **IUserIdentity2** interface inherits from [**IUserIdentity**](iuseridentity.md). **IUserIdentity2** also has these types of members:

- [Methods](#methods)

### Methods

The **IUserIdentity2** interface has these methods.



| Method                                                  | Description                                                       |
|:--------------------------------------------------------|:------------------------------------------------------------------|
| [**ChangePassword**](iuseridentity2-changepassword.md) | Deprecated. Sets a new password for the identity.<br/>      |
| [**GetOrdinal**](iuseridentity2-getordinal.md)         | Deprecated. Gets the ordinal number for this identity.<br/> |
| [**SetName**](iuseridentity2-setname.md)               | Deprecated. Sets the display name of the identity.<br/>     |



 

## Remarks

This interface also provides the methods of the [**IUserIdentity**](iuseridentity.md) interface, from which it inherits.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows 2000 Professional<br/>                                                   |
| End of server support<br/>    | Windows 2000 Server<br/>                                                         |
| Header<br/>                   | <dl> <dt>Msident.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msident.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msident.dll</dt> </dl> |



## See also

<dl> <dt>

[**IUserIdentity**](iuseridentity.md)
</dt> </dl>

 

 




