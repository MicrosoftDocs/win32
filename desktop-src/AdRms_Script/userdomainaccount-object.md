---
Description: 'Contains account credential information.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'b36c5656-54b8-474d-8ac8-8db231f8c81f'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: UserDomainAccount object
---

# UserDomainAccount object

The **UserDomainAccount** object contains account credential information. This object is retrieved by calling the [**UserAccount**](proxyauthentication-useraccount-property.md) property on the [**ProxyAuthentication**](proxyauthentication-object.md) object or the [**CurrentServiceAccount**](serviceidentity-currentserviceaccount-property.md) property on the [**ServiceIdentity**](serviceidentity-object.md) object.

## Members

The **UserDomainAccount** object has these types of members:

-   [Properties](#properties)

### Properties

The **UserDomainAccount** object has these properties.



| Property                                                           | Description                                                |
|:-------------------------------------------------------------------|:-----------------------------------------------------------|
| [**Domain**](userdomainaccount-domain-property.md)<br/>     | Specifies or retrieves the account domain name.<br/> |
| [**Password**](userdomainaccount-password-property.md)<br/> | Specifies or retrieves the account password.<br/>    |
| [**UserId**](userdomainaccount-userid-property.md)<br/>     | Specifies or retrieves the account user ID.<br/>     |



 

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

 

 




