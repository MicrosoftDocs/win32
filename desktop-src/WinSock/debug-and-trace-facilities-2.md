---
description: Debug and trace facilities and Windows Sockets 2.
ms.assetid: eb29fc21-92d6-4471-860a-fd1c531686f6
title: Debug and Trace Facilities
ms.topic: article
ms.date: 05/31/2018
---

# Debug and Trace Facilities

Windows Sockets 2 application developers need to isolate bugs in:

-   The application.
-   The *Ws2\_32.dll* or one of the compatibility shim DLLs.
-   The service provider.

Windows Sockets 2 addresses this need through several components and features:

-   Integrated support for Winsock tracing on Windows Vista and later.
-   A specially devised debug version of the *Ws2\_32.dll* on Windows Vista.
-   A separate primitive debug and trace facility for use on Windows Server 2003 and Windows XP.

## Winsock Tracing using Event Tracing for Windows

Integrated support for Winsock tracing using Event Tracing for Windows (ETW) is included on Windows Vista and later. This is the preferred method for tracing Winsock calls on Windows Vista and later. Winsock tracing using ETW is lightweight and works on retail versions of Windows. No additional software or components are required. This feature just needs to be enabled on Windows Vista and later. For more detailed information, see the [Winsock Tracing](winsock-tracing.md) topics.

## Using a Debug Version of Ws2\_32.dll

The combination of a debug version of the *Ws2\_32.dll* on Windows Vista and Winsock tracing allows all procedure calls across the Windows Sockets 2 API or SPI to be monitored and, to some extent, controlled.

If a version of the Microsoft Windows Software Development Kit (SDK) for Windows Vista is installed to the default location, debug versions of the *Ws2\_32.dll* for various architectures are located under the following folder:

**C:\\Program Files\\Microsoft SDKs\\Windows\\v6.0\\NoRedist**

A checked version of the *Ws2\_32.dll* that matches the version of Windows and the Service Pack you are testing on should be used. Be aware that security patches may have been applied that updated the *Ws2\_32.dll* on your test system. The Windows SDK for Windows Vista and the earlier Platform Software Development Kit (SDK) DVD/CD subscriptions include checked builds for the various versions of Windows. You should use the same checked version of the *Ws2\_32.dll* as the retail version that was used on the system being tested. Note also that behavior running under a checked build will not be the same as running with a retail build.

**Note**  The Windows SDK for Windows Server 2008 and later no longer includes special debug versions of the *Ws2\_32.dll*. Developers should use Winsock tracing using ETW instead, since this feature does not require debug builds.

## Winsock Debug and Trace Facility on Windows Server 2003 and Windows XP

Older versions of Windows prior to Windows 8 and Windows Server 2012 support a separate primitive debug and trace facility that is included as a sample with the Windows SDK and the older Platform SDK. The debug/trace facility should only be used on Windows Server 2003 and Windows XP where Winsock tracing is not supported.

If the Windows SDK for Windows 7 is installed to the default location, this primitive Winsock tracing feature is installed in the following folder:

**C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\NetDs\\winsock\\dt\_dll**

The *DbgSpec.doc* file in this folder provides documentation on this primitive trace facility. The sample code in the dt\_dll folder needs to be compiled to use this facility. Developers are free to use the source code to develop versions of the debug/trace DLL that meet their specific needs.

Note that this primitive Winsock trace feature will only work with the debug version of *Ws2\_32.dll* installed. So you will need to get a checked version of the *Ws2\_32.dll* that matches the version of Windows and the Service Pack you are testing on.

A limitation of this primitive dt\_dll trace facility is that the sample code uses a global lock (critical section) for each Winsock function call. So this facility is not useful in dealing with race conditions. The sample code would need to be substantially rewritten to make this trace facility useful for dealing with most real Winsock problems (replacing the global locks). This sample code does allow developers to trace the procedure calls, procedure returns, parameter values, and return values.

Developers can use this primitive mechanism to trace procedure calls, procedure returns, parameter values, and return values. Parameter values and return values can be altered on procedure call or procedure return. If desired, a procedure call can be prevented or redirected. With access to this level of information and control, a developer is better able to isolate a problem in the application, *Ws2\_32.dll*, or service provider.

## Related topics

<dl> <dt>

[Winsock Tracing](winsock-tracing.md)
</dt> </dl>

 

 



