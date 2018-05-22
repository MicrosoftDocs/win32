---
Description: 'Retrieves information about the directory services database.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '9fed2b47-9deb-46c9-812a-5c4ba202878c'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'EnterpriseDatabase.DirectoryServices property'
---

# EnterpriseDatabase.DirectoryServices property

The **DirectoryServices** property retrieves information about the directory services database.

This property is read-only.

## Syntax


```VB
EnterpriseDatabase.DirectoryServices
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
' Retrieve the directory services database.

SUB GetDatabases()

  DIM enterpriseDb
  DIM DsDbServer
  DIM DsDbName

  ' Retrieve the EnterpriseDatabase object.
  SET enterpriseDb = config_manager.Enterprise.EnterpriseDatabase
  CheckError()

  ' Retrieve the name of the directory services database and the 
  ' server on which it is installed.
  DsDbServer = enterpriseDb.DirectoryServices.Server
  DsDbName = enterpriseDb.DirectoryServices.DBName
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

[**EnterpriseDatabase**](enterprisedatabase-object.md)
</dt> </dl>

 

 




