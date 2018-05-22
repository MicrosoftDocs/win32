---
Description: 'Retrieves an object that can be used to manage the configuration, directory services, and logging databases.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'f2f54f53-f2bb-4026-a9ef-afd95834ed60'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'Enterprise.EnterpriseDatabase property'
---

# Enterprise.EnterpriseDatabase property

The **EnterpriseDatabase** property retrieves an object that can be used to manage the configuration, directory services, and logging databases.

This property is read-only.

## Syntax


```VB
Enterprise.EnterpriseDatabase
```



## Property value

This property returns an [**EnterpriseDatabase**](enterprisedatabase-object.md) object.

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
' Retrieve databases.

SUB GetDatabases()

  DIM enterpriseDb
  DIM configDbServer
  DIM configDbName
  DIM DsDbServer
  DIM DsDbName
  DIM loggingDbServer
  DIM loggingDbName

  ' Retrieve the EnterpriseDatabase object.
  SET enterpriseDb = config_manager.Enterprise.EnterpriseDatabase
  CheckError()

  ' Retrieve the name of the configuration database and the 
  ' server on which it is installed.
  configDbServer = enterpriseDb.Configuration.Server 
  configDbName = enterpriseDb.Configuration.DBName
  CheckError()

  ' Retrieve the name of the directory services database and the 
  ' server on which it is installed.
  DsDbServer = enterpriseDb.DirectoryServices.Server
  DsDbName = enterpriseDb.DirectoryServices.DBName
  CheckError()

  ' Retrieve the name of the logging database and the 
  ' server on which it is installed.
  loggingDbServer = enterpriseDb.Logging.Server
  loggingDbName = enterpriseDb.Logging.DBName
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**Enterprise**](enterprise-object.md)
</dt> </dl>

 

 




