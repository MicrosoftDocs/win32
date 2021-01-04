---
title: InternetGetProxyInfo function
description: Retrieves proxy data for accessing specified resources.
ms.assetid: 5fc0f471-420c-4125-8323-cb1e1e72e43f
keywords:
- InternetGetProxyInfo function WinINet
topic_type:
- apiref
api_name:
- InternetGetProxyInfo
api_location:
- JSProxy.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# InternetGetProxyInfo function

> [!NOTE]
> This function is deprecated. For autoproxy support, use HTTP Services (WinHTTP) version 5.1 instead. For more information, see [WinHTTP AutoProxy Support](../winhttp/winhttp-autoproxy-support.md).

Retrieves proxy data for accessing specified resources. This function can only be called by dynamically linking to "JSProxy.dll".

## Syntax

```cpp
BOOL InternetGetProxyInfo(
  _In_  LPCSTR  lpszUrl,
  _In_  DWORD   dwUrlLength,
  _In_  LPSTR   lpszUrlHostName,
  _In_  DWORD   dwUrlHostNameLength,
  _Out_ LPSTR   *lplpszProxyHostName,
  _Out_ LPDWORD lpdwProxyHostNameLength
);
```

## Parameters

<dl> <dt>

*lpszUrl* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the URL of the target HTTP resource.

</dd> <dt>

*dwUrlLength* \[in\]
</dt> <dd>

The size, in bytes, of the URL pointed to by *lpszUrl*.

</dd> <dt>

*lpszUrlHostName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the host name of the target URL.

</dd> <dt>

*dwUrlHostNameLength* \[in\]
</dt> <dd>

The size, in bytes, of the host name pointed to by *lpszUrlHostName*.

</dd> <dt>

*lplpszProxyHostName* \[out\]
</dt> <dd>

A pointer to the address of a buffer that receives the URL of the proxy to use in an HTTP request for the specified resource. The application is responsible for freeing this string.

</dd> <dt>

*lpdwProxyHostNameLength* \[out\]
</dt> <dd>

A pointer to a variable that receives the size, in bytes, of the string returned in the *lplpszProxyHostName* buffer.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise. To get extended error data, call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

To call **InternetGetProxyInfo**, you must dynamically link to it using the defined function-pointer type **pfnInternetGetProxyInfo**. The code snippet below shows how to declare an instance of this function-pointer type and then initialize and call it.

```cpp
  HMODULE hModJS;                               // Handle for loading the DLL
  pfnInternetGetProxyInfo pIGPI;                // Function-pointer instance

  hModJS = LoadLibrary( TEXT("jsproxy.dll") );
  if (!hModJS)
  {
    _tprintf( TEXT("\nLoadLibrary failed to load jsproxy.dll with error: %d\n"),
            GetLastError( ) );
    return( FALSE );
  }

  pIGPI = (pfnInternetGetProxyInfo)
          GetProcAddress( hModJS, "InternetGetProxyInfo" );
  if (!pIGPI)         
  {
    _tprintf( TEXT("\nGetProcAddress failed to find InternetGetProxyInfo, error: %d\n"),
            GetLastError( ) );
    return( FALSE );
  }

  // The pIGPI function pointer can now be used to call InternetGetProxyInfo.
```

Like all other aspects of the WinINet API, this function cannot be safely called from within DllMain or the constructors and destructors of global objects.

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>JSProxy.dll</dt> </dl> |

## See also

[**InternetInitializeAutoProxyDll**](/windows/win32/api/winineti/nf-winineti-internetinitializeautoproxydll)

[**InternetDeInitializeAutoProxyDll**](/previous-versions/windows/desktop/legacy/aa384580(v=vs.85))

[**DetectAutoProxyUrl**](/windows/win32/api/winineti/nf-winineti-detectautoproxyurl)
