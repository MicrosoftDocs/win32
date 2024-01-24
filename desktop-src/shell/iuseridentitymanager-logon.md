---
description: IUserIdentityManager::Logon is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: ba146ee1-6c9c-4f97-ae90-431aa084ea16
title: IUserIdentityManager::Logon method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUserIdentityManager.Logon
api_type: 
- COM
api_location: 
- Msident.dll
---

# IUserIdentityManager::Logon method

\[**IUserIdentityManager::Logon** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Displays a UI to the user, allowing the user to choose a user identity. If successful, the user identity will be logged on and retrieved.

## Syntax


```C++
HRESULT Logon(
  [in]  HWND          hwndParent,
  [in]  DWORD         dwFlags,
  [out] IUserIdentity **ppIdentity
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **HWND**

An **HWND** value that identifies a window that will be brought to the foreground after the logon UI is dismissed.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Optional flags to define how the UI will behave. Set to UIL\_FORCE\_UI to force the UI to display, even if an identity has already been chosen.

</dd> <dt>

*ppIdentity* \[out\]
</dt> <dd>

Type: **[**IUserIdentity**](iuseridentity.md)\*\***

The address of the pointer that receives the chosen user identity.

</dd> </dl>

## Return value

Type: **HRESULT**

Result of the logon operation. If successful, it returns S\_OK. Otherwise it will return one of the following error codes.



| Return code                                                                                            | Description                                                                                 |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_USER\_CANCELLED**</dt> </dl>      | The user canceled the logon operation from the UI.<br/>                               |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>          | The user identity could not be created.<br/>                                          |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>           | The operation failed unexpectedly.<br/>                                               |
| <dl> <dt>**E\_IDENTITIES\_DISABLED**</dt> </dl> | Identity management is disabled on the system.<br/>                                   |
| <dl> <dt>**S\_IDENTITIES\_DISABLED**</dt> </dl> | Identity management is disabled on the system.<br/>                                   |
| <dl> <dt>**E\_IDENTITY\_CHANGING**</dt> </dl>   | The system is currently switching identities, and cannot complete the operation.<br/> |



 

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

[**IUserIdentityManager**](iuseridentitymanager.md)
</dt> <dt>

[**IUserIdentityManager::Logoff**](iuseridentitymanager-logoff.md)
</dt> <dt>

[**IUserIdentityManager::ManageIdentities**](iuseridentitymanager-manageidentities.md)
</dt> </dl>

 

 




