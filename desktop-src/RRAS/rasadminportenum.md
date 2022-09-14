---
title: RasAdminPortEnum function (Rassapi.h)
description: The RasAdminPortEnum function enumerates all ports on the specified RAS server. For each port on the server, the function returns the RAS\_PORT\_0 structure that contains information about the port.
ms.assetid: ad23727c-8f54-4b10-9bc7-1425ac22bc88
keywords:
- RasAdminPortEnum function RAS
topic_type:
- apiref
api_name:
- RasAdminPortEnum
api_location:
- Rassapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RasAdminPortEnum function

\[This function is provided only for backward compatibility with Windows NT Server 4.0. It returns ERROR\_CALL\_NOT\_IMPLEMENTED on Windows Server 2003. Applications should use the [**MprAdminPortEnum**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportenum) function.\]

The **RasAdminPortEnum** function enumerates all ports on the specified RAS server. For each port on the server, the function returns the [**RAS\_PORT\_0**](ras-port-0-str.md) structure that contains information about the port.

## Syntax


```C++
DWORD RasAdminPortEnum(
  _In_  const WCHAR       *lpszServer,
  _Out_       PRAS_PORT_0 *ppRasPort0,
  _Out_       WORD        *pcEntriesRead
);
```



## Parameters

<dl> <dt>

*lpszServer* \[in\]
</dt> <dd>

Pointer to a null-terminated Unicode string that specifies the name of the RAS server. Specify the name with leading "\\\\" characters, in the form: \\\\*servername*.

</dd> <dt>

*ppRasPort0* \[out\]
</dt> <dd>

Pointer to a variable that receives a pointer to a buffer that contains an array of [**RAS\_PORT\_0**](ras-port-0-str.md) structures. When the application has finished with the memory, free it by calling the [**RasAdminFreeBuffer**](rasadminfreebuffer.md) function.

</dd> <dt>

*pcEntriesRead* \[out\]
</dt> <dd>

Pointer to a 16-bit variable that receives the total number of [**RAS\_PORT\_0**](/windows/desktop/api/Mprapi/ns-mprapi-ras_port_0) structures returned in the *ppRasPort0* array.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value can be the following error code.



| Value                                                                                             | Meaning                                                                                                                                     |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NERR\_ItemNotFound**</dt> </dl> | No ports could be enumerated. This could be because all configured ports on the server are currently being used for dialing out.<br/> |



 

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

[**RAS\_PORT\_0**](ras-port-0-str.md)
</dt> <dt>

[**RasAdminFreeBuffer**](rasadminfreebuffer.md)
</dt> </dl>

 

