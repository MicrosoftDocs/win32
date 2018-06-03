---
Description: Retrieves an object that can be used to manage configuration settings of a proxy server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 2913333e-fc68-4c61-bd24-2ce915f1ed76
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Enterprise.ProxySettings property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enterprise.ProxySettings property

The **ProxySettings** property retrieves an object that can be used to manage configuration settings of a proxy server.

This property is read-only.

## Syntax


```VB
Enterprise.ProxySettings
```



## Property value

This property returns a [**ProxySettings**](proxysettings-object.md) object.

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

  ' Specify new settings.
  proxySettings.Required = TRUE
  proxySettings.Server = "NetProxy"
  proxySettings.Port = 80
  proxySettings.Bypass = TRUE
  proxySettings.BypassFilter = "http://www.widgets.microsoft.com/"
  proxySettings.Authentication.Required = TRUE
  proxySettings.Authentication.Scheme = 3
  proxySettings.Authentication.UserAccount.Domain = "user_Domain"
  proxySettings.Authentication.UserAccount.UserId = "user_ID"
  proxySettings.Authentication.UserAccount.Password = "user_Psswd"

  ' Update the proxy settings on the server.
  proxySettings.Update()
  CheckError()

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

[**Enterprise**](enterprise-object.md)
</dt> </dl>

 

 




