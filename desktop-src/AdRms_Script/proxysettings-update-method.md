---
Description: 'Updates the proxy setting state on the AD RMS server.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '4f27c94a-acf6-4149-89b4-ff0a2ab43299'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ProxySettings.Update method'
---

# ProxySettings.Update method

The **Update** method updates the proxy setting state on the AD RMS server.

## Syntax


```VB
ProxySettings.Update()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method updates the collection on the server with your changes while preserving the changes made by others. Call the [**Refresh**](proxysettings-refresh-method.md) method to update your collection from the server database.

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

  ' Specify settings.
  proxySettings.Required = TRUE
  proxySettings.Server = "NetProxy"
  proxySettings.Port = 80
  proxySettings.Bypass = FALSE
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ProxySettings**](proxysettings-object.md)
</dt> </dl>

 

 




