---
title: TLSDisconnectFromServer function
description: Closes an open handle to a Remote Desktop license server.
ms.assetid: b4b001ec-823b-4514-bbec-839a83a9a189
ms.tgt_platform: multiple
keywords:
- TLSDisconnectFromServer function Remote Desktop Services
topic_type:
- apiref
api_name:
- TLSDisconnectFromServer
api_location:
- Mstlsapi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# TLSDisconnectFromServer function

Closes an open handle to a Remote Desktop license server.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mstlsapi.dll.

 

## Syntax


```C++
void WINAPI TLSDisconnectFromServer(
  _In_ TLS_HANDLE hHandle
);
```



## Parameters

<dl> <dt>

*hHandle* \[in\]
</dt> <dd>

Handle to a Remote Desktop license server that is opened by a call to the [**TLSConnectToLsServer**](tlsconnecttolsserver.md) function.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Call the **TLSDisconnectFromServer** function as part of your program's clean-up routine to close all the server handles that are opened by calls to the [**TLSConnectToLsServer**](tlsconnecttolsserver.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Mstlsapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**TLS\_HANDLE**](tls-handle.md)
</dt> <dt>

[**TLSConnectToLsServer**](tlsconnecttolsserver.md)
</dt> </dl>

 

