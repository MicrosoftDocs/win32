---
title: Detecting the Remote Desktop Services environment
description: To optimize performance, it is good practice for applications to detect whether they are running in a Remote Desktop Services client session.
ms.assetid: 9ba03801-8471-43a9-8e24-114a082d5776
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Detecting the Remote Desktop Services environment

To optimize performance, it is good practice for applications to detect whether they are running in a Remote Desktop Services client session. For example, when an application is running on a remote session, it should eliminate unnecessary graphic effects, as described in [Graphic Effects](graphic-effects.md). If the user is running the application in a local environment, it is not as critical for the application to optimize its behavior.

The following example shows a function that returns **TRUE** if the application is running in a remote session and **FALSE** if the application is running on the console.


```C++
#include <windows.h>
#pragma comment(lib, "user32.lib")

BOOL IsRemoteSession(void)
{
   return GetSystemMetrics( SM_REMOTESESSION );
}
```



For more information, see [Run-time Linking to Wtsapi32.dll](run-time-linking-to-wtsapi32-dll.md).

You should not use **GetSystemMetrics(SM\_REMOTESESSION)** to determine if your application is running in a remote session in Windows 8 and later or Windows Server 2012 and later if the remote session may also be using the RemoteFX vGPU improvements to the Microsoft Remote Display Protocol (RDP). In this case, **GetSystemMetrics(SM\_REMOTESESSION)** will identify the remote session as a local session.

Your application can check the following registry key to determine whether the session is a remote session that uses RemoteFX vGPU. If a local session exists, this registry key provides the ID of the local session.

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Terminal Server\\GlassSessionId**

If the ID of the current session in which the application is running is the same as in the registry key, the application is running in a local session. Sessions identified as remote session in this way include remote sessions that use RemoteFX vGPU. The following sample code demonstrates this.


```C++
#define TERMINAL_SERVER_KEY _T("SYSTEM\\CurrentControlSet\\Control\\Terminal Server\\")
#define GLASS_SESSION_ID    _T("GlassSessionId")

BOOL
IsCurrentSessionRemoteable()
{
    BOOL fIsRemoteable = FALSE;
                                       
    if (GetSystemMetrics(SM_REMOTESESSION)) 
    {
        fIsRemoteable = TRUE;
    }
    else
    {
        HKEY hRegKey = NULL;
        LONG lResult;

        lResult = RegOpenKeyEx(
            HKEY_LOCAL_MACHINE,
            TERMINAL_SERVER_KEY,
            0, // ulOptions
            KEY_READ,
            &hRegKey
            );

        if (lResult == ERROR_SUCCESS)
        {
            DWORD dwGlassSessionId;
            DWORD cbGlassSessionId = sizeof(dwGlassSessionId);
            DWORD dwType;

            lResult = RegQueryValueEx(
                hRegKey,
                GLASS_SESSION_ID,
                NULL, // lpReserved
                &dwType,
                (BYTE*) &dwGlassSessionId,
                &cbGlassSessionId
                );

            if (lResult == ERROR_SUCCESS)
            {
                DWORD dwCurrentSessionId;

                if (ProcessIdToSessionId(GetCurrentProcessId(), &dwCurrentSessionId))
                {
                    fIsRemoteable = (dwCurrentSessionId != dwGlassSessionId);
                }
            }
        }

        if (hRegKey)
        {
            RegCloseKey(hRegKey);
        }
    }

    return fIsRemoteable;
}
```



 

 




