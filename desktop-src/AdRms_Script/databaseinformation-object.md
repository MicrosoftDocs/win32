---
Description: 'The DatabaseInformation object is used to represent the logging, configuration, and directory services databases.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '062d2554-f921-436d-a2e5-be87d630ff86'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: DatabaseInformation object
---

# DatabaseInformation object

The **DatabaseInformation** object is used to represent the logging, configuration, and directory services databases. Databases are files stored on a database server such as SQL Server. You can use this object to retrieve the names of the file and server. The object can be retrieved by calling the [**DatabaseInformation**](loggingsysteminformation-databaseinformation-property.md) property on the [**LoggingSystemInformation**](loggingsysteminformation-object.md) object or the [**Configuration**](enterprisedatabase-configuration-property.md) and [**DirectoryServices**](enterprisedatabase-directoryservices-property.md) properties on the [**EnterpriseDatabase**](enterprisedatabase-object.md) object.

## Members

The **DatabaseInformation** object has these types of members:

-   [Properties](#properties)

### Properties

The **DatabaseInformation** object has these properties.



| Property                                                         | Description                                            |
|:-----------------------------------------------------------------|:-------------------------------------------------------|
| [**DBName**](databaseinformation-dbname-property.md)<br/> | Retrieves the name of the logging database.<br/> |
| [**Server**](databaseinformation-server-property.md)<br/> | Retrieves the name of the logging server.<br/>   |



 

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

SUB GetDatabaseInfo()

  DIM loggingSysInfo

  SET loggingSysInfo = _
          config_manager.AuditReport.LoggingSystemInformation
  CheckError()

  CALL WScript.Echo("Server Name:" & _
                    loggingSysInfo.DatabaseInformation.Server)
  CALL WScript.Echo("Database:" & _
                    loggingSysInfo.DatabaseInformation.DBName)

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> <dt>

[**AuditReport**](auditreport-object.md)
</dt> <dt>

[**LoggingSystemInformation**](loggingsysteminformation-object.md)
</dt> </dl>

 

 




