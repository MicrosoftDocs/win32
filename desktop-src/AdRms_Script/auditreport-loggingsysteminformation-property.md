---
Description: Retrieves information about the logging database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7bbdf63f-a883-43b4-9b80-4eeb5e3b726c
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AuditReport.LoggingSystemInformation property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AuditReport.LoggingSystemInformation property

The **LoggingSystemInformation** property retrieves information about the logging database.

This property is read-only.

## Syntax


```VB
AuditReport.LoggingSystemInformation
```



## Property value

This property returns a [**LoggingSystemInformation**](loggingsysteminformation-object.md) object.

## Remarks

The [**AuditReport**](auditreport-object.md) object must be enabled before this property can be called. For more information, see [**Enabled**](auditreport-enabled-property.md).

You can use the [**LoggingSystemInformation**](loggingsysteminformation-object.md) object to retrieve the name of the logging service and a [**DatabaseInformation**](databaseinformation-object.md) object that can be used to retrieve the names of the database and the logging server.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**AuditReport**](auditreport-object.md)
</dt> <dt>

[**DatabaseInformation**](databaseinformation-object.md)
</dt> <dt>

[**LoggingSystemInformation**](loggingsysteminformation-object.md)
</dt> </dl>

 

 




