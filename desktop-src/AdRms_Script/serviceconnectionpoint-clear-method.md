---
Description: Deletes the current SCP URL from Active Directory so that it can be reset.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c2f52257-71e4-4dfb-9a03-a94bc42c4388
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ServiceConnectionPoint.Clear method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ServiceConnectionPoint.Clear method

The **Clear** method deletes the current SCP URL from Active Directory so that it can be reset.

## Syntax


```VB
ServiceConnectionPoint.Clear()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

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

 

 




