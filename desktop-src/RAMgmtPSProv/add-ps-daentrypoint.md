---
title: Add method of the PS\_DAEntryPoint class
description: Adds an entry point to a multisite deployment. The cmdlet verifies DirectAccess prerequisites and adds the server as an entry point to the multisite deployment.
audience: developer
ms.assetid: 67390648-c647-4b9b-b4a4-1f45efb76897
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DAEntryPoint class
- PS_DAEntryPoint class, Add method
topic_type:
- apiref
api_name:
- PS_DAEntryPoint.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add method of the PS\_DAEntryPoint class

Adds an entry point to a multisite deployment. The cmdlet verifies DirectAccess prerequisites and adds the server as an entry point to the multisite deployment.

## Syntax


```mof
uint32 Add(
  [in]  string       ComputerName,
  [in]  string       ServerGpoName,
  [in]  string       Name,
  [in]  string       GslbIP,
  [in]  boolean      DeployNat,
  [in]  boolean      NoPrerequisite,
  [in]  string       RemoteAccessServer,
  [in]  string       InternalInterface,
  [in]  string       InternetInterface,
  [in]  string       ClientIPv6Prefix,
  [in]  string       ConnectToAddress,
  [in]  boolean      Force,
  [in]  boolean      PassThru,
  [out] DAEntryPoint cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name or address (IPv4 or IPv6) of a remote access server in the multisite deployment. If no value is specified the local computer on which the cmdlet runs is used.

</dd> <dt>

*ServerGpoName* \[in\]
</dt> <dd>

This parameter specifies the name of the GPO in which DirectAccess server configuration settings for this entrypoint are stored. If a value is not specified the cmdlet creates a GPO with the name DirectAccess Server Settings - Entry point name. The GPO is created on the domain where the server indicated by the RemoteAccessServer parameter is joined.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the entry point.

</dd> <dt>

*GslbIP* \[in\]
</dt> <dd>

IPv4 or IPv6 address used for global load balancing for the entry point. This parameter can be only be specified if global load balancing FQDN is configured in the multisite deployment.

</dd> <dt>

*DeployNat* \[in\]
</dt> <dd>

Indicates that the remote access server or server cluster is deployed behind a NAT device.

</dd> <dt>

*NoPrerequisite* \[in\]
</dt> <dd>

Indicates that a prerequisite check for DirectAccess deployment requirements should not be performed. The default value is false.

</dd> <dt>

*RemoteAccessServer* \[in\]
</dt> <dd>

The name or address (IPv4 or IPv6) of the remote access server to be the first server of the entry point. If the domain of the RemoteAccessServer is in a different domain, the name of the server should be provided in fully qualified name format.

</dd> <dt>

*InternalInterface* \[in\]
</dt> <dd>

The name of the internal network adapter of the first server in the entry point. If the name is not specified the cmdlet tries to automatically detect the network adapter.

</dd> <dt>

*InternetInterface* \[in\]
</dt> <dd>

The name of the Internet network adapter of the first server in the entry point. If the name is not specified the cmdlet tries to automatically detect the network adapter.

</dd> <dt>

*ClientIPv6Prefix* \[in\]
</dt> <dd>

IPv6 address prefix assigned to remote clients connecting over IP-HTTPS. The prefix length must be 59 or 64 bits. This parameter should be specified only in case IPv6 is deployed on the internal network.

</dd> <dt>

*ConnectToAddress* \[in\]
</dt> <dd>

Specifies the public name or IPv4 address of the Remote Access server (or NAT server) to which remote clients connect.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Suppresses the option to allow a user to override a setting. It should continue prompts.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifying PassThru returns the DAEntrypoint object which contains the DAEntrypoint configuration. This cmdlet doesn't generate an object by default.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Entry point name. 2. IPv4 or IPv6 address used for global load balancing for the entry point 3. List of servers in the entry point.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DAEntryPoint**](ps-daentrypoint.md)
</dt> </dl>

 

 





