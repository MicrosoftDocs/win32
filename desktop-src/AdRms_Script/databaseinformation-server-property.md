---
Description: 'Retrieves the name of the logging server.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '197638c0-6f26-492f-908d-2478d1412598'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'DatabaseInformation.Server property'
---

# DatabaseInformation.Server property

The **Server** property retrieves the name of the logging server.

This property is read-only.

## Syntax


```VB
DatabaseInformation.Server
```



## Property value

This property returns a string value that contains the name.

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

[**DatabaseInformation**](databaseinformation-object.md)
</dt> <dt>

[**LoggingSystemInformation**](loggingsysteminformation-object.md)
</dt> </dl>

 

 




