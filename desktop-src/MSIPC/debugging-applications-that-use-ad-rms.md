---
title: How-to debug a rights-enabled application
description: The following topic shows how to debug your application and use the Windows Event Log.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 6F6C7651-6A6E-45DD-A0C5-F036F803249B
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How-to: debug a rights-enabled application

The following topic shows how to debug your application and use the Windows Event Log.

## Debugging your application

In Rights Management Services SDK 2.1, the anti-debugging checks in the developer version of our runtime are disabled.

You can turn on debug tracing by using the following registry key. (To turn debug tracing off, change the value to 0.) Nothing else is required for debugging in this release.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         MSIPC
            "Trace" = 00000001<dl>
<dt>

            Data type
</dt>
<dd>            dword</dd>
</dl>
```

## Application logging by using the Windows Event Log

The name of the event log is "Microsoft-RMS-MSIPC/Debug". This means that in the Windows Event Viewer, your log appears as "Application and Services Logs\\Microsoft\\RMS\\MSIPC\\Debug".

> [!Note]  
> The log is enabled by default and set to verbosity level 3.

 

To change the settings of the logging feature, you can use either the UI for the Windows Event Viewer or Wevtutil, a command line tool built into Windows.

Through the Wevtutil interface, you can control the level of verbosity of your log.

At this time, we support 3 levels of logging:

-   Level 2—Error
-   Level 3—Warning
-   Level 4—Information

For example, the following command will enable the MSIPC event log and set the level of verbosity to information.

**wevtutil sl Microsoft-RMS-MSIPC/Debug /e:true /l:4**

> [!Note]  
> In the Windows Event Viewer on the **View** menu, select **Show Analytic and Debug Logs** to make the MSIPC Debug log visible.

 

## Related topics

<dl> <dt>

[How-to use](https://msdn.microsoft.com/library/windows/desktop/hh535252)
</dt> </dl>

 

 




