---
Description: 'Specifies or retrieves the service connection point (SCP) URL.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'f722f4c2-2959-4952-96e1-14bf64ba8d91'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ServiceConnectionPoint.Url property'
---

# ServiceConnectionPoint.Url property

The **Url** property specifies or retrieves the service connection point (SCP) URL.

## Syntax


```VB
ServiceConnectionPoint.Url
```



## Property value

This property sets or returns a string value.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ServiceConnectionPoint**](serviceconnectionpoint-object.md)
</dt> </dl>

 

 




