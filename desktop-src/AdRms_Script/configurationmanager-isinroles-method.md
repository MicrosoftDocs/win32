---
Description: 'Retrieves a Boolean value that specifies whether a role is permitted.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'fa000cde-eed1-4899-aba3-9713fd68fc69'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ConfigurationManager.IsInRoles method'
---

# ConfigurationManager.IsInRoles method

The **IsInRoles** method retrieves a Boolean value that specifies whether a role is permitted.

## Syntax


```VB
ConfigurationManager.IsInRoles( _
  ByVal role _
)
```



## Parameters

<dl> <dt>

*role* 
</dt> <dd>

A value that identifies the role. This can be one of the following.

<dt>

<span id="RoleAuditor"></span><span id="roleauditor"></span><span id="ROLEAUDITOR"></span>

<span id="RoleAuditor"></span><span id="roleauditor"></span><span id="ROLEAUDITOR"></span>**[**RoleAuditor**](constants-roleauditor-property.md)** (0x1)


</dt> <dd>

The auditing role is defined.

</dd> <dt>

<span id="RoleTemplateEditor"></span><span id="roletemplateeditor"></span><span id="ROLETEMPLATEEDITOR"></span>

<span id="RoleTemplateEditor"></span><span id="roletemplateeditor"></span><span id="ROLETEMPLATEEDITOR"></span>**[**RoleTemplateEditor**](constants-roletemplateeditor-property.md)** (0x2)


</dt> <dd>

The rights template editing role is defined.

</dd> <dt>

<span id="RoleAdministrator"></span><span id="roleadministrator"></span><span id="ROLEADMINISTRATOR"></span>

<span id="RoleAdministrator"></span><span id="roleadministrator"></span><span id="ROLEADMINISTRATOR"></span>**[**RoleAdministrator**](constants-roleadministrator-property.md)** (0x4)


</dt> <dd>

The administrator role is defined.

</dd> </dl> </dd> </dl>

## Return value

This method returns a Boolean value.

## Remarks

The access control list on the AD RMS Administration website determines whether a role is supported.

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
' Determine whether the Auditing role is supported.

SUB ChkSupportedRole()

  DIM bRole
  bRole = config_manager.IsInRoles(1)
  CheckError()

  IF bRole <> 0 THEN
    ' TODO: Do something.
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

' *******************************************************************
' Generate a runtime error.

SUB RaiseError(errId, desc)
  CALL Err.Raise( errId, "", desc )
  CheckError()
END SUB
```



## Requirements



|                                     |                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ConfigurationManager**](configurationmanager-object.md)
</dt> </dl>

 

 




