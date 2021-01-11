---
description: GetIdentityFolder is not supported and may be altered or unavailable in the future. Instead, use User Accounts with Fast User Switching and Remote Desktop.
ms.assetid: cd3370a2-b393-4cb9-ad9c-a46086987aaa
title: IUserIdentity::GetIdentityFolder method (Msident.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUserIdentity.GetIdentityFolder
api_type: 
- COM
api_location: 
- Msident.dll
---

# IUserIdentity::GetIdentityFolder method

\[**GetIdentityFolder** is not supported and may be altered or unavailable in the future. Instead, use [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md).\]

Gets the file folder associated with this identity.

## Syntax


```C++
HRESULT GetIdentityFolder(
  [in] DWORD dwFlags,
  [in] WCHAR *pszPath,
  [in] ULONG ulBuffSize
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Required. A value that specifies whether the folder associated with this identity is roaming. Must be one of the following values.

<dt>



 (GIF\_ROAMING\_FOLDER)


</dt> <dd>

The folder is roaming.

</dd> <dt>



 (GIF\_NON\_ROAMING\_FOLDER)


</dt> <dd>

The folder is local.

</dd> </dl> </dd> <dt>

*pszPath* \[in\]
</dt> <dd>

Type: **WCHAR\***

A pointer to a wide-character string that receives the folder path.

</dd> <dt>

*ulBuffSize* \[in\]
</dt> <dd>

Type: **ULONG**

A value that specifies the size of *pszPath*.

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

[**IUserIdentity::OpenIdentityRegKey**](iuseridentity-openidentityregkey.md)
</dt> </dl>

 

 




