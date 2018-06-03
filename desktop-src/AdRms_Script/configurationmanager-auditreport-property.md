---
Description: Retrieves an AuditReport object that can be used to obtain the number of federated and domain user accounts.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 27c3ddaa-b537-4a73-be82-45e91381bcd2
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ConfigurationManager.AuditReport property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConfigurationManager.AuditReport property

The **AuditReport** property retrieves an [**AuditReport**](auditreport-object.md) object that can be used to obtain the number of federated and domain user accounts.

This property is read-only.

## Syntax


```VB
ConfigurationManager.AuditReport
```



## Property value

This property returns an [**AuditReport**](auditreport-object.md) object. The property is read-only.

## Error codes

This property returns an [**AuditReport**](auditreport-object.md) object.

## Remarks

The [**AuditReport**](auditreport-object.md) object is configured when the [**Initialize**](configurationmanager-initialize-method.md) method is called if the access control list on the AD RMS Administration website supports the Administrator (0x4) or Auditor (0x1) roles.

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
' Retrieve an AuditReport object. Check the object state, enable it,
' and retrieve the number of licensed user accounts.

SUB ChkAuditReport()

  DIM state
  DIM certCount

  state = config_manager.AuditReport.Enabled
  CheckError()
  CALL WScript.Echo( vbTab & "AuditReport.Enabled: " & state)
    
  CALL WScript.Echo( vbTab & "Enable logging...")
  config_manager.AuditReport.Enabled = true
  CheckError()
    
  certCount = config_manager.AuditReport.CertifiedUsersCount
  CheckError()
  CALL WScript.Echo( vbTab & "AuditReport.CertifiedUsersCount: " _
    & certCount)

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

 

 




