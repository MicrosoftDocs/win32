---
title: Writing Scripts
description: The troubleshooting manifest specifies the scripts that are run during the troubleshooting, resolution, and verification phases.
ms.assetid: 'a9075aa8-b2c3-463b-ad9e-c119974f5a6c'
---

# Writing Scripts

The troubleshooting manifest specifies the scripts that are run during the troubleshooting, resolution, and verification phases. For a manifest that uses the local troubleshooting model, there is one troubleshooter script per root cause; however, for a manifest that uses the global troubleshooting model, there is only one troubleshooter script and it is responsible for detecting all root causes in the manifest. Also, for the local model, the troubleshooter and verifier scripts are typically the same script; however, for the global model, they must be different scripts.

During the troubleshooting phase, the troubleshooter scripts check for root causes on the computer and indicate whether each root cause was detected. For each root cause that was detected, WTP queues the related resolver and verifier scripts to run after the troubleshooting phase completes. You can specify more than one resolver script for a root cause. A resolver script can automatically resolve the issue or provide information to the user to have them resolve the issue.

After a resolver script runs, WTP runs the verifier script (verifier scripts are optional) to determine whether the resolver script fixed the root cause. If the resolver did not fix the root cause, WTP will apply any remaining resolvers associated with that root cause until it is fixed, or until there are no more resolvers to run. WTP will then attempt to resolve any remaining root causes that have been detected.

The following example shows a single script that can be used as a troubleshooter and verifier script for a manifest that uses local troubleshooters. The example also shows how to use the [Update-DiagRootcause](update-diagrootcause-cmdlet.md) cmdlet to update the root cause's status.


```PowerShell
#This is an example Troubleshooter/Verifier that detects/confirms that the popup blocker has been enabled.
#Note that this example does not provide any error handling.

#Write a progress message to the user
Write-DiagProgress -Activity "Checking Pop-up Blocker..."
    
#Get the popup blocker settings from the registry
$PopupMgr = Get-ItemProperty "Registry::HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\New Windows" "PopupMgr"
   
if (($PopupMgr.PopupMgr -ieq "no") -or ($PopupMgr.PopupMgr -eq "0")) 
{
    #Popup blocker is DISABLED. Rootcause DETECTED.
    Update-DiagRootcause -Id DetectPopupBlocker -Detected $true
    
}
else
{
    #Popup blocker is ENABLED. Rootcause NOT DETECTED.
    Update-DiagRootcause -Id DetectPopupBlocker -Detected $false
}
```



Because resolutions are tied to a specific root cause and are invoked when the root cause is detected, a resolver script should focus only on fixing the issue. The following is an example of a resolver script.


```PowerShell
#This is an example Resolver that enables the IE Popup blocker.
#Note that this example does not provide any error handling.

$PopupMgr = Get-ItemProperty "Registry::HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\New Windows" "PopupMgr"

if($PopupMgr.PopupMgr -ieq "no")
{
    Set-ItemProperty -Path "Registry::HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\New Windows" -Name PopupMgr -Value "yes"
}

if($PopupMgr.PopupMgr -eq "0")
{
    Set-ItemProperty -Path "Registry::HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\New Windows" -Name PopupMgr -Value "1"
}
```



For details on using the WTP cmdlets in your scripts, see [Using the WTP Cmdlets](using-the-wtp-cmdlets.md).

 

 




