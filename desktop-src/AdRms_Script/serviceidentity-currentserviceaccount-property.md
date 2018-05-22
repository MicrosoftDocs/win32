---
Description: 'Retrieves the current service account from the server.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '10a6b16b-b7b5-49d2-88d4-7161ddc09fa6'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ServiceIdentity.CurrentServiceAccount property'
---

# ServiceIdentity.CurrentServiceAccount property

The **CurrentServiceAccount** property retrieves the current service account from the server.

This property is read-only.

## Syntax


```VB
ServiceIdentity.CurrentServiceAccount
```



## Property value

This property returns a [**UserDomainAccount**](userdomainaccount-object.md) object.

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
' Retrieve the current account.

SUB GetCurrentSvcAccnt()

  DIM AcctMgr
  DIM currentAcct

  ' Create a ServiceIdentity that can be used to change the 
  ' service account.
  SET AcctMgr = config_manager.ServiceIdentity
  CheckError()

  ' Retrieve the current service account.
  SET currentAcct = AcctMgr.CurrentServiceAccount
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

[**ServiceIdentity**](serviceidentity-object.md)
</dt> </dl>

 

 




