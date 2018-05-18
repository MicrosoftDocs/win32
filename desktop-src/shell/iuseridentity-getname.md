---
Description: 'IUserIdentity::GetName is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.'
ms.assetid: '4db24dd2-d2b8-4a58-9c16-0e721bc195da'
title: 'IUserIdentity::GetName method'
---

# IUserIdentity::GetName method

\[**IUserIdentity::GetName** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Gets the name associated with this user identity.

## Syntax


```C++
HRESULT GetName(
  [in] WCHAR *pszName,
  [in] ULONG ulBuffSize
);
```



## Parameters

<dl> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **WCHAR\***

A pointer to a wide-character string that receives the name of this user identity.

</dd> <dt>

*ulBuffSize* \[in\]
</dt> <dd>

Type: **ULONG**

A value that specifies the size of *pszName*.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP<br/>                                                                  |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| Header<br/>                   | <dl> <dt>Msident.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msident.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msident.dll</dt> </dl> |



## See also

<dl> <dt>

[**IUserIdentity**](iuseridentity.md)
</dt> <dt>

[**SetName**](iuseridentity2-setname.md)
</dt> </dl>

 

 




