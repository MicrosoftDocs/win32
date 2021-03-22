---
title: RasAdminServerGetInfo function (Rassapi.h)
description: The RasAdminServerGetInfo function gets the server configuration of a RAS server.
ms.assetid: a1c371fd-462c-443c-8016-592efb2f0b1a
keywords:
- RasAdminServerGetInfo function RAS
topic_type:
- apiref
api_name:
- RasAdminServerGetInfo
api_location:
- Rassapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RasAdminServerGetInfo function

\[This function is provided only for backward compatibility with Windows NT Server 4.0. It returns ERROR\_CALL\_NOT\_IMPLEMENTED on Windows Server 2003. Applications should use the [**MprAdminServerGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminservergetinfo) function.\]

The **RasAdminServerGetInfo** function gets the server configuration of a RAS server.

## Syntax


```C++
DWORD RasAdminServerGetInfo(
  _In_  const WCHAR         *lpszServer,
  _Out_       PRAS_SERVER_0 pRasServer0
);
```



## Parameters

<dl> <dt>

*lpszServer* \[in\]
</dt> <dd>

Pointer to a **null**-terminated Unicode string that specifies the name of the Windows NT/Windows 2000 RAS server. If this parameter is **NULL**, the function returns information about the local computer. Specify the name with leading "\\\\" characters, in the form: \\\\*servername*.

</dd> <dt>

*pRasServer0* \[out\]
</dt> <dd>

Pointer to the [**RAS\_SERVER\_0**](ras-server-0-str.md) structure that receives the number of ports configured on the server, the number of ports currently in use, and the server version number.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is an error code. Possible error codes include those returned by [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) for the [**CallNamedPipe**](/windows/desktop/api/winbase/nf-winbase-callnamedpipea) function. There is no extended error information for this function; do not call **GetLastError**.

## Remarks

To enumerate all RAS servers in a domain, call the [**NetServerEnum**](/windows/desktop/api/lmserver/nf-lmserver-netserverenum) function and specify SV\_TYPE\_DIALIN for the *servertype* parameter.

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

[**NetServerEnum**](/windows/win32/api/lmserver/nf-lmserver-netserverenum)
</dt> <dt>

[**RAS\_SERVER\_0**](ras-server-0-str.md)
</dt> </dl>

 

