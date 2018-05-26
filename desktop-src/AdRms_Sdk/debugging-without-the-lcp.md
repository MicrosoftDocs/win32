---
Description: Although debugging is greatly simplified by using the lockbox communication proxy (LCP), using the LCP does have some disadvantages.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c7bf1f73-2665-465b-b008-eaa0dd920f51
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Debugging Without the LCP
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Debugging Without the LCP

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Although debugging is greatly simplified by using the lockbox communication proxy (LCP), using the LCP does have some disadvantages. For instance, using the LCP does not allow you to test the validity of the application manifest. Also, a certain number of functions, listed in [Debugging With the LCP](debugging-with-the-lcp.md), do not function normally. In these circumstances, the best choice for debugging an AD RMS-enabled application is to include frequent console printing functions, such as the `wprintf`, or `assert` statements to track the progress of an application. You can add an `assert` statement that fails when a function fails, attach a debugger to examine the environment, then detach and restart. So, for example, you can use the following `assert` after a secure function, as shown in the following example. For an example of using the `wprintf` function to track progress, see [OfflineSigning\_GetSignedIL.cpp](offlinesigning-getsignedil-cpp.md).

**RMS Client 1.0 SP2, Windows Vista, and Windows Server 2008:** The LCP is not supported. If you attach a debugger and try to step over the [**DRMInitEnvironment**](/windows/previous-versions/Msdrm/nf-msdrm-drminitenvironment?branch=master) function, you will receive an E\_DRM\_DEBUGGER\_DETECTED error. To debug code following this function, you must break into the process and attach a debugger after the secure environment has been created.


```C++
hr = DRMCreateClientSession(
          &amp;StatusCallback,                    // Callback function
          0,                                  // Reserved
          DRM_DEFAULTGROUPIDTYPE_WINDOWSAUTH, // Authentication type
          wszID,                              // User ID
          &amp;hClient);                          // Client handle
          if (FAILED(hr))
          {
            _ASSERTE(!"DRMCreateClientSession - Could not create!");
          }
```



If the function fails, attach the debugger, examine the environment, detach, ignore the assertion, and continue. The **\_ASSERTE** macro is included in the Crtdbg.h header. For more information about **\_ASSERTE**, see [\_ASSERT, \_ASSERTE Macros](http://go.microsoft.com/fwlink/p/?linkid=87267).

## Related topics

<dl> <dt>

[Debugging With the LCP](debugging-with-the-lcp.md)
</dt> <dt>

[Debugging an Application](debugging-an-application.md)
</dt> <dt>

[Troubleshooting](troubleshooting.md)
</dt> </dl>

 

 



