---
Description: Can be used to enable logging and to retrieve information that identifies where data is logged and the name of the logging service and queue.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 0722186b-2400-4168-9cb4-dbdfb7fb50b5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AuditReport object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# AuditReport object

The **AuditReport** object can be used to enable logging and to retrieve information that identifies where data is logged and the name of the logging service and queue. Log files are typically stored on a database server and can be used to audit the use of rights-protected content in an organization. If logging is enabled, the AD RMS logging service uses Message Queuing to send log messages from the cluster to the logging database. To use this object, the access control list on the AD RMS Administration website must support the Administrator (0x4) or the Auditor (0x1) role. You can retrieve the object by calling the [**AuditReport**](configurationmanager-auditreport-property.md) property on the [**ConfigurationManager**](configurationmanager-object.md) object.

## Members

The **AuditReport** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **AuditReport** object has these methods.



| Method                                                                                              | Description                                                                                                                                |
|:----------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**ExportReportDefinitionLang**](auditreport-exportreportdefinitionlang-method.md)                 | Sends a report definition language (RDL) for a specific report type to a file.<br/>                                                  |
| [**ExportRequestTypeAverageDuration**](auditreport-exportrequesttypeaverageduration-method.md)     | Generates a report for the number of total and average request durations, in milliseconds, for a given request type.<br/>            |
| [**ExportRequestTypeDomainSummary**](auditreport-exportrequesttypedomainsummary-method.md)         | Generates a report for the number of total, successful, and failed requests for a given request type for each domain.<br/>           |
| [**ExportRequestTypeDomainUserSummary**](auditreport-exportrequesttypedomainusersummary-method.md) | Generates a report for the number of total, successful, and failed requests for a given request type for each user in a domain.<br/> |
| [**ExportRequestTypeSummary**](auditreport-exportrequesttypesummary-method.md)                     | Generates a report for the number of total, successful, and failed requests of all types.<br/>                                       |
| [**ExportUserRequestSummary**](auditreport-exportuserrequestsummary-method.md)                     | Generates a report for the number of total, successful, and failed requests for a given user and domain.<br/>                        |
| [**ExportUserRequestTypeList**](auditreport-exportuserrequesttypelist-method.md)                   | Generates a report for a given request type and user.<br/>                                                                           |



 

### Properties

The **AuditReport** object has these properties.



| Property                                                                                                   | Access type           | Description                                                                                  |
|:-----------------------------------------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------|
| [**CertifiedDomainUserAccountCount**](auditreport-certifieddomainuseraccountcount-property.md)<br/> |                       | Retrieves the number of licensed domain user accounts.<br/>                            |
| [**CertifiedFederatedIdentityCount**](auditreport-certifiedfederatedidentitycount-property.md)<br/> |                       | Retrieves the number of Active Directory Federation Services (ADFS) accounts.<br/>     |
| [**Enabled**](auditreport-enabled-property.md)<br/>                                                 | Read/write<br/> | Specifies or retrieves a Boolean value that indicates whether logging is enabled.<br/> |
| [**LoggingSystemInformation**](auditreport-loggingsysteminformation-property.md)<br/>               |                       | Retrieves information about the logging database.<br/>                                 |



 

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> <dt>

[**LoggingSystemInformation**](loggingsysteminformation-object.md)
</dt> </dl>

 

 




