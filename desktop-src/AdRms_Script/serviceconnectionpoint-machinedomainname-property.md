---
Description: Retrieves the server domain name.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: fbd47a6a-acd5-4d3d-8b35-a21e6bc8f235
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ServiceConnectionPoint.MachineDomainName property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ServiceConnectionPoint.MachineDomainName property

The **MachineDomainName** property retrieves the server domain name.

This property is read-only.

## Syntax


```VB
ServiceConnectionPoint.MachineDomainName
```



## Property value

This property returns a string value.

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
' Manage the service connection point.

SUB ManageSCP()

  DIM SCP
  DIM scpURL
  DIM scpDomain

  ' Retrieve the ServiceConnectionPoint object.
  SET SCP = config_manager.Enterprise.ServiceConnectionPoint
  CheckError()

  ' Retrieve the current SCP URL.
  scpURL = SCP.URL

  ' Unregister the SCP URL.
  SCP.Clear()
  CheckError()

  ' Retrieve the domain name.
  scpDomain = SCP.MachineDomainName

  ' Register a new SCP URL.
  SCP.URL = "http://www.widgets.microsoft.com/"

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

[**ServiceConnectionPoint**](serviceconnectionpoint-object.md)
</dt> </dl>

 

 




