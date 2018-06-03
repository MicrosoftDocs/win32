---
Description: Sends a report definition language (RDL) for a specific report type to a file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1e671586-d762-487a-ad22-209dfbeeeed7
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AuditReport.ExportReportDefinitionLang method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AuditReport.ExportReportDefinitionLang method

The **ExportReportDefinitionLang** method sends a report definition language (RDL) for a specific report type to a file.

## Syntax


```VB
AuditReport.ExportReportDefinitionLang( _
  ByVal reportName, _
  ByVal exportFolder _
)
```



## Parameters

<dl> <dt>

*reportName* \[in\]
</dt> <dd>

A **String** value that contains the RDL to export to a file. This can be one of the following values.

<dt>

<span id="Report_Health_RequestTypeSummary"></span><span id="report_health_requesttypesummary"></span><span id="REPORT_HEALTH_REQUESTTYPESUMMARY"></span>

<span id="Report_Health_RequestTypeSummary"></span><span id="report_health_requesttypesummary"></span><span id="REPORT_HEALTH_REQUESTTYPESUMMARY"></span>**Report\_Health\_RequestTypeSummary** ()


</dt> <dd>

Lists the number of total, successful, and failed requests for each request type.

</dd> <dt>

<span id="Report_Health_RequestTypeDomainSummary"></span><span id="report_health_requesttypedomainsummary"></span><span id="REPORT_HEALTH_REQUESTTYPEDOMAINSUMMARY"></span>

<span id="Report_Health_RequestTypeDomainSummary"></span><span id="report_health_requesttypedomainsummary"></span><span id="REPORT_HEALTH_REQUESTTYPEDOMAINSUMMARY"></span>**Report\_Health\_RequestTypeDomainSummary** ()


</dt> <dd>

Lists the number of total, successful, and failed requests for each domain for a given request type.

</dd> <dt>

<span id="Report_Health_RequestTypeDomainUserSummary"></span><span id="report_health_requesttypedomainusersummary"></span><span id="REPORT_HEALTH_REQUESTTYPEDOMAINUSERSUMMARY"></span>

<span id="Report_Health_RequestTypeDomainUserSummary"></span><span id="report_health_requesttypedomainusersummary"></span><span id="REPORT_HEALTH_REQUESTTYPEDOMAINUSERSUMMARY"></span>**Report\_Health\_RequestTypeDomainUserSummary** ()


</dt> <dd>

Lists the number of total, successful, and failed requests for each user in a domain for a given request type.

</dd> <dt>

<span id="Report_Health_RequestAvgDuration"></span><span id="report_health_requestavgduration"></span><span id="REPORT_HEALTH_REQUESTAVGDURATION"></span>

<span id="Report_Health_RequestAvgDuration"></span><span id="report_health_requestavgduration"></span><span id="REPORT_HEALTH_REQUESTAVGDURATION"></span>**Report\_Health\_RequestAvgDuration** ()


</dt> <dd>

Lists, for each type of request, the total number of requests received and the average duration that each type took to process.

</dd> <dt>

<span id="Report_TroubleShooting_UserRequestSummary"></span><span id="report_troubleshooting_userrequestsummary"></span><span id="REPORT_TROUBLESHOOTING_USERREQUESTSUMMARY"></span>

<span id="Report_TroubleShooting_UserRequestSummary"></span><span id="report_troubleshooting_userrequestsummary"></span><span id="REPORT_TROUBLESHOOTING_USERREQUESTSUMMARY"></span>**Report\_TroubleShooting\_UserRequestSummary** ()


</dt> <dd>

Lists the number of total, successful, and failed requests by user and request type.

</dd> <dt>

<span id="Report_TroubleShooting_UserRequestTypeList"></span><span id="report_troubleshooting_userrequesttypelist"></span><span id="REPORT_TROUBLESHOOTING_USERREQUESTTYPELIST"></span>

<span id="Report_TroubleShooting_UserRequestTypeList"></span><span id="report_troubleshooting_userrequesttypelist"></span><span id="REPORT_TROUBLESHOOTING_USERREQUESTTYPELIST"></span>**Report\_TroubleShooting\_UserRequestTypeList** ()


</dt> <dd>

Lists all successful and failed requests by user and request type.

</dd> <dt>

<span id="Report_TroubleShooting_UserRequestDetail"></span><span id="report_troubleshooting_userrequestdetail"></span><span id="REPORT_TROUBLESHOOTING_USERREQUESTDETAIL"></span>

<span id="Report_TroubleShooting_UserRequestDetail"></span><span id="report_troubleshooting_userrequestdetail"></span><span id="REPORT_TROUBLESHOOTING_USERREQUESTDETAIL"></span>**Report\_TroubleShooting\_UserRequestDetail** ()


</dt> <dd>

Lists detailed information for all successful and failed requests by user and request type.

</dd> <dt>

<span id="Report_TroubleShooting_UserRequestCertificateInfo"></span><span id="report_troubleshooting_userrequestcertificateinfo"></span><span id="REPORT_TROUBLESHOOTING_USERREQUESTCERTIFICATEINFO"></span>

<span id="Report_TroubleShooting_UserRequestCertificateInfo"></span><span id="report_troubleshooting_userrequestcertificateinfo"></span><span id="REPORT_TROUBLESHOOTING_USERREQUESTCERTIFICATEINFO"></span>**Report\_TroubleShooting\_UserRequestCertificateInfo** ()


</dt> <dd>

Lists detailed certificate information by user and request type.

</dd> <dt>

<span id="Report_TroubleShooting_AllEULsFromIssuanceLicense"></span><span id="report_troubleshooting_alleulsfromissuancelicense"></span><span id="REPORT_TROUBLESHOOTING_ALLEULSFROMISSUANCELICENSE"></span>

<span id="Report_TroubleShooting_AllEULsFromIssuanceLicense"></span><span id="report_troubleshooting_alleulsfromissuancelicense"></span><span id="REPORT_TROUBLESHOOTING_ALLEULSFROMISSUANCELICENSE"></span>**Report\_TroubleShooting\_AllEULsFromIssuanceLicense** ()


</dt> <dd>

Lists the end user licenses for a selected issuance license.

</dd> </dl> </dd> <dt>

*exportFolder* 
</dt> <dd>

A **String** value that contains the export file path.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Microsoft SQL Server supports report definitions that contain data retrieval and layout information for a report. A report definition language (RDL) is an XML representation of the report definition. You can use this method to write the XML for a given report type to a file.

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
' Export a report definition language schema.

SUB ExportRDL()

  DIM auditReport

  ' Create an AuditReport object.
  SET auditReport = _
          config_manager.AuditReport
  CheckError()

  ' Send the RDL schema for the RequestTypeAvgDuration report 
  ' to the c:\ folder.
  CALL auditReport.ExportReportDefinitionLang( _
               "Report_Health_RequestAvgDuration", _
               "c:\")
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

[**AuditReport**](auditreport-object.md)
</dt> </dl>

 

 




