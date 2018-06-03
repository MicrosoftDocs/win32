---
Description: Retrieves an object that can be used to manage a service connection point (SCP).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f111d37a-f185-448c-a73b-39fffda279de
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Enterprise.ServiceConnectionPoint property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enterprise.ServiceConnectionPoint property

The **ServiceConnectionPoint** property retrieves an object that can be used to manage a service connection point (SCP).

This property is read-only.

## Syntax


```VB
Enterprise.ServiceConnectionPoint
```



## Property value

This property returns a [**ServiceConnectionPoint**](serviceconnectionpoint-object.md) object.

## Remarks

A valid SCP enables clients to discover an AD RMS service so that they can request use licenses, publishing licenses, or rights account certificates.

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

[**Enterprise**](enterprise-object.md)
</dt> </dl>

 

 




