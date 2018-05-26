---
title: Iterating a Collection
description: Iterating a Collection
ms.assetid: 2a502415-c12a-4d07-9f72-a3967e87d37d
keywords:
- Windows Firewall
- using
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Iterating a Collection

The following code example iterates through a collection of [**AuthorizedApplications**](/windows/previous-versions/Netfw/nf-netfw-inetfwprofile-get_authorizedapplications?branch=master) displaying their properties.


```VB

Option Explicit

On Error Resume Next

' IP Version Constants

Const NET_FW_IP_VERSION_V4 = 0
Const NET_FW_IP_VERSION_V4_NAME = "IPv4"

Const NET_FW_IP_VERSION_V6 = 1
Const NET_FW_IP_VERSION_V6_NAME = "IPv6"

Const NET_FW_IP_VERSION_ANY = 2
Const NET_FW_IP_VERSION_ANY_NAME = "Any"

' Scope Constants

Const NET_FW_SCOPE_ALL = 0
Const NET_FW_SCOPE_ALL_NAME = "All"

Const NET_FW_SCOPE_LOCAL_SUBNET = 1
Const NET_FW_SCOPE_LOCAL_SUBNET_NAME = "Local Subnet"

Const NET_FW_SCOPE_CUSTOM = 2
Const NET_FW_SCOPE_CUSTOM_NAME = "Custom"


WScript.Echo("Create the FwPolicy object.")

Dim fwMgr
Set fwMgr = CreateObject("HNetCfg.FwMgr")

WScript.Echo("Get the Policy object.")

Dim fwPolicy
Set fwPolicy = fwMgr.LocalPolicy

WScript.Echo("Get the Profile Object.")

Dim CurrentProfile
Set CurrentProfile = fwPolicy.CurrentProfile

WScript.Echo("Get Authorized Applications Object.")

Dim fwAuthorizedApplications
Set fwAuthorizedApplications = CurrentProfile.AuthorizedApplications

if fwAuthorizedApplications.Count > 0 then
    
   WScript.Echo("Enumerating " & fwAuthorizedApplications.Count & " Authorized Application(s):")

   Dim app        
   For Each app In CurrentProfile.AuthorizedApplications

      WScript.Echo("  Name:             " & app.Name)
      WScript.Echo("  Image Filename    " & app.ProcessImageFileName)

      Select Case app.IpVersion
         Case NET_FW_IP_VERSION_V4 WScript.Echo("  IP Version:       " & NET_FW_IP_VERSION_V4_NAME)
         Case NET_FW_IP_VERSION_V6 WScript.Echo("  IP Version:       " & NET_FW_IP_VERSION_V6_NAME)
         Case NET_FW_IP_VERSION_ANY WScript.Echo("  IP Version:       " & NET_FW_IP_VERSION_ANY_NAME)
      End Select

      Select Case app.Scope
         Case NET_FW_SCOPE_ALL WScript.Echo("  Scope:            " & NET_FW_SCOPE_ALL_NAME)
         Case NET_FW_SCOPE_LOCAL_SUBNET WScript.Echo("  Scope:            " & NET_FW_SCOPE_LOCAL_SUBNET_NAME)
         Case NET_FW_SCOPE_CUSTOM WScript.Echo("  Scope:            " & NET_FW_SCOPE_CUSTOM_NAME)
      End Select
  
      WScript.Echo("  RemoteAddresses:  " & app.RemoteAddresses)
      WScript.Echo("  Enabled:          " & app.Enabled)

      WScript.Echo("")
 
   Next

else

   WScript.Echo("No Authorized Applications were found for Current Profile.")

end if


```



 

 




