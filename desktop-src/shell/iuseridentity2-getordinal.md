---
description: GetOrdinal is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: 20b1c1d0-b09f-43a8-9026-9cdbac28c108
title: IUserIdentity2::GetOrdinal method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUserIdentity2.GetOrdinal
api_type: 
- COM
api_location: 
- Msident.dll
---

# IUserIdentity2::GetOrdinal method

\[**GetOrdinal** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Gets the ordinal number for this identity.

## Syntax


```C++
HRESULT GetOrdinal(
  [out] DWORD *dwOrdinal
);
```



## Parameters

<dl> <dt>

*dwOrdinal* \[out\]
</dt> <dd>

Type: **DWORD\***

A pointer to a **DWORD** value that receives the ordinal number for this identity.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The ordinal determines the order of the identities in the identity list, but may not persist throughout operations on the identities. To get a unique value for an identity, call [**GetCookie**](iuseridentity-getcookie.md).

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

[**GetCookie**](iuseridentity-getcookie.md)
</dt> </dl>

 

 




