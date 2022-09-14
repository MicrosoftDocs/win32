---
title: RasAdminGetErrorString function (Rassapi.h)
description: The RasAdminGetErrorString function retrieves a message string that corresponds to a RAS error code returned by one of the RAS server administration (RasAdmin) functions.
ms.assetid: b51bc1f9-fed7-43b6-9a07-f19ea4c0cd01
keywords:
- RasAdminGetErrorString function RAS
topic_type:
- apiref
api_name:
- RasAdminGetErrorString
api_location:
- Rassapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# RasAdminGetErrorString function

\[This function is provided only for backward compatibility with Windows NT Server 4.0. It returns ERROR\_CALL\_NOT\_IMPLEMENTED on Windows Server 2003. Applications should use the [**MprAdminGetErrorString**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmingeterrorstring) function.\]

The **RasAdminGetErrorString** function retrieves a message string that corresponds to a RAS error code returned by one of the RAS server administration (RasAdmin) functions. These message strings are retrieved from the Rasmsg.dll that is installed as part of RAS.

## Syntax


```C++
DWORD RasAdminGetErrorString(
  _In_  UINT  ResourceId,
  _Out_ WCHAR *lpszString,
  _In_  DWORD InBufSize
);
```



## Parameters

<dl> <dt>

*ResourceId* \[in\]
</dt> <dd>

Specifies an error code returned by one of the RasAdmin functions. This value must be in the range of error codes from RASBASE to RASBASEEND. These are defined in Raserror.h.

</dd> <dt>

*lpszString* \[out\]
</dt> <dd>

Pointer to a buffer that receives the error message that corresponds to the specified error code.

</dd> <dt>

*InBufSize* \[in\]
</dt> <dd>

Specifies the size, in characters, of the *lpszString* buffer. Error messages are typically 80 characters or less; a buffer size of 512 characters is always adequate.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is an error code. This value can be a last error value set by the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya), [**GlobalAlloc**](/windows/win32/api/winbase/nf-winbase-globalalloc), or [**LoadString**](/windows/win32/api/winuser/nf-winuser-loadstringa) functions; or it can be one of the following error codes.



| Value                                                                                                      | Meaning                                                                  |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_PARAMETER**</dt> </dl>   | The *ResourceId* or *lpszString* parameters are invalid.<br/>      |
| <dl> <dt>**ERROR\_INSUFFICIENT\_BUFFER**</dt> </dl> | The size specified by the *InBufSize* parameter is too small.<br/> |



 

There is no extended error information for this function; do not call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

The RasAdmin functions can return error codes that are not in the range supported by the **RasAdminGetErrorString** function. For example, the RasAdmin functions can return error codes that are defined in Lmerr.h and Winerror.h. Before calling **RasAdminGetErrorString**, verify that the error code is in the range RASBASE to RASBASEEND, as defined in Raserror.h.

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

[**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya)
</dt> <dt>

[**GlobalAlloc**](/windows/win32/api/winbase/nf-winbase-globalalloc)
</dt> <dt>

[**LoadString**](/windows/win32/api/winuser/nf-winuser-loadstringa)
</dt> </dl>

 

