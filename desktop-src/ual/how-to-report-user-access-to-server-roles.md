---
title: How to report user access to a server.
description: This topic explains how to report user access to a server by using User Access Logging (UAL).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8A4EF5D9-4BCF-42F9-AB76-A74E9F57A8E4
ms.prod: windows-server-dev
ms.technology: user-access-logging
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# How to report user access to a server.

This topic explains how to report user access to a server by using [User Access Logging](user-access-logging.md) (UAL).

### Prerequisites

-   The example in this topic is provided in C++. A basic understanding of server roles is recommended.

## Instructions

### 

1.  Register the server role by calling the [**UalRegisterProduct**](/windows/previous-versions/Ual/nf-ual-ualregisterproduct?branch=master) function. Call this function either at application setup or at first launch.
2.  Allocate and populate a [**UAL\_DATA\_BLOB**](/windows/previous-versions/Ual/ns-ual-tagual_data_blob?branch=master) structure.
3.  Start a UAL session by calling the [**UalStart**](/windows/previous-versions/Ual/nf-ual-ualstart?branch=master) function. Call this function each time the application starts.
4.  Call the [**UalInstrument**](/windows/previous-versions/Ual/nf-ual-ualinstrument?branch=master) function to log user access.
5.  Call the [**UalStop**](/windows/previous-versions/Ual/nf-ual-ualstop?branch=master) function to stop the UAL session and clean up resources.

## Remarks

By default, UAL is configured to update data every 24 hours. For testing purposes, you might want to shorten this interval. To do this, add a registry key of type **DWORD** that specifies the interval between updates. For example, to shorten the interval to 2 minutes, add the following registry value:

**HKLM**\\**System**\\**CurrentControlSet**\\**Control**\\**WMI**\\**Autologger**\\**Sum**\\*PollingInterval* = 120000<dl> <dt>

                  Data type
</dt> <dd>                  REG\_DWORD</dd> </dl>

Restart UAL after creating this registry key.

## Complete example


```C++
// UalSample.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <strsafe.h>
#include <ws2tcpip.h>
#include "ual.h"

GUID RoleIdentifier = { 0x3D1A8E20, 0xAD01, 0x457B, 0xB0, 0x44, 0x79, 0x11, 0x3F, 0x30, 0xC5, 0x4C };
GUID TenantIdentifier = { 0xEB3114F6, 0xD9D0, 0x41EF, 0x81, 0xE3, 0xD3, 0x24, 0xD3, 0xCE, 0x56, 0x62 };

int wmain(int argc, wchar_t* argv[])
{
    UalRegisterProduct(L"ProductName", L"RoleName", L"{3D1A8E20-AD01-457B-B044-79113F30C54C}");

    UAL_DATA_BLOB ualDataBlob;
    ZeroMemory(&amp;ualDataBlob, sizeof(UAL_DATA_BLOB));
    ualDataBlob.Size = sizeof(UAL_DATA_BLOB);
    ualDataBlob.RoleGuid = RoleIdentifier;
    ualDataBlob.TenantId = TenantIdentifier;

    if (S_OK == UalStart(&amp;ualDataBlob))
    {
        // Log user access IPv4 address.
        ualDataBlob.Address.ss_family = AF_INET;
        InetPton(AF_INET, L"192.168.2.100", &amp;(reinterpret_cast<SOCKADDR_IN *>(&amp;ualDataBlob.Address)->sin_addr));
        UalInstrument(&amp;ualDataBlob);

        // Log user access IPv6 address.
        ualDataBlob.Address.ss_family = AF_INET6;
        InetPton(AF_INET6, L"2001:4898:2b:4:551d:3aaa:f951:b202", &amp;(reinterpret_cast<SOCKADDR_IN6 *>(&amp;ualDataBlob.Address)->sin6_addr));
        UalInstrument(&amp;ualDataBlob);

        // Log user access IP address and name.
        StringCchCopy(ualDataBlob.UserName, ARRAYSIZE(ualDataBlob.UserName), L"ClientName");
        UalInstrument(&amp;ualDataBlob);

        UalStop(&amp;ualDataBlob);
    }

    return 0;
}

```



 

 




