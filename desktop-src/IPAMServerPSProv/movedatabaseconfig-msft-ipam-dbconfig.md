---
Description: 'Migrates an IPAM database.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'a348ad13-6a29-4b14-a18e-c73e1cdc677b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'MoveDatabaseConfig method of the MSFT\_IPAM\_DBConfig class'
---

# MoveDatabaseConfig method of the MSFT\_IPAM\_DBConfig class

Migrates an IPAM database.

## Syntax


```mof
uint32 MoveDatabaseConfig(
  [in]  string             DatabaseServer,
  [in]  string             DatabaseName,
  [in]  uint16             DatabasePort,
  [in]  uint16             DatabaseAuthType,
  [in]  string             DatabaseCredential,
  [out] MSFT_IPAM_DBConfig Output
);
```



## Parameters

<dl> <dt>

*DatabaseServer* \[in\]
</dt> <dd>

The IP address or FQDN of the database server.

</dd> <dt>

*DatabaseName* \[in\]
</dt> <dd>

The name of the database to migrate.

</dd> <dt>

*DatabasePort* \[in\]
</dt> <dd>

The port used to run the SQL service.

</dd> <dt>

*DatabaseAuthType* \[in\]
</dt> <dd>

The type of authentication to use to connect to the IPAM database.

The possible values are:

<dt>

0
</dt> <dd>

Authentication Not Configured.

</dd> <dt>

1
</dt> <dd>

Windows Authentication.

> [!Note]  
> If you use Windows authentication, IPAM will use the server machine account to connect to the database.

 

</dd> <dt>

2
</dt> <dd>

SQL Authentication.

> [!Note]  
> If you use Windows SQL authentication, specify a username and password to connect to the database.

 

</dd> </dl> </dd> <dt>

*DatabaseCredential* \[in\]
</dt> <dd>

The credentials to the database.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the updated database configuration object.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

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

[**MSFT\_IPAM\_DBConfig**](msft-ipam-dbconfig.md)
</dt> </dl>

 

 




