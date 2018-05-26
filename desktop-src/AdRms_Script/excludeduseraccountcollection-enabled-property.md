---
Description: Specifies or retrieves a Boolean value that indicates whether the collection is enabled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d4d63f75-a1c2-4d4c-b3a6-9203bdc29184
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExcludedUserAccountCollection.Enabled property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExcludedUserAccountCollection.Enabled property

The **Enabled** property specifies or retrieves a Boolean value that indicates whether the collection is enabled. The collection must be enabled before you can add items to it or retrieve information from it.

## Syntax


```VB
ExcludedUserAccountCollection.Enabled
```



## Property value

This property specifies or returns a Boolean value. If this value is **False**, no item in the collection will be excluded.

## Remarks

User account exclusion prohibits AD RMS from issuing an end-user license or client licensor certificate to a requesting user if the user account is on the exclusion list and the account exclusion collection has been enabled.

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
</dt> <dt>

[**ExcludedUserAccountCollection**](excludeduseraccountcollection-object.md)
</dt> </dl>

 

 




