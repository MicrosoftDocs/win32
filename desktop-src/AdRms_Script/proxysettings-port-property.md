---
Description: Specifies or retrieves the proxy port number.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1e96dcde-ad6c-4c85-810f-c0ef3ed60244
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ProxySettings.Port property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ProxySettings.Port property

The **Port** property specifies or retrieves the proxy port number.

## Syntax


```VB
ProxySettings.Port
```



## Property value

This property sets or returns an integer value.

## Remarks

The port number identifies the port that the proxy server uses to connect to the Internet.

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

  proxySettings.Required = TRUE
  proxySettings.Server = "NetProxy"
  proxySettings.Port = 80

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

[**ProxySettings**](proxysettings-object.md)
</dt> </dl>

 

 




