---
Description: 'Decommissions a server.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '659536dc-0cf6-4bdd-8512-fd9f09841485'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'SecurityPolicy.DecommissionNow method'
---

# SecurityPolicy.DecommissionNow method

The **DecommissionNow** method decommissions a server.

## Syntax


```VB
SecurityPolicy.DecommissionNow()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

When you decommission an AD RMS cluster, AD RMS provides a key that can be used to decrypt published content that had been previously protected, thereby enabling you to save the content unprotected. You must call the [**EnableDecommission**](securitypolicy-enabledecommission-method.md) method before calling this method.

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

[**SecurityPolicy**](securitypolicy-object.md)
</dt> </dl>

 

 




