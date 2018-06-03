---
Description: Retrieves the day and time the account was excluded.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f8678e72-7512-4eec-b317-5e94f5cc1cc9
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExcludedUserAccount.Date property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ExcludedUserAccount.Date property

The **Date** property retrieves the day and time the account was excluded.

This property is read-only.

## Syntax


```VB
ExcludedUserAccount.Date
```



## Property value

This property returns a **DateTime** value. The property is read-only.

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

 

 




