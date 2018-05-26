---
Description: Contains information about the AD RMS logging environment.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 59551a73-cff4-4cee-9c46-37027cb24980
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: LoggingSystemInformation object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# LoggingSystemInformation object

The **LoggingSystemInformation** object contains information about the AD RMS logging environment. This includes the name of the logging database, the name of the message queue used to send log messages to the database, and the name of the logging service. You can retrieve this object by calling the [**LoggingSystemInformation**](auditreport-loggingsysteminformation-property.md) property on the [**AuditReport**](auditreport-object.md) object. The **AuditReport** object must be enabled before messages can be logged.

## Members

The **LoggingSystemInformation** object has these types of members:

-   [Properties](#properties)

### Properties

The **LoggingSystemInformation** object has these properties.



| Property                                                                                        | Description                                                  |
|:------------------------------------------------------------------------------------------------|:-------------------------------------------------------------|
| [**DatabaseInformation**](loggingsysteminformation-databaseinformation-property.md)<br/> | Retrieves information about the logging database.<br/> |
| [**LoggingQueueName**](loggingsysteminformation-loggingqueuename-property.md)<br/>       | Retrieves the name of the message queue.<br/>          |
| [**LoggingServiceName**](loggingsysteminformation-loggingservicename-property.md)<br/>   | Retrieves the name of the ADRMS logging service.<br/>  |



 

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

SUB GetLoggingSystem()

  DIM loggingSysInfo
    
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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> <dt>

[**AuditReport**](auditreport-object.md)
</dt> </dl>

 

 




