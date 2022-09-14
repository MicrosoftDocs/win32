---
title: RasAdminPortGetInfo function (Rassapi.h)
description: The RasAdminPortGetInfo function retrieves information about a specified port on a specified server.
ms.assetid: 22837685-62a4-4e55-b88f-11019d5d4154
keywords:
- RasAdminPortGetInfo function RAS
topic_type:
- apiref
api_name:
- RasAdminPortGetInfo
api_location:
- Rassapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RasAdminPortGetInfo function

\[This function is provided only for backward compatibility with Windows NT Server 4.0. It returns ERROR\_CALL\_NOT\_IMPLEMENTED on Windows Server 2003. Applications should use the [**MprAdminPortGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportgetinfo) function.\]

The **RasAdminPortGetInfo** function retrieves information about a specified port on a specified server.

## Syntax


```C++
DWORD RasAdminPortGetInfo(
  _In_  const WCHAR               *lpszServer,
  _In_  const WCHAR               *lpszPort,
  _Out_       RAS_PORT_1          *pRasPort1,
  _Out_       RAS_PORT_STATISTICS *pRasStats,
  _Out_       RAS_PARAMETERS      **ppRasParams
);
```



## Parameters

<dl> <dt>

*lpszServer* \[in\]
</dt> <dd>

Pointer to a null-terminated Unicode string that specifies the name of the RAS server. Specify the name with leading "\\\\" characters, in the form: \\\\*servername*.

</dd> <dt>

*lpszPort* \[in\]
</dt> <dd>

Pointer to a null-terminated Unicode string that specifies the name of the port on the server.

</dd> <dt>

*pRasPort1* \[out\]
</dt> <dd>

Pointer to the [**RAS\_PORT\_1**](ras-port-1-str.md) structure that the function fills in with information about the state of the port.

</dd> <dt>

*pRasStats* \[out\]
</dt> <dd>

Pointer to the [**RAS\_PORT\_STATISTICS**](ras-port-statistics-str.md) structure that the function fills in with statistics about the port.

</dd> <dt>

*ppRasParams* \[out\]
</dt> <dd>

Pointer to a pointer variable that receives the address of an array of [**RAS\_PARAMETERS**](ras-parameters-str.md) structures. Each structure contains the name of a media-specific key, such as MAXCONNECTBPS, and its associated value. When the application is finished with this memory, free it by calling the [**RasAdminFreeBuffer**](rasadminfreebuffer.md) function.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value can be one of the following error codes.



| Value                                                                                                     | Meaning                                                                          |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_DEV\_NOT\_EXIST**</dt> </dl>     | The specified port is invalid.<br/>                                        |
| <dl> <dt>**ERROR\_NOT\_ENOUGH\_MEMORY**</dt> </dl> | Insufficient memory to allocate a buffer for the *ppRasParams* array.<br/> |



 

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

[**RAS\_PARAMETERS**](ras-parameters-str.md)
</dt> <dt>

[**RAS\_PORT\_1**](ras-port-1-str.md)
</dt> <dt>

[**RAS\_PORT\_STATISTICS**](ras-port-statistics-str.md)
</dt> <dt>

[**RasAdminFreeBuffer**](rasadminfreebuffer.md)
</dt> </dl>

 

