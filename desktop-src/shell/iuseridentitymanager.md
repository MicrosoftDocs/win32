---
description: IUserIdentityManager is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: 3d24b858-bbaf-455c-83cd-3f6f93aba2a8
title: IUserIdentityManager interface (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUserIdentityManager
api_type: 
- COM
api_location: 
- Msident.dll
---

# IUserIdentityManager interface

\[**IUserIdentityManager** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Exposes methods that identify, enumerate, and manage user identities on the system.

## Members

The **IUserIdentityManager** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IUserIdentityManager** also has these types of members:

- [Methods](#methods)

### Methods

The **IUserIdentityManager** interface has these methods.



| Method                                                                  | Description                                                                                                                                                             |
|:------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnumIdentities**](iuseridentitymanager-enumidentities.md)           | Deprecated. Gets an [**IEnumUserIdentity**](ienumuseridentity.md) object, which can be used to enumerate through the user identities present on the system.<br/> |
| [**GetIdentityByCookie**](iuseridentitymanager-getidentitybycookie.md) | Deprecated. Gets a specific user identity by the cookie used to uniquely identify it.<br/>                                                                        |
| [**Logoff**](iuseridentitymanager-logoff.md)                           | Deprecated. Log off the current identity.<br/>                                                                                                                    |
| [**Logon**](iuseridentitymanager-logon.md)                             | Deprecated. Displays a UI to the user, allowing the user to choose a user identity. If successful, the user identity will be logged on and retrieved.<br/>        |
| [**ManageIdentities**](iuseridentitymanager-manageidentities.md)       | Deprecated. Displays a UI to the user, allowing the user to manage user identities.<br/>                                                                          |



 

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
</dt> <dt>

[**IUserIdentity2**](iuseridentity2.md)
</dt> <dt>

[**IEnumUserIdentity**](ienumuseridentity.md)
</dt> <dt>

[**IIdentityChangeNotify**](iidentitychangenotify.md)
</dt> </dl>

 

 
