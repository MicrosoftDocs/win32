---
Description: 'Specifies or retrieves an integer value that identifies the type of authentication required.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '56ff9e20-0912-48bc-b84e-832b420ad93d'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ProxyAuthentication.Scheme property'
---

# ProxyAuthentication.Scheme property

The **Scheme** property specifies or retrieves an integer value that identifies the type of authentication required.

## Syntax


```VB
ProxyAuthentication.Scheme
```



## Property value

This property sets or returns one of the following values.

<dt>



 (0x0)


</dt> <dd>

No authentication is specified.

</dd> <dt>

<span id="ProxySchemeBasic"></span><span id="proxyschemebasic"></span><span id="PROXYSCHEMEBASIC"></span>

<span id="ProxySchemeBasic"></span><span id="proxyschemebasic"></span><span id="PROXYSCHEMEBASIC"></span>**[**ProxySchemeBasic**](constants-proxyschemebasic-property.md)** (0x1)


</dt> <dd>

Basic authentication.

</dd> <dt>

<span id="ProxySchemeDigest"></span><span id="proxyschemedigest"></span><span id="PROXYSCHEMEDIGEST"></span>

<span id="ProxySchemeDigest"></span><span id="proxyschemedigest"></span><span id="PROXYSCHEMEDIGEST"></span>**[**ProxySchemeDigest**](constants-proxyschemedigest-property.md)** (0x2)


</dt> <dd>

Digest authentication.

</dd> <dt>

<span id="ProxySchemeWindowsIntegrated"></span><span id="proxyschemewindowsintegrated"></span><span id="PROXYSCHEMEWINDOWSINTEGRATED"></span>

<span id="ProxySchemeWindowsIntegrated"></span><span id="proxyschemewindowsintegrated"></span><span id="PROXYSCHEMEWINDOWSINTEGRATED"></span>**[**ProxySchemeWindowsIntegrated**](constants-proxyschemewindowsintegrated-property.md)** (0x3)


</dt> <dd>

Integrated Windows authentication.

</dd> </dl>

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

[**ProxyAuthentication**](proxyauthentication-object.md)
</dt> </dl>

 

 




