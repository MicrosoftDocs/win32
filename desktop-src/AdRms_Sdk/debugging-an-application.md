---
Description: Debugging an application built by using the Active Directory Rights Management (AD RMS) SDK is not as simple as debugging other types of applications.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bccf89ca-775d-488c-a63b-490f6c4522e8
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Debugging an Application
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Debugging an Application

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Debugging an application built by using the Active Directory Rights Management (AD RMS) SDK is not as simple as debugging other types of applications. This is because when an AD RMS application is running inside a debugger and any function that requires the lockbox is called, the application will fail. The application will fail whether or not a breakpoint was set on the secure function. Because of this, you can only start an AD RMS-enabled application inside a debugger mode and debug it until you reach a secure function, or you can attach to the running process after the environment object and other secure objects have been created.

## Lockbox Communication Proxy

To allow a more normal debugging process, Microsoft provides a tool, called the lockbox communication proxy (LCP), that acts as a proxy to the actual lockbox. This proxy allows your application to run in a different process than the lockbox. When you use this proxy, you can run your application in debug mode in a relatively normal manner. The LCP is installed with the SDK in the Bin directory.

**RMS Client 1.0 SP2 and later:** The LCP is not supported. If you attach a debugger and try to step over the [**DRMInitEnvironment**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drminitenvironment) function, you will receive an E\_DRM\_DEBUGGER\_DETECTED error. To debug code following this function, you must break into the process and attach a debugger after the secure environment has been created.

For information about how to debug with and without the LCP and what advantages there are to each method, see the following topics:

-   [Debugging Without the LCP](debugging-without-the-lcp.md)
-   [Debugging With the LCP](debugging-with-the-lcp.md)

## Debug Message Tracing

The RMS client 1.0 SP2 and AD RMS running on Windows Server 2008 or Windows Vista can log debug and troubleshooting messages to the debug output window. By default, debug message tracing is not enabled. This option is enabled by setting a value in the registry of the client computer. To enable debug message tracing, add or set the following REG\_DWORD registry value.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**MSDRM**\\    **Trace** = 1<dl> <dt>

            Data type
</dt> <dd>            REG\_DWORD</dd> </dl>

To disable debug message tracing, set this registry value to zero or remove the value altogether. After this registry value is changed, it will take effect the next time you start your application.

## Related topics

<dl> <dt>

[Troubleshooting](troubleshooting.md)
</dt> <dt>

[Using the AD RMS SDK](using-the-ad-rms-sdk.md)
</dt> </dl>

 

 



