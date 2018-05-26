---
Description: Retrieves information about the configuration database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bb3531de-0689-45ce-860a-53258443fbcd
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: EnterpriseDatabase.Configuration property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnterpriseDatabase.Configuration property

The **Configuration** property retrieves information about the configuration database.

This property is read-only.

## Syntax


```VB
EnterpriseDatabase.Configuration
```



## Property value

This property returns a [**DatabaseInformation**](databaseinformation-object.md) object that contains the names of the database and the server on which the database is installed.

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
' Retrieve the configuration database.

SUB GetDatabases()

  DIM enterpriseDb
  DIM configDbServer
  DIM configDbName

  ' Retrieve the EnterpriseDatabase object.
  SET enterpriseDb = config_manager.Enterprise.EnterpriseDatabase
  CheckError()

  ' Retrieve the name of the configuration database and the 
  ' server on which it is installed.
  configDbServer = enterpriseDb.Configuration.Server 
  configDbName = enterpriseDb.Configuration.DBName
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
```



## Requirements



|                                     |                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**EnterpriseDatabase**](enterprisedatabase-object.md)
</dt> </dl>

 

 




