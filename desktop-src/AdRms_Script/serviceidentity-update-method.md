---
Description: 'Updates a new service account to the server.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '73bf08bf-e010-4c75-b5ec-810dcaa3dff0'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ServiceIdentity.Update method'
---

# ServiceIdentity.Update method

The **Update** method updates a new service account to the server.

## Syntax


```VB
ServiceIdentity.Update()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Updating replaces the account previously contained in the RMS Service Group with the new account. This method performs the following tasks on the local computer. Remote access is not supported.

-   Grants database access to the service account.
-   Saves the account in the configuration database.
-   Changes the logging database service account to match.
-   Changes the IIS service account.
-   Changes the logging service account.
-   Changes the Message Queuing service account.
-   Adds the user to the local database service group.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ServiceIdentity**](serviceidentity-object.md)
</dt> </dl>

 

 




