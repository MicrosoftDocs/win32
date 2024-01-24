---
title: Critical System Services
description: Critical system services cannot be stopped and restarted by the Restart Manager without a system restart. Updates to any file or resource in use by one of these services requires a system restart.
ms.assetid: 8db7c91c-2f96-4d0c-a5b8-59c41a7e4845
ms.topic: article
ms.date: 05/31/2018
---

# Critical System Services

Critical system services cannot be stopped and restarted by the Restart Manager without a system restart. Updates to any file or resource in use by one of these services requires a system restart.

**To determine whether a process is a critical system service.**

1.  Register the process using the [**RmRegisterResources**](/windows/desktop/api/RestartManager/nf-restartmanager-rmregisterresources) function.
2.  Call the [**RmGetList**](/windows/desktop/api/RestartManager/nf-restartmanager-rmgetlist) function to get the [**RM\_PROCESS\_INFO**](/windows/desktop/api/RestartManager/ns-restartmanager-rm_process_info) structure.
3.  The **ApplicationType** member of the returned [**RM\_PROCESS\_INFO**](/windows/desktop/api/RestartManager/ns-restartmanager-rm_process_info) structure contains a [**RM\_APP\_TYPE**](/windows/desktop/api/RestartManager/ne-restartmanager-rm_app_type) enumeration value. This value is set to **RmCritical** for a critical system process.

Critical system services include smss.exe, csrss.exe, wininit.exe, logonui.exe, lsass.exe, services.exe, winlogon.exe, System, svchost.exe with RPCSS, and svchost.exe with Dcom/PnP.

 

 




