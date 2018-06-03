---
Description: Retrieves a value that identifies the role.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 970f3cd5-2067-4009-b8e0-5915b6e19630
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ConfigurationManager.Roles property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConfigurationManager.Roles property

The **Roles** property retrieves a value that identifies the role.

This property is read-only.

## Syntax


```VB
ConfigurationManager.Roles
```



## Property value

This property is read-only. The property returns an bitwise-combination of the following values.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0x0)


</dt> <dd>

No role is defined.

</dd> <dt>

<span id="Auditor"></span><span id="auditor"></span><span id="AUDITOR"></span>

<span id="Auditor"></span><span id="auditor"></span><span id="AUDITOR"></span>**Auditor** (0x1)


</dt> <dd>

The auditing role is defined.

</dd> <dt>

<span id="TemplateEditor"></span><span id="templateeditor"></span><span id="TEMPLATEEDITOR"></span>

<span id="TemplateEditor"></span><span id="templateeditor"></span><span id="TEMPLATEEDITOR"></span>**TemplateEditor** (0x2)


</dt> <dd>

The rights template editing role is defined.

</dd> <dt>

<span id="Administrator"></span><span id="administrator"></span><span id="ADMINISTRATOR"></span>

<span id="Administrator"></span><span id="administrator"></span><span id="ADMINISTRATOR"></span>**Administrator** (0x4)


</dt> <dd>

The administrator role is defined.

</dd> </dl>

## Remarks

The role is determined by the access control list on the AD RMS Administration website.

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
' Retrieve the roles.

SUB GetUserRoles()

  admin_role = config_manager.Roles
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ConfigurationManager**](configurationmanager-object.md)
</dt> </dl>

 

 




