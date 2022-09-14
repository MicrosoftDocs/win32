---
title: RasAdminUserSetInfo function (Rassapi.h)
description: The RasAdminUserSetInfo function sets the RAS permissions and call-back phone number for a specified user.
ms.assetid: 5b049dfd-ecc8-47e4-82cc-71a875752714
keywords:
- RasAdminUserSetInfo function RAS
topic_type:
- apiref
api_name:
- RasAdminUserSetInfo
api_location:
- Rassapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RasAdminUserSetInfo function

\[This function is provided only for backward compatibility with Windows NT Server 4.0. It returns ERROR\_CALL\_NOT\_IMPLEMENTED on Windows Server 2003. Applications should use the [**MprAdminUserSetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminusersetinfo) function.\]

The **RasAdminUserSetInfo** function sets the RAS permissions and call-back phone number for a specified user.

## Syntax


```C++
DWORD RasAdminUserSetInfo(
  _In_ const WCHAR       *lpszUserAccountServer,
  _In_ const WCHAR       *lpszUser,
  _In_ const PRAS_USER_0 pRasUser0
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

Pointer to a null-terminated Unicode string that specifies the name of the user for whom RAS information is to be set.

</dd> <dt>

*pRasUser0* \[in\]
</dt> <dd>

Pointer to the [**RAS\_USER\_0**](ras-user-0-str.md) structure that specifies the new RAS data for the specified user.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value can be one of the following error codes.



| Value                                                                                                           | Description                                                                                     |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_DATA**</dt> </dl>             | The *pRasUser0* buffer contains invalid data.<br/>                                        |
| <dl> <dt>**ERROR\_INVALID\_CALLBACK\_NUMBER**</dt> </dl> | The callback number specified in the *pRasUser0* buffer contains invalid characters.<br/> |
| <dl> <dt>**NERR\_BufTooSmall** </dt> </dl>               | Insufficient memory to perform this function.<br/>                                        |



 

There is no extended error information for this function; do not call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

When setting the RAS permissions for a user, the **bfPrivilege** member of the [**RAS\_USER\_0**](ras-user-0-str.md) structure must specify at least one of the call-back flags. For example, to set a user's privileges to allow dial-in privilege but no call-back privilege, set **bfPrivilege** to RASPRIV\_DialinPrivilege \| RASPRIV\_NoCallback.

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

[**RasAdminUserGetInfo**](rasadminusergetinfo.md)
</dt> </dl>

 

