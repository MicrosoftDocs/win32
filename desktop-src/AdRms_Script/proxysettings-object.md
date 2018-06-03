---
Description: Represents the configuration settings of a proxy server for the AD RMS installation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f4859594-3e10-4ca2-870e-483ccd9f86ab
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ProxySettings object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ProxySettings object

The **ProxySettings** object represents the configuration settings of a proxy server for the AD RMS installation. AD RMS clusters use proxy servers to connect to external networks such as the Internet or another forest. The properties you can specify include the name of the proxy server, the port number through which the proxy can communicate, whether a proxy is required, whether the proxy can be bypassed, and the proxy authentication credentials. You can retrieve this object by calling the [**ProxySettings**](enterprise-proxysettings-property.md) property on the [**Enterprise**](enterprise-object.md) object.

## Members

The **ProxySettings** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ProxySettings** object has these methods.



| Method                                          | Description                                                                                          |
|:------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**Refresh**](proxysettings-refresh-method.md) | Refreshes the proxy settings from the settings that currently exist on the AD RMS server.<br/> |
| [**Update**](proxysettings-update-method.md)   | Updates the proxy setting state on the AD RMS server.<br/>                                     |



 

### Properties

The **ProxySettings** object has these properties.



| Property                                                                   | Description                                                                                                                                                                |
|:---------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Authentication**](proxysettings-authentication-property.md)<br/> | Retrieves an object that can be used to require proxy authentication, specify the type of authentication required, and retrieve or specify account credentials.<br/> |
| [**Bypass**](proxysettings-bypass-property.md)<br/>                 | Specifies or retrieves a Boolean value that indicates whether the proxy is bypassed for local connections.<br/>                                                      |
| [**BypassFilter**](proxysettings-bypassfilter-property.md)<br/>     | Specifies or retrieves one or more websites for which the proxy server cannot be used.<br/>                                                                          |
| [**Port**](proxysettings-port-property.md)<br/>                     | Specifies or retrieves the proxy port number.<br/>                                                                                                                   |
| [**Required**](proxysettings-required-property.md)<br/>             | Specifies or retrieves a Boolean value that indicates whether a proxy server is required.<br/>                                                                       |
| [**Server**](proxysettings-server-property.md)<br/>                 | Specifies or retrieves the IP address or Domain Name System (DNS) name of the proxy server.<br/>                                                                     |



 

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




