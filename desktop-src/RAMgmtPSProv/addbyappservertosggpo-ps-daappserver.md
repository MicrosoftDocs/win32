---
title: AddByAppServerToSGGpo method of the PS\_DAAppServer class
description: This cmdlet is not applicable when DirectAccess is deployed only for the management of remote clients.
audience: developer
ms.assetid: ae93c8e3-1a81-4c78-8fc4-15fc34d8402d
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByAppServerToSGGpo method
- AddByAppServerToSGGpo method, PS_DAAppServer class
- PS_DAAppServer class, AddByAppServerToSGGpo method
topic_type:
- apiref
api_name:
- PS_DAAppServer.AddByAppServerToSGGpo
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByAppServerToSGGpo method of the PS\_DAAppServer class

This cmdlet performs the following operations:

-   Adds a new application server security group to the DA deployment.
-   Adds an application servers to an application server security group that is already part of the DA deployment.
-   Adds application server GPO in a domain.

This cmdlet is not applicable when DirectAccess is deployed only for the management of remote clients.

## Syntax


```mof
uint32 AddByAppServerToSGGpo(
  [in]  string      GpoName[],
  [in]  string      SecurityGroupName,
  [in]  string      Name[],
  [in]  string      ComputerName,
  [in]  boolean     PassThru,
  [out] DAAppServer cmdletOutput
);
```



## Parameters

<dl> <dt>

*GpoName* \[in\]
</dt> <dd>

This parameter represents the name to be used when creating the app server GPO in the specified domain or represents the domain in which an app server GPO with the default name should be created. GPO is specified in the format DOMAIN\\GPO\_NAME. Domain is specified in the format DOMAIN. If the parameter contains only the domain name then the following default GPO name is used: \[domain\] application server policy for \[DA connection friendly name\]. A list of GPOs can be specified

</dd> <dt>

*SecurityGroupName* \[in\]
</dt> <dd>

Name of a security group that is already part of the DA deployment to which the specified list of app servers should be added. Specified in DOMAIN\\SG\_NAME format

</dd> <dt>

*Name* \[in\]
</dt> <dd>

List of application servers that have to be added to the DA deployment. The servers are specified by their hostnames and are added to the Security Group specified by the SecurityGroupName parameter. The servers cannot be specified by their IPv4 or IPv6 addresses

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the Application server policy object. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The entire app server policy object is outputted. Consists of the following: a. List of app server SGs present in the DA deployment. b. List of all app server GPOs in the DA deployment. c. App server connection properties, viz. 1. Connectivity type. 2. IPsec traffic protection

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

[**PS\_DAAppServer**](ps-daappserver.md)
</dt> </dl>

 

 





