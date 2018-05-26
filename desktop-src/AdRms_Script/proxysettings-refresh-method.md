---
Description: Refreshes the proxy settings from the settings that currently exist on the AD RMS server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e355a454-6a74-463e-87e2-0a2f2ef4d03d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ProxySettings.Refresh method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ProxySettings.Refresh method

The **Refresh** method refreshes the proxy settings from the settings that currently exist on the AD RMS server.

## Syntax


```VB
ProxySettings.Refresh()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

All of the settings for the current object will be overwritten when you call this method. Use this method to refresh your settings to ensure that you have the latest updates made by other administrators.

## Examples


```VB
DIM config_manager
DIM admin_role

' *******************************************************************
' Create and initialize a ConfigurationManager object.

SUB InitObject()

  CALL WScript.Echo( "Create ConfigurationManager object...")
  SET config_manager = CreateObject _
    ("Microsoft.RightsManagementServices.Admin.ConfigurationManager")      
  CheckError()
    
  CALL WScript.Echo( "Initialize...")
  admin_role=config_manager.Initialize(false,"localhost",80,"","","")
  CheckError()

END SUB

' *******************************************************************
' Retrieve and set proxy settings.

SUB Proxy()

  DIM proxySettings

  ' Retrieve the ProxySettings object.
  SET proxySettings = config_manager.Enterprise.ProxySettings
  CheckError()

  ' Refresh the settings.
  proxySettings.Refresh()
  CheckError()

  ' Display the current settings.
  WScript.Echo("required: " _
               & proxySettings.Required)
  WScript.Echo("server : " _
               & proxySettings.Server)
  WScript.Echo("Port   : " _
               & proxySettings.Port)
  WScript.Echo("ByPass : " _
               & proxySettings.Bypass)
  WScript.Echo("ByPassFilter : " _
               & proxySettings.BypassFilter)
  WScript.Echo("Auth : ")
  WScript.Echo("Required : " _
               & proxySettings.Authentication.Required)
  WScript.Echo("Scheme : " _
                & proxySettings.Authentication.Scheme)
  WScript.Echo("Domain : " _
                & proxySettings.Authentication.UserAccount.Domain)
  WScript.Echo("UserID : " _
               & proxySettings.Authentication.UserAccount.UserId)
  WScript.Echo("Passwd : " _
               & proxySettings.Authentication.UserAccount.Password)

END SUB

' *******************************************************************
' Error checking function.

FUNCTION CheckError()
  CheckError = Err.number
  IF Err.number <> 0 THEN
    CALL WScript.Echo( vbTab & "*****Error Number: " _
                       & Err.number _
                       & " Desc:" _
                       & Err.Description _
                       & "*****")
    WScript.StdErr.Write(Err.Description)
    WScript.Quit( Err.number )
  END IF
END FUNCTION
```



## Requirements



|                                     |                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ProxySettings**](proxysettings-object.md)
</dt> </dl>

 

 




