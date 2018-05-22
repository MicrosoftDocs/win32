---
Description: 'Retrieves information about the logging database.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'b7b8709c-2cdf-40b7-8a4d-a28628047531'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'LoggingSystemInformation.DatabaseInformation property'
---

# LoggingSystemInformation.DatabaseInformation property

The **DatabaseInformation** property retrieves information about the logging database.

This property is read-only.

## Syntax


```VB
LoggingSystemInformation.DatabaseInformation
```



## Property value

This property returns a [**DatabaseInformation**](databaseinformation-object.md) object.

## Remarks

The [**DatabaseInformation**](databaseinformation-object.md) object represents the database used to log information about the use of rights-protected content. You can use the object to retrieve the names of the logging database and server.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**LoggingSystemInformation**](loggingsysteminformation-object.md)
</dt> </dl>

 

 




