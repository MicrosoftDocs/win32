---
Description: 'Retrieves the number of licensed Active Directory Federation Services (ADFS) accounts.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '8a7cc8e3-4f1b-426f-bf33-f3dd0207ca4f'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'AuditReport.CertifiedFederatedIdentityCount property'
---

# AuditReport.CertifiedFederatedIdentityCount property

The **CertifiedFederatedIdentityCount** property retrieves the number of licensed Active Directory Federation Services (ADFS) accounts.

This property is read-only.

## Syntax


```VB
AuditReport.CertifiedFederatedIdentityCount
```



## Property value

This property returns an integer value.

## Remarks

The [**AuditReport**](auditreport-object.md) object must be enabled before this property can be called. For more information, see [**Enabled**](auditreport-enabled-property.md).

The property value can be used to determine licensing fees based on the number of certified accounts.

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
' Retrieve logging information.

SUB AuditTest()

  DIM loggingSysInfo
  DIM state
  DIM certCount
  DIM adfsCount
    
  SET loggingSysInfo = _
          config_manager.AuditReport.LoggingSystemInformation
  CheckError()

  CALL WScript.Echo("Server Name:" & _
                    loggingSysInfo.DatabaseInformation.Server)
  CALL WScript.Echo("Database:" & _
                    loggingSysInfo.DatabaseInformation.DBName)
  CALL WScript.Echo("Queue Name:" & _
                    loggingSysInfo.LoggingQueueName)
  CALL WScript.Echo("Service" & _
                    loggingSysInfo.LoggingServiceName)

  state = config_manager.AuditReport.Enabled
  CheckError()
  CALL WScript.Echo( "AuditReport.Enabled: " & state)

  CALL WScript.Echo( "Enable logging...")
  config_manager.AuditReport.Enabled = true
  CheckError()

  certCount = _
     config_manager.AuditReport.CertifiedDomainUserAccountCount
  CheckError()
  CALL WScript.Echo("AuditReport.CertifiedUsersCount: " & certCount)

  adfsCount = _
      config_manager.AuditReport.CertifiedFederatedIdentityCount
  CheckError()
  CALL WScript.Echo("AuditReport.AdfsCount: " & adfsCount)

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

[**AuditReport**](auditreport-object.md)
</dt> </dl>

 

 




