---
description: IUserIdentity2::SetName is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: 1c9c3beb-fa1c-4b4d-9cfd-656b97949036
title: IUserIdentity2::SetName method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUserIdentity2.SetName
api_type: 
- COM
api_location: 
- Msident.dll
---

# IUserIdentity2::SetName method

\[**IUserIdentity2::SetName** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Sets the display name of the identity.

## Syntax


```C++
HRESULT SetName(
  [in] WCHAR *pszName
);
```



## Parameters

<dl> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **WCHAR\***

The wide-character string that contains the new name of the identity.

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

[**IUserIdentity2**](iuseridentity2.md)
</dt> <dt>

[**GetName**](iuseridentity-getname.md)
</dt> </dl>

 

 




