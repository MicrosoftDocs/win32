---
description: GetCookie is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: 4a743d64-9af3-43cf-9a9f-d808676ab337
title: IUserIdentity::GetCookie method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUserIdentity.GetCookie
api_type: 
- COM
api_location: 
- Msident.dll
---

# IUserIdentity::GetCookie method

\[**GetCookie** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Gets the cookie used to uniquely identify this user identity.

## Syntax


```C++
HRESULT GetCookie(
  [out] GUID *puidCookie
);
```



## Parameters

<dl> <dt>

*puidCookie* \[out\]
</dt> <dd>

Type: **GUID\***

A pointer to a **GUID** value that receives the cookie used to uniquely identify this user identity.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

[**GetOrdinal**](iuseridentity2-getordinal.md)
</dt> </dl>

 

 




