---
Description: Initializes the administration environment, connects to the AD RMS server, and retrieves the appropriate role.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ba642a40-3dd6-406c-b26b-d544541c0a23
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ConfigurationManager.Initialize method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ConfigurationManager.Initialize method

The **Initialize** method initializes the administration environment, connects to the AD RMS server, and retrieves the appropriate role.

## Syntax


```VB
ConfigurationManager.Initialize( _
  ByVal isHttps, _
  ByVal clusterName, _
  ByVal portNumber, _
  ByVal userDomain, _
  ByVal userId, _
  ByVal password _
)
```



## Parameters

<dl> <dt>

*isHttps* \[in\]
</dt> <dd>

A Boolean value that indicates whether the connection is secure HTTP. If this value is **True**, specify 443 for the *portNumber* parameter.

</dd> <dt>

*clusterName* \[in\]
</dt> <dd>

A **String** value that contains the name of the AD RMS service that the client connects to.

</dd> <dt>

*portNumber* \[in\]
</dt> <dd>

An **Integer** value that contains the port number through which the client connects. To connect to a remote server by using a Secure Socket Layer (SSL) connection, specify 443 for this parameter and set the *isHttps* parameter to **True**.

</dd> <dt>

*userDomain* \[in\]
</dt> <dd>

A **String** value that contains the user account domain name or an empty string. If this value is empty, the current domain name is used.

</dd> <dt>

*userId* \[in\]
</dt> <dd>

A **String** value that contains the user account ID. If this value is empty, the logon user account name is used.

</dd> <dt>

*password* \[in\]
</dt> <dd>

A **String** value that contains the user account password or an empty string. If the *userID* parameter is not empty, the correct password for that account must be specified. If the *userID* parameter is empty, the password is ignored and the logon user credentials are used.

</dd> </dl>

## Return value

This method returns an integer value that identifies an appropriate role. The role is determined by the access control list on the AD RMS Administration website. This role value can be a bitwise-combination of the following flags.

<dl> <dt>


</dt> <dd>

0x0

No role is defined.

</dd> <dt>

**[**RoleAuditor**](constants-roleauditor-property.md)**
</dt> <dd>

0x1

The auditing role is defined.

</dd> <dt>

**[**RoleTemplateEditor**](constants-roletemplateeditor-property.md)**
</dt> <dd>

0x2

The rights template editing role is defined.

</dd> <dt>

**[**RoleAdministrator**](constants-roleadministrator-property.md)**
</dt> <dd>

0x4

The administrator role is defined.

</dd> </dl>

## Remarks

The following objects are configured during the initialization process depending on the role value returned by the AD RMS server.



| Object                                                      | Description                                                                            |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**AuditReport**](auditreport-object.md)                   | If the role is Administrator (0x4) or Auditor (0x1), this object is initialized.       |
| [**ClusterInformation**](clusterinformation-object.md)     | If the role is any value other than None (0x0), this object is initialized.            |
| [**Enterprise**](enterprise-object.md)                     | If the role is Administrator (0x4), this object is initialized.                        |
| [**RightsTemplatePolicy**](rightstemplatepolicy-object.md) | If the role is Administrator (0x4) or TemplateEditor(0x2), this object is initialized. |



 

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

 

 




