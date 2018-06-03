---
Description: Can be used to manage an AD RMS service account.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 69c29ef0-62ed-4cd8-abdb-81decbc22c78
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ServiceIdentity object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ServiceIdentity object

The **ServiceIdentity** object can be used to manage an AD RMS service account. Services, like users, are provided with accounts that can be authenticated. When you provision AD RMS on a server, you must define a service account and specify the account credentials. If the SQL server is shared by more than one AD RMS installation, the service account must be a domain account but not the same domain account that you used to install AD RMS. The service account is made a member of the RMS Service Group and is granted the permissions of that group.

You can retrieve the object by calling the [**ServiceIdentity**](configurationmanager-serviceidentity-property.md) property on the [**ConfigurationManager**](configurationmanager-object.md) object. You can use the **ServiceIdentity** object to change the service account. Doing so replaces the account previously contained in the RMS Service Group with the new account. This object does not support remote access.

## Members

The **ServiceIdentity** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ServiceIdentity** object has these methods.



| Method                                          | Description                                             |
|:------------------------------------------------|:--------------------------------------------------------|
| [**Update**](serviceidentity-update-method.md) | Updates a new service account to the server.<br/> |



 

### Properties

The **ServiceIdentity** object has these properties.



| Property                                                                                   | Description                                                                                    |
|:-------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**CurrentServiceAccount**](serviceidentity-currentserviceaccount-property.md)<br/> | Retrieves the current service account from the server.<br/>                              |
| [**NewServiceAccount**](serviceidentity-newserviceaccount-property.md)<br/>         | Retrieves a new service account object that can be populated and set on the server.<br/> |



 

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
  DIM oldAcct
  DIM newAcct

  ' Create a ServiceIdentity that can be used to change the 
  ' service account.
  SET chngMgr = config_manager.ServiceIdentity
  CheckError()

  ' Retrieve the current service account.
  SET oldAcct = chngMgr.CurrentServiceAccount
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

' *******************************************************************
' Generate a runtime error.

SUB RaiseError(errId, desc)
  CALL Err.Raise( errId, "", desc )
  CheckError()
END SUB
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

 

 




