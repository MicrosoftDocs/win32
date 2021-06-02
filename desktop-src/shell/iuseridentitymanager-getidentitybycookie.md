---
description: GetIdentityByCookie is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: c2f549ac-e13d-4198-864f-7f5fbec30c72
title: IUserIdentityManager::GetIdentityByCookie method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUserIdentityManager.GetIdentityByCookie
api_type: 
- COM
api_location: 
- Msident.dll
---

# IUserIdentityManager::GetIdentityByCookie method

\[**GetIdentityByCookie** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Gets a specific user identity by the cookie used to uniquely identify it.

## Syntax


```C++
HRESULT GetIdentityByCookie(
  [in]  GUID          *uidCookie,
  [out] IUserIdentity **ppIdentity
);
```



## Parameters

<dl> <dt>

*uidCookie* \[in\]
</dt> <dd>

Type: **GUID\***

The address of a **GUID** value that represents the cookie for the identity you want to retrieve.

</dd> <dt>

*ppIdentity* \[out\]
</dt> <dd>

Type: **[**IUserIdentity**](iuseridentity.md)\*\***

The address of the pointer that will receive the user identity object.

</dd> </dl>

## Return value

Type: **HRESULT**

The result of the retrieval request. If successful, it returns S\_OK. Otherwise it will return one of the following error codes.



| Return code                                                                                            | Description                                               |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**E\_IDENTITY\_NOT\_FOUND**</dt> </dl> | The identity requested could not be found.<br/>     |
| <dl> <dt>**E\_IDENTITIES\_DISABLED**</dt> </dl> | Identity management is disabled on the system.<br/> |



 

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



 

 




