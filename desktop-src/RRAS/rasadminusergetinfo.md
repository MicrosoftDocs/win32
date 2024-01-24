---
title: RasAdminUserGetInfo function (Rassapi.h)
description: The RasAdminUserGetInfo function gets the RAS permissions and callback phone number information for a specified user.
ms.assetid: 178ff775-9cd2-43f0-9a9a-dbae337c5fe8
keywords:
- RasAdminUserGetInfo function RAS
topic_type:
- apiref
api_name:
- RasAdminUserGetInfo
api_location:
- Rassapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RasAdminUserGetInfo function

\[This function is provided only for backward compatibility with Windows NT Server 4.0. It returns ERROR\_CALL\_NOT\_IMPLEMENTED on Windows Server 2003. Applications should use the [**MprAdminUserGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminusergetinfo) function.\]

The **RasAdminUserGetInfo** function gets the RAS permissions and callback phone number information for a specified user.

## Syntax


```C++
DWORD RasAdminUserGetInfo(
  _In_ const WCHAR       *lpszUserAccountServer,
  _In_ const WCHAR       *lpszUser,
             PRAS_USER_0 pRasUser0
);
```



## Parameters

<dl> <dt>

*lpszUserAccountServer* \[in\]
</dt> <dd>

Pointer to a null-terminated Unicode string that specifies the name of the primary or backup domain controller that has the user account database. Use the [**RasAdminGetUserAccountServer**](rasadmingetuseraccountserver.md) function to get this server name.

</dd> <dt>

*lpszUser* \[in\]
</dt> <dd>

Pointer to a null-terminated Unicode string that specifies the name of the user for whom to get RAS information.

</dd> <dt>

*pRasUser0* 
</dt> <dd>

Pointer to the [**RAS\_USER\_0**](ras-user-0-str.md) structure that receives the RAS data for the specified user.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value can be the following error code.



| Value                                                                                            | Meaning                                                  |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**NERR\_BufTooSmall**</dt> </dl> | Insufficient memory to perform this function.<br/> |



 

There is no extended error information for this function; do not call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows 2000 Professional<br/>                                                   |
| End of server support<br/> | Windows 2000 Server<br/>                                                         |
| Header<br/>                | <dl> <dt>Rassapi.h</dt> </dl>   |
| Library<br/>               | <dl> <dt>Rassapi.lib</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Rassapi.dll</dt> </dl> |



## See also

<dl> <dt>

[Remote Access Service (RAS) Overview](about-remote-access-service.md)
</dt> <dt>

[RAS Server Administration Functions](ras-server-administration-functions.md)
</dt> <dt>

[**RAS\_USER\_0**](ras-user-0-str.md)
</dt> <dt>

[**RasAdminGetUserAccountServer**](rasadmingetuseraccountserver.md)
</dt> <dt>

[**RasAdminUserSetInfo**](rasadminusersetinfo.md)
</dt> </dl>

 

