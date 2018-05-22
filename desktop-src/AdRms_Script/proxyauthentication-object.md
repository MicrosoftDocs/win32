---
Description: 'Can be used to specify the type of proxy server authentication required, if any, and to set the authentication credentials.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '7865664c-13f6-447c-b5d5-c91cd7350a4e'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: ProxyAuthentication object
---

# ProxyAuthentication object

The **ProxyAuthentication** object can be used to specify the type of proxy server authentication required, if any, and to set the authentication credentials. You can retrieve this object by calling the [**Authentication**](proxysettings-authentication-property.md) property on the [**ProxySettings**](proxysettings-object.md) object.

## Members

The **ProxyAuthentication** object has these types of members:

-   [Properties](#properties)

### Properties

The **ProxyAuthentication** object has these properties.



| Property                                                                   | Description                                                                                                 |
|:---------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**Required**](proxyauthentication-required-property.md)<br/>       | Specifies or retrieves a Boolean value that identifies whether proxy authentication is required.<br/> |
| [**Scheme**](proxyauthentication-scheme-property.md)<br/>           | Specifies or retrieves an integer value that identifies the type of authentication required.<br/>     |
| [**UserAccount**](proxyauthentication-useraccount-property.md)<br/> | Retrieves an object that can be used to set or return account credentials.<br/>                       |



 

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




