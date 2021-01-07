---
description: IUserIdentityManager::ManageIdentities is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: 9a5a85bd-d007-4247-859b-e402ed290785
title: IUserIdentityManager::ManageIdentities method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUserIdentityManager.ManageIdentities
api_type: 
- COM
api_location: 
- Msident.dll
---

# IUserIdentityManager::ManageIdentities method

\[**IUserIdentityManager::ManageIdentities** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Displays a UI to the user, allowing the user to manage user identities.

## Syntax


```C++
HRESULT ManageIdentities(
  [in] HWND  hwndParent,
  [in] DWORD dwFlags
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **HWND**

An **HWND** value that identifies a window that will be brought to the foreground after the UI is dismissed.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Optional flags to define how the UI will behave. Set to UIMI\_CREATE\_NEW\_IDENTITY to prompt the user to create a new identity.

</dd> </dl>

## Return value

Type: **HRESULT**

The result of the management operation. If successful, it returns S\_OK. Otherwise it will return one of the following error codes.



| Return code                                                                                            | Description                                               |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**E\_IDENTITIES\_DISABLED**</dt> </dl> | Identity management is disabled on the system.<br/> |
| <dl> <dt>**E\_USER\_CANCELLED**</dt> </dl>      | The user canceled the dialog.<br/>                  |



 

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

[**IUserIdentityManager::Logon**](iuseridentitymanager-logon.md)
</dt> <dt>

[**IUserIdentityManager::Logoff**](iuseridentitymanager-logoff.md)
</dt> </dl>

 

 




