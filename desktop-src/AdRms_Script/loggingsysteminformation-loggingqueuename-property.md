---
Description: Retrieves the name of the message queue.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5dc92e66-7ed3-4097-989b-a8f3824d66d9
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: LoggingSystemInformation.LoggingQueueName property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LoggingSystemInformation.LoggingQueueName property

The **LoggingQueueName** property retrieves the name of the message queue.

This property is read-only.

## Syntax


```VB
LoggingSystemInformation.LoggingQueueName
```



## Property value

This property returns a string value.

## Remarks

ADRMS uses Message Queuing to send log messages to the logging database. If the logging database or the database server becomes unavailable, MSMQ saves the messages in a dead letter queue until the server or the database are again available. The format of the queue name is drms\_logging\_*cluster* where *cluster* is the name of your ADRMS cluster. The name of the dead letter queue is drms\_logging\_*cluster*\_deadletter.

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

[**LoggingSystemInformation**](loggingsysteminformation-object.md)
</dt> </dl>

 

 




