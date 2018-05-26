---
Description: Configures the AD RMS environment to allow a server to be decommissioned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 2de70f49-68e8-4ac8-bbfb-a509aab880dd
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: SecurityPolicy.EnableDecommission method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SecurityPolicy.EnableDecommission method

The **EnableDecommission** method configures the AD RMS environment to allow a server to be decommissioned.

## Syntax


```VB
SecurityPolicy.EnableDecommission()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

After a server has been decommissioned, AD RMS provides a content key that can be used to decrypt previously published and encrypted content. You must call this method before calling the [**DecommissionNow**](securitypolicy-decommissionnow-method.md) method.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**SecurityPolicy**](securitypolicy-object.md)
</dt> </dl>

 

 




