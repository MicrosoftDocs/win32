---
Description: Retrieves a ServiceIdentity object that can be used to manage an AD RMS service account.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 74d7c37b-782a-47f3-ad92-361239290cff
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ConfigurationManager.ServiceIdentity property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConfigurationManager.ServiceIdentity property

The **ServiceIdentity** property retrieves a [**ServiceIdentity**](serviceidentity-object.md) object that can be used to manage an AD RMS service account.

This property is read-only.

## Syntax


```VB
ConfigurationManager.ServiceIdentity
```



## Property value

This property returns a [**ServiceIdentity**](serviceidentity-object.md) object. The property is read-only.

## Remarks

A [**ServiceIdentity**](serviceidentity-object.md) object is typically used to change the service account.

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
' Change the service account.

SUB ChangeServiceAccount()
    
  DIM changeSvcAccount_manager
  SET changeSvcAccount_manager = config_manager.ServiceIdentity
  CheckError()
    
  DIM currentSvcAccount
  SET currentSvcAccount = _
    changeSvcAccount_manager.CurrentServiceAccount
  CheckError()

  DIM newSvcAccount
  SET newSvcAccount = changeSvcAccount_manager.NewServiceAccount
  CheckError()

  newSvcAccount.Type = _
    config_manager.Constants.ServiceAccountTypeDomainIdentity
  newSvcAccount.UserDomainAccount.Domain = "xxxx"
  newSvcAccount.UserDomainAccount.UserId = "yyyy"
  newSvcAccount.UserDomainAccount.Password = "zzzz"

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

[**ConfigurationManager**](configurationmanager-object.md)
</dt> </dl>

 

 




