---
description: Sets the caller IP address to appear in security audit events.
ms.assetid: 21f8652e-4e7a-4176-8e91-eb4e78eb1afe
title: SeciAllocateAndSetIPAddress function
ms.topic: reference
ms.date: 07/31/2023
topic_type: 
- APIRef
api_name: 
- SeciAllocateAndSetIPAddress
api_type: 
- UserDefined
api_location: 
---

# SeciAllocateAndSetIPAddress function

Sets the caller IP address to appear in security audit events.

## Syntax

```C++
SECURITY_STATUS SEC_ENTRY SeciAllocateAndSetIPAddress(
  _in_  PUCHAR IPAddress,
  _in_  ULONG  IPAddressLength,
  _out_ PBOOL  FreeCallContext
);
```

## Parameters

*IPAddress* `[in]`

A pointer to the IP address to be set. The IP address is represented as a [SOCKADDR](/windows/win32/winsock/sockaddr-2) structure.

*IPAddressLength* `[in]`

The length of the *IPAddress* structure.

*FreeCallContext* `[out]`

If set to `TRUE`, the caller is responsible for calling [SeciFreeCallContext](SeciFreeCallContext.md).

## Return value

If the function succeeds, it returns **SEC_E_OK**.

If the function fails, it returns a nonzero error code.

## Remarks

This function is not present in the SDK headers. To use it, call the [LoadLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) function to obtain a handle to SSPICLI.DLL and then use [GetProcAddress](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) to obtain the function address.

The *IPAddress* parameter should be a valid pointer to an IP address structure obtained from the network layer. This corresponds to the *addr* output parameter to the [Accept](/windows/win32/api/winsock2/nf-winsock2-accept) function.

If *FreeCallContext* is set to `TRUE` on output, the caller must call [SeciFreeCallContext](SeciFreeCallContext.md) function before relinquishing the thread.

## Requirements

| Requirement | Value |
|--------|--------|
| Minimum supported client | Windows Vista \[desktop apps \| UWP apps\] |
| Minimum supported server | Windows Server 2008 \[desktop apps \| UWP apps\] |
| Target platform | Windows |
| Header | None |
| Library | None |
| DLL | SSPICLI.DLL |

## See also

[SeciFreeCallContext](SeciFreeCallContext.md)

[Accept](/windows/win32/api/winsock2/nf-winsock2-accept)

[SspiUnmarshalAuthIdentity](/windows/win32/api/sspi/nf-sspi-sspiunmarshalauthidentity)

[HttpListenerRequest.RemoteEndPoint](/dotnet/api/system.net.httplistenerrequest.remoteendpoint)
