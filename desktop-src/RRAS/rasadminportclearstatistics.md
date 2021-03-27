---
title: RasAdminPortClearStatistics function (Rassapi.h)
description: The RasAdminPortClearStatistics function resets the counters representing the various statistics reported by the RasAdminPortGetInfo function in the RAS\_PORT\_STATISTICS structure. The counters are reset to zero and start accumulating.
ms.assetid: d2ce4652-1034-4ded-aa26-2678c719d5b9
keywords:
- RasAdminPortClearStatistics function RAS
topic_type:
- apiref
api_name:
- RasAdminPortClearStatistics
api_location:
- Rassapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RasAdminPortClearStatistics function

\[This function is provided only for backward compatibility with Windows NT Server 4.0. It returns ERROR\_CALL\_NOT\_IMPLEMENTED on Windows Server 2003. Applications should use the [**MprAdminPortClearStats**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminportclearstats) function.\]

The **RasAdminPortClearStatistics** function resets the counters representing the various statistics reported by the [**RasAdminPortGetInfo**](rasadminportgetinfo.md) function in the [**RAS\_PORT\_STATISTICS**](ras-port-statistics-str.md) structure. The counters are reset to zero and start accumulating.

## Syntax


```C++
DWORD RasAdminPortClearStatistics(
  _In_ const WCHAR *lpszServer,
  _In_ const WCHAR *lpszPort
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

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value can be the following error code.



| Value                                                                                                 | Meaning                                   |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**ERROR\_DEV\_NOT\_EXIST**</dt> </dl> | The specified port is invalid.<br/> |



 

There is no extended error information for this function; do not call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

The **RasAdminPortClearStatistics** function clears the statistics on the server, not locally within the application that makes the call. This means that the statistics are also reset for any other application that is monitoring the specified port.

If the *lpszPort* port is part of a multilink connection, **RasAdminPortClearStatistics** resets the statistics for the specified port, The function also resets the cumulative statistics for the multilink connection. However, the function does not effect the individual statistics for other ports that are part of the multilink connection.

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

[**RAS\_PORT\_STATISTICS**](ras-port-statistics-str.md)
</dt> <dt>

[**RasAdminPortGetInfo**](rasadminportgetinfo.md)
</dt> </dl>

 

