---
Description: Generates a report for a given request type and user.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7864622c-832e-49e3-92d7-d15a148aa56b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AuditReport.ExportUserRequestTypeList method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AuditReport.ExportUserRequestTypeList method

The **ExportUserRequestTypeList** method generates a report for a given request type and user.

## Syntax


```VB
AuditReport.ExportUserRequestTypeList( _
  ByVal languageId, _
  ByVal start, _
  ByVal end, _
  ByVal userDomain, _
  ByVal userName, _
  ByVal requestTypeId, _
  ByVal filePath, _
  ByVal fileType _
)
```



## Parameters

<dl> <dt>

*languageId* 
</dt> <dd>

An integer that contains the locale ID (LCID) of the report language. For example, the LCID for U.S. English is 1033. For a complete list of the LCIDs supported by Microsoft, see [List of Locale ID (LCID) Values as Assigned by Microsoft](http://go.microsoft.com/fwlink/p/?linkid=63028).

</dd> <dt>

*start* 
</dt> <dd>

A **DateTime** value that contains the beginning time for the report.

</dd> <dt>

*end* 
</dt> <dd>

A **DateTime** value that contains the ending time for the report.

</dd> <dt>

*userDomain* 
</dt> <dd>

A **String** value that contains the user domain name.

</dd> <dt>

*userName* 
</dt> <dd>

A **String** value that contains the name of the requesting user. This cannot be an empty string.

</dd> <dt>

*requestTypeId* 
</dt> <dd>

An integer value that specifies the type of request. This can be one of the following values.

<dt>

0
</dt> <dd>

Activate the user through a proxy.

</dd> <dt>

1
</dt> <dd>

Find service locations for a service type.

</dd> <dt>

2
</dt> <dd>

Find service locations for an authenticated user.

</dd> <dt>

3
</dt> <dd>

Certify the user.

</dd> <dt>

4
</dt> <dd>

Precertify the user by creating a rights account certificate before the user can consume protected content.

</dd> <dt>

5
</dt> <dd>

Retrieve the client licensor certificate.

</dd> <dt>

6
</dt> <dd>

Edit the issuance license.

</dd> <dt>

7
</dt> <dd>

Sign the issuance license.

</dd> <dt>

8
</dt> <dd>

Acquire a license.

</dd> <dt>

9
</dt> <dd>

Acquire a prelicense by creating an end user license before the user can consume protected content.

</dd> <dt>

10
</dt> <dd>

Acquire the key used to encrypt content.

</dd> <dt>

11
</dt> <dd>

Retrieve the licensor certificate.

</dd> <dt>

12
</dt> <dd>

Determine whether the principal is a member of the given group.

</dd> <dt>

13
</dt> <dd>

Retrieve issuance license template information.

</dd> <dt>

14
</dt> <dd>

Retrieve the issuance license templates.

</dd> </dl> </dd> <dt>

*filePath* 
</dt> <dd>

A **String** value that contains the report file path.

</dd> <dt>

*fileType* 
</dt> <dd>

An integer that contains the export file type. This can be one of the following values.

<dt>

0
</dt> <dd>

Microsoft Excel (.xls) file.

</dd> <dt>

2
</dt> <dd>

Portable Document Format (PDF) file.

</dd> </dl> </dd> </dl>

## Return value

This method returns a Boolean value. **True** specifies that a report was generated. **False** specifies that no report could be generated for the given input.

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
' Generate a UserRequestTypeList report.
'
' Variables:
'    auditReport - AuditReport object
'    lcid        - 1033 is the U.S. English LCID
'    endDate     - Today's date
'    startDate   - Ten days prior to the end date
'    domainName  - Domain name for the report
'    userName    - User name
'    requestId   - Eight (8) represents an acquire license request
'    outFile     - Output file path
'    fileType    - Zero (0) represents an Excel (.xls) file

SUB CreateReport()

  DIM auditReport
  DIM lcid
  DIM endDate
  DIM startDate
  DIM domainName
  DIM userName
  DIM requestId
  DIM outFile
  DIM fileType

  lcid = 1033
  endDate = Now
  startDate = DateAdd("d", -10, endDate)
  domainName = "example.com"
  userName = "someone"
  requestId = 8
  outFile = "c:\UserRequestTypeList.xls"
  fileType = 0

  ' Create an AuditReport object.
  SET auditReport = _
          config_manager.AuditReport
  CheckError()

  ' Generate the report.
  CALL auditReport.ExportUserRequestTypeList( _
      lcid, _ 
      startDate, _ 
      endDate, _ 
      domainName, _
      userName, _
      requestId, _
      outFile, _ 
      fileType)
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

 

 




