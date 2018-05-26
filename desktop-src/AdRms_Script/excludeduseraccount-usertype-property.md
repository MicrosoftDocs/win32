---
Description: Retrieves the type of the excluded user account.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c8431452-a724-43e8-83a3-de59fbb83f64
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExcludedUserAccount.UserType property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExcludedUserAccount.UserType property

The **UserType** property retrieves the type of the excluded user account.

This property is read-only.

## Syntax


```VB
ExcludedUserAccount.UserType
```



## Property value

This read-only property returns one of the following integer values.

<dt>

<span id="ExcludedDomainUserType"></span><span id="excludeddomainusertype"></span><span id="EXCLUDEDDOMAINUSERTYPE"></span>

<span id="ExcludedDomainUserType"></span><span id="excludeddomainusertype"></span><span id="EXCLUDEDDOMAINUSERTYPE"></span>**[**ExcludedDomainUserType**](constants-excludeddomainusertype-property.md)** (0)


</dt> <dd>

Domain account.

</dd> <dt>

<span id="ExcludedFederationUserType"></span><span id="excludedfederationusertype"></span><span id="EXCLUDEDFEDERATIONUSERTYPE"></span>

<span id="ExcludedFederationUserType"></span><span id="excludedfederationusertype"></span><span id="EXCLUDEDFEDERATIONUSERTYPE"></span>**[**ExcludedFederationUserType**](constants-excludedfederationusertype-property.md)** (1)


</dt> <dd>

Federated account.

</dd> <dt>

<span id="ExcludedExternalUserType"></span><span id="excludedexternalusertype"></span><span id="EXCLUDEDEXTERNALUSERTYPE"></span>

<span id="ExcludedExternalUserType"></span><span id="excludedexternalusertype"></span><span id="EXCLUDEDEXTERNALUSERTYPE"></span>**[**ExcludedExternalUserType**](constants-excludedexternalusertype-property.md)** (2)


</dt> <dd>

External account.

</dd> </dl>

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
' Get information about each excluded user.

SUB ExcludedUserInfo()

  DIM exclusionPolicy
  DIM excludedUser
  DIM excludedUserColl   

  ' Retrieve the ExclusionPolicy object.
  SET exclusionPolicy = config_manager.Enterprise.ExclusionPolicy
  CheckError()

  ' Retrieve the ExcludedUSerAccountCollection object.
  SET excludedUserColl = exclusionPolicy.UserAccounts
  CheckError()

  ' Loop through the collection and retrieve the date and type.
  For Each excludedUser in excludedUserColl
    CALL WScript.Echo( "UserId: " & excludedUser.UserId)
    CALL WScript.Echo( "Type: " & excludedUser.UserType)
    CALL WScript.Echo( "Date: " & excludedUser.Date)
  Next

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

[**ExcludedUserAccount**](excludeduseraccount-object.md)
</dt> </dl>

 

 




