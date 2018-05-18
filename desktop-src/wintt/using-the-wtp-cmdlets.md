---
title: Using the WTP Cmdlets
ms.assetid: '045e5f05-dd81-4e77-ad62-42d4991bd672'
description: 
---

# Using the WTP Cmdlets

WTP provides the following cmdlets that you use in your scripts to communicate with WTP:

-   [Get-DiagInput](get-diaginput-cmdlet.md)
-   [Update-DiagReport](update-diagreport-cmdlet.md)
-   [Update-DiagRootcause](update-diagrootcause-cmdlet.md)
-   [Write-DiagProgress](write-progress-cmdlet.md)

## Using Update-DiagRootcause

To let WTP know the detection status of a root cause, the troubleshooter and verifier scripts use the [Update-DiagRootcause](update-diagrootcause-cmdlet.md) cmdlet. If a root cause ID in the troubleshooting manifest is DetectPopupBlocker, the following example shows how to call Update-DiagRootcause from a verifier script.


```PowerShell
#root cause Detected
Update-DiagRootcause -Id DetectPopupBlocker -Detected $true
```



## Using Write-DiagProgress

To provide feedback to the user that the troubleshooting pack is making progress, use the [Write-DiagProgress](write-progress-cmdlet.md) cmdlet. You should provide progress information whenever an action takes a long time to complete (more than one second). The following example shows how to use the Write-DiagProgress cmdlet to provide progress information to the user.


```PowerShell
#Write a progress message to the user.
Write-DiagProgress -Activity "Checking Pop-up Blocker..."
```



## Using Get-DiagInput

To get information from the user or to ask the user to perform a task, use the [Get-DiagInput](get-diaginput-cmdlet.md) cmdlet. The interaction that you use must be defined in the troubleshooting manifest. For more details on using interactions, see [Interacting with the User](interacting-with-the-user.md). If an interaction ID in the troubleshooting manifest is IT\_Notification, the following example shows how to call Get-DiagInput.


```PowerShell
#Lets the user select a color from a list of colors.
$color = Get-DiagInput -Id "ColorSelection"
```



## Using Update-DiagReport

To add additional information to the results report that WTP creates, call the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet. You can use the cmdlet to include the information directly in the report or you can include a link to a file that contains the additional information. For more details on providing custom reporting, see [Reporting](reporting.md). The following example shows how to use Update-DiagReport to include IE popup settings with the details of the root cause in the report.


```PowerShell
#Shows how to log the Internet Explorer Popup Settings to the Results Report in the troubleshooting phase.
$PopupMgr = Get-ItemProperty "Registry::HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\New Windows" "PopupMgr"
$PopupMgr | ConvertTo-Xml | Update-DiagReport -Id PopupMgr -RootcauseId DetectPopupBlocker -Name "Popup setting"-Description "Registry setting for Popup Blocker."
```



 

 




