---
Description: Lists the DLL exports that must be implemented to create a credential manager.
ms.assetid: 8b176dd6-0e0b-4330-8889-f87384977ceb
title: Implementing a Credential Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementing a Credential Manager

To create a credential manager, you must create a DLL that exports the following functions:

-   [**NPLogonNotify**](/windows/win32/Npapi/nf-npapi-nplogonnotify?branch=master)
-   [**NPPasswordChangeNotify**](/windows/win32/Npapi/nf-npapi-nppasswordchangenotify?branch=master)

To restore notifications to the [**NPLogonNotify**](/windows/win32/Npapi/nf-npapi-nplogonnotify?branch=master) and [**NPPasswordChangeNotify**](/windows/win32/Npapi/nf-npapi-nppasswordchangenotify?branch=master) functions for smart card logon, create a registry entry called **SmartCardLogonNotify** as a **DWORD**, and set it to 1:

```
HKEY_LOCAL_MACHINE
   Software
   Microsoft
   Windows NT
   CurrentVersion
      Winlogon
         Notify
            SmartCardLogonNotify = 1
```

**Windows Server 2003 and Windows XP:** The **SmartCardLogonNotify** registry entry is not required.

In addition, credential managers should also support the [**NPGetCaps**](/windows/win32/Npapi/nf-npapi-npgetcaps?branch=master) function for WNNC\_START (supporting other indexes is not required for credential managers). This tells MPR when a credential manager will start. By calling **NPGetCaps** with the *nIndex* parameter set to WNNC\_START, the MPR gets the time to wait before calling the provider's credential management entry point functions. And if the MPR has this information, it can forward it to the credential manager, setting the time out.

 

 



