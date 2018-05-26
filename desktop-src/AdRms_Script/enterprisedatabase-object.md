---
Description: Can be used to retrieve the configuration and directory services databases.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1d05305d-9148-4cfa-b239-4078fe7f7aa4
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: EnterpriseDatabase object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# EnterpriseDatabase object

The **EnterpriseDatabase** object can be used to retrieve the configuration and directory services databases.

-   Configuration. This database contains configuration information, all certificates and keys, the encrypted server private key (unless hardware encryption was used), and the private key password hash.
-   Directory services. This database contains the results of Active Directory group membership queries.

To retrieve the logging database, call the [**LoggingSystemInformation**](auditreport-loggingsysteminformation-property.md) property on the [**AuditReport**](auditreport-object.md) object.

## Members

The **EnterpriseDatabase** object has these types of members:

-   [Properties](#properties)

### Properties

The **EnterpriseDatabase** object has these properties.



| Property                                                                              | Description                                                             |
|:--------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| [**Configuration**](enterprisedatabase-configuration-property.md)<br/>         | Retrieves information about the configuration database.<br/>      |
| [**DirectoryServices**](enterprisedatabase-directoryservices-property.md)<br/> | Retrieves information about the directory services database.<br/> |



 

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




