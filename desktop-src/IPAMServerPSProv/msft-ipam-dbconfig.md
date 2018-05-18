---
Description: 'Represents an IPAM database configuration.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'e6c101a9-6746-4075-8105-b5bab891ce75'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'MSFT\_IPAM\_DBConfig class'
---

# MSFT\_IPAM\_DBConfig class

Represents an IPAM database configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Database::System"), ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_DBConfig : CIM_DatabaseParameter
{
  string Caption;
  string Description;
  string ElementName;
  string InstanceID;
  uint16 DatabaseType;
  string WidSchemaPath;
  string DatabaseServer;
  string DatabaseName;
  uint16 DatabasePort;
  uint16 DatabaseAuthType;
  string DatabaseUser;
};
```

## Members

The **MSFT\_IPAM\_DBConfig** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_IPAM\_DBConfig** class has these methods.



| Method                                                              | Description                                        |
|:--------------------------------------------------------------------|:---------------------------------------------------|
| [**MoveDatabaseConfig**](movedatabaseconfig-msft-ipam-dbconfig.md) | Migrates an IPAM database.<br/>              |
| [**SetDatabaseConfig**](setdatabaseconfig-msft-ipam-dbconfig.md)   | Updates an IPAM database configuration.<br/> |



 

### Properties

The **MSFT\_IPAM\_DBConfig** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The **Caption** property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**DatabaseAuthType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of authentication to use to connect to the IPAM database.

The possible values are:

<dt>

<span id="Authentication_Not_Configured"></span><span id="authentication_not_configured"></span><span id="AUTHENTICATION_NOT_CONFIGURED"></span>

<span id="Authentication_Not_Configured"></span><span id="authentication_not_configured"></span><span id="AUTHENTICATION_NOT_CONFIGURED"></span>**Authentication Not Configured** (0)


</dt> <dd>

Authentication Not Configured.

</dd> <dt>

<span id="Windows_Authentication"></span><span id="windows_authentication"></span><span id="WINDOWS_AUTHENTICATION"></span>

<span id="Windows_Authentication"></span><span id="windows_authentication"></span><span id="WINDOWS_AUTHENTICATION"></span>**Windows Authentication** (1)


</dt> <dd>

Windows Authentication.

> [!Note]  
> If you use Windows authentication, IPAM will use the server machine account to connect to the database.

 

</dd> <dt>

<span id="SQL_Authentication"></span><span id="sql_authentication"></span><span id="SQL_AUTHENTICATION"></span>

<span id="SQL_Authentication"></span><span id="sql_authentication"></span><span id="SQL_AUTHENTICATION"></span>**SQL Authentication** (2)


</dt> <dd>

SQL Authentication.

> [!Note]  
> If you use Windows SQL authentication, specify a username and password to connect to the database.

 

</dd> </dl>

</dd> <dt>

**DatabaseName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the IPAM database.

</dd> <dt>

**DatabasePort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port used to run the SQL service.

</dd> <dt>

**DatabaseServer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address or FQDN of the database server.

</dd> <dt>

**DatabaseType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of database to configure.

<dt>

<span id="Database_Not_Configured"></span><span id="database_not_configured"></span><span id="DATABASE_NOT_CONFIGURED"></span>

**Database Not Configured** (0)


</dt> <dd></dd> <dt>

<span id="Windows_Internal_Database"></span><span id="windows_internal_database"></span><span id="WINDOWS_INTERNAL_DATABASE"></span>

**Windows Internal Database** (1)


</dt> <dd></dd> <dt>

<span id="Microsoft_SQL_Server"></span><span id="microsoft_sql_server"></span><span id="MICROSOFT_SQL_SERVER"></span>

**Microsoft SQL Server** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**DatabaseUser**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user name for SQL authentication.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **Description** property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user-friendly name for this instance of SettingData. In addition, the user-friendly name can be used as an index property for a search or query. (Note: The name does not have to be unique within a namespace.)

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Uniquely and opaquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This pattern is similar to the structure of schema class names. In addition, to ensure uniqueness, the first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefore the *OrgID* must not contain a colon (':').
>
> *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
>
> If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
>
> For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

 

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**WidSchemaPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path to the schema and log files for a Windows Internal Database.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_DatabaseParameter**](cim-databaseparameter.md)
</dt> <dt>

[IPAM Server WMI Provider Reference](ipam-server-wmi-provider-reference.md)
</dt> </dl>

 

 




