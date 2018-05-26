---
title: Troubleshooting Cmdlets
description: Windows Troubleshooting Platform (WTP) provides cmdlets that let you communicate with the rest of the troubleshooting infrastructure.
ms.assetid: 1811f1e6-c0ff-4df2-9671-45f1337cb4f3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Troubleshooting Cmdlets

Windows Troubleshooting Platform (WTP) provides cmdlets that let you communicate with the rest of the troubleshooting infrastructure. The following are the cmdlets that WTP provides:

-   [Get-DiagInput](get-diaginput-cmdlet.md)
-   [Get-TroubleshootingPack](get-troubleshootingpack-cmdlet.md)
-   [Invoke-TroubleshootingPack](invoke-troubleshootingpack-cmdlet.md)
-   [Update-DiagReport](update-diagreport-cmdlet.md)
-   [Update-DiagRootcause](update-diagrootcause-cmdlet.md)
-   [Write-DiagProgress](write-progress-cmdlet.md)

You can call the [Get-TroubleshootingPack](get-troubleshootingpack-cmdlet.md) and [Invoke-TroubleshootingPack](invoke-troubleshootingpack-cmdlet.md) from any Windows PowerShell window; however, the others can be called only from a script in your troubleshooting pack (the cmdlets are available only during the execution of the pack).

 

 




