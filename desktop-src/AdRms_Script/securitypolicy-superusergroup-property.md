---
Description: Specifies or retrieves the super user group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c7413108-1728-495d-ab11-90e8f66e771f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: SecurityPolicy.SuperUserGroup property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SecurityPolicy.SuperUserGroup property

The **SuperUserGroup** property specifies or retrieves the super user group.

## Syntax


```VB
SecurityPolicy.SuperUserGroup
```



## Property value

This property sets or returns a string value that contains the email address of the super user group. The format of the string is *GroupName@DomainName.com*.

## Remarks

When provisioned, AD RMS creates a special, super users group that has full control over all rights-protected content stored on the server. The super users group has no members by default, but you can use this property to specify a new or existing Active Directory distribution group by email address. You must call the [**EnableSuperUserGroup**](securitypolicy-enablesuperusergroup-property.md) property before calling the **SuperUserGroup** property.

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

 

 




