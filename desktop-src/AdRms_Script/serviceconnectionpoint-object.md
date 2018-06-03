---
Description: Can be used to manage a service connection point (SCP).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4038435f-42c5-438d-b216-a441a26c5638
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ServiceConnectionPoint object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ServiceConnectionPoint object

The **ServiceConnectionPoint** object can be used to manage a service connection point (SCP). You must register the SCP URL in Active Directory so that clients can discover the root certification server and use the services running on the server. Clients will not be able to discover RMS to request use licenses, publishing licenses, or rights account certificates without a valid SCP. You can use this object to register or reset the SCP URL. You must, however, be logged on with a valid domain user account that has sufficient privileges to create a container object in the Services container. By default, this object uses the current user logon account information. You can retrieve the object by calling the [**ServiceConnectionPoint**](enterprise-serviceconnectionpoint-property.md) property on the [**Enterprise**](enterprise-object.md) object.

## Members

The **ServiceConnectionPoint** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ServiceConnectionPoint** object has these methods.



| Method                                               | Description                                                                           |
|:-----------------------------------------------------|:--------------------------------------------------------------------------------------|
| [**Clear**](serviceconnectionpoint-clear-method.md) | Deletes the current SCP URL from Active Directory so that it can be reset.<br/> |



 

### Properties

The **ServiceConnectionPoint** object has these properties.



| Property                                                                                  | Description                                    |
|:------------------------------------------------------------------------------------------|:-----------------------------------------------|
| [**MachineDomainName**](serviceconnectionpoint-machinedomainname-property.md)<br/> | Retrieves the server domain name.<br/>   |
| [**Url**](serviceconnectionpoint-url-property.md)<br/>                             | Specifies or retrieves the SCP URL.<br/> |



 

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




