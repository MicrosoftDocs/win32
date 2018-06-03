---
Description: Can be used to decommission a server and to specify a super users group. You can retrieve this object by calling the SecurityPolicy property on the Enterprise object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ce68643b-bbee-4c61-8a6d-d46f1226e6a4
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: SecurityPolicy object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# SecurityPolicy object

The **SecurityPolicy** object can be used to decommission a server and to specify a super users group. You can retrieve this object by calling the [**SecurityPolicy**](enterprise-securitypolicy-property.md) property on the [**Enterprise**](enterprise-object.md) object.

When provisioned, AD RMS creates a special distribution group that has full control over all rights-protected content stored on the server. Members of this group can decrypt any protected content files or remove protection from them. By default, this super users group is not set, but you can use this object to specify a new or existing Active Directory distribution group to use. The group must exist in the same Active Directory forest as the AD RMS installation and is specified by its email address. Any user accounts that are members of the group that you specify are automatically granted super user permissions.

You can also use this object to decommission an AD RMS server. After a server has been decommissioned, AD RMS issues an end user license to any user who requests content, thereby effectively eliminating protection for that content.

## Members

The **SecurityPolicy** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SecurityPolicy** object has these methods.



| Method                                                                 | Description                                                                          |
|:-----------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
| [**DecommissionNow**](securitypolicy-decommissionnow-method.md)       | Decommissions a server.<br/>                                                   |
| [**EnableDecommission**](securitypolicy-enabledecommission-method.md) | Configures the AD RMS environment to allow a server to be decommissioned.<br/> |



 

### Properties

The **SecurityPolicy** object has these properties.



| Property                                                                                | Description                                                                                                                          |
|:----------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| [**EnableSuperUserGroup**](securitypolicy-enablesuperusergroup-property.md)<br/> | Specifies or retrieves a Boolean value that indicates whether a security group can be designated as the super user group.<br/> |
| [**SuperUserGroup**](securitypolicy-superusergroup-property.md)<br/>             | Specifies or retrieves the super user group.<br/>                                                                              |



 

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

  ' Enable the decommissioning process.
  securityPolicy.EnableDecommission()
  CheckError()

  ' Decommission the server.
  securityPolicy.DecommissionNow()
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

 

 




