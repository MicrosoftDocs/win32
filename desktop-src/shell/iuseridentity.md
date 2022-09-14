---
description: IUserIdentity is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: c2f11f8b-f944-445b-b4fc-ac57b0fe3a74
title: IUserIdentity interface (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUserIdentity
api_type: 
- COM
api_location: 
- Msident.dll
---

# IUserIdentity interface

\[**IUserIdentity** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Exposes methods that provide identification, registry, and folder data for a specific user identity.

## Members

The **IUserIdentity** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IUserIdentity** also has these types of members:

-   [Methods](#methods)

### Methods

The **IUserIdentity** interface has these methods.



| Method                                                         | Description                                                                                      |
|:---------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [**GetCookie**](iuseridentity-getcookie.md)                   | Deprecated. Gets the cookie used to uniquely identify this user identity.<br/>             |
| [**GetIdentityFolder**](iuseridentity-getidentityfolder.md)   | Deprecated. Gets the file folder associated with this identity.<br/>                       |
| [**GetName**](iuseridentity-getname.md)                       | Deprecated. Gets the name associated with this user identity.<br/>                         |
| [**OpenIdentityRegKey**](iuseridentity-openidentityregkey.md) | Deprecated. Retrieves the key in the registry that corresponds to this user identity.<br/> |



 

## Remarks

This interface provides information that corresponds to a specific user identity present on the system. You can access this user identity's identity folder, its registry key, and its identification cookie, as well as retrieve the name associated with the user identity.

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

[**IUserIdentity2**](iuseridentity2.md)
</dt> <dt>

[**IUserIdentityManager**](iuseridentitymanager.md)
</dt> <dt>

[**IEnumUserIdentity**](ienumuseridentity.md)
</dt> </dl>

 

 
