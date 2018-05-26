---
Description: Retrieves a new service account object that can be populated and set on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 75b7af80-864d-4008-aec1-9e2fb7e7c7b4
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ServiceIdentity.NewServiceAccount property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ServiceIdentity.NewServiceAccount property

The **NewServiceAccount** property retrieves a new service account object that can be populated and set on the server.

This property is read-only.

## Syntax


```VB
ServiceIdentity.NewServiceAccount
```



## Property value

This property returns a [**UserDomainAccount**](userdomainaccount-object.md) object.

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
' Retrieve the current account and change it.

SUB ChangeServiceAccount()

  DIM chngMgr
  DIM newAcct

  ' Create a ServiceIdentity that can be used to change the 
  ' service account.
  SET chngMgr = config_manager.ServiceIdentity
  CheckError()

  ' Create a new account.
  SET newAcct = chngMgr.NewServiceAccount
  CheckError()

  newAcct.Domain = "domain_name"
  newAcct.UserId = "User_id"
  newAcct.Password = "password"

  ' Update service account with the new account information.
  chngMgr.Update()
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ServiceIdentity**](serviceidentity-object.md)
</dt> </dl>

 

 




