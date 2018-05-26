---
Description: Retrieves a value that specifies Digest authentication for a proxy server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7cf7402d-de4c-4036-8eb1-6c8151197c95
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Constants.ProxySchemeDigest property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Constants.ProxySchemeDigest property

The **ProxySchemeDigest** property retrieves a value that specifies Digest authentication for a proxy server.

This property is read-only.

## Syntax


```VB
Constants.ProxySchemeDigest
```



## Property value

This property returns an integer value (0x2).

## Remarks

You can use this property value with the [**Scheme**](proxyauthentication-scheme-property.md) property on the [**ProxyAuthentication**](proxyauthentication-object.md) object.

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
' Retrieve proxy authentication scheme.

SUB GetProxyScheme()

  DIM proxySettings
  DIM constant
  DIM scheme

  ' Retrieve the Constants object.
  SET constant = config_manager.Constants 

  ' Retrieve the ProxySettings object.
  SET proxySettings = config_manager.Enterprise.ProxySettings
  CheckError()

  ' Retrieve the scheme.
  scheme = proxySettings.Authentication.Scheme

  IF scheme = constant.ProxySchemeBasic THEN
    CALL WScript.Echo("Proxy scheme is Basic authentication.")
  ELSEIF scheme = constant.ProxySchemeDigest THEN
    CALL WScript.Echo("Proxy scheme is Digest authentication.")
  ELSEIF scheme = constant.ProxySchemeWindowsIntegrated THEN
    CALL WScript.Echo("Proxy scheme is Windows Integrated.")
  ELSE
    CALL WScript.Echo("Authentication.Scheme error.")
  END IF

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

[**Constants**](constants-object.md)
</dt> <dt>

[**ProxySchemeBasic**](constants-proxyschemebasic-property.md)
</dt> <dt>

[**ProxySchemeWindowsIntegrated**](constants-proxyschemewindowsintegrated-property.md)
</dt> </dl>

 

 




