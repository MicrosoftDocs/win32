---
title: Critical System Services
description: Critical system services cannot be stopped and restarted by the Restart Manager without a system restart. Updates to any file or resource in use by one of these services requires a system restart.
ms.assetid: 8db7c91c-2f96-4d0c-a5b8-59c41a7e4845
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Critical System Services

Critical system services cannot be stopped and restarted by the Restart Manager without a system restart. Updates to any file or resource in use by one of these services requires a system restart.

**To determine whether a process is a critical system service.**

1.  Register the process using the [**RmRegisterResources**](/windows/win32/RestartManager/nf-restartmanager-rmregisterresources?branch=master) function.
2.  Call the [**RmGetList**](/windows/win32/RestartManager/nf-restartmanager-rmgetlist?branch=master) function to get the [**RM\_PROCESS\_INFO**](/windows/win32/RestartManager/ns-restartmanager-_rm_process_info?branch=master) structure.
3.  The **ApplicationType** member of the returned [**RM\_PROCESS\_INFO**](/windows/win32/RestartManager/ns-restartmanager-_rm_process_info?branch=master) structure contains a [**RM\_APP\_TYPE**](/windows/win32/RestartManager/ne-restartmanager-_rm_app_type?branch=master) enumeration value. This value is set to **RmCriticial** for a critical system process.

Critical system services include smss.exe, csrss.exe, wininit.exe, logonui.exe, lsass.exe, services.exe, winlogon.exe, System, svchost.exe with RPCSS, and svchost.exe with Dcom/PnP.

 

 




