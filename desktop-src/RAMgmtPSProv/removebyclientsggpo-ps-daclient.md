---
title: RemoveByClientSGGpo method of the PS\_DAClient class
description: This cmdlet performs the following operations1.
audience: developer
ms.assetid: 72698317-b30d-4075-b778-7114e66ffa6e
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByClientSGGpo method
- RemoveByClientSGGpo method, PS_DAClient class
- PS_DAClient class, RemoveByClientSGGpo method
topic_type:
- apiref
api_name:
- PS_DAClient.RemoveByClientSGGpo
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveByClientSGGpo method of the PS\_DAClient class

This cmdlet performs the following operations1. Removes one or more client machine security group(s) from the DA deployment 2. Removes one or more DA client GPO(s) from domain(s) 3. In a multi-site deployment, removes one or more security group(s) of down-level clients from the DA deployment. These down-level clients can connect only to the specified site 4. In a multi-site deployment, removes one or more down-level DA client GPO(s) from domain(s).

## Syntax


```mof
uint32 RemoveByClientSGGpo(
  [in]  string   SecurityGroupNameList[],
  [in]  string   ComputerName,
  [in]  boolean  PassThru,
  [in]  string   DomainName[],
  [out] DAClient cmdletOutput
);
```



## Parameters

<dl> <dt>

*SecurityGroupNameList* \[in\]
</dt> <dd>

Specifies a list of client security groups that are part of the DA deployment which need to be removed. Name of security group is in DOMAIN\\SG\_NAME format

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the DA client object. By default this cmdlet does not generate any output

</dd> <dt>

*DomainName* \[in\]
</dt> <dd>

List of domains in which client GPOs need to be removed. Domain is specified in the format DOMAIN

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. List of client SGs present in the DA deployment. 2. List of client GPOs present in the DA deployment. 3. Status of force tunnel. 4. NRPT object (for force tunnel properties). 5. Support for down-level (enable/disable). 6. Laptop-only deployment (enable/disable).

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

[**PS\_DAClient**](ps-daclient.md)
</dt> </dl>

 

 





