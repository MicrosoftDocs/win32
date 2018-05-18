---
title: Adding an Application
description: The Windows Firewall exceptions list concept and a sample demonstrating its use.
ms.assetid: '47a09bbc-7b34-41e4-bef8-124b275da0ba'
keywords: ["Windows Firewall", "using"]
---

# Adding an Application

The Windows Firewall exceptions list concept and a sample demonstrating its use.

An application that needs to listen to the network can be added to the Windows Firewall exceptions list. If an application is on the Windows Firewall exceptions list, Windows opens the necessary port automatically, regardless of the application's security context. When an application is on the Windows Firewall exceptions list, only the necessary ports are opened, and they are only opened for the duration that the application is listening on those ports. An application cannot open a port that it is not using, which might deliberately or inadvertently expose another application or service to network traffic from that port. This also allows applications that are listening to the network to run as a regular user.

It is recommended that independent software vendors (ISVs) place their application on the Windows Firewall exceptions list during installation.

The following VBScript sample demonstrates adding an application to the Windows Firewall exceptions list.


```VB
Option Explicit

' Set constants
Const NET_FW_PROFILE_DOMAIN = 0
Const NET_FW_PROFILE_STANDARD = 1

' Scope
Const NET_FW_SCOPE_ALL = 0

' IP Version <entity type="ndash"/> ANY is the only allowable setting for now
Const NET_FW_IP_VERSION_ANY = 2

' Declare variables
Dim errornum

' Create the firewall manager object.
Dim fwMgr
Set fwMgr = CreateObject("HNetCfg.FwMgr")

' Get the current profile for the local firewall policy.
Dim profile
Set profile = fwMgr.LocalPolicy.CurrentProfile

Dim app
Set app = CreateObject("HNetCfg.FwAuthorizedApplication")

app.ProcessImageFileName = "%PROGRAMFILES%\Outlook Express\msimn.exe"
app.Name = "Outlook Express"
app.Scope = NET_FW_SCOPE_ALL
' Use either Scope or RemoteAddresses, but not both
'app.RemoteAddresses = "*"
app.IpVersion = NET_FW_IP_VERSION_ANY
app.Enabled = TRUE

' Use this line if you want to add the app, but disabled.
'app.Enabled = FALSE

On Error Resume Next
errornum = 0
profile.AuthorizedApplications.Add app
errornum = Err.Number
if errornum <> 0 then Wscript.Echo("Adding authorized application failed with: " & errornum)

```



 

 




