---
Description: 'Specifies or retrieves one or more websites for which the proxy server cannot be used.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'b8298ebe-3521-4af2-a930-fdff1120f447'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ProxySettings.BypassFilter property'
---

# ProxySettings.BypassFilter property

The **BypassFilter** property specifies or retrieves one or more websites for which the proxy server cannot be used.

## Syntax


```VB
ProxySettings.BypassFilter
```



## Property value

This property sets or returns a string value that contains the IP addresses or DNS names of the sites that cannot be reached through the proxy server. You can separate multiple sites by using a semicolon (;). If you are using IP addresses, you can specify an incomplete address to indicate that all addresses beginning with the octets you specify cannot be reached through the proxy.

## Remarks

You can call the [**Bypass**](proxysettings-bypass-property.md) property to specify whether a filter is required.

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

  proxySettings.Bypass = TRUE
  proxySettings.BypassFilter = "http://www.widgets.microsoft.com/"

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ProxySettings**](proxysettings-object.md)
</dt> </dl>

 

 




