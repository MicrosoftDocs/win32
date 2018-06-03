---
Description: Retrieves a value that specifies a federated user account.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 247892f2-fcb6-45ca-9d19-7881f1d7601d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Constants.ExcludedFederationUserType property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Constants.ExcludedFederationUserType property

The **ExcludedFederationUserType** property retrieves a value that specifies a federated user account.

This property is read-only.

## Syntax


```VB
Constants.ExcludedFederationUserType
```



## Property value

This property returns an integer value (0x3) that identifies an Active Directory Federation Services (ADFS) user.

## Remarks

The property value can be used with the [**UserType**](excludeduseraccount-usertype-property.md) property on the [**ExcludedUserAccount**](excludeduseraccount-object.md) object.

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
' Retrieve the type of each excluded user.

SUB GetExclUserType()

  DIM exclPolicy
  DIM exclUser
  DIM exclUserColl
  DIM constant

  ' Retrieve the Constants object.
  SET constant = config_manager.Constants

  ' Retrieve the ExclusionPolicy object.
  SET exclPolicy = config_manager.Enterprise.ExclusionPolicy
  CheckError()

  ' Retrieve the ExcludedUSerAccountCollection object.
  SET exclUserColl = exclusionPolicy.UserAccounts
  CheckError()

 ' Loop through the collection and retrieve the user type.
  For Each exclUser in exclUserColl
   CALL WScript.Echo("UserId: " & exclUser.UserId)
   IF exclUser.UserType = constant.ExcludedDomainUserType THEN
    CALL WScript.Echo("Excluded user is domain type.")
   ELSEIF exclUser.UserType=constant.ExcludedExternalUserType THEN
    CALL WScript.Echo("Excluded user is external type.")
   ELSEIF exclUser.UserType=constant.ExcludedFederationUserType THEN
    CALL WScript.Echo("Excluded user is ADFS type.")
   ELSE
    CALL WScript.Echo("Excluded user type cannot be determined.")
   END IF
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

[**Constants**](constants-object.md)
</dt> <dt>

[**ExcludedDomainUserType**](constants-excludeddomainusertype-property.md)
</dt> <dt>

[**ExcludedExternalUserType**](constants-excludedexternalusertype-property.md)
</dt> </dl>

 

 




