---
Description: 'Retrieves an object that can be used to decommission a server and to specify a super users group.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '00d9e43d-376a-4cbe-9392-c8b73ecfa731'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'Enterprise.SecurityPolicy property'
---

# Enterprise.SecurityPolicy property

The **SecurityPolicy** property retrieves an object that can be used to decommission a server and to specify a super users group.

This property is read-only.

## Syntax


```VB
Enterprise.SecurityPolicy
```



## Property value

This property returns a [**SecurityPolicy**](securitypolicy-object.md) object.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**Enterprise**](enterprise-object.md)
</dt> </dl>

 

 




