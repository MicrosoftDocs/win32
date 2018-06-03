---
Description: Identifies a user account for which new end-user license (EUL) and client licensor certificate (CLC) requests are denied.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 22ed9a8f-adb3-43d5-9c96-a4c107b0bee9
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExcludedUserAccount object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ExcludedUserAccount object

The **ExcludedUserAccount** object identifies a user account for which new end-user license (EUL) and client licensor certificate (CLC) requests are denied. You can exclude a user by user ID or by the public key contained in the rights account certificate (RAC). The next time the user attempts to acquire an EUL or CLC for new content, the AD RMS server will deny the request. To acquire a new EUL or CLC, the user must obtain a new RAC containing a new key pair.

## Members

The **ExcludedUserAccount** object has these types of members:

-   [Properties](#properties)

### Properties

The **ExcludedUserAccount** object has these properties.



| Property                                                               | Description                                                                  |
|:-----------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| [**Date**](excludeduseraccount-date-property.md)<br/>           | Retrieves the day and time the account was excluded.<br/>              |
| [**PublicKey**](excludeduseraccount-publickey-property.md)<br/> | Specifies or retrieves the public key of the user to be excluded.<br/> |
| [**UserId**](excludeduseraccount-userid-property.md)<br/>       | Specifies or retrieves the email address of the user.<br/>             |
| [**UserType**](excludeduseraccount-usertype-property.md)<br/>   | Retrieves the type of the excluded user account.<br/>                  |



 

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

  ' Identify the excluded public key.
  excludedUser.PublicKey = "D3QgTm9y1ujYqiy4tocvmnyvnlp" _
        & "kthp5+TrtF94qJN/I38bxALpAj9ExB4Do6P+rHWvMR+0HztV7Yelo" _
        & "B3r2IlX2lQYe7mxZwnF2D5/7GUzPj5hKxCT/By55tX3Bzs4Eno7cX" _
        & "fTeJ6mnMDO+KyjNoObg9kPRCy2hmHhj2ftRvLk="
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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




