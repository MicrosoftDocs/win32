---
title: Developing RPC Windows Applications
description: When you install the Windows Software Development Kit (SDK), the following RPC development environment, the run-time libraries, and tools are automatically installed
ms.assetid: d5da3bca-5251-4ba4-b873-0817fe0f298d
ms.topic: article
ms.date: 05/31/2018
---

# Developing RPC Windows Applications

When you install the [Windows Software Development Kit (SDK)](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/), the following RPC development environment, the run-time libraries, and tools are automatically installed:

-   C/C++ language header (.H) files
-   RPC import libraries (.lib) files
-   Sample programs
-   RPC reference Help files
-   The **uuidgen** utility

When you install Windows, the following are installed:

-   RPC Run-time DLLs
-   Microsoft Locator (not supported on Windows Vista and later)
-   RPC Endpoint-mapping services

The following RPC import libraries.



| Import library | Description                |
|----------------|----------------------------|
| Rpcns4.lib     | Name-service functions     |
| Rpcrt4.lib     | Windows run-time functions |



 

> [!Note]  
> Rpcns4.lib is obsolete and no longer supported.

 

The following RPC libraries are included for down-level support.



| Dynamic-link library | Description                 | Platform                           |
|----------------------|-----------------------------|------------------------------------|
| Rpcltc1.dll          | Client named-pipe transport | Windows NT, Windows 98, Windows 95 |
| Rpclts1.dll          | Server named-pipe transport | Windows NT, Windows 98, Windows 95 |
| Rpcltc3.dll          | Client TCP/IP transport     | Windows NT, Windows 98, Windows 95 |
| Rpclts3.dll          | Server TCP/IP transport     | Windows NT, Windows 98, Windows 95 |
| Rpcltc5.dll          | Client NetBIOS transport    | Windows NT, Windows 98, Windows 95 |
| Rpclts5.dll          | Server NetBIOS transport    | Windows NT, Windows 98, Windows 95 |
| Rpcltc6.dll          | Client SPX transport        | Windows NT, Windows 98, Windows 95 |
| Rpclts6.dll          | Server SPX transport        | Windows NT, Windows 98, Windows 95 |
| Rpcdgc6.dll          | Client IPX transport        | Windows NT                         |
| Rpcdgs6.dll          | Server IPX transport        | Windows NT                         |
| Rpcdgc3.dll          | Client UDP transport        | Windows NT                         |
| Rpcdgs3.dll          | Server UDP transport        | Windows NT                         |



 

You will also need the Microsoft Interface Definition Language (MIDL) compiler. For more information, see [Using The MIDL Compiler](/windows/desktop/Midl/using-the-midl-compiler-2).

 

 
