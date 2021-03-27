---
title: RasAdminPortDisconnect function (Rassapi.h)
description: The RasAdminPortDisconnect function disconnects a port that is currently in use.
ms.assetid: 7ed3bc46-2d56-44c8-afd5-fcbdad0f7f3a
keywords:
- RasAdminPortDisconnect function RAS
topic_type:
- apiref
api_name:
- RasAdminPortDisconnect
api_location:
- Rassapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RasAdminPortDisconnect function

\[This function is provided only for backward compatibility with Windows NT Server 4.0. It returns ERROR\_CALL\_NOT\_IMPLEMENTED on Windows Server 2003. Applications should use the [**MprAdminPortDisconnect**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportdisconnect) function.\]

The **RasAdminPortDisconnect** function disconnects a port that is currently in use.

## Syntax


```C++
DWORD RasAdminPortDisconnect(
  _In_ const WCHAR *lpszServer,
  _In_ const WCHAR *lpszPort
);
```



## Parameters

<dl> <dt>

*lpszServer* \[in\]
</dt> <dd>

Pointer to a null-terminated Unicode string that specifies the name of the Windows NT/Windows 2000 RAS server. Specify the name with leading "\\\\" characters, in the form: \\\\*servername*.

</dd> <dt>

*lpszPort* \[in\]
</dt> <dd>

Pointer to a null-terminated Unicode string that specifies the name of the port on the server.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value can be one of the following error codes.



| Value                                                                                               | Meaning                                      |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_PORT**</dt> </dl> | The specified port is invalid.<br/>    |
| <dl> <dt>**NERR\_UserNotFound**</dt> </dl>   | The port is not currently in use.<br/> |



 

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
</dt> </dl>

 

