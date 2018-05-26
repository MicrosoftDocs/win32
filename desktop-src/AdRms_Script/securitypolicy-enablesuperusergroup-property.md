---
Description: Specifies or retrieves a Boolean value that indicates whether a security group can be designated as the super user group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6828036c-cb6a-4a24-acf6-a6423dfdbdf9
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: SecurityPolicy.EnableSuperUserGroup property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SecurityPolicy.EnableSuperUserGroup property

The **EnableSuperUserGroup** property specifies or retrieves a Boolean value that indicates whether a security group can be designated as the super user group.

## Syntax


```VB
SecurityPolicy.EnableSuperUserGroup
```



## Property value

This property is read/write.

## Remarks

Members of the super user group can decrypt any protected content files or remove protection from them. The super users group has no members by default, but you can call the [**SuperUserGroup**](securitypolicy-superusergroup-property.md) property to specify a distribution group by email address. You must call the **EnableSuperUserGroup** property before calling **SuperUserGroup**.

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
' Security policy.

SUB EnableSecurityPolicy()

  DIM securityPolicy   

  ' Create a SecurityPolicy object.
  SET securityPolicy = config_manager.Enterprise.SecurityPolicy
  CheckError()

  ' Enable the super user group.
  securityPolicy.EnableSuperUserGroup = TRUE
  CheckError()
  
  ' Set the super user group.
  securityPolicy.SuperUserGroup = group_name@domain_name.com
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

[**SecurityPolicy**](securitypolicy-object.md)
</dt> </dl>

 

 




