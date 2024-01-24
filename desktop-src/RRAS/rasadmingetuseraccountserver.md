---
title: RasAdminGetUserAccountServer function (Rassapi.h)
description: The RasAdminGetUserAccountServer function retrieves the name of the server that has the user account database. Use the returned server name in the RasAdminUserGetInfo and RasAdminUserSetInfo functions to get or set information about a specified user.
ms.assetid: db91aa48-32af-49ac-87ed-8c484926ca15
keywords:
- RasAdminGetUserAccountServer function RAS
topic_type:
- apiref
api_name:
- RasAdminGetUserAccountServer
api_location:
- Rassapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RasAdminGetUserAccountServer function

\[This function is provided only for backward compatibility with Windows NT Server 4.0. It returns ERROR\_CALL\_NOT\_IMPLEMENTED on Windows Server 2003. Applications should use the [**MprAdminGetPDCServer**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmingetpdcserver) function.\]

The **RasAdminGetUserAccountServer** function retrieves the name of the server that has the user account database. Use the returned server name in the [**RasAdminUserGetInfo**](rasadminusergetinfo.md) and [**RasAdminUserSetInfo**](rasadminusersetinfo.md) functions to get or set information about a specified user.

## Syntax


```C++
DWORD RasAdminGetUserAccountServer(
  _In_  const WCHAR  *lpszDomain,
  _In_  const WCHAR  *lpszServer,
  _Out_       LPWSTR lpszUserAccountServer
);
```



## Parameters

<dl> <dt>

*lpszDomain* \[in\]
</dt> <dd>

Pointer to a **null**-terminated Unicode string that specifies the name of the domain to which the RAS server belongs. This parameter is **NULL** for the RAS administration applications running on workstations or servers that are not members of a domain. If this parameter is **NULL**, the *lpszServer* parameter must be non-**NULL**.

</dd> <dt>

*lpszServer* \[in\]
</dt> <dd>

Pointer to a **null**-terminated Unicode string that specifies the name of the RAS server. Specify the name with leading "\\\\" characters, in the form: \\\\*servername*. This parameter can be **NULL** if the *lpszDomain* parameter is not **NULL**.

</dd> <dt>

*lpszUserAccountServer* \[out\]
</dt> <dd>

Pointer to a buffer that receives a **null**-terminated Unicode string that specifies the name of a domain controller that has the user account database. The buffer should be big enough to hold the server name (UNCLEN +1). The function prefixes the returned server name with leading "\\\\" characters, in the form: \\\\*servername*.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value can be the following error code.



| Value                                                                                                    | Meaning                                                     |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl> | Both *lpszDomain* and *lpszServer* are **NULL**.<br/> |



 

There is no extended error information for this function; do not call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

The **RasAdminGetUserAccountServer** function obtains the name of the server with the user accounts database. This function requires the name of the RAS server or the name of the domain in which the RAS server resides.

The *lpszDomain* parameter should specify a valid domain name. This parameter is **NULL** for RAS administration applications running on servers that are not members of a domain (for example, the server is in its own workgroup). In this case, the *lpszServer* parameter must specify the server name. To get the server name, call the [**GetComputerName**](/windows/win32/api/winbase/nf-winbase-getcomputernamea) function. Be sure to prefix the server name with the "\\\\" characters.

If the server name specified by *lpszServer* is a stand-alone server (that is, the server or workstation is not a member of a domain), then the server name itself is returned in the *lpszUserAccountServer* buffer.

Then use the name of the user account server in a call to the [**NetQueryDisplayInformation**](/windows/win32/api/lmaccess/nf-lmaccess-netquerydisplayinformation) function to enumerate the users in the user account database.

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

[**GetComputerName**](/windows/win32/api/winbase/nf-winbase-getcomputernamea)
</dt> <dt>

[**RasAdminUserGetInfo**](rasadminusergetinfo.md)
</dt> <dt>

[**RasAdminUserSetInfo**](rasadminusersetinfo.md)
</dt> </dl>

 

