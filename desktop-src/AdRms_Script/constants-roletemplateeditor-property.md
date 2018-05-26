---
Description: Retrieves a value that specifies template editor privileges.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e2936b46-0b5e-4421-9a06-76adccef9f5d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Constants.RoleTemplateEditor property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Constants.RoleTemplateEditor property

The **RoleTemplateEditor** property retrieves a value that specifies template editor privileges.

This property is read-only.

## Syntax


```VB
Constants.RoleTemplateEditor
```



## Property value

This property returns an integer value (0x2).

## Remarks

The role is returned when you call the [**Initialize**](configurationmanager-initialize-method.md) method on the [**ConfigurationManager**](configurationmanager-object.md) object, and it is determined by the access control list on the AD RMS Administration website. The role can be a bitwise-combination of the following flags.



| Value                                                                   | Description                                  |
|-------------------------------------------------------------------------|----------------------------------------------|
| [**RoleAuditor**](constants-roleauditor-property.md) (0x1)             | The auditing role is defined.                |
| **RoleTemplateEditor** (0x2)                                            | The rights template editing role is defined. |
| [**RoleAdministrator**](constants-roleadministrator-property.md) (0x4) | The administrator role is defined.           |



 

## Examples


```VB
' *******************************************************************
' Create and initialize a ConfigurationManager object.

SUB InitObject()

  DIM config_manager
  DIM admin_role
  DIM constant

  ' Retrieve a ConfigurationManager object.
  CALL WScript.Echo( "Create ConfigurationManager object...")
  SET config_manager = CreateObject _
    ("Microsoft.RightsManagementServices.Admin.ConfigurationManager")      
  CheckError()

  ' Retrieve a Constants object.
  SET constant = config_manager.Constants
  CheckError()

  ' Retrieve the role.    
  CALL WScript.Echo( "Initialize...")
  admin_role=config_manager.Initialize(false,"localhost",80,"","","")
  CheckError()

  IF config_manager.IsInRoles(constant.RoleAuditor) THEN
    CALL WScript.Echo("Role is auditor.")
  END IF

  IF config_manager.IsInRoles(constant.RoleTemplateEditor) THEN
    CALL WScript.Echo("Role is template editor.")
  END IF

  IF config_manager.IsInRoles(constant.RoleAdministrator) THEN
    CALL WScript.Echo("Role is administrator.")
  END IF

  IF admin_role < 1 OR admin_role > 4 THEN
    CALL WScript.Echo("Role is undefined.")
  END IF

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

[**RoleAdministrator**](constants-roleadministrator-property.md)
</dt> <dt>

[**RoleAuditor**](constants-roleauditor-property.md)
</dt> </dl>

 

 




