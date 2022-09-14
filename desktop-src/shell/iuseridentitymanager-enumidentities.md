---
description: IUserIdentityManager::EnumIdentities is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: 8111fbcd-dc4d-45cb-83e0-3c2cd7c4df27
title: IUserIdentityManager::EnumIdentities method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUserIdentityManager.EnumIdentities
api_type: 
- COM
api_location: 
- Msident.dll
---

# IUserIdentityManager::EnumIdentities method

\[**IUserIdentityManager::EnumIdentities** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Gets an [**IEnumUserIdentity**](ienumuseridentity.md) object, which can be used to enumerate through the user identities present on the system.

## Syntax


```C++
HRESULT EnumIdentities(
  [out] IEnumUserIdentity **ppEnumUser
);
```



## Parameters

<dl> <dt>

*ppEnumUser* \[out\]
</dt> <dd>

Type: **[**IEnumUserIdentity**](ienumuseridentity.md)\*\***

The address of the pointer to the new identity enumeration object.

</dd> </dl>

## Return value

Type: **HRESULT**

The result of the retrieval operation. If successful, it returns S\_OK. If the enumeration object could not be created, it returns E\_OUTOFMEMORY.

## Remarks

This method is useful for iteration over the list of identities on the system. To retrieve a single identity by its cookie without accessing the list, call [**IUserIdentityManager::GetIdentityByCookie**](iuseridentitymanager-getidentitybycookie.md).

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

[**IEnumUserIdentity**](ienumuseridentity.md)
</dt> <dt>

[**IUserIdentityManager::GetIdentityByCookie**](iuseridentitymanager-getidentitybycookie.md)
</dt> </dl>

 

 




