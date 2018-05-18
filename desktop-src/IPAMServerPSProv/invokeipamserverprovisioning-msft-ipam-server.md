---
Description: 'Provisions an IPAM server.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '85dc4dda-c424-45ec-995b-a43f19d9190f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'InvokeIpamServerProvisioning method of the MSFT\_IPAM\_Server class'
---

# InvokeIpamServerProvisioning method of the MSFT\_IPAM\_Server class

Provisions an IPAM server.

## Syntax


```mof
uint32 InvokeIpamServerProvisioning(
  [in] string DatabaseServer,
  [in] string DatabaseName,
  [in] uint16 DatabasePort,
  [in] uint16 DatabaseAuthType,
  [in] string DatabaseCredential,
  [in] uint16 ProvisioningMethod,
  [in] string GpoPrefix,
  [in] string WidSchemaPath
);
```



## Parameters

<dl> <dt>

*DatabaseServer* \[in\]
</dt> <dd>

The name of the server to provision.

</dd> <dt>

*DatabaseName* \[in\]
</dt> <dd>

The name of the IPAM database.

</dd> <dt>

*DatabasePort* \[in\]
</dt> <dd>

The incoming port to configure on the server.

</dd> <dt>

*DatabaseAuthType* \[in\]
</dt> <dd>

The type of authentication to use to connect to the IPAM database.

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

The credentials for the IPAM database.

</dd> <dt>

*ProvisioningMethod* \[in\]
</dt> <dd>

The provisioning method to configure on the server.

</dd> <dt>

*GpoPrefix* \[in\]
</dt> <dd>

The GPO prefix to use for Group Policy based provisioning.

</dd> <dt>

*WidSchemaPath* \[in\]
</dt> <dd></dd> </dl>

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

[**MSFT\_IPAM\_Server**](msft-ipam-server.md)
</dt> </dl>

 

 




