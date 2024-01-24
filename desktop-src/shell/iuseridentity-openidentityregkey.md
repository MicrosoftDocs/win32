---
description: Deprecated. Retrieves the key in the registry that corresponds to this user identity.
ms.assetid: eecf8b73-e86a-4274-8d9c-c601153f81db
title: IUserIdentity::OpenIdentityRegKey method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUserIdentity.OpenIdentityRegKey
api_type: 
- COM
api_location: 
- Msident.dll
---

# IUserIdentity::OpenIdentityRegKey method

\[The **IUserIdentity::OpenIdentityRegKey** method is available for use in Windows 2000. In Windows XP, this functionality has been superseded by [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md), and might be altered or unavailable in subsequent versions.\]

Deprecated. Retrieves the key in the registry that corresponds to this user identity.

## Syntax


```C++
HRESULT OpenIdentityRegKey(
  [in]  DWORD dwDesiredAccess,
  [out] HKEY  *phKey
);
```



## Parameters

<dl> <dt>

*dwDesiredAccess* \[in\]
</dt> <dd>

Type: **DWORD**

A value that describes the access level requested of the registry key.

</dd> <dt>

*phKey* \[out\]
</dt> <dd>

Type: **HKEY\***

A pointer that receives the registry key.

</dd> </dl>

## Return value

Type: **HRESULT**

The result of the registry request. If successful, it returns **S\_OK**. Otherwise it will return one of the following error codes.



| Return code                                                                                            | Description                                                        |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**E\_IDENTITY\_NOT\_FOUND**</dt> </dl> | This identity does not have an associated registry key.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                 | The registry key was unable to be accessed.<br/>             |



 

## Remarks

The *dwDesiredAccess* parameter is a standard registry access security descriptor that describes the access you want to gain to the registry key. For more information on registry security, including a list of acceptable values for this parameter, see [Registry Key Security and Access Rights](../sysinfo/registry-key-security-and-access-rights.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Msident.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msident.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msident.dll</dt> </dl> |



## See also

<dl> <dt>

[**IUserIdentity**](iuseridentity.md)
</dt> <dt>

[**IUserIdentity::GetIdentityFolder**](iuseridentity-getidentityfolder.md)
</dt> </dl>

 

 
