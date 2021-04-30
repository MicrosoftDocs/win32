---
description: ChangePassword is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: bc8813a0-9b40-481f-9ab3-cf6a9a0796d2
title: IUserIdentity2::ChangePassword method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUserIdentity2.ChangePassword
api_type: 
- COM
api_location: 
- Msident.dll
---

# IUserIdentity2::ChangePassword method

\[**ChangePassword** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Sets a new password for the identity.

## Syntax


```C++
HRESULT ChangePassword(
  [in] WCHAR *szOldPass,
  [in] WCHAR *szNewPass
);
```



## Parameters

<dl> <dt>

*szOldPass* \[in\]
</dt> <dd>

Type: **WCHAR\***

The wide-character string that contains the password currently associated with the identity.

</dd> <dt>

*szNewPass* \[in\]
</dt> <dd>

Type: **WCHAR\***

The wide-character string that contains the new password to be associated with the identity.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The value of *szOldPass* must match the current password of the identity for *szNewPass* to be applied. An incorrect value of *szOldPass* will result in a return value of E\_FAIL.

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



 

 




