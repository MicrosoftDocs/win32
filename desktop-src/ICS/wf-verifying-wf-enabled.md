---
title: Verifying Windows Firewall is Enabled
description: Verifying Windows Firewall is Enabled
ms.assetid: ff3bbe5f-0fe6-40a1-bf65-8406a5aa2e5a
keywords:
- Windows Firewall
- using
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Verifying Windows Firewall is Enabled

The following example shows a verification of the status of the Windows Firewall.


```VB

Option Explicit

'Create Shell object
Dim objShell
set objShell = CreateObject("Shell.Application")

'Declare Firewall variables
Dim fwMgr
Dim profile

'Verify that the SharedAccess service is running. If it isn't, then start it.
If objShell.IsServiceRunning("SharedAccess") = FALSE Then
    objShell.ServiceStart "SharedAccess", TRUE
    'Sleep 1 second to make sure the service is started
    ' before trying to create the objects below. If there
    ' is no sleep, then the script is too fast and the
    ' firewall objects can't be created.
    WScript.Sleep 1000
End If
WScript.Echo("SharedAccess is running: " & objShell.IsServiceRunning("SharedAccess"))

' Firewall objects have to be created after making sure
' the service is running. If the service isn't running,
' the script will fail.

' Create the firewall manager object.
Set fwMgr = CreateObject("HNetCfg.FwMgr")

' Get the current profile for the local firewall policy.
Set profile = fwMgr.LocalPolicy.CurrentProfile

'Verify that the Firewall is enabled. If it isn't, then enable it.
If profile.FirewallEnabled = FALSE Then
    profile.FirewallEnabled = TRUE
End If
WScript.Echo("Firewall Enabled: " & profile.FirewallEnabled)

WScript.Echo("Firewall Exceptions Not Allowed: " & profile.ExceptionsNotAllowed)


```



 

 




