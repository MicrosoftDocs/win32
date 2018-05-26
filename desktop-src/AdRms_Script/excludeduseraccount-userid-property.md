---
Description: Specifies or retrieves the email address of the user.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 70d61669-6c6a-4d66-a0d6-10e3048eb71e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExcludedUserAccount.UserId property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExcludedUserAccount.UserId property

The **UserId** property specifies or retrieves the email address of the user.

## Syntax


```VB
ExcludedUserAccount.UserId
```



## Property value

This property specifies or returns a string that contains an email address such as *someone@example.com*.

## Remarks

You can exclude a user by public key or by user ID but not both. To exclude a user by public key, call the [**PublicKey**](excludeduseraccount-publickey-property.md) property. The user ID is an email address.

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
' Exclude user accounts.

SUB ExcludeUser()

  DIM exclusionPolicy
  DIM excludedUser
  DIM excludedUserColl   
  Dim excludedUserType
  Dim excludedUserDate


  ' Retrieve the ExclusionPolicy object.
  SET exclusionPolicy = config_manager.Enterprise.ExclusionPolicy
  CheckError()

  ' Create an ExcludedUserAccount object.
  SET excludedUser = CreateObject( _
    "Microsoft.RightsManagementServices.Admin.ExcludedUserAccount")
  CheckError()

  ' Set the user ID.
  excludedUser.UserId = "someone@example.com"
  CheckError()

  ' Retrieve the ExcludedUSerAccountCollection object.
  SET excludedUserColl = exclusionPolicy.UserAccounts
  CheckError()

  ' Enable the collection.
  excludedUserColl.Enabled = TRUE

  ' Add the new user account to the collection.
  excludedUserColl.Add( excludedUser )
  CheckError()

  ' Retrieve the user type.
  excludedUserType = excludedUser.Type
  CheckError()

  ' Retrieve the date on which the user account was excluded.
  excludedUserDate = excludedUser.Date
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

[**ExcludedUserAccount**](excludeduseraccount-object.md)
</dt> </dl>

 

 




