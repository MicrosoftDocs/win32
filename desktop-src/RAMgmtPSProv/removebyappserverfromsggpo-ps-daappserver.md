---
title: RemoveByAppServerFromSGGpo method of the PS\_DAAppServer class
description: This cmdlet performs the following operations1.
audience: developer
ms.assetid: 081dc245-24a7-4f5a-8f1f-d582783f404c
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByAppServerFromSGGpo method
- RemoveByAppServerFromSGGpo method, PS_DAAppServer class
- PS_DAAppServer class, RemoveByAppServerFromSGGpo method
topic_type:
- apiref
api_name:
- PS_DAAppServer.RemoveByAppServerFromSGGpo
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveByAppServerFromSGGpo method of the PS\_DAAppServer class

This cmdlet performs the following operations1. Removes the specified lit of application server Security groups from the DA deployment2. Removes the specified application servers from the specified DA application server security group3. Removes the application server GPOs in the specified domains. This cmdlet is not applicable when DirectAccess is deployed only for the management of remote clients.

## Syntax


```mof
uint32 RemoveByAppServerFromSGGpo(
  [in]  string      SecurityGroupName,
  [in]  string      Name[],
  [in]  string      ComputerName,
  [in]  boolean     PassThru,
  [in]  string      DomainName[],
  [out] DAAppServer cmdletOutput
);
```



## Parameters

<dl> <dt>

*SecurityGroupName* \[in\]
</dt> <dd>

Name of a security group that is already part of the DA deployment from which the specified list of app servers should be deleted. Specified in DOMAIN\\SG\_NAME format

</dd> <dt>

*Name* \[in\]
</dt> <dd>

List of application servers that have to be deleted from the DA deployment. The servers are specified by their hostnames and are deleted from the Security Group specified by the SecurityGroupName parameter. The servers cannot be specified by their IPv4 or IPv6 addresses

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the DA Application Server object. By default this cmdlet does not generate any output

</dd> <dt>

*DomainName* \[in\]
</dt> <dd>

List of domains from which application server GPOs need to be removed. Domain is specified in the format DOMAIN.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The entire app server policy object is outputted. Consists of the following: a. List of app server SGs present in the DA deployment. b. List of all app server GPOs in the DA deployment. c. App server connection properties, viz. 1. Connectivity type. 2. IPsec traffic protection.

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

 

 





